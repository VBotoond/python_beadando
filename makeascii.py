import PIL.Image
import math


def resize(image, width=400):
    #old_w, old_h=image.size
    #new_height=math.floor(width*old_h/old_w)
    new_height=math.floor(width/2)

    return image.resize((width, new_height))

def to_greyscale(image):
    return image.convert("L")

def pixel_to_ascii(image):
    pixels=image.getdata()
    ascii_str=""
    for pixel in pixels:

        ascii_str+=ASCII[math.floor(pixel/4)]
    return ascii_str

ASCII="$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,'. "

def makeascii(filename):
    global ascii
    try:
        image = PIL.Image.open(filename)


    except:
        print("A kép nem található")

    image = resize(image)
    grey=to_greyscale(image)

    ascii_str = pixel_to_ascii(grey)

    width = grey.width
    art = ""

    for i in range(0, len(ascii_str), width):
        art += ascii_str[i:i + width] + "\n"

    with open("ascii.txt", "w") as f:
        f.write(art)

