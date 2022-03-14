import layoutparser as lp
import cv2
from PIL import Image
import pdf2image
model = lp.AutoLa
model = lp.model.auto_layoutmodel.AutoLayoutModel()
image = pdf2image.convert_from_path("cours.pdf")
model = lp.model.auto_layoutmodel.AutoLayoutModel()
layout = model.detect(image[0])
print(layout)