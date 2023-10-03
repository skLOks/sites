from django.db import models

class  back(models.Model):
	cover = models.ImageField('Изображение товара', upload_to='images', blank=True)
	name = models.CharField('Имя устройства', max_length = 200)
	info = models.TextField('Информация')
	price = models.CharField('Цена', max_length = 200)