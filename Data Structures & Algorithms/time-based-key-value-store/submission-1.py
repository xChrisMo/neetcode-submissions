class TimeMap:

    def __init__(self):
        # key-value based that stores multiple values for same key 
        self.dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # key: [timestamp][value] 
        if key not in self.dict:
            self.dict[key] = []

        self.dict[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        # return [key][timestamp]
        # if not [key][timestamp]; return ''
        if key not in self.dict:
            return ''   
        
        def condition(i):
            # if greater than or rqual to timestamp, return True
            return self.dict[key][i][0] > timestamp 

        l = 0
        r = len(self.dict[key])

        while l < r:
            m = l + (r - l) // 2

            if condition(m):
                r = m

            else:
                l = m + 1
        if l == 0:
            return ''

        return self.dict[key][l - 1][1]


