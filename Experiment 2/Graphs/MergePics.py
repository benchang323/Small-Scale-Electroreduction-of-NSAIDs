from fpdf import FPDF
from PIL import Image
import glob
import os

image_directory = 'Experiment 2/Graphs/'
extensions = ('*.jpg','*.png','*.gif')
pdf = FPDF()
imagelist=[]

for ext in extensions:
    imagelist.extend(glob.glob(os.path.join(image_directory,ext)))

for imageFile in imagelist:
    cover = Image.open(imageFile)
    width, height = cover.size

    # convert pixel in mm with 1px=0.264583 mm
    width, height = float(width * 0.264583), float(height * 0.264583)

    # given we are working with A4 format size 
    pdf_size = {'P': {'w': 210, 'h': 297}, 'L': {'w': 297, 'h': 210}}

    # get page orientation from image size 
    orientation = 'P' if width < height else 'L'

    #  make sure image size is not greater than the pdf format size
    width = width if width < pdf_size[orientation]['w'] else pdf_size[orientation]['w']
    height = height if height < pdf_size[orientation]['h'] else pdf_size[orientation]['h']

    pdf.add_page(orientation=orientation)

    pdf.image(imageFile, 0, 0, width, height)
pdf.output(image_directory + "E2-Graphs.pdf", "F")