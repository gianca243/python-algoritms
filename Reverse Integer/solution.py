class Solution:
    def reverse(self, x: int) -> int:
        negative = 0
        new_int = str(x)
        if x < 0:
            new_int = new_int[1:]

        new_int = new_int[::-1]
        new_int = int(new_int)
        new_int = new_int if x >= 0 else new_int * (-1)
        if new_int > 2 ** 31 - 1 or new_int < -2 ** 31:
            return 0
        return new_int
