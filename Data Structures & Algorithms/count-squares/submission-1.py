'''




'''


class CountSquares:

    def __init__(self):
        self.ptscount = defaultdict(int)
        self.pts = []
        

    def add(self, point: List[int]) -> None:
        self.ptscount[tuple(point)] += 1
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        x1, y1 = point

        for x, y in self.pts:
            if (x1 - x) == 0 or (y1 - y) == 0 or (abs(x1-x) - abs(y1-y) != 0):
                continue

            res += self.ptscount[x1, y] * self.ptscount[x, y1]

        return res
        
