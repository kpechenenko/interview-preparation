class Solution:
    def get_sum_of_digits(self, num: int) -> int:
        if num % 10 == num:
            return num
        digits_sum = 0
        while num > 0:
            digits_sum += num % 10
            num //= 10
        return digits_sum


    def addDigits(self, num: int) -> int:
        while num % 10 != num:
            num = self.get_sum_of_digits(num)
        return num


