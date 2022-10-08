from django.db.models import \
    Model, CharField, ImageField, IntegerField, \
    DateField, BooleanField, ForeignKey, TextField, DO_NOTHING

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

    def img_upload_path(instance, filename):
        return f'{instance.user.id}/images/{filename}'

    name = CharField(max_length=64)
    description = TextField()
    image = ImageField(blank=True, upload_to=img_upload_path)
    price = IntegerField()
    pub_date = DateField(auto_now_add=True)
    is_active = BooleanField(blank=True, default=True)
    type = ForeignKey(Type, on_delete=DO_NOTHING)
    category = ForeignKey(Category, on_delete=DO_NOTHING)
    condition = ForeignKey(Condition, on_delete=DO_NOTHING)
    user = ForeignKey(CustomUser, on_delete=DO_NOTHING)

    def __str__(self):
        return self.name

