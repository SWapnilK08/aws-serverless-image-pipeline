import json
import boto3
import urllib.parse

# Initialize AWS Client variables
s3_client = boto3.client('s3')
rekognition_client = boto3.client('rekognition')
dynamodb = boto3.resource('dynamodb')
sns_client = boto3.client('sns')

# Define your resource names
TABLE_NAME = "ImageMetadata"
SNS_TOPIC_ARN = "arn:aws:sns:us-east-1:123456789012:ImageAlerts"

def lambda_handler(event, context):
    try:
        # 1. Parse bucket name and file name from the S3 upload event
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
        
        # 2. Call Amazon Rekognition to detect labels inside the image
        response = rekognition_client.detect_labels(
            Image={'S3Object': {'Bucket': bucket, 'Name': key}},
            MaxLabels=5,
            MinConfidence=80
        )
        
        # Extract name properties into an array
        detected_labels = [label['Name'] for label in response['Labels']]
        print(f"Detected Labels for {key}: {detected_labels}")
        
        # 3. Store the metadata into Amazon DynamoDB
        table = dynamodb.Table(TABLE_NAME)
        table.put_item(
            Item={
                'ImageID': key,
                'BucketName': bucket,
                'Labels': detected_labels,
                'Status': 'PROCESSED'
            }
        )
        
        # 4. Publish a notification text via Amazon SNS
        message = f"New Image Processed Successfully!\n\nFile: {key}\nLabels Found: {', '.join(detected_labels)}"
        sns_client.publish(
            TopicArn=SNS_TOPIC_ARN,
            Message=message,
            Subject="Cloud Pipeline Alert: Image Processed"
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps('Image processed and recorded successfully!')
        }
        
    except Exception as e:
        print(f"Error handling event: {str(e)}")
        raise e
