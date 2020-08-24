
def fat(x):

    if x == 0:
        return 1
    return x * fat(x - 1)

f = int(input())
print(fat(f))
