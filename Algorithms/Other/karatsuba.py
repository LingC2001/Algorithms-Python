"""
Karatsuba multiplication algorithm complexity analysis:

Time complexity:
    The recurrence relation is: T(n) = 3T(n/2) + cn
    Solving this with induction gives O(n^1.59)

Space complexity:
    Since the pad_size function converts the numbers to strings,
    therefore, O(n)

"""

def pad_size(num1, num2):
    snum1 = str(num1)
    snum2 = str(num2)
    len_diff = len(snum1) - len(snum2)
    n = max(len(snum1), len(snum2))

    # making same length
    if len_diff != 0:
        if len_diff > 0: #n1 > n2
            num2 = num2 * 10**len_diff
        else:
            num1 = num1 * 10**abs(len_diff)
    
    return num1, num2, n, len_diff


def karatsuba(num1: int, num2: int) -> int:
    # deal with zeros
    if num1 == 0 or num2 == 0:
        return 0
    
    # deal with negatives
    positive = True
    if num1 < 0:
        positive = not positive
        num1 = num1 * -1
    if num2 < 0:
        positive = not positive
        num2 = num2 * -1
    
    if num1 < 10 and num2 < 10:
        if positive: 
            return num1*num2 # single digit multiplication
        else:
            return num1*num2*-1  
    else:
        # Make the 2 nums the same size:
        num1, num2, n, len_diff = pad_size(num1, num2)
        
        res = karatsuba_multiply(num1, num2, n)//(10**abs(len_diff))

        if positive:
            return res
        else:
            return res * -1



def karatsuba_multiply(num1, num2, n=None):
    len_diff = 0
    if n is None:
        num1, num2, n, len_diff = pad_size(num1, num2)

    if n == 1:
            return num1*num2 # single digit multiplication
    else:
        half_n = n//2

        xm = num1//(10**half_n)
        xl = num1%(10**half_n)
        ym = num2//(10**half_n)
        yl = num2%(10**half_n)
        
        if n % 2 == 0:
            r1 = karatsuba_multiply(xm, ym, half_n)
            r2 = karatsuba_multiply(xl, yl, half_n)
            r3 = karatsuba_multiply(xm+xl, ym+yl, half_n)
        else:
            r1 = karatsuba_multiply(xm, ym, (n+1)//2)
            r2 = karatsuba_multiply(xl, yl, half_n)
            r3 = karatsuba_multiply(xm+xl, ym+yl, (n+1)//2)

        z = r3 - r2 - r1
        res = (r1*10**(half_n*2) + z*10**half_n + r2)//(10**abs(len_diff))

        return res
