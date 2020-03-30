
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import array_to_img
datagen = ImageDataGenerator(
    rotation_range=40,#图像旋转角度0-180
    width_shift_range=0.2,
    height_shift_range=0.2,
    #ranges (as a fraction of total width or height) within which to randomly translate pictures vertically or horizontally
    #随机水平或垂直转换图片的范围（作为总宽度或高度的一部分）
    rescale=1./255,
    #rescale is a value by which we will multiply the data before any other processing. Our original images consist in RGB
    # coefficients in the 0-255, but such values would be too high for our models to process (given a typical learning rate),
    # so we target values between 0 and 1 instead by scaling with a 1/255. factor.
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,#水平翻转
    fill_mode='nearest'
)

img = load_img('E:/datasets/train/cat/cat.0.jpg')
x = img_to_array(img) #this is a Numpy array with shape (3, 150, 150)
x = x.reshape((1,)+ x.shape) # this is a Numpy array with shape (1, 3, 150, 150)

i = 0
for batch in datagen.flow(x,batch_size=1,
                          save_to_dir='E:/datasets/preprocess',save_format='jpeg',save_prefix='cat'):
    i += 1
    if i > 20:
        break #otherwise the generator would loop indefinitely