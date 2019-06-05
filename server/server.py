from flask import Flask
from flask import jsonify
from flask import send_file
from flask_cors import CORS
from PIL import Image, ImageFilter, ImageDraw, ImageFont
import glob, os
import random
import logging
import PIL
import base64
from io import BytesIO

app = Flask(__name__)

CORS(app)

def drawText(image, text, coordinates):
    font = ImageFont.truetype('Arial Black.ttf', 500)
    draw = ImageDraw.Draw(image)
    color = 'rgb(0, 0, 0)'

    draw.text((coordinates[0], coordinates[1]), text, fill=color)

@app.route('/generate', methods=['GET'])
def generate():
    BAND_NAMES = ['Porkchop Water', 'The Beets', 'Cooper and the Footies', 'Maggie Misdemeaner Elliot']
    ALBUM_TITLES = ['Arghhh', 'I have something stuck in my throat', 'Is this real life']
    IMAGE_ANGLES = [45, 90, 180, 360]
    IMAGE_FILTERS = [
        ImageFilter.BLUR,
        ImageFilter.CONTOUR,
        ImageFilter.DETAIL,
        ImageFilter.EDGE_ENHANCE,
        ImageFilter.EDGE_ENHANCE_MORE,
        ImageFilter.EMBOSS,
        ImageFilter.FIND_EDGES,
        ImageFilter.SHARPEN,
        ImageFilter.SMOOTH,
        ImageFilter.SMOOTH_MORE
    ]
    processed_images = []
    index = 0
    images = glob.glob('./assets/album_art/*')
    random_image = random.choice(images)

    current_image = Image.open(random_image)

    resized_image = current_image.resize((300, 350), PIL.Image.ANTIALIAS)

    album_title = random.choice(ALBUM_TITLES)
    band_name = random.choice(BAND_NAMES)

    (x, y, r, b) = resized_image.getbbox();
    SPACING = len(album_title) * 8

    drawText(resized_image, album_title, (r - SPACING, b - SPACING))
    drawText(resized_image, band_name, (100, 100))

    resized_image.rotate(random.choice(IMAGE_ANGLES))
    resized_image.filter(random.choice(IMAGE_FILTERS))

    album_name = 'album_art-' + str(index);

    buffered = BytesIO()
    resized_image.save(buffered, 'png', optimize=True)
    
    return base64.b64encode(buffered.getvalue())
        
    