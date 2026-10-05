# 🎯 AI Object Detection & Tracking

An AI-powered object detection and tracking application built using Python, YOLO, ByteTrack, OpenCV, and Gradio.

This project was developed as part of the **CodeAlpha Artificial Intelligence Internship – Task 4**.

## 📌 Project Overview

The application takes a video as input and uses a pretrained YOLO model to detect objects such as people, cars, buses, and other supported classes.

ByteTrack is then used to track detected objects across video frames and assign tracking IDs.

## 🚀 Features

- Video upload
- Real-time object detection
- Bounding boxes
- Object class labels
- Object tracking
- Unique tracking IDs
- Confidence threshold
- Gradio web interface
- Browser-friendly output video

## 🧠 How It Works

```text
Input Video
     ↓
YOLO Object Detection
     ↓
Bounding Boxes + Labels
     ↓
ByteTrack
     ↓
Tracking IDs
     ↓
Processed Video
🛠️ Technologies Used
Python
YOLO
Ultralytics
ByteTrack
OpenCV
Gradio

📦 Installation

Clone the repository:

git clone https://github.com/YOUR-USERNAME/CodeAlpha_ObjectDetectionTracking.git

Move into the project directory:

cd CodeAlpha_ObjectDetectionTracking

Install the required dependencies:

pip install -r requirements.txt
▶️ Run the Application

Run the following command:

python app.py

The Gradio interface will open and allow you to upload a video.

🎯 How to Use
Open the application.
Upload a video.
Click Detect & Track.
YOLO detects objects in the video.
ByteTrack tracks detected objects across frames.
The processed video is displayed with bounding boxes, labels, and tracking IDs.
🔍 Example

The system can produce results such as:

Person → ID: 1
Person → ID: 2
Car    → ID: 3
Bus    → ID: 4

The tracking IDs help maintain the identity of detected objects as they move through the video.

📚 Key Concepts
Object Detection

Object detection identifies objects within an image or video and determines their locations using bounding boxes.

YOLO

YOLO (You Only Look Once) is a real-time object detection model used to identify objects efficiently in images and video.

ByteTrack

ByteTrack is an object tracking algorithm that associates detected objects across consecutive video frames and assigns tracking IDs.

OpenCV

OpenCV is used for computer vision and video processing tasks.

Gradio

Gradio provides the interactive web interface for uploading videos and displaying the processed output.

🔮 Future Improvements
Real-time webcam detection
Object counting
Vehicle counting
Speed estimation
Line-crossing detection
Custom-trained object detection models
Real-time analytics dashboard
🎓 Internship

This project was completed as part of the:

CodeAlpha Artificial Intelligence Internship

Task 4: Object Detection and Tracking

👩‍💻 Author

Tayyaba Mubejo

Built with Python and AI as part of my journey toward becoming an AI Engineer.
