
while True:

    try:
        exp = input()
        pilha = 0
        for caracter in exp:
            if caracter == '(':
                pilha += 1

            elif caracter == ')':
                pilha -= 1
            
            if pilha < 0:
                break
        
        if pilha != 0:
            print('incorrect')
        else:
            print('correct')

    except EOFError:
        break
