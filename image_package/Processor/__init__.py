from ..Handler import ImageHandler
from PIL import Image, ImageFilter, ImageDraw, ImageFont


class ImageProcessor():
    def __init__(self, path):
        self.path = path
        self.image_bl = None  
        self.draw = None 
        self.result = None

    def image_loading(self):
        #Загрузка изображения
        try:
            image = Image.open(f"{self.path}")
            self.image = image
        except Exception as e:
            raise TypeError("Неправильно задан путь")

    
    def add_blur(self):
        self.image_bl = self.image.filter(ImageFilter.BLUR)
        

    def add_text (self, text="Вариант 1", position=(200, 250), color="white"):
        #Создаем холст 
        self.draw = ImageDraw.Draw(self.image_bl)
        #Добавляем текст
        font = ImageFont.truetype("arialbd.ttf", 15)
        self.draw.text(position, text, fill=color, font = font)
        self.result = self.image_bl 

    def save_result(self, path):
        try:
            self.result.save(path)
        except Exception as e:
            raise Exception(f"Ошибка в сохранении файла: {e}")

            