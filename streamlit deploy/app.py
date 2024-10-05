import streamlit as st
import cv2
import torch
from ultralytics import YOLO
import numpy as np
from twilio.rest import Client  


account_sid = 'Put Your SID KEY'  
auth_token = 'Put Your Token KEY'    
twilio_number = 'whatsapp:+14155238886'  
recipient_number = 'whatsapp:+9665your numbers'  

client = Client(account_sid, auth_token)

# Load YOLOv8 model
model = YOLO('model best.pt')  

# Customize page with title and logo
st.set_page_config(page_title="RASD By Real-Time", page_icon=":camera:")
st.image("RASD logo.png", width=250)
st.title("Real-Time Accident Detection and Classification for Enhanced Analysis")

# Sidebar with options
st.sidebar.title("Options")
source_option = st.sidebar.selectbox(
    "Select Source", ["Image", "Video", "Webcam"])

# Function to detect objects in the image
def detect_objects(image):
    results = model(image)
    severe_detected = False  

    for result in results:
        if result.boxes:  
            for box in result.boxes:
                
                class_id = int(box.cls[0])
                class_name = result.names[class_id]

                if class_name == 'severe':
                    severe_detected = True
                    st.warning(f"'severe' Accident detected: {class_name}")

    return results, severe_detected  

# Function to send a WhatsApp alert via Twilio
def send_alert():
    message = client.messages.create(
        body="Alert: 'severe' Accident detected in the video/image!",
        from_=twilio_number,
        to=recipient_number
    )
    st.success('WhatsApp alert sent!')  
    print(message.sid) 

# For Image Input
if source_option == "Image":
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        image = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), 1)
        st.image(image, channels="BGR", caption="Uploaded Image")

        # Object detection
        if st.button("Detect Objects"):
            with st.spinner('Detecting...'):
                results, severe_detected = detect_objects(image)
                result_image = results[0].plot()
                st.image(result_image, caption="Processed Image")

                if severe_detected:  
                    send_alert()

# For Video Input
elif source_option == "Video":
    uploaded_video = st.file_uploader("Upload a video", type=["mp4", "mov", "avi"])
    
    if uploaded_video is not None:
        st.video(uploaded_video)
        video_path = "uploaded_video.mp4"
        with open(video_path, "wb") as f:
            f.write(uploaded_video.read())
        
        # Video processing and detection
        if st.button("Process Video"):
            with st.spinner('Processing...'):
                cap = cv2.VideoCapture(video_path)

                width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                fps = int(cap.get(cv2.CAP_PROP_FPS))

                stframe = st.empty()  
                severe_detected = False  

                while cap.isOpened():
                    ret, frame = cap.read()
                    if not ret:
                        break

                   
                    results, detected_in_frame = detect_objects(frame)
                    if detected_in_frame:
                        severe_detected = True

                    result_frame = results[0].plot()

                    
                    stframe.image(result_frame, channels="BGR")

                cap.release()

                
                if severe_detected:
                    send_alert()

# For Webcam Input
elif source_option == "Webcam":
    st.write("Webcam will start shortly...")

    def process_webcam():
        cap = cv2.VideoCapture(0)  # Use 0 for webcam
        stframe = st.empty()  
        severe_detected = False

        while True:
            ret, frame = cap.read()
            if not ret:
                break
            results, detected_in_frame = detect_objects(frame)
            if detected_in_frame:
                severe_detected = True
            result_frame = results[0].plot()
            stframe.image(result_frame, channels="BGR")

        cap.release()

        if severe_detected:
            send_alert()

    if st.button("Start Webcam Detection"):
        process_webcam()
