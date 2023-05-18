# ASCII Art Generator

The ASCII Art Generator is a Python application that allows you to convert images into ASCII art. It provides a simple graphical user interface using tkinter.

## Usage

1. Clone the repository or download the source code.

2. Open a terminal or command prompt and navigate to the project directory.

3. Run the following command to start the application: `python ascii_art_generator.py`

4. The application window will appear. Click on the "Upload File" button to select a JPG image file.

5. After selecting the image, the application will generate the ASCII art and save it as `ascii.txt` in the program's directory.

6. A popup window will appear, indicating a successful generation. You can find the generated ASCII art in the `ascii.txt` file.

- To change the default width of the ASCII art, modify the `width` parameter in the `resize` function in the `ascii_art_generator.py` file.
- To modify the ASCII characters used for the conversion, you can update the `ASCII` string in the `pixel_to_ascii` function.
