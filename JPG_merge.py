from PIL import Image
import os

# -------------------------------------------------------------
# put here the name of the folder containing JPG files to merge
# -------------------------------------------------------------
folder = "JPG_folder"

# -------------------------------------------------------------
# so the script will read all the files with these extensions into that folder
# -------------------------------------------------------------
x = [a for a in os.listdir(folder) if a.endswith(".jpg") or a.endswith(".jpeg")]

imagelist = []

for jpg in x:
    
    image = Image.open(r'' + folder + '/' + jpg)
    im = image.convert('RGB')
    imagelist.append(im)


# -------------------------------------------------------------
#  ...and save into the file named below. Just adjust as you want
# -------------------------------------------------------------
im.save(r'mergedImages.pdf',save_all=True, append_images=imagelist)