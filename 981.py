# 981. Time Based Key-Value Store
class TimeMap:

    def __init__(self):
        self.hashMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashMap:
            self.hashMap[key] = []
        self.hashMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashMap:
            return ""
        values = self.hashMap[key]
        low, high = 0, len(values) - 1
        while low <= high:
            mid = (low + high) // 2
            if values[mid][0] == timeMap:
                return [mid][1]
            if values[mid][0] < timeMap:
                low = mid + 1
            else:
                high = mid - 1
        return values[high][1] if high >= 0 else ""


timeMap = TimeMap()
timeMap.set("alice", "happy", 1)
timeMap.get("alice", 1)
timeMap.get("alice", 2)
timeMap.set("alice", "sad", 3)
timeMap.get("alice", 3)
