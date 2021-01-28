# Method 1
from PIL import Image
path = r'C:\..\Image-to-PDF-Python\Sample-Image.jpg'
pdf = Image.open(path)
pdf.save(r'C:\..\Sample-Image.pdf')

# Method 2
import img2pdf

with open(r'C:\..\Sample-Image.pdf', 'wb') as f:
    f.write(img2pdf.convert(r'C:\..\Image-to-PDF-Python\Sample-Image.jpg'))