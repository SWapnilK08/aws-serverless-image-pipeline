# ⚡ Serverless Automated Image Analysis Pipeline

A mid-level, event-driven cloud architecture that automatically processes user-uploaded images to detect visual labels and log metadata in real time without managing servers.

## 🔗 Project Links
* **Live Demo Interface:** https://YOUR_GITHUB_USERNAME.github.io/aws-serverless-image-pipeline/
* **Source Code Repository:** https://github.com

---

## 🛠️ Tech Stack & Architecture
* **Frontend:** Responsive HTML5, Tailwind CSS (Hosted via GitHub Pages)
* **Compute:** AWS Lambda (Python 3.11)
* **Storage:** Amazon S3 (Simple Storage Service)
* **AI/ML Service:** Amazon Rekognition (Computer Vision API)
* **Database:** Amazon DynamoDB (NoSQL Key-Value Store)
* **Notifications:** Amazon SNS (Simple Notification Service)
* **Infrastructure as Code (IaC):** AWS SAM (Serverless Application Model)

[User Interface] ──> [Amazon S3 Upload] ──> [AWS Lambda Trigger] ──> [Amazon Rekognition]│▼[Admin Alert Notification] <── [Amazon SNS] <── [Amazon DynamoDB Metadata Logging]


---

## ✨ Core Features
* **Fully Responsive UI:** A drag-and-drop dashboard optimized for mobile, tablet, and desktop views.
* **Event-Driven Execution:** Uploading an image to the S3 bucket automatically wakes up the Lambda function.
* **Automated Object Detection:** Amazon Rekognition scans the image grid and isolates labels with >80% confidence arrays.
* **NoSQL Persistence:** Instant storage of extracted parameters, image keys, and execution status items into DynamoDB.
* **Instant Alerts:** Sends a real-time notification summary straight to the system administrator when processing finishes.

---

## 📂 File Structure
* `index.html` - Fully responsive client web dashboard interface.
* `lambda_function.py` - Core serverless logic processing image events via Boto3 SDK.
* `template.yaml` - Infrastructure configuration file deploying the complete AWS resource tree.

---

## 🚀 How to Run Locally

1. **Clone the Repository:**
   ```bash
   git clone https://github.com
   ```

2. **Deploy Backend with AWS SAM:**
   Ensure your local AWS CLI environment profiles are set up correctly, then run:
   ```bash
   sam build
   sam deploy --guided
   ```

3. **Launch Frontend Dashboard:**
   Open the `index.html` file directly in your browser or access your deployed GitHub Pages domain link to run live end-to-end simulation runs.
