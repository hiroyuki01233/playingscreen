import numpy as np
import PIL.ImageDraw
import math

source_file = 'dark.jpg'
source = PIL.Image.open(source_file).convert('RGBA')

# colorLists = np.array(source)
# print(len(colorLists))
# print(colorLists[0][0][2])

small_img = source.resize((100, 100))
color_arr = np.array(small_img)
w_size, h_size, n_color = color_arr.shape
color_arr = color_arr.reshape(w_size * h_size, n_color)

color_mean = np.mean(color_arr, axis=0)
color_mean = color_mean.astype(int)
color_mean = tuple(color_mean)

# imagelis = []
# clr = color_mean[0]
# clg = color_mean[1]
# clb = color_mean[2]
# times = 1.0

# for i in range(1000):
#     image1 = []
#     if i % 10 == 0:
#         if clr*times < 256: clr = math.floor(clr*times)
#         if clg*times < 256: clg = math.floor(clg*times)
#         if clb*times < 256: clb = math.floor(clb*times)
#         times = times + 0.001

#     for ii in range(500):
#         image1.append([clr,clg,clb])
#     imagelis.append(image1)
#     print("{} {} {}".format(clr,clg,clb))

# numLis = np.array(imagelis)
# print(color_mean)


# print(color_mean)

im = PIL.Image.new('RGB', (1080, 1920), color_mean).convert('RGBA')
img_clear = PIL.Image.new("RGBA", im.size, (255, 255, 255, 0))
im2 = PIL.Image.open("white.png").resize((1080, 1080)).convert('RGBA')
img_clear.paste(im2)
im = PIL.Image.alpha_composite(im, img_clear)
im.save('base.png')

whites = np.array(im2)

for i in range(1080):
    print(whites[i][0])




# im = PIL.Image.fromarray(np.uint8(numLis)).save("result.png", quality=100)