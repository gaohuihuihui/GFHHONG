import unittest
import requests


class testclass(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("set up class")
    def setUp(self):
        print("setup")
    def test_demo1(self):

        print("1")
    def test_demo2(self):
        print("2")
    def tearDown(self) -> None:
        print("teardown")
    @classmethod
    def tearDownClass(cls) -> None:
        print("tear down class")

if __name__=="__main__":
    unittest.main()
