from django.db import models
from djrichtextfield.models import RichTextField

class DateTimeStamp(models.Model):
    created = models.DateTimeField('Created', auto_now=True)
    updated = models.DateTimeField('Updated', auto_now_add=True)

    class Meta:
        abstract = True


class Category(DateTimeStamp):
    name = models.CharField('Имя категории', max_length=25, unique=True)
    url = models.URLField('Url', blank=True)
    email = models.EmailField ('Email', blank=True)
    description = RichTextField ('Описание', blank=True)
    activate = models.BooleanField('Active', default=False)
    image = models.URLField('Image URL', blank=True)



    class Meta:
        verbose_name= "Категория"
        verbose_name_plural = "Категории"
        ordering = ["-name"]

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField('Имя товару', max_length=25, unique=True)
    uuid = models.UUIDField ('UUID')

    class Meta:
        verbose_name= "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.name


class Parametr(models.Model):
    name = models.CharField('Параметр Товара', max_length=25, unique=True)

    class Meta:
        verbose_name= 'Параметр'
        verbose_name_plural = 'Параметры'

    def __str__(self):
        return self.name


class Goods(DateTimeStamp):
    name = models.CharField('Имя товару', max_length=25, unique=True)
    description = RichTextField('Описание', blank=True)
    price = models.FloatField('Price', default=0)
    activate = models.BooleanField('Active', default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='goods')
    tags = models.ManyToManyField(Tag, related_name='goods_tag')
    image = models.ImageField('Image', upload_to='image', blank=True)
    parametr = models.ForeignKey(Parametr, on_delete=models.CASCADE, related_name='parametr', null=True, blank=True)

    class Meta:
        verbose_name= "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name
