import torch
from torch.utils.data import DataLoader
from dataset import CustomDataset
from model import get_model
from config import ANNOTATION_FILE, IMAGE_FOLDER, BATCH_SIZE, LEARNING_RATE, EPOCHS
from torchvision import transforms

def train():
    dataset = CustomDataset(ANNOTATION_FILE, IMAGE_FOLDER, transforms=transforms.ToTensor())
    dataloader = DataLoader(dataset, batch_size=BATCH_SIZE, shuffle=True)
    model = get_model(num_classes=2)
    optimizer = torch.optim.Adam(model.parameters(), lr=LEARNING_RATE)
    for epoch in range(EPOCHS):
        for images, targets in dataloader:
            loss_dict = model(images, targets)
            loss = sum(loss for loss in loss_dict.values())
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
