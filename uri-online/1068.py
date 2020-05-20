

exp = input()

i = 0
p = []

while i < len(exp):
    if exp[i] == '(':
        p.append('(')

    if exp[i] == ')':
        if len(p) > 0:
            topo = p.pop(-1)
        else:
            p.append(')')
            break
    i+=1

if len(p) == 0:
    print('correct')
else:
    print('incorrect')
