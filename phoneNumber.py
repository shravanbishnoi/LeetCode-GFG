chars = {1: "", 2: "ABC", 3: "DEF", 4: "GHI", 5: "JKL", 6: "MNO", 7: "PQRS", 8: "TUV", 9: "WXYZ", 0: ""}
def func(n, lst=None):
    if lst is None:
        lst = [""]
    if n <= 0:
        return lst
    
    while True:
        digit = n % 10
        n = n // 10
        if digit != 1 and digit != 0:
            break
        
    new_lst = []
    for i in chars[digit]:
        for j in lst:
            new_lst.append(i + j)
    return func(n, new_lst)

result = func(0000)
print(result)