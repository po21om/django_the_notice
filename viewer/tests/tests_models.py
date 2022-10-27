from django.db import DataError
from django.test import TestCase

from viewer.models import Notice, Category, Type, Condition, CustomUser


# Create your tests here.


class NoticeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Notice.objects.create(
            name="Consider our form for renewing books. This has just one field for the renewal date",
            description="¥üЯת؁؈ق@ - barbie doll",
            price=2,
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
        field_label = notice.name
        # print(type(field_label))
        # print(field_label)
        self.assertEqual(field_label, "Consider our form for renewing books. This has just one field for the renewal date")


    def test_description_label(self):
        description = Notice.objects.get(id=1)
        field_label = description.description
        # print(type(field_label))
        # print(field_label)
        self.assertEqual(field_label, '¥üЯת؁؈ق@ - barbie doll')

    def test_name_label_max_length(self):
        notice = Notice.objects.get(id=1)
        name_length = len(notice.name)
        print(name_length)
        self.assertTrue(name_length <= 64)



    # def test_correct_price(self):
    #     test_subject = Notice.objects.get(id=1)
    #     price = test_subject.price
    #     print(type(price))
    #     self.assertEqual(price, 2)
