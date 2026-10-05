# CodeAlpha Object Detection & Tracking

An AI-powered object detection and tracking system built using Python and Computer Vision.

This project was developed as part of the **CodeAlpha Artificial Intelligence Internship – Task 4**.

## 📌 Project Overview

The application accepts a video file, processes it frame by frame, detects objects using the YOLO model, and tracks each object across frames using the ByteTrack algorithm. Every detected object receives a bounding box, a class label, and a unique tracking ID.

The final output is an annotated video that can be played directly in the browser.

## 🚀 Features

- Object detection using YOLOv8
- Multi-object tracking with ByteTrack
- Unique tracking ID for every object
- Bounding boxes and class labels on every frame
- Interactive Gradio interface
- Automatic conversion to browser-friendly MP4

## 🧠 How It Works

```javascript
Upload Video
      ↓
Read Frames (OpenCV)
      ↓
YOLO Object Detection
      ↓
Bounding Boxes + Class Labels
      ↓
ByteTrack Tracking
      ↓
Unique Object IDs
      ↓
Annotate Frames
      ↓
Convert to MP4 (ffmpeg)
      ↓
Tracked Output Video

```

## 🛠️ Technologies Used

- Python
- Ultralytics YOLO (YOLOv8)
- OpenCV
- Gradio
- ffmpeg

## 👁️ Computer Vision Techniques

### Object Detection

YOLO (You Only Look Once) analyzes each frame and detects objects from 80+ classes (person, car, dog, etc.) in a single forward pass, making it fast enough for video processing.

### Multi-Object Tracking

ByteTrack assigns a persistent, unique ID to each detected object, so the same person or car keeps the same ID as it moves through the video.

### Video Processing Pipeline

OpenCV reads and writes video frames, and ffmpeg converts the output to the H.264 MP4 format so it plays smoothly in any browser.

## 💻 Installation

Clone the repository:

```javascript
git clone https://github.com/YOUR-USERNAME/CodeAlpha_Object-Detection-Tracking.git
```

Move into the project directory:

```javascript
cd CodeAlpha_Object-Detection-Tracking
```

Install the required libraries:

```javascript
pip install -r requirements.txt
```

> The YOLOv8n weights (`yolov8n.pt`, ~6 MB) download automatically on first run.
> ffmpeg must be installed on your system for MP4 conversion.

## ▶️ Run the Application

Run:

```javascript
python app.py
```

The Gradio interface will launch. Upload any video, click **Detect & Track**, and download the annotated result.

## 🎯 Example Use

- Upload a street/traffic video → cars and pedestrians are detected and tracked
- Upload a sports clip → players get unique tracking IDs
- Upload an animal video → each animal is detected and followed

## 🔮 Future Improvements

Possible future improvements include:

- Real-time webcam detection mode
- People counting and line-crossing analytics
- Custom-trained YOLO models
- Export tracking data to CSV
- Deploy as a public Hugging Face Space
- Speed/trajectory estimation per object

## 👩‍💻 Author

Developed as part of the CodeAlpha AI Internship.

**Project:** Object Detection & Tracking
**Task:** CodeAlpha Artificial Intelligence – Task 4
