from ultralytics import YOLO
import glob

# get image files
image_files = glob.glob("datasets/valid/images/" + "*")

# Load the model.
model = YOLO('./runs/detect/epoch_5002/weights/best.pt')

for i in range(len(image_files)):
    model.predict(image_files[i], save=True)