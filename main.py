import tkinter as tk
from tkinter import filedialog
import PIL.Image
import math



def resize(image, width=400):
    """
        Resize an image while maintaining the aspect ratio.

        Args:
            image: PIL.Image.Image
                The input image to be resized.
            width: int, optional
                The desired width of the resized image. Default is 400.

        Returns:
            PIL.Image.Image
                The resized image with the specified width and proportional height.

        """
    new_height = math.floor(width / 2)

    return image.resize((width, new_height))


def to_greyscale(image):
    """
     Convert an image to grayscale.

     Args:
         image: PIL.Image.Image
             The input image to be converted.

     Returns:
         PIL.Image.Image
             The grayscale version of the input image.

     """
    return image.convert("L")


def pixel_to_ascii(image):
    """
     Convert an image to ASCII art representation.

     Args:
         image: PIL.Image.Image
             The input image to be converted.

     Returns:
         str
             The ASCII art representation of the input image.

     """
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        ascii_str += ASCII[math.floor(pixel / 4)]
    return ascii_str


ASCII = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,'. "


def makeascii(filename):
    """
       Convert an image to ASCII art and save it to a file.

       Args:
           filename: str
               The path to the input image file.

       Returns:
           None

       """
    global ascii
    try:
        image = PIL.Image.open(filename)


    except:
        print("A kép nem található")

    image = resize(image)
    grey = to_greyscale(image)

    ascii_str = pixel_to_ascii(grey)

    width = grey.width
    art = ""

    for i in range(0, len(ascii_str), width):
        art += ascii_str[i:i + width] + "\n"

    with open("ascii.txt", "w") as f:
        f.write(art)

    popup()


win = tk.Tk()
win.title("Ascii art készítés")

# Get the screen width and height
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

# Calculate the x and y coordinates for the window to be centered
x = int((screen_width / 2) - (win.winfo_reqwidth() / 2))-150
y = int((screen_height / 2) - (win.winfo_reqheight() / 2))
# Set the window position
win.geometry(f"+{x}+{y}")

win.resizable(False, False)
my_font1 = ('times', 18, 'bold')
l1 = tk.Label(win, text='Upload a photo to make an ASCII art', width=30, font=my_font1)
l1.grid(row=1, column=1)
b1 = tk.Button(win, text='Upload File', width=20, command=lambda: open_jpg_file())
b1.grid(row=2, column=1)


def open_jpg_file():
    global img
    f_types = [('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    makeascii(filename)


def popup():
    """
      Open a popup window to display a success message after generating ASCII art.

      Returns:
          None

      """
    popup_window = tk.Toplevel()

    popup_window.title("")

    label = tk.Label(popup_window,
                     text="Sikeres generálás! A kész ASCII artot a program mappájában ascii.txt néven találja.")

    label.pack()

    popup_window.grab_set()
    popup_window.focus_set()
    popup_window.wait_window()


win.mainloop()
