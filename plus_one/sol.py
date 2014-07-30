class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        parity = 1
        for i in range(len(digits)-1, -1, -1):
            digits[i] += parity
            parity = 0
            if digits[i] < 10:
                return digits
            else:
                digits[i] = 0
                parity = 1
        if parity:
            return [1] + digits
        return digits
