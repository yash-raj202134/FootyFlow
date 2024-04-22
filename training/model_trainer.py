from ultralytics import YOLO
import os

# Define the model and training parameters

model_path = 'models/yolov5x.pt'  # Path to the YOLOv5x pre-trained model
data_path = 'training/football-players-detection-1/data.yaml'  # Path to the data.yaml file from the dataset


epochs = 1  # Number of epochs to train
imgsz = 640  # Image size for training

# # Initialize the model
model = YOLO(model_path)

# Train the model using the specified parameters
results = model.train(
    data=data_path,  # Path to data.yaml file
    epochs=epochs,  # Number of epochs
    imgsz=imgsz  # Image size
)

# Output training results (optional)
print("Training complete.")
print("Results:", results)
