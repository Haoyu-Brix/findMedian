# Author: Haoyu
# Desc: 生成一串随机数
# Data: 2020/08/09


class FindMedian:
    def __init__(self):
        pass

    def findMedian(self, stream):
        # 第一遍遍历，记录长度，最大值，最小值
        stream.reset()
        length, minval, maxval = 0, float('inf'), float('-inf')
        while stream.isValid():
            val = stream.read()
            length += 1
            minval = min(minval, val)
            maxval = max(maxval, val)
        stream.reset()

        # 开始找中位数，对奇偶分类处理
        return self.findMedianOdd(stream, length, minval, maxval) if length % 2 else self.findMedianEven(stream, length, minval, maxval)

    def findMedianOdd(self, stream, length, minval, maxval):
        left, right = minval, maxval     # 左右区间[left, right]
        first_time = True                # 是否第一次执行，避免abs(sl-sr)>1失效
        sl, sr = 0, 0                    # 累计左右数量

        while (first_time or abs(sl-sr) > 1) or sl+sr < length:
            stream.reset()

            first_time = False
            mid = (left + right) / 2
            l, r = 0, 0                       # 当前区间左右数量
            isexist = False                   # 记录是否存在
            count = 0                         # 出现多少次

            while stream.isValid():
                val = stream.read()
                if left <= val <= mid:        # 等于的全部记录到left里
                    l += 1
                    if val == mid:
                        count += 1
                        isexist = True
                elif mid < val <= right:
                    r += 1

            # 如果l == 0 or r == 0，意味着此区间内都是相同元素, 或者出现数据倾斜
            if not l or not r:
                left, right = self.checkSkew(left, right, stream)
                if left == right:                                               # 搜索范围里数据相同
                    return self.findDepulicatedNumber(left, right, stream)
                continue                                                        # 数据倾斜

            # 找到了
            if abs((sl+l) - (sr+r)) == 1:
                if isexist:
                    # mid在数据流
                    if sl+l > sr+r:
                        return int(mid)
                    else:
                        return self.findIntegerLargerThanMid(mid, stream)
                else:
                    # mid不在数据流
                    if sl+l > sr+r:
                        return self.findIntegerLessThanMid(mid, stream)
                    else:
                        return self.findIntegerLargerThanMid(mid, stream)
            # 未找到
            else:
                if isexist:
                    if sl+l < sr+r:
                        # 出现在右端，右端做分解
                        left = mid
                        sl = sl + l - count     # 保证搜索区间
                    else:
                        right = mid
                        sr = sr + r
                else:
                    # mid不在数据流内
                    if sl+l < sr+r:
                        left = mid
                        sl = sl + l
                    else:
                        right = mid
                        sr = sr + r
            stream.reset()

    def findMedianEven(self, stream, length, minval, maxval):
        left, right = minval, maxval     # 左右区间[left, right]
        first_time = True                # 是否第一次执行，避免abs(sl-sr)>1失效
        sl, sr = 0, 0                    # 累计左右数量

        while (first_time or abs(sl-sr) > 1) or sl+sr < length:
            stream.reset()

            first_time = False
            mid = (left + right) / 2
            l, r = 0, 0                       # 当前区间左右数量
            isexist = False                   # 记录是否存在
            count = 0                         # 出现多少次

            while stream.isValid():
                val = stream.read()
                if left <= val <= mid:        # 等于全部记录到left里
                    l += 1
                    if val == mid:
                        count += 1
                        isexist = True
                elif mid < val <= right:
                    r += 1

            # 如果l == 0 or r == 0，意味着此区间内都是相同元素, 或者出现数据倾斜
            if not l or not r:
                left, right = self.checkSkew(left, right, stream)
                if left == right:       # 搜索范围里数据相同
                    return self.findDepulicatedNumber(left, right, stream)
                continue                # 数据倾斜

            # 找到了
            if sl+l == sr+r:
                if isexist:
                    # mid在数据流，且因为<=,一定在左边
                    return (mid + self.findIntegerLargerThanMid(mid, stream)) / 2
                else:
                    # mid不在数据流
                    return (self.findIntegerLessThanMid(mid, stream) + self.findIntegerLargerThanMid(mid, stream)) / 2

            # 未找到
            else:
                if isexist:
                    if sl + l < sr + r:
                        # 出现在右端，右端做分解
                        left = mid
                        sl = sl + l - count  # 保证区间
                    else:
                        right = mid
                        sr = sr + r
                else:
                    # mid不在数据流内
                    if sl + l < sr + r:
                        left = mid
                        sl = sl + l
                    else:
                        right = mid
                        sr = sr + r
            stream.reset()

    def findIntegerLessThanMid(self, mid, stream):
        minval = float('inf')
        res = None
        stream.reset()
        while stream.isValid():
            val = stream.read()
            if val < mid and mid - val < minval:
                minval = mid - val
                res = val
        return res

    def findIntegerLargerThanMid(self, mid, stream):
        minval = float('inf')
        res = None
        stream.reset()
        while stream.isValid():
            val = stream.read()
            if val > mid and val - mid < minval:
                minval = val - mid
                res = val
        return res

    def findDepulicatedNumber(self, left, right, stream):
        stream.reset()
        while stream.isValid():
            val = stream.read()
            if left <= val <= right:
                return val
        return None

    def checkSkew(self, left, right, stream):
        mydic = set()
        minval = float('inf')
        maxval = float('-inf')
        stream.reset()
        while stream.isValid():
            val = stream.read()
            if left <= val <= right:
                mydic.add(val)
                minval = min(minval, val)
                maxval = max(maxval, val)
        return minval, maxval


