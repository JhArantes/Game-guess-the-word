palavra_secreta = ['p', 'e', 'r' ,'f' ,'u' ,'m' , 'e']
palavra_user = ['*', '*','*' ,'*' ,'*' ,'*' ,'*']


print('-=' * 20)
print('Vamos jogar um jogo!!\nFale letras e direi se ela existe na palavra secreta ou não')
print('-=' * 20)


import os
# loop para caso o user erre  

contador = 0
while True:
    #pega letra
    letra_user = input("Digite uma letra: ").lower().strip()
    
    # Apenas 1 
    if len(letra_user) > 1:
        print('Passe apenas uma letra')
        continue
    
    
    for p, i in enumerate(palavra_secreta):
        if i == letra_user:
            palavra_user[p] = i

    visao_palavra = ''.join(palavra_user)
    print(visao_palavra)
    contador += 1
    
    if palavra_secreta == palavra_user:
        break
os.system('cls')

print('Você Ganhou!! com ', contador,' tentativas')
