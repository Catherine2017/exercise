import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def rndChar():
    return chr(random.randint(65, 90))

def rndColor():
    return (random.randint(64, 255), random.randint(64, 255),
            random.randint(64, 255))

def rndColor1():
    return (random.randint(32, 127), random.randint(32, 127),
            random.randint(32, 127))

def get_code(outfile, form):
    width = 60*4
    height = 60
    image = Image.new("RGB", (width, height), (255, 255, 255))
    font = ImageFont.truetype("arial.ttf", 36)
    draw = ImageDraw.Draw(image)
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=rndColor())

    for i in range(4):
        draw.text((60*i + 10, 10), rndChar(), font=font, fill=rndColor1())

    image = image.filter(ImageFilter.BLUR)
    image.save(outfile, form)

get_code('../data/code.jpg', 'jpeg')
