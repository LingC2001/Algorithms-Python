def naive_multiplication(num1: int, num2: int) -> int:
    # dealing with 0s
    if num1 == 0 or num2 == 0:
        return 0
    
    # dealing with negative numbers
    positive = True
    if num1 < 0:
        positive = not positive
        num1 = num1*-1
    if num2 < 0:
        positive = not positive 
        num2 = num2*-1

    # separating digits
    n1_rev = []
    while num1 > 0:
        n1_rev.append(num1%10)
        num1 = num1//10

    # separating digits
    n2_rev = []
    while num2 > 0:
        n2_rev.append(num2%10)
        num2 = num2//10
    
    # performing multiplication
    res = []
    for i in range(len(n1_rev)):
        for j in range(len(n2_rev)):
            res.append(n1_rev[i] * n2_rev[j] * 10**(j+i))
    if positive:
        return sum(res)
    else:
        return sum(res)*-1