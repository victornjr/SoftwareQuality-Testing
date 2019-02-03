import unittest
import hello

class TestHello(unittest.TestCase):

    # First test case -> returning Hello World!
    def test_SayHello(self):
        # If the method returns "Hello World!", then the test will pass
        self.assertEqual(hello.sayHello(),"Hello World!")

    def test_add(self):
        # For this test case, I will have two asserts
        #   if one fails, then all the test case fails.
        self.assertEqual(hello.add(3,5),8)
        # This second assert will fail,
        #   because I'm saying that the resukt will be 3 when the result is 15
        #   if we change the value to 15, then it will pass
        self.assertEqual(hello.add(10,5),3)

if __name__ == '__main__':
    unittest.main()
