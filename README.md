Object Detection Using Mask R-CNN





📌 Overview
This project implements Mask R-CNN for object detection and instance segmentation. The model detects objects in images and generates both bounding boxes and pixel-level masks. The application focuses on maritime safety and rescue by accurately identifying objects in the maritime domain.

🚀 Technologies Used
Google Colab – Model training and evaluation
Python – Programming language
PyTorch – Deep learning framework
Torchvision – Pre-trained models and transformations
OpenCV – Image processing
Matplotlib & Seaborn – Visualization

📂 Dataset
Used a maritime dataset containing labeled objects for detection and segmentation.
Data preprocessing includes resizing, normalization, and augmentation.


🏋️‍♂️ Training Process
Backbone: ResNet + Feature Pyramid Network (FPN)
Loss Function: Combination of classification, bounding box regression, and mask loss
Evaluation Metrics: Mean IoU, mAP (Mean Average Precision)


🎯 Results
Achieved high-accuracy object detection with precise segmentation.
Optimized performance for real-world maritime applications.


📌 Installation & Usage


1️⃣ Clone the Repository

git clone https://github.com/your-username/object-detection-mask-rcnn.git
cd object-detection-mask-rcnn


2️⃣ Install Dependencies
pip install -r requirements.txt


🤝 Contributors
Neethu Vasundharan Sheeja – Developer

