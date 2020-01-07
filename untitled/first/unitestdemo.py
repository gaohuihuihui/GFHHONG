import unittest
import requests

class testclass(unittest.TestCase):
    def setUp(self):
        print("setup")
    def test_demo1(self):
        print("1")
    def tearDown(self) -> None:
        print("teardown")

if __name__=="__main__":
    unittest.main()
