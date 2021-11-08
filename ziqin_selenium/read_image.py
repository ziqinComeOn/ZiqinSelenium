#coding=utf-8
import pytesseract
from PIL import Image
from util.ShowapiRequest import ShowapiRequest
image = Image.open("图片路径")
text = pytesseract.image_to_string(image)
print(text)

