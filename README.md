<img src="https://github.com/user-attachments/assets/4e3480b8-926c-4da0-8792-119bc9c2272f" alt="Logo" width="200"/>


# Accident Deection Projct
## (Real-Time Accident Detection and Classification for Enhanced Analysis)
This is a capstone project for Zeham Management Bootcamp.

# Overview:
Traffic congestion is a major issue in rapidly growing cities like Riyadh, with traffic accidents being a key contributor. These accidents not only cause delays but also pose safety risks and strain emergency response times. Our project aims to develop an automatic accident detection system using on-road surveillance cameras and the YOLO model to detect incidents in real time. The system categorizes accidents as either “accident” or “severe” and immediately alerts authorities for quick action. This project aligns with Saudi Arabia’s Vision 2030, supporting smart city development and improved road safety and traffic management.

# Dashboard:
We surveyed Riyadh residents to understand how accidents affect daily traffic flow. The survey explored residents' perceptions of congestion caused by accidents and its impact on the city’s transportation network. Results findings are presented in a dashboard, offering a clear visualization of respondents' feedback.

![image](https://github.com/user-attachments/assets/71651012-7e89-4dc5-91a4-f14ea0e4213e)

# Solution Architecture
![solution_arc](https://github.com/user-attachments/assets/539b5032-7914-4737-895d-7f6dd4dd3c4a)

# Dataset
- Approximately 12,500 images, labeled into two classes: **Accident** and **Severe**.
- Preprocessing Images were resized to 640x640, with noise and blur augmentation applied to enhance model generalization.
- Sources:
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




# Team Members:
1. Haya Almalki
2. Jehan Almutairi
3. Hanan Mohammed
