from django.db import models


class Product(models.Model):
    name = models.CharField('Наименование - RU', max_length=100, unique=True)
    name_en = models.CharField('Наименование - EN', max_length=100, unique=True, null=True)


    class Meta:
        verbose_name = 'Продукты'
        verbose_name_plural = 'Продукт'

    def __str__(self):
        return f'{self.name} -'f'{self.name_en}' if self.name_en != None else self.name




class Invoice(models.Model):
    number = models.CharField(max_length=255, null=True)
    products = models.ManyToManyField(Product, through="ProductInvoice")
    phone = models.CharField('Телефон', max_length=255)
    receiver = models.CharField('Получатель', max_length=255)
    sender = models.CharField('Отправитель', max_length=255)
    weight = models.CharField(max_length=255, null=True)
    date = models.CharField(max_length=255, null=True)
    total = models.IntegerField(default=0, null=True)
    passport_seria = models.CharField('Паспорт (серия)', max_length=100, unique=True, null=True)
    address = models.CharField('Адрес', max_length=100, null=True)

    class Meta:
        verbose_name = 'Счет фактрура'
        verbose_name_plural = 'Счет фактрура'

    def __str__(self):
        return f'{self.receiver} | {self.sender}'


class ProductInvoice(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    product_count = models.IntegerField(default=0)
    price = models.IntegerField('Цена', default=0)



    class Meta:
        verbose_name = 'Фактура'
        verbose_name_plural = 'Фактура'

    def __str__(self):
        return f'{self.product}'
