import img2pdf

with open(r'C:\Users\Ovaiz Ali\Desktop\Development\Teach-Kolachi\Image-to-PDF-Python\Sample-Image.pdf', 'wb') as f:
    f.write(img2pdf.convert(r'C:\Users\Ovaiz Ali\Desktop\Development\Teach-Kolachi\Image-to-PDF-Python\Sample-Image.jpg'))