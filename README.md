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
