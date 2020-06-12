class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []

    def append(self, item):
        self.data.append(item)
        if len(self.data) == self.capacity:
            self.cur = 0
            self.__class__ = self.__Full

    def get(self):
        return self.data
    class __Full:
        def __init__(self, n):
            raise

        def append(self, x):
            self.data[self.cur] = x
            self.cur = (self.cur+1) % self.capacity

        def get(self):
            return self.data
            # return self.data[self.cur:]+self.data[:self.cur]