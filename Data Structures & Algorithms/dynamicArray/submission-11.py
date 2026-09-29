class DynamicArray:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.arr = [0] * self.cap

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.cap:
            self.resize()
        

        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        if self.size > 0:
            self.size -= 1
        return self.arr.pop(self.size)

    def resize(self) -> None:
        self.cap *= 2
        newArr = [0] * self.cap

        for i in range(self.size):
            newArr[i] = self.arr[i]
        self.arr = newArr

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.cap