import assign1
import unittest

class TestAssign1Functions(unittest.TestCase):

    def testHelloWorldNormal(self):
        self.assertEqual('hello world', assign1.helloWorldNormal())

    def testHelloWorldInReverse(self):
        self.assertEqual('hello world'[::-1], assign1.helloWorldInReverse())

    def testHelloWorldTimesX(self):
        self.assertEqual('hello world'*3, assign1.helloWorldTimesX(3))
