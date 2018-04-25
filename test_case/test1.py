import Home_Page
import unittest

class TestOne(unittest.TestCase):
    def setUp(self):
        self.page = Home_Page.home_Page('ff')


    def test_login0(self):
        self.page.open('https://pc.shaxiaoseng.com:4433')
        title=self.page.get_title()
        self.page.click_HomeLoginBtn('13511111105','111111')
        print(title)

    def test_login1(self):
        self.page.open('https://pc.shaxiaoseng.com:4433')
        title = self.page.get_title()
        self.page.click_HomeLoginBtn('13511111105', '1111111')
        print(title)
    def tearDown(self):
        self.page.close()

if __name__ == "__main__":
    unittest.main()