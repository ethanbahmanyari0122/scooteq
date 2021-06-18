from scooteq.routes import app
import unittest

class TestFoo(unittest.TestCase):
    #The Configuration
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = True
        self.app = app.test_client()

    #Test if the home page has correct http status
    def test_foo_with_client(self):
        respone = self.app.get('/', content_type="html/text")
        self.assertEqual(respone.status_code, 200)

    #Test if the response of the login page contain Login
    def test_login_page_loads(self):
        respone = self.app.get('/login', content_type="html/text")
        self.assertTrue(b'Login' in respone.data)

    #Test to login with incorrect inpute
    def test_incorrect_login(self):
        respone = self.app.post('/login', data=dict(username="rawezh", password="123457"),
                              follow_redirects=True)
        self.assertFalse(b'login Unsuccessful. Please check username and password' in respone.data)

    #Test correct login
    def test_correct_login(self):
        respone = self.app.post('/login', data=dict(username="rawezh11", password="1234567"),
                              follow_redirects=True)
        self.assertEqual(respone.status_code, 200)

    #Test registration
    def test_registration(self):
        respone = self.app.post('/register', data=dict(firstname="paul",lastname="dachboden",
                                                       username="paul1", email="paul@germany.de",
                                                       password="123456789", confirmpassword="123456789"),
                                follow_redirects=True)
        self.assertIn(b'Your account has been created! paul! Please login.', respone.data)



if __name__ == "__main__":
    unittest.main()