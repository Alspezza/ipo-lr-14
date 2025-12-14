from image_package.Handler import ImageHandler
from image_package.Processor import ImageProcessor

#C:\Users\user\Desktop\Лабы и тп\ИПО\lr14\картинки\image_1.jpg

choose = int(input("Введите номер изменяемой картинки (1-5): "))

if choose == 1:
    image1 = ImageHandler("картинки\\image_1.jpg")
    image1.image_load()
    image1.size_change()
    image1.image_save_png("картинки\\image_1_new.png")

    image1_result = ImageProcessor("картинки\\image_1_new.png")
    image1_result.image_loading()
    image1_result.add_blur()
    image1_result.add_text()
    image1_result.save_result("картинки\\result1.png")
    print("\nОбработка фотки прошла успешно")

elif choose == 2:
    image1 = ImageHandler("картинки\\image_2.jpg")
    image1.image_load()
    image1.size_change()
    image1.image_save_png("картинки\\image_2_new.png")

    image1_result = ImageProcessor("картинки\\image_2_new.png")
    image1_result.image_loading()
    image1_result.add_blur()
    image1_result.add_text()
    image1_result.save_result("картинки\\result2.png")
    print("\nОбработка фотки прошла успешно")

elif choose == 3:
    image1 = ImageHandler("картинки\\image_3.jpg")
    image1.image_load()
    image1.size_change()
    image1.image_save_png("картинки\\image_3_new.png")

    image1_result = ImageProcessor("картинки\\image_3_new.png")
    image1_result.image_loading()
    image1_result.add_blur()
    image1_result.add_text()
    image1_result.save_result("картинки\\result3.png")
    print("\nОбработка фотки прошла успешно")

elif choose == 4:
    image1 = ImageHandler("картинки\\image_4.jpg")
    image1.image_load()
    image1.size_change()
    image1.image_save_png("картинки\\image_4_new.png")

    image1_result = ImageProcessor("картинки\\image_4_new.png")
    image1_result.image_loading()
    image1_result.add_blur()
    image1_result.add_text()
    image1_result.save_result("картинки\\result4.png")
    print("\nОбработка фотки прошла успешно")

elif choose == 5:
    image1 = ImageHandler("картинки\\image_5.jpg")
    image1.image_load()
    image1.size_change()
    image1.image_save_png("картинки\\image_5_new.png")

    image1_result = ImageProcessor("картинки\\image_5_new.png")
    image1_result.image_loading()
    image1_result.add_blur()
    image1_result.add_text()
    image1_result.save_result("картинки\\result5.png")
    print("\nОбработка фотки прошла успешно")

else:
    print("\nВведен неверный номер изображения")
    



