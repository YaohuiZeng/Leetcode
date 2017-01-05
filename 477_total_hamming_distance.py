"""

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Now your job is to find the total Hamming distance between all pairs of the given numbers.

Example:
Input: 4, 14, 2

Output: 6

Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
showing the four bits relevant in this case). So the answer will be:

HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.

Note:
Elements of the given array are in the range of 0 to 10^9
Length of the array will not exceed 10^4.

"""

class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count, n = 0, len(nums)
        bit_strs = map("{:032b}".format, nums)

        for j in xrange(32):
            n_zeros, n_ones = 0, 0
            for bs in bit_strs:
                if bs[j] == "0":
                    n_zeros += 1
                else:
                    n_ones += 1
            count += n_zeros * n_ones

        return count

    def totalHammingDistance2(self, nums):
        return sum(b.count('0') * b.count('1') for b in zip(*map(lambda x: bin(x)[2:].zfill(32), nums)))

    def totalHammingDistance3(self, nums):
        return sum(b.count('0') * b.count('1') for b in zip(*map('{:032b}'.format, nums)))


if __name__ == "__main__":
    nums = [4, 14, 2]
    print Solution().totalHammingDistance(nums)
    print Solution().totalHammingDistance2(nums)
    print Solution().totalHammingDistance3(nums)
