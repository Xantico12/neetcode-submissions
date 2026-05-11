class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append([value, timestamp])
        
        
        print("set:", key, value, timestamp)
        print(self.timeMap)

    def get(self, key: str, timestamp: int) -> str:
        print("get:", key, timestamp)
        if key not in self.timeMap:
            return ""
        else:
            n = len(self.timeMap[key])
            res = ""

            if n == 1 and self.timeMap[key][0][1] <= timestamp:
                res = self.timeMap[key][0][0]
                print("res:", res)
                return res
            
            l, r = 0, n - 1

            while l <= r:
                mid = (l + r) // 2

                if self.timeMap[key][mid][1] == timestamp:
                    res = self.timeMap[key][mid][0]
                    print("res:", res)
                    return res
                elif self.timeMap[key][mid][1] > timestamp:
                    
                    r = mid - 1
                else:
                    res = self.timeMap[key][mid][0]
                    l = mid + 1
                print("l:", l, "r:", r, "mid:", mid)
            print("res:", res)
            return res
