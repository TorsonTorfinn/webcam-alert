import cv2
import time
from emailing import send_email

video = cv2.VideoCapture(0)
time.sleep(1)

first_frame = None
status_list = []

while True:
    status = 0 
    check, frame = video.read()  
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame_gauss = cv2.GaussianBlur(gray_frame, (21, 21), 0)

    if first_frame is None:
        first_frame = gray_frame_gauss
    
    delta_frame = cv2.absdiff(first_frame, gray_frame_gauss)
    threshold_frame = cv2.threshold(delta_frame, 60, 255, cv2.THRESH_BINARY)[1]
    dilate_frame = cv2.dilate(threshold_frame, None, iterations=2)

    cv2.imshow('Builtin Cam Video', dilate_frame)
    
    contours, check = cv2.findContours(dilate_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        rectangle = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        
        if rectangle.any():
            status = 1
    
    status_list.append(status) # 0 - no object && 1 - there's object

    status_list = status_list[-2:]
    if status_list[0] == 1 and status_list[1] == 0:
        send_email()

    cv2.imshow('Video', frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

video.release()


# video = cv2.VideoCapture(0)
# time.sleep(1)

# first_frame = None

# while True:
#     check, frame = video.read()  
#     gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     gray_frame_gauss = cv2.GaussianBlur(gray_frame, (21, 21), 0)

#     if first_frame is None:
#         first_frame = gray_frame_gauss
    
#     delta_frame = cv2.absdiff(first_frame, gray_frame_gauss)
#     threshold_frame = cv2.threshold(delta_frame, 60, 255, cv2.THRESH_BINARY)[1]
#     dilate_frame = cv2.dilate(threshold_frame, None, iterations=2)

#     cv2.imshow('Builtin Cam Video', dilate_frame)
    
#     contours, check = cv2.findContours(dilate_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#     for contour in contours:
#         if cv2.contourArea(contour) < 5000:
#             continue
#         x, y, w, h = cv2.boundingRect(contour)
#         rectangle = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        
#         if rectangle.any():
#             send_email()

#     cv2.imshow('Video', frame)

#     key = cv2.waitKey(1)
#     if key == ord("q"):
#         break

# video.release()