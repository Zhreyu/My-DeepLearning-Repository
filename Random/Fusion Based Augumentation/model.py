import torchvision.models as models
import torch.nn as nn
class TwoStreamNetwork(nn.Module):
    def __init__(self):
        super(TwoStreamNetwork, self).__init__()
        
        # replace with modifed resnet 
        self.hf_resnet = models.resnet18(pretrained=True)
        self.lf_resnet = models.resnet18(pretrained=True)
        
        # Removing the last layer to get features
        self.hf_resnet = nn.Sequential(*list(self.hf_resnet.children())[:-1])
        self.lf_resnet = nn.Sequential(*list(self.lf_resnet.children())[:-1])
        
        # Fusion layers
        self.fc1 = nn.Linear(512, 256)
        self.fc2 = nn.Linear(256, 2)  # Assuming binary classification
        
    def forward(self, hf_image, lf_image):
        hf_features = self.hf_resnet(hf_image)
        lf_features = self.lf_resnet(lf_image)
        
        # Fusion
        combined_features = hf_features + lf_features
        x = combined_features.view(combined_features.size(0), -1)
        x = self.fc1(x)
        x = self.fc2(x)
        
        return x