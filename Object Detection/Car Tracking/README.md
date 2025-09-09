🚗 Vehicle Counter with YOLOv8 & SORT TRACK
Welcome to the Vehicle Counter project! This script uses object detection and tracking to count vehicles passing through a designated line in a video.

🎥 See it in Action!
Check out a live demonstration of this project on LinkedIn. Click the link below to watch!

[💻Project Demo Video](https://www.linkedin.com/posts/hoshimov_computervision-deeplearning-ultralytics-activity-7225104973380870146-NEuN?utm_source=share&utm_medium=member_desktop&rcm=ACoAADRRZmEBpj2CrLXdfNr_PIRZSAYMgVpvZxg)


✨ How It Works
The magic happens in a few simple steps:

Detect: YOLOv8 model finds all objects in a video frame/

Track: The SORT (Simple Online and Realtime Tracking) algorithm is used to follow each vehicle and assign it a unique ID.

Count: When a tracked vehicle crosses the line, I increment the counter!

🛠️ Libraries & Technologies Used
This project is built with some amazing Python libraries. Here’s what you’ll need to get it running:

OpenCV (cv2)

Ultralytics (YOLO)

NumPy

cvzone

SORT

To install them, you can run:

pip install numpy ultralytics opencv-python cvzone filterpy

Note: sort.py and mask files shoudl be in the same directory as your app.py file, if you stored the files in different directory adjust the location on the code.

Happy coding!
