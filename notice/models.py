from django.db import models

from accounts.models import CustomUser


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Condition(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Notice(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    image = models.ImageField(blank=True)
    price = models.IntegerField()
    pub_date = models.DateField()
    is_active = models.BooleanField(blank=True)
    type_id = models.ForeignKey(Type, on_delete=models.DO_NOTHING)
    category_id = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    condition_id = models.ForeignKey(Condition, on_delete=models.DO_NOTHING)
    user_id = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
