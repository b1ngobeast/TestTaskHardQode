from django.db import models
from django.contrib.auth.models import User


# Продукт

class Product(models.Model):
    product_id = models.IntegerField(blank=True, unique=True, primary_key=True)
    creator = models.ForeignKey(User, on_delete=models.PROTECT, related_name='Создатель', blank=True)
    name = models.TextField(blank=True)
    price = models.IntegerField(blank=True)
    min_users = models.IntegerField()
    max_users = models.IntegerField()
    date_started = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


## Уроки в продукте ##
class Lesson(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    name = models.TextField(blank=True)
    link = models.CharField(max_length=200)


##Группы##
## По задумке группы добавляются по необходимости, вручную, чтобы во всех группах не было min_users ##
class Group(models.Model):
    group = models.IntegerField(unique=True, blank=True, primary_key=True)
    product_name = models.ForeignKey(Product, on_delete=models.PROTECT)
    num_in_product = models.IntegerField()  # Чтобы видеть, сколько групп в продукте


## Таблица студентов в группах ##
class StudentInGroup(models.Model):
    group_id = models.ForeignKey(Group, on_delete=models.PROTECT)
    student_id = models.ForeignKey(User, on_delete=models.CASCADE)


## Таблица связности для понимания, есть ли у пользователя доступ к продукту ##


class AccessList(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.PROTECT)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

