from PIL import Image
from os import listdir
import numpy as np

filenames = listdir("myOutput")

for filename in filenames:

    i1 = Image.open("myOutput/" + filename)
    i2 = Image.open("refOutput/" + filename)

    rgb1 = Image.new("RGBA", i1.size)
    rgb2 = Image.new("RGBA", i2.size)

    rgb1.paste(i1)
    rgb2.paste(i2)

    pairs = zip(rgb1.getdata(), rgb2.getdata())

    diff = np.array([
        abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + abs(p1[2] - p2[2])
        for p1, p2 in pairs
    ])

    print(filename)
    print("Total pixels: 921600")
    print("Largest pixel difference in bits:", max(diff))
    print()
    print("Difference is 1 to 3 bits:", len(diff[(diff >= 1) & (diff <= 3)]))
    print("Difference is 4 to 6 bits:", len(diff[(diff >= 4) & (diff <= 6)]))
    print("Difference is 7 to 12 bits:", len(diff[(diff >= 7) & (diff <= 12)]))
    print("Difference is 13 to 24 bits:", len(
        diff[(diff >= 13) & (diff <= 24)]))
    print("Difference is 25 to 48 bits:", len(
        diff[(diff >= 25) & (diff <= 48)]))
    print("Difference is 49 bits and more:", len(diff[diff >= 49]))
    print()
    print()
