from django.db.models import Model, CharField, ImageField, IntegerField, DateField, BooleanField, ForeignKey, DO_NOTHING

from accounts.models import CustomUser


# Create your models here.


class Category(Model):
    name = CharField(max_length=32)

    def __str__(self):
        return self.name


class Type(Model):
    name = CharField(max_length=32)

    def __str__(self):
        return self.name


class Condition(Model):
    name = CharField(max_length=32)

    def __str__(self):
        return self.name


class Notice(Model):
    name = CharField(max_length=64)
    description = CharField(max_length=256)
    image = ImageField(blank=True)
    price = IntegerField()
    pub_date = DateField()
    is_active = BooleanField(blank=True)
    type_id = ForeignKey(Type, on_delete=DO_NOTHING)
    category_id = ForeignKey(Category, on_delete=DO_NOTHING)
    condition_id = ForeignKey(Condition, on_delete=DO_NOTHING)
    user_id = ForeignKey(CustomUser, on_delete=DO_NOTHING)

    def __str__(self):
        return self.name
