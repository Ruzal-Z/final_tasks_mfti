from PIL import Image # считаем картинку в numpy array
import numpy as np

img = Image.open('lunar_images/lunar01_raw.jpg')
data1 = np.array(img)
img = Image.open('lunar_images/lunar02_raw.jpg')
data2 = np.array(img)
img = Image.open('lunar_images/lunar03_raw.jpg')
data3 = np.array(img)

ar1 = [(i - np.min(data1)) * (255 // ((np.max(data1))-(np.min(data1)))) for i in data1]
ar2 = [(i - np.min(data2)) * (255 // ((np.max(data2))-(np.min(data2)))) for i in data2]
ar3 = [(i - np.min(data3)) * (255 // ((np.max(data3))-(np.min(data3)))) for i in data3]


updated_data = np.array(ar1)
res_img = Image.fromarray(updated_data)
res_img.save('lunar_images/new_lunar01_raw.jpg')

updated_data = np.array(ar2)
res_img = Image.fromarray(updated_data)
res_img.save('lunar_images/new_lunar02_raw.jpg')

updated_data = np.array(ar3)
res_img = Image.fromarray(updated_data)
res_img.save('lunar_images/new_lunar03_raw.jpg')
    
