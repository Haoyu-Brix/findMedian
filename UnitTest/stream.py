# Author: Haoyu
# Desc: 生成一串随机数
# Data: 2020/08/09

import random


class Stream:
    def __init__(self, minval=1, maxval=1000, n=100):
        self.minval = minval
        self.maxval = maxval
        self.n = n
        self.offset = 0
        self.stream = None

    def generateSameStream(self):
        val = random.randint(self.minval, self.maxval)
        self.stream = [val for _ in range(self.n)]

    def generateRepeatableStream(self):
        self.stream = [random.randint(self.minval, self.maxval) for _ in range(self.n)]

    def generateUnRepeatableStream(self):
        mydic, count = set(), self.n        # 如果要节约存储，可使用布隆过滤器
        stream = []
        while count:
            count -= 1
            val = random.randint(self.minval, self.maxval)
            while val in mydic:
                val = random.randint(self.minval, self.maxval)
            stream.append(val)
            mydic.add(val)
        self.stream = stream

    def generatContinousStream(self):
        # 生成有序数组 + 洗牌
        self.stream = [_ for _ in range(1, self.n + 1)]
        for i in range(self.n - 1, -1, -1):
            ran = random.randint(0, i)
            self.stream[i], self.stream[ran] = self.stream[ran], self.stream[i]

    def read(self):
        if self.offset < self.n:
            self.offset += 1
            return self.stream[self.offset - 1]
        return -1

    def isValid(self):
        # Stream合法 and 非空+offset在有效范围内
        return self.stream and self.offset < self.n

    def reset(self):
        self.offset = 0



