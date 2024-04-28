from django.urls import reverse

from django.db import models

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=False, verbose_name='URL')

    def __str__(self):
        return self.name


    class Meta:
        db_table = 'category'
        verbose_name = 'Категорию'
        verbose_name_plural  = 'Категории'

class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=False, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание товара')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Изображение товра')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Стоимость товара')
    discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Скидка на товар в %')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Колличество товара')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категория')



    def __str__(self):
        return self.name

    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('id',)

    def get_absolute_url(self):
        return reverse("catalog:product", kwargs={"product_slug": self.slug})

    def display_id(self):
        return f"{self.id:05}"

    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)
        return self.price