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

    def generateTestStream(self):
        # self.stream =  [15, 50, 87, 169, 171, 184, 287, 290, 295, 298, 331, 373, 459, 460, 488, 505, 555, 585, 626, 671, 673, 679, 739, 749, 751, 752, 759, 774, 788, 802, 822, 825, 844, 848, 850, 862, 916, 934, 973, 993, 998]
        self.stream = [37, 73, 86, 110, 145, 148, 160, 217, 271, 310, 316, 422, 423, 442, 457, 482, 499, 505, 510, 537, 538, 591, 603, 621, 656, 662, 680, 726, 731, 742, 751, 813, 835, 892, 895, 909, 925, 935, 978, 991]
            # [1,2,2,3,3,4,6,7,8] # [3, 7, 5, 8, 9] #
        self.n = len(self.stream)

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



