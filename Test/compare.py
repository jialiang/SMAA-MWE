from PIL import Image
from os import listdir
from os.path import isfile, join

filenames = listdir("myOutput")

for filename in filenames:

    i1 = Image.open("myOutput/" + filename)
    i2 = Image.open("refOutput/" + filename)

    rgb1 = Image.new("RGBA", i1.size)
    rgb2 = Image.new("RGBA", i2.size)

    rgb1.paste(i1)
    rgb2.paste(i2)

    pairs = zip(rgb1.getdata(), rgb2.getdata())

    diff = [
        abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + abs(p1[2] - p2[2])
        for p1, p2 in pairs
    ]

    print(filename)
    print("Largest Difference (bits):", max(diff))
    print("Affected Pixels %:", len(list(filter(None, diff))) / len(diff) * 100)
    print("")
