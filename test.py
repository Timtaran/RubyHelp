from PIL import Image, ImageChops
image_1_t=Image.open('photo1.jpg')
image_2_t=Image.open('photo2.jpg')
image_1=image_1_t.crop((300, 195, 850, 635)) 
image_2=image_2_t.crop((300, 195, 850, 635)) 
result=ImageChops.difference(image_1, image_2)

#Вычисляет ограничивающую рамку ненулевых областей на изображении.
print(result.getbbox()) 

# result.getbbox() в данном случае вернет (0, 0, 888, 666)
result.save('result.jpg')