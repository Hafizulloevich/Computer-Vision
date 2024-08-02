import numpy as np
from ultralytics import YOLO
import cv2
import cvzone
import math
import sort
cap = cv2.VideoCapture('../Videos/cars.mp4')

model = YOLO('../Yolo-Weights/yolov8n.pt')

classnames = [
    "person",
    "bicycle",
    "car",
    "motorbike",
    "aeroplane",
    "bus",
    "train",
    "truck",
    "boat",
    "traffic light",
    "fire hydrant",
    "stop sign",
    "parking meter",
    "bench",
    "bird",
    "cat",
    "dog",
    "horse",
    "sheep",
    "cow",
    "elephant",
    "bear",
    "zebra",
    "giraffe",
    "backpack",
    "umbrella",
    "handbag",
    "tie",
    "suitcase",
    "frisbee",
    "skis",
    "snowboard",
    "sports ball",
    "kite",
    "baseball bat",
    "baseball glove",
    "skateboard",
    "surfboard",
    "tennis racket",
    "bottle",
    "wine glass",
    "cup",
    "fork",
    "knife",
    "spoon",
    "bowl",
    "banana",
    "apple",
    "sandwich",
    "orange",
    "broccoli",
    "carrot",
    "hot dog",
    "pizza",
    "donut",
    "cake",
    "chair",
    "sofa",
    "pottedplant",
    "bed",
    "diningtable",
    "toilet",
    "tvmonitor",
    "laptop",
    "mouse",
    "remote",
    "keyboard",
    "cell phone",
    "microwave",
    "oven",
    "toaster",
    "sink",
    "refrigerator",
    "book",
    "clock",
    "vase",
    "scissors",
    "teddy bear",
    "hair drier",
    "toothbrush"
]

mask = cv2.imread('mask.png')

#Tracking
tracker = sort.Sort(max_age=20, min_hits=3, iou_threshold=0.3)

limits = [403, 297, 673, 297]
counter = []

while True:
    success, img = cap.read()
    imgRegion = cv2.bitwise_and(img, mask)

    results = model(imgRegion, stream=True)
    detections = np.empty((0, 5))

    for r in results:
        boxes = r.boxes
        for box in boxes:
            #Bounding Box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            #cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

            w, h = x2-x1, y2-y1
            bbox = int(x1), int(y1), int(w), int(h)


            #Confidence
            conf = math.ceil((box.conf[0]*100))/100
            #class of an object
            cls = int(box.cls[0])
            text = f"{classnames[cls]} {conf:.2f}"

            current_class = classnames[cls]
            needed_class = ['car', 'truck', 'bus', 'motorbike']

            if current_class in needed_class and conf > 0.3:
                # Display the text on the image
                #cvzone.putTextRect(img, text, (max(0, x1), max(35, y1)), scale=1, thickness=1, offset=5)
                cvzone.cornerRect(img, bbox, l=9, rt=5)

                currentArray = np.array([x1,y1, x2, y2, conf])
                detections = np.vstack((detections, currentArray))

    resultsTracker = tracker.update(detections)

    cv2.line(img, (limits[0], limits[1]), (limits[2], limits[3]),(0,0,255),5)

    for result in resultsTracker:
        x1, y1, x2, y2, ID= result
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        print(result)
        #cvzone.cornerRect(img, bbox, l=9, rt=2, colorR=(255,0,0))
        cvzone.putTextRect(img, f" {int(ID)}", (max(0, x1), max(35, y1)), scale=2, thickness=1, offset=5)

        cx, cy = x1+w//2, y1+h//2
        #cv2.circle(img,(cx,cy), 5, (255,0,255), cv2.FILLED)

        if limits[0]<cx< limits[2] and limits[1] - 15 < cy < limits[1] + 15:
            if counter.count(ID) == 0:
                counter.append(ID)
                cv2.line(img, (limits[0], limits[1]), (limits[2], limits[3]), (0, 255, 0), 5)

    cvzone.putTextRect(img, f" Car count: {len(counter)}", (50,50))
    cv2.imshow('Image', img)
    #cv2.imshow('ImageRegion', imgRegion)
    cv2.waitKey(10)
