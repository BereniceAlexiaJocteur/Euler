# -------------------------------------------------------------------------------
# Name:        
# Purpose:     
# Created:     
# -------------------------------------------------------------------------------



def sum_digits3(n):
    r = 0
    while n:
        r, n = r + n % 10, n // 10
    return r


a = 5
for i in range(2, 10**15-4):
    a += sum_digits3(a)
print(a)