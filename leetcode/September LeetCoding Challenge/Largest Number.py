class Solution:
    def largestNumber(self, nums):
        compare = lambda a, b: -1 if a+b > b+a else 1 if a+b < b+a else 0
        print(compare)
        return str(int("".join(sorted(map(str, nums), key = cmp_to_key(compare)))))