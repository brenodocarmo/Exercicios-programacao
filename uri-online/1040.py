
n1,n2,n3,n4 = input().split()

n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

m = ((n1*2)+(n2*3)+(n3*4)+(n4*1)) / 10

if m > 7.0:
    print('Media: {:.1f}'.format(m))
    print('Aluno aprovado.')
elif m < 5.0:
    print('Media: {:.1f}'.format(m))
    print('Aluno reprovado.')
else:
    print('Media: {:.1f}'.format(m))
    print('Aluno em exame.')
    n5 = float(input())
    print('Nota do exame: {:.1f}'.format(n5))
    
    nova_media = (m + n5) / 2

    if nova_media > 5.0:
        print('Aluno aprovado.')
        print('Media final: {:.1f}'.format(nova_media))
    else:
        print('Aluno reprovado')
        print('Media final: {:.1f}'.format(nova_media))
