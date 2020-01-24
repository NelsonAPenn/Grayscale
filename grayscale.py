from PIL import Image, ImageFilter

def dot(a, b):
    return sum([ a[i] * b[i] for i in range(len(a))])
print("Enter filename: ")
name = input()
with Image.open(name) as im:
    pixList= list(im.getdata())
    n = len(pixList[0])
    lvec = [1 for i in range(n)]
    px = im.load()

    for r in range(im.size[0]):
        for c in range(im.size[1]):
            px[r, c] = tuple([ int(dot(px[r, c], lvec) / dot(lvec, lvec)) for i in range(n)])

    splitName = name.split(".")
    im.save(splitName[0] + "_transformed." + splitName[1])
