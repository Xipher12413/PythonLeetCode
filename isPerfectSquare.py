import math
def isPerfectSquare(self, num: int) -> bool:
    if round(math.sqrt(num), 0) == math.sqrt(num):
        return True
    else:
        return False
