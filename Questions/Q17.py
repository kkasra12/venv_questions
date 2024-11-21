from PIL import Image, ImageDraw

img = Image.new("RGB", (200, 200), "white")
draw = ImageDraw.Draw(img)
draw.ellipse((50, 50, 150, 150), fill="yellow", outline="black")
draw.ellipse((75, 75, 90, 90), fill="black")
draw.ellipse((110, 75, 125, 90), fill="black")
draw.arc((75, 100, 125, 125), start=0, end=180, fill="black")

img.show()
