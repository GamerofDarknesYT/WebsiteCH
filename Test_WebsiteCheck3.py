import unittest
import WebsiteCheck3

class Test_WebsiteCheck3(unittest.TestCase):

    def testEqual(self):
        self.assertEqual(WebsiteCheck3.WebsiteCheck("https://youtube.com"), True)
        self.assertEqual(WebsiteCheck3.WebsiteCheck("https://monitoring.cloud.1home.io"), False)
        self.assertEqual(WebsiteCheck3.WebsiteCheck("https://google.com"), True)
        self.assertEqual(WebsiteCheck3.WebsiteCheck("https://github.com"), True)
        self.assertEqual(WebsiteCheck3.WebsiteCheck("https://python.org"), True)

#class StatCTest(unittest.TestCase):
    #def test_add(self):
        #result = ()
        #self.assertEqual(result, 200)

if __name__ == '__main__':
    unittest.main()