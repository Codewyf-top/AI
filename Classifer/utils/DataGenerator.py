
import torchvision.transforms as tfs
from PIL import Image
import matplotlib.pyplot as plt



img_path = "E:/datasets/train/cat/cat.0.jpg"

im_aug = tfs.Compose([
        tfs.ToTensor(),
        tfs.RandomCrop(96),
        tfs.RandomHorizontalFlip(),  # default 0.5
        tfs.RandomRotation(15),
        tfs.ColorJitter(brightness=0.5, contrast=0.5, hue=0.5),  # 认为会添加模型噪声

        tfs.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
if __name__ == '__main__':
    img = Image.open(img_path).convert('RGB')
    # mg = Image.resize((96,96))
    img = tfs.ToTensor(img)
    img = im_aug(img)
    # img.show()
    plt.imshow(img)
    plt.show()


