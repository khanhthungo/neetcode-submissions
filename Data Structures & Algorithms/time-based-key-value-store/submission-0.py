class TimeMap:
    def __init__(self):
        self.freq = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None: 
        self.freq[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        rng = self.freq[key]
        l = 0 
        r = len(rng) - 1
        while l <= r: 
            m = l + (r-l)//2
            if rng[m][0] <= timestamp: 
                res = rng[m][1]
                l = m + 1
            else: 
                r = m - 1 
        return res