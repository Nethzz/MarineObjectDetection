Object Detection Using Mask R-CNN





📌 Overview
This project implements Mask R-CNN for object detection and instance segmentation. The model detects objects in images and generates both bounding boxes and pixel-level masks. The application focuses on maritime safety and rescue by accurately identifying objects in the maritime domain.

🚀 Technologies Used
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


Clone the Repository

git clone https://github.com/your-username/object-detection-mask-rcnn.git
cd object-detection-mask-rcnn



## Folder Structure
```
mask_rcnn_project/
│── config.py       # Configuration settings
│── dataset.py      # Custom dataset class for loading images and annotations
│── model.py        # Model definition using Mask R-CNN
│── train.py        # Training script
│── main.py         # Entry point to start training
```



## Usage
- Modify `config.py` to set the correct paths for your dataset.
- Start training:
   ```sh
   python main.py
   ```

## File Descriptions


### config.py
Stores configuration settings like dataset paths, batch size, and learning rate.

### dataset.py
Defines a `CustomDataset` class to load images and annotations.

### model.py
Loads a pre-trained Mask R-CNN model and modifies it for custom classes.

### train.py
Handles the training loop, optimizing the model using PyTorch.

### main.py
Runs the training process.




🤝 Contributors
Neethu Vasundharan Sheeja – Developer

