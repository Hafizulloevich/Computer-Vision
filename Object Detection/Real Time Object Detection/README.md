Real-Time Webcam Object Detection with YOLOv8
This project uses the YOLOv8n (nano) model to perform real-time object detection on a live webcam feed. The script is built with Python and utilizes the Ultralytics, OpenCV, and CVZone libraries to identify objects

🚀 Demo
Check out a video of the project in action on LinkedIn:

[Watch the Video Implementation Here](https://www.linkedin.com/posts/hoshimov_im-happy-to-share-my-2-project-on-cnn-activity-7224656002871128064-metB?utm_source=share&utm_medium=member_desktop&rcm=ACoAADRRZmEBpj2CrLXdfNr_PIRZSAYMgVpvZxg)

✨ Features
80 Object Classes: Can detect up to 80 different object classes from the COCO dataset.
Custom Labeling: I just changed 'person' label of the dataset with my name (nom - variable)

Prerequisites
Python 3.8 or later

A webcam connected to your computer, or a laptop with camera

Install the required libraries:
Open your terminal or command prompt and run:

pip install ultralytics opencv-python cvzone

💻 Usage
Navigate to the directory where you saved the Yolo-WebCam.py file using your terminal.

Install and Run the script with:

python Yolo-WebCam.py

A window titled "Image" will pop up, showing your webcam feed with object detection overlays.

To stop the program, press the 'q' key on your keyboard.
