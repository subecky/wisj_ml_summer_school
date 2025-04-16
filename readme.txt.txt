1. Please put 40images and labels in the following folders for training purpose

datasets/train/images/
datasets/train/labels/

2. Please put remaining 10images and labels in the following folders for testing purpose

datasets/valid/images/
datasets/valid/labels/

3. Please change the name of class as densha instead of Amyloid in the following file

datasets/classes

4. Please change the name of class as densha instead of Amyloid in the following file

custom_data.yaml

5. Please run the following command to start training from the anaconda environment where you install YOLOv8 library

python main.py

6. Please run the following file to predict densha one image at a time.

python predict.py