
vetor = []
for i in range(3):
    n = int(input())
    vetor.append(n)

for ind, x in enumerate(vetor):
    if x is None or x <= 0:
        x = 1
    print('X[{}] = {}'.format(ind, x))