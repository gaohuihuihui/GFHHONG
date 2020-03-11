import unittest

class simple_test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("set up ,class")
    def setUp(self) -> None:
        print("")

    def test_1(self):

        pass
    def test_2(self):
        pass
    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass




if __name__=="__main__":
    unittest.main()
