from PIL import Image
import matplotlib.pyplot as plt



if __name__ == '__main__':
    image_path = 'memes1/i1.jpg'

    img = Image.open(image_path)

    plt.imshow(img)
    plt.axis('off')
    plt.show()