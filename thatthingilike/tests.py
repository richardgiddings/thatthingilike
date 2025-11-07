from django.test import TestCase

from .models import Thing, Tag, Location

class IndexTests(TestCase):
    def test_index_view_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_index_view_with_filters(self):

        loc1 = Location.objects.create(name="Location 1")
        loc2 = Location.objects.create(name="Location 2")

        tag1 = Tag.objects.create(name="Tag 1")
        tag2 = Tag.objects.create(name="Tag 2")

        thing1 = Thing.objects.create(
            title="Thing 1",
            description="Description 1",
            location=loc1
        )
        thing1.tag.set([tag1, tag2])
        thing2 = Thing.objects.create(
            title="Thing 2",
            description="Description 2",
            location=loc1
        )
        thing2.tag.set([tag2])
        thing3 = Thing.objects.create(
            title="Thing 3",
            description="Description 3",
            location=loc2
        )
        thing3.tag.set([tag1, tag2])

        # loc1, tag1 -> thing1
        response = self.client.get('/?location=1&tag=1')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Thing 1")
        self.assertNotContains(response, "Thing 2")
        self.assertNotContains(response, "Thing 3")

        # loc1, tag2 -> thing1, thing2
        response = self.client.get('/?location=1&tag=2')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Thing 1")
        self.assertContains(response, "Thing 2")
        self.assertNotContains(response, "Thing 3")

        # loc2, tag1 -> thing3
        response = self.client.get('/?location=2&tag=1')
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "Thing 1")
        self.assertNotContains(response, "Thing 2")
        self.assertContains(response, "Thing 3")