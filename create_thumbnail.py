from PIL import Image, ImageDraw, ImageFont

img = Image.new('RGB', (1280, 720), color=(73, 109, 137))
draw = ImageDraw.Draw(img)
draw.text((100, 300), "5 Passive Income Ideas", fill=(255, 255, 255))
img.save("output/thumbnail.png")
