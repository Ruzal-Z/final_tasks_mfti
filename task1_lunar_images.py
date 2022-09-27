from PIL import Image # считаем картинку в numpy array
import numpy as np

def update_img(f_name):
    img = Image.open(f_name)
    data = np.array(img)
    updated_data = [(i - np.min(data)) * (255 // ((np.max(data)) - (np.min(data)))) for i in data]
    updated_data = np.array(updated_data )
    res_img = Image.fromarray(updated_data)
    res_img.save(f'lunar_images/new_lunar{f_name[-10:-8]}_raw.jpg')
    res_img.show()

update_img('lunar_images/lunar01_raw.jpg')
update_img('lunar_images/lunar02_raw.jpg')
update_img('lunar_images/lunar03_raw.jpg')


