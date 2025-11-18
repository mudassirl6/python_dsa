class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        
        # i = 0
        # while i < (len(bits)-1):
        #     if bits[i] == 1:
        #         i += 2

        #     else:
        #         i += 1


        # if i == len(bits):
        #     return False

        # else:
        #     return True


        #optimal approach
        i = len(bits)-2
        count_ones = 0

        while i >=0 and bits[i] == 1:
            count_ones += 1
            i -= 1

        return True if count_ones % 2 == 0 else False


        
