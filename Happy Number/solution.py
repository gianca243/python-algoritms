"""My approach"""

class Solution:

    def isHappy(self, n: int) -> bool:
        memory = set()
        if n == 1:
            return True
        while n not in memory:
            memory.add(n)
            n = str(n)
            accumulator = 0
            for number in n:
                accumulator += int(number)**2
            if accumulator == 1:
                return True
            n = str(accumulator)
        return False

# two pointer try

class Solution:
    def isHappy(self, n: int) -> bool:
        def calculate(n: int):
            cent = 0
            while n > 0:
                cent += (n%10)**2
                n = n // 10
            return cent

        slow = calculate(n)
        fast = calculate(calculate(n))
        if fast == 1:
            return True
        while fast != slow:
            if fast == 1:
                return True
            slow = calculate(slow)
            fast = calculate(calculate(fast))
        return False

# learned way

class Solution:
    def isHappy(self, n: int) -> bool:

        def get_next_number(n):
            output = 0

            while n:
                digit = n % 10
                output += digit ** 2
                n = n // 10

            return output

        slow = get_next_number(n)
        fast = get_next_number(get_next_number(n))

        while slow != fast:
            if fast == 1: return True
            slow = get_next_number(slow)
            fast = get_next_number(get_next_number(fast))

        return slow == 1


