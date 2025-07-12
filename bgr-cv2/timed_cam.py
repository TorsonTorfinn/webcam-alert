import streamlit as st
import cv2
from datetime import datetime

st.title("Motion Detector")

col1, col2 = st.columns(2)
with col1:
    start_button = st.button('Start Camera')
with col2:
    stop_button = st.button('Stop Camera')

if start_button:
    streamlit_img = st.image([])
    video = cv2.VideoCapture(0)

    while True:
        current_time = datetime.now()
        check, frame = video.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        cv2.putText(img=frame,
                    text=current_time.strftime("%A"),
                    org=(28, 50),
                    fontFace=cv2.FONT_HERSHEY_PLAIN,
                    fontScale=2,
                    color=(240, 0, 0),
                    thickness=2,
                    lineType=cv2.LINE_AA)
        
        cv2.putText(img=frame,
                    text=current_time.strftime("%H:%M:%S"),
                    org=(10, 80),
                    fontFace=cv2.FONT_HERSHEY_PLAIN,
                    fontScale=2,
                    color=(240, 255, 255),
                    thickness=2,
                    lineType=cv2.LINE_AA)

        streamlit_img.image(frame)

        if stop_button:
            break
