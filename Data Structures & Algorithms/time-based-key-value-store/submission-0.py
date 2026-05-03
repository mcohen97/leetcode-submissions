class TimeMap:

    def __init__(self):
        self.store = {}        

    def set(self, key: str, value: str, timestamp: int) -> None:
        values = self.store.get(key, [])
        values.append({"value": value, "timestamp": timestamp})
        self.store[key] = values


    def get(self, key: str, timestamp: int) -> str:
        values = self.store.get(key, [])
        if not values:
            return ""
        
        l, r = 0, len(values) - 1

        mostRecent = None

        while l <= r:
            m = (l + r) // 2

            if values[m]["timestamp"] == timestamp:
                return values[m]["value"]
            elif values[m]["timestamp"] < timestamp:
                mostRecent = values[m]
                l = m + 1
            else:
                r = m - 1
        
        return mostRecent["value"] if mostRecent else ""
