from PIL import Image
from PIL import ImageFilter

with Image.open("original.jpg") as file:
    print(file.size)
    print(file.format)
    
with Image.open('original.jpg') as pic_original:
    pic_original.show()

pic_gray = pic_original.convert('L')
pic_gray.save('original.jpg')
pic_gray.show()

pic_up = pic_gray.transpose(Image.ROTATE_90)
pic_up.save('original.jpg')
pic_up.show()
#open file with the original image 

#change the color of original to white and black 

#make the image blur 

#rotate o

