import imageio.v3 as iio

filenames = [
    "images/frame1.png",
    "images/frame2.png",
    "images/frame3.png",
]
images = []

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite("output/my_gif.gif", images, duration=300, loop=0)

print("Created output/my_gif.gif!")
