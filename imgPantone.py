from PIL import Image, ImageDraw, ImageFont

# drawColorAlias = "Blooming Dahlia"
# drawColorCode = "13-1520"
# drawColorHex = "#72DEC2"
# drawColorRgb = "114, 222, 194"
# filename = 'out_bot.png'

def drawPantone(drawColorAlias, drawColorCode, drawColorHex, drawColorRgb, filename):
    # Returns the name of the image file
    mode = 'RGBA'
    rat = 4
    imgW = 300
    imgH = 188
    # Golden ratio
    # We will make the image x4 bigger and then resize it to the original size, to avoid aliasing on the font
    size = (imgW*rat, imgH*rat)
    fontLogo = ImageFont.truetype('fonts/Helvetica-neue-bold.ttf', 18*rat)
    fontRegi = ImageFont.truetype('fonts/HelveticaNeue.ttf', 8*rat)
    fontCode = ImageFont.truetype('fonts/Helvetica-Regular-45W.ttf', 14*rat)
    fontTitl = ImageFont.truetype('fonts/Helvetica-neue-bold.ttf', 16*rat)
    fontData = ImageFont.truetype('fonts/Helvetica-Regular-45W.ttf', 18*rat)

    img = Image.new(mode, size, '#FFFFFF')

    # In case you wanted to use a frame
    # frame = Image.open("bg_bot2.png").convert('RGBA')
    # img.paste(frame, (0, 0), frame)

    d = ImageDraw.Draw(img)
    # greybg
    d.rectangle(((0, 0), (imgW*rat, imgW*rat)), fill='#F3F3F3')
    # pantonechart
    d.rectangle(((0, 118*rat), (118*rat, imgW*rat)), fill='#FFFFFF')
    d.rectangle(((0, 0), (118*rat, 118*rat)), fill=drawColorHex)

    d.text((6*rat,125*rat), "PANTONE", font=fontLogo, fill=(0, 0, 0))
    d.text((95*rat,128*rat), "®", font=fontRegi, fill=(0, 0, 0))
    d.text((150*rat,22*rat), "Hexadecimal", font=fontTitl, fill=(0, 0, 0))
    d.text((150*rat,102*rat), "RGB", font=fontTitl, fill=(0, 0, 0))

    d.text((6*rat,147*rat), drawColorCode, font=fontCode, fill=(0, 0, 0))
    d.text((6*rat,165*rat), drawColorAlias, font=fontCode, fill=(0, 0, 0))
    d.text((170*rat,48*rat), drawColorHex, font=fontData, fill=(0, 0, 0))
    d.text((170*rat,128*rat), drawColorRgb, font=fontData, fill=(0, 0, 0))

    img_final = img.resize((imgW,imgH), resample=Image.ANTIALIAS)
    img_final.save(filename, format='png')
    # img_final.show()

    return filename
