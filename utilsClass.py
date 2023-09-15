class utils:
    def reversed(val):
        #takes number and reversed in int
        sum = 0 
        while val > 0:
            rightMostNumber = val%10
            valueWithoutLastDecimal = (val - (val%10))/10
            val = valueWithoutLastDecimal
            sum = sum*10
            sum+= rightMostNumber
        #print(sum)
        return sum
    def formatter(val):
        #takes a number and returns the number in base 2 and base 8
        binary = bin(val)
        octal  = oct(val)
        return binary, octal
