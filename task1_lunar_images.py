from PIL import Image # считаем картинку в numpy array
import numpy as np

img = Image.open('lunar_images\lunar03_raw.jpg')
data = np.array(img)

ar = [(i - np.min(data)) * (255 //((np.max(data))-(np.min(data)))) for i in data]

updated_data = np.array(ar)
res_img = Image.fromarray(updated_data)
res_img.save('new_lunar3_raw.jpg')
