from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from lists.models import Item


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        self.client.post('/', data={'item_text': 'A new list item'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_POST(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/list/the-only-list-in-the-world/')

    def test_only_save_items_when_necessary(self):
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)


class ItemModelTest(TestCase):

    def test_saving_and_retrieveing_item(self):
        first_item = Item()
        first_item.text = "the first (ever) list item"
        first_item.save()

        second_item = Item()
        second_item.text = "Item the second"
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_item_saved = saved_items[0]
        second_item_saved = saved_items[1]
        self.assertEqual(first_item_saved.text, "the first (ever) list item")
        self.assertEqual(second_item_saved.text, "Item the second")


class ListViewTest(TestCase):

    def test_uses_list_template(self):
        response = self.client.get('list/the-only-list-in-the-world/')
        self.assertTemplateUsed(response, 'list.html')

    def test_display_all_items(self):
        Item.objects.create(text="itemy 1")
        Item.objects.create(text="itemy 2")

        response = self.client.get('/list/the-only-list-in-the-world/')

        self.assertContains(response, 'itemy 1')
        self.assertContains(response, 'itemy 2')
