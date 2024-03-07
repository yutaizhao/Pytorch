from torch.utils.data import Dataset
from PIL import Image
import os

class Mydata(Dataset):

    def __init__ (self, root_dir, label_dir) :
        self.rood_dir = root_dir
        self.label_dir = label_dir
        self.img_dir = os.path.join(root_dir,label_dir)
        self.img_list = os.listdir(self.img_dir)
    
    def __getitem__ (self, idx):
        img_name = self.img_list[idx]
        img = Image.open(os.path.join(self.img_dir,img_name))
        label = self.img_dir
        return img, label

    def __len__(self):
        return len(self.img_list)
    
root_dir = "hymenoptera_data/train"
label_dir = "ants"
test_dataset = Mydata(root_dir,label_dir)

img, label = test_dataset[0]
print(len(test_dataset))
