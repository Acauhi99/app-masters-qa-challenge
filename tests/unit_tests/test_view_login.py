import pytest
from unittest import TestCase
from views.fake_view import login, view_dashboard, forgot_password

@pytest.mark.unit
class TestLogin(TestCase):

    def test_valid_email_and_password(self):
        self.assertTrue(login('email@example.com', 'password123'))

    def test_invalid_email(self):
        self.assertFalse(login('emailexample.com', 'password123'))
        self.assertFalse(login('email@example', 'password123'))
        self.assertFalse(login('email@.com', 'password123'))

    def test_invalid_password(self):
        self.assertFalse(login('email@example.com', 'pass'))

    def test_invalid_email_and_password(self):
        self.assertFalse(login('emailexample.com', 'pass'))

    def test_admin_dashboard(self):
        login('admin@example.com', 'adminpassword')
        self.assertEqual(view_dashboard('admin@example.com'), 'Admin: estatísticas')

    def test_user_dashboard(self):
        login('user@example.com', 'userpassword')
        self.assertEqual(view_dashboard('user@example.com'), 'Usuário: últimas ações')

    def test_password_boundary(self):
        self.assertTrue(login('email@example.com', 'password'))  # 8 caracteres
        self.assertFalse(login('email@example.com', 'passwor'))  # 7 caracteres

    def test_forgot_password_link(self):
        result = forgot_password('email@example.com')
        self.assertEqual(result['status'], 'success')
        self.assertEqual(result['message'], 'Link para reset enviado para: email@example.com')

