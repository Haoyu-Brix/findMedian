import unittest
from src.findMedian import FindMedian
from UnitTest.stream import Stream
import random


class TestFindMedian(unittest.TestCase):
    def test_same_stream_odd(self):
        number = 101
        stream = Stream(n=number)
        stream.generateSameStream()
        fm = FindMedian()
        mid = fm.findMedian(stream)
        self.assertEqual(stream.stream[0], mid)

    def test_same_stream_even(self):
        number = 100
        stream = Stream(n=number)
        stream.generateSameStream()
        fm = FindMedian()
        mid = fm.findMedian(stream)
        self.assertEqual(stream.stream[0], mid)

    def test_continuous_stream_odd(self):
        number = 101
        stream = Stream(n=number)
        stream.generatContinousStream()
        arr = sorted(stream.stream)
        fm = FindMedian()
        mid = fm.findMedian(stream)
        self.assertEqual(arr[len(arr)//2], mid)

    def test_continuous_stream_even(self):
        number = 100
        stream = Stream(n=number)
        stream.generatContinousStream()
        arr = sorted(stream.stream)
        fm = FindMedian()
        mid = fm.findMedian(stream)
        self.assertEqual((arr[number//2-1] + arr[number//2])/2, mid)

    def test_random_unrepeatable_stream_odd(self):
        count = 20
        while count:
            count -= 1
            number = random.randint(100, 201)
            number = number if number % 2 else number+1
            stream = Stream(n=number)
            stream.generateUnRepeatableStream()
            arr = sorted(stream.stream)
            fm = FindMedian()
            mid = fm.findMedian(stream)
            self.assertEqual(arr[len(arr)//2], mid)

    def test_random_unrepeatable_stream_even(self):
        count = 20
        while count:
            count -= 1
            number = random.randint(100, 201)
            number = number if not number % 2 else number + 1
            stream = Stream(n=number)
            stream.generateUnRepeatableStream()
            arr = sorted(stream.stream)
            fm = FindMedian()
            mid = fm.findMedian(stream)
            self.assertEqual((arr[number // 2 - 1] + arr[number // 2]) / 2, mid)

    def test_random_repeatable_stream_odd(self):
        count = 20
        while count:
            count -= 1
            number = random.randint(100, 201)
            number = number if number % 2 else number + 1
            stream = Stream(n=number)
            stream.generateRepeatableStream()
            arr = sorted(stream.stream)
            fm = FindMedian()
            mid = fm.findMedian(stream)
            self.assertEqual(arr[len(arr) // 2], mid)

    def test_random_repeatable_stream_even(self):
        count = 20
        while count:
            count -= 1
            number = random.randint(100, 201)
            number = number if not number % 2 else number + 1
            stream = Stream(n=number)
            stream.generateRepeatableStream()
            arr = sorted(stream.stream)
            fm = FindMedian()
            mid = fm.findMedian(stream)
            self.assertEqual((arr[number // 2 - 1] + arr[number // 2]) / 2, mid)


if __name__ == '__main__':
    unittest.main()
