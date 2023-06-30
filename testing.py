import numpy as np
import time

dict = {
    0:
        {"min":1,
        "med":3,
         "max":5},
    1:
        {"min":6,
        "med":8,
         "max":10},
    2:
        {"min":11,
        "med":12,
         "max":15},
    3:
        {"min":16,
        "med":16,
         "max":20},

}


a = [
    [[1,2,3],
     [4,5,6]],

    [[7,8,9],
     [10,11,12]],

    [[13,14,15],
    [16,17,18]]
]


array = np.array(a)

print(array)
now = time.time()

for diapason in dict:
    array [(array <= dict[diapason]["max"]) & (array >= dict[diapason]['min']) ] = dict[diapason]["med"]

time = time.time() - now
print(array)
print(time)

for nr in range(10):
    print(nr)


from PIL import Image
file_path = 'instance/photos/Frigider_1.jpg'
img_op = Image.open(file_path)
print(img_op.size)
print(img_op.info)
print()

img_op.save('instance/photos/Puna_uscata1.jpg', quality=100)
img_op1 = Image.open('instance/photos/Puna_uscata1.jpg')

img_op1.thumbnail((100, 80))
# img_op1.save('instance/photos/Puna_uscata1.jpg')
# img_op1 = Image.open('instance/photos/Puna_uscata1.jpg')
print(img_op1.size)
print(img_op1.info)

img_op.save('instance/photos/Puna_uscata2.jpg', quality=100)
img_op2 = Image.open('instance/photos/Puna_uscata2.jpg')
print(img_op2.size)
print(img_op2.info)


      # if self.img_op.size
      #   self.img_arr = np.array(self.img_op)
      #   self.img_op.