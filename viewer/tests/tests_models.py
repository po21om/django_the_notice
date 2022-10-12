from django.test import TestCase

from viewer.models import Notice, Category, Type, Condition, CustomUser


# Create your tests here.


class NoticeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Notice.objects.create(
            name="Barbie doll - ¥üЯת؁؈ق@",
            description="¥üЯת؁؈ق@ - barbie doll",
            price=-1,
            is_active=True,
            type=Type.objects.create(name='sell'),
            category=Category.objects.create(name='militaria'),
            condition=Condition.objects.create(name='used'),
            user=CustomUser.objects.create(first_name="Kot", last_name="Czarny",
                                           email="abc@wp.pl",
                                           phone_number = "000000000",
                                           postal_code = "80288",
                                           town_name = "Tczew",
                                           username="kotek"
        ))

    def test_name_label(self):
        notice = Notice.objects.get(id=1)
        field_label = notice._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_description_label(self):
        description = Notice.objects.get(id=1)
        field_label = description._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')
