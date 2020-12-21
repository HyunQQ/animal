from django.test import TestCase

from app.models.users import AnimalUser


class AnimalModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        AnimalUser.objects.create(name='TestUser', email='test@test.com')

    def test_first_name_label(self):
        author = AnimalUser.objects.get(id=1)
        field_label = author._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_first_name_max_length(self):
        author = AnimalUser.objects.get(id=1)
        max_length = author._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)

    def test_object_name_is_name_comma_email(self):
        author = AnimalUser.objects.get(id=1)
        expected_object_name = f'{author.name}, {author.email}'
        self.assertEquals(expected_object_name, str(author))
