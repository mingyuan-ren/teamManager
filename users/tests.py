from django.test import TestCase
from django.urls import reverse
from urllib import response
from django.test import Client
from .models import Member

# Create your tests here.

#set up a temp db for the test everytime
class MemberTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index(self):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, 200)

    def test_add_user(self):
        test_member = {'firstname': 'Leon', 'lastname': 'Kennedy', 'email': 'l.s.k@gmail.com', 'phone': '123123123', 'admin': 'False'}
        url=reverse("users:add")
        response = self.client.post(url, test_member, follow=True)

        assert test_member['firstname'] in response.content.decode()
        assert test_member['lastname'] in response.content.decode()
        assert test_member['email'] in response.content.decode()
        assert test_member['phone'] in response.content.decode()

    def test_delete_user(self):
        test_member = {'firstname': 'Leon', 'lastname': 'Kennedy', 'email': 'l.s.k@gmail.com', 'phone': '123123123', 'admin': 'False'}

        self.client.post('/users/add/', test_member)
        member_id=Member.objects.get(firstname=test_member['firstname']).id
        url=reverse("users:delete", kwargs={'pk':member_id})
        response = self.client.post(url, follow=True)

        assert test_member['firstname'] not in response.content.decode()
        assert test_member['lastname'] not in response.content.decode()
        assert test_member['email'] not in response.content.decode()
        assert test_member['phone'] not in response.content.decode()

    def test_edit_user(self):
        test_member_1 = {'firstname': 'Leon', 'lastname': 'Kennedy', 'email': 'l.s.k@gmail.com', 'phone': '123123123', 'admin': 'False'}
        test_member_2 = {'firstname': 'Claire', 'lastname': 'Redfield', 'email': 'claire.r@yahoo.com', 'phone': '987654321', 'admin': 'True'}
        self.client.post('/users/add/', test_member_1)
        member_id=Member.objects.get(firstname=test_member_1['firstname']).id
        url=reverse("users:edit", kwargs={'pk':member_id})
        response = self.client.post(url, test_member_2, follow=True)

        assert test_member_2['firstname'] in response.content.decode()
        assert test_member_2['lastname'] in response.content.decode()
        assert test_member_2['email'] in response.content.decode()
        assert test_member_2['phone'] in response.content.decode()

