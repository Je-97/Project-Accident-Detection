![RASD logo](https://github.com/user-attachments/assets/0d3a4f96-9f51-48e3-93b5-1fcd4174fe20)

# Accident Deection Projct
## (Real-Time Accident Detection and Classification for Enhanced Analysis)
This is a capstone project for Zeham Management Bootcamp.

# Overview:
Traffic congestion is a major issue in rapidly growing cities like Riyadh, with traffic accidents being a key contributor. These accidents not only cause delays but also pose safety risks and strain emergency response times. Our project aims to develop an automatic accident detection system using on-road surveillance cameras and the YOLO model to detect incidents in real time. The system categorizes accidents as either “accident” or “severe” and immediately alerts authorities for quick action. This project aligns with Saudi Arabia’s Vision 2030, supporting smart city development and improved road safety and traffic management.

# Dashboard:
We surveyed Riyadh residents to understand how accidents affect daily traffic flow. The survey explored residents' perceptions of congestion caused by accidents and its impact on the city’s transportation network. Results findings are presented in a dashboard, offering a clear visualization of respondents' feedback.
![image](https://github.com/user-attachments/assets/71651012-7e89-4dc5-91a4-f14ea0e4213e)

# Solution Architecture
![image](https://github.com/user-attachments/assets/fcae5308-e07d-4a3a-82c2-0ee863823a31)

# Dataset
Source: 12,000 images from Roboflow, labeled into two classes: Accident and Severe Accident.
Additional Data: 461 images sourced from YouTube videos were added to enrich the dataset.
Preprocessing: Images were resized to 640x640, with noise and blur augmentation applied to enhance model generalization.
1. [Roboflow](https://universe.roboflow.com/accident-test-set/accident-test-set/dataset/4).
2. youtube videos for accident.

# Model & Result 
Model: YOLOv8
Training Configuration: 50 epochs, batch size of 16.
Performance Metrics:
- mAP@0.5: 93%
- Recall: 85%
- Precision: 92%
   ![image](https://github.com/user-attachments/assets/2adf6868-1d9a-4e27-a4b4-b1e59930f782)

   
# Tools used

| Feature       | Tools                        |
|---------------|------------------------------|
| Dashboard     | Power BI - Python (Word Cloud) |
| Build Model   | YOLOv8                       |
| Workspace     | Colab - VS Code             |
| Deployment    | Streamlit                   |
| Notification  | Twilio                      |

# Challenges
The primary challenge involved the dataset's complexity. Initially, the model misclassified large vehicles, like trucks, as accidents. We addressed this by adding more diverse images and creating a new class in the YAML configuration, improving the model's accuracy.

 ![image](https://github.com/user-attachments/assets/0aca61f5-6c29-483f-859f-2deef5cab99c)


 # Demo



https://github.com/user-attachments/assets/c39f19da-5f78-4026-b865-3355fd9df104


# Future Work 
Adding more classes to capture different types of road incidents.
Deploying the model on dashcams in passing vehicles to further improve real-time response capabilities.
Diversifying the dataset to enhance performance in varying traffic conditions.

# Conclusion
This project demonstrates significant potential for improving road safety and reducing response times for accidents. By enabling faster identification and categorization of incidents, authorities can take swift action to manage traffic and ensure safer roads.

# Team Members:
1. Haya Almalki
2. Jehan Almutairi
3. Hanan Mohammed
