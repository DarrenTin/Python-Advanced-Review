def iter_exp(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

def rec_exp(num):
    if num == 1:
        return 1
    return num * rec_exp(num - 1)

num = int(input("num: "))

print('1 - iterative\n2 - recursion')
method = int(input('method: '))

if method == 1:
    result = iter_exp(num)
    print(result)
elif method == 2:
    result = rec_exp(num)
    print(result)
else:
    print("method not exist")