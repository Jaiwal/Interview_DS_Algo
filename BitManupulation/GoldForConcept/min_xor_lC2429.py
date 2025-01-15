#solution1: just take x as num1 because min chiyh after xor and see bit current and bits needed

class Solution:


    def isSet(self,x,bit):
        return x&(1<<bit)

    def setBit(self,x,bit):
        return x | (1<<bit)

    def unsetBit(self,x,bit):
        return x & ~(1<<bit)


    def minimizeXor(self, num1: int, num2: int) -> int:
        #lets take num1 as x only because in best case x xor x gives 0 minimum so good for us
        x=num1

        requiredBitCount=bin(num2).count('1')
        currentSetBitCount=bin(num1).count('1')
        
        #start setting and unsetting from LSB
        bit=0 

        if currentSetBitCount<requiredBitCount:
            #need to set bit and since need min then start from leftest
            #till they are equal
            while currentSetBitCount<requiredBitCount:
                if not self.isSet(x,bit):
                    x=self.setBit(x,bit)
                    currentSetBitCount+=1
                bit+=1
        else:
            #need to unset bit and since need min then start from leftest
            #till they are equal
            while currentSetBitCount>requiredBitCount:
                if self.isSet(x,bit):
                    x=self.unsetBit(x,bit)
                    currentSetBitCount-=1
                bit+=1



        return x


#solution2: take x=0 and build step by step to no of bits in num2 and how can we have min when xor with num1(start from MSB to cancel 1 from num1)

class Solution:

    def isSet(self, x, bit):
        return x & (1 << bit)

    def setBit(self, x, bit):
        return x | (1 << bit)

    def unsetBit(self, x, bit):
        return x & ~(1 << bit)

    def isUnset(self, x, bit):
        return (x & (1 << bit)) == 0

    def minimizeXor(self, num1: int, num2: int) -> int:
        # Let's take x=0 and build it
        x = 0
        requiredBitCount = bin(num2).count('1')
    
        # Start setting bits from MSB in x at positions where num1 is set
        # This helps cancel bits and minimize the value as a result
        bit = 31
        while bit >= 0 and requiredBitCount:
            if self.isSet(num1, bit):
                x = self.setBit(x, bit)
                requiredBitCount -= 1
            bit -= 1

        # In case there are bits left to be set but no more set bits in num1,
        # set bits from LSB in x
        bit = 0
        while bit <= 31 and requiredBitCount:
            if self.isUnset(x, bit):
                x = self.setBit(x, bit)
                requiredBitCount -= 1
            bit += 1

        return x