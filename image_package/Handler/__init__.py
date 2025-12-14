from PIL import Image

class ImageHandler():
    def __init__(self, path):
        self.path = path
    
    def image_load(self):
        #Загрузка изображения
        try:
            image = Image.open(f"{self.path}")
            self.image = image
        except Exception as e:
            raise TypeError("Неправильно задан путь")

    def size_change(self):
        try:
            self.image = Image.open(f"{self.path}")
            print(f" Изображение загружено: {self.image.size}")
        except Exception as e:
            raise TypeError(f"Ошибка загрузки: {e}")
        #Изменение размера
        try:
            width = int(input("Введите новую ширину изображения (300): "))
            heigth = int(input("Введите новую высоту изображения (300): "))
            new_size = (width, heigth)
            self.image = self.image.resize(new_size)
        except ValueError:
            raise ValueError("Некорректный ввод чисел для размера")
        

    def image_save_png(self, new_path):
        #Сохранение изображения
        if self.image is None:
            raise ValueError("Сначала загрузите изображение (вызовите image_load())")
        try:
            agree = input("Вы уверены что хотите сохранить изображение - (да\нет): ")
            if agree == "да":
                self.image.save(new_path, "PNG")
            else:
                print("Сохранение отменено")
        except Exception as e:
            raise TypeError(f"Ошибка: {e}")
        

    


