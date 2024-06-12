import glob
import contextlib
from PIL import Image
import re

# Function for natural sorting (for the png files) becuase the default sorting is not in order
def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split('([0-9]+)', s)]

def gif_generate(fileName):
    # Filepaths for input PNG images and output GIF
    fp_in = fr"results/{fileName}/png/*.png"  
    fp_out = fr"results/{fileName}/outputs.gif"  

    # Use ExitStack to automatically close opened images
    with contextlib.ExitStack() as stack:
        # Find all PNG files and sort them using natural sorting
        png_files = sorted(glob.glob(fp_in), key=natural_sort_key)

        # print the files for clarity and debugging purposes
        print("Files to be included in the GIF:")
        for f in png_files:
            print(f)

        # Lazily load images, closed after use
        imgs = (stack.enter_context(Image.open(f)) for f in png_files)

        # Extract the first image from the iterator
        img = next(imgs)

        # saving the image into a GIF
        img.save(fp=fp_out, format='GIF', append_images=imgs,
                save_all=True, duration=.2, loop=0) #change duration to make long or short la

    print(f"GIF created and saved to {fp_out}")