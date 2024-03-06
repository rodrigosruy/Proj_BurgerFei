import datetime
import os
import string


#O jeito que fiz o menu é que opção "1- Novo Pedido" cria uma conta. 
#Após a criação da conta, ele imediatamente cria uma .txt que contém o pedido (esse arquivo em sí é o pedido).
#Quando o pedido é cancelado usando "2- Cancela Pedido" a .txt é deletada, impossibilitando a adição, remoção e modificação do pedido.
#Para criar uma nova .txt, usar "1- Novo Pedido", você pode logar com uma conta pre-existente e criar um novo pedido, lhe providenciando uma nova .txt.

now = datetime.datetime.now()
def mostrarpedido(CPF,x = 0):            ##checa se o pedido existe, aí cria uma lista com as informações do PEDIDO e do MENU e mostra o PEDIDO com os nomes
    T = 0                                ## o x serve para saber se a opção 5 está sendo usada
    CPFpedido = ("%s.txt"%(CPF))
    try:
        pedido = open(CPFpedido,"r")  ##checa se o arquivo do pedido existe
    except FileNotFoundError:
        print("Pedido não existe!\nCrie um usando Novo Pedido!")
        E = 1                           ## E é utilizado para erros dentro do código. E = 1 significa que existe um erro! 
        return(E)
    pedido2 = pedido.read()
    pedido.close()
    pedido3 = pedido2.split("\n")     ##transforma o arquivo em uma lista desorganizada
    pedido4 = []
    while pedido3 != []:
        pedido4.append(pedido3[:2])    ##transforma a lista desorganizada em uma lista que contém código e quantidade
        pedido3 = pedido3[2:]
    pedido4.pop(-1)
    menu = open("menu.txt","r")
    menu2 = menu.read()
    menu3 = menu2.split("\n")   ##transforma o menu em uma lista
    menu.close()
    menu4 = []                     
    while menu3 != []:
        menu4.append(menu3[:4])  ##organiza a lista do menu, a qual agora contém código, nome e preço (mantive o R$ porque não sei se posso o remover sem perder ponto)
        menu3 = menu3[4:]
    
    
    print("Pedido Atual:")     
    for linha in range(len(pedido4)): ## mostra os seus pedidos já feitos, usando os nomes dentro da lista do menu, e as quantidades do pedido
        
        N = int(pedido4[linha][0])
        print("Produto: %2s"%(menu4[N-1][1]),end=' ')
        print("%2s Unidades" %(pedido4[linha][1]),end=' ')
        print("Preço por unidade: R$%2s"%(menu4[N-1][3]),end=" ")
        print()
    if x != 0:
        for linha in range(len(pedido4)):
            N = int(pedido4[linha][0]) ##número do item
            P = float(menu4[N-1][3])  ##preço da unidade do item
            Q = int(pedido4[linha][1])  ##qt. do item
            T += (P * Q) ##preço total


        return(T)
    return(pedido4)
        
            
         
        
    

def menupedido(CPF):   ##código que mostra o MENU e o disponibiliza para adicionar
    print("Código  Produto  Preço")
    menu = open("menu.txt","r")   
    menu2 = menu.read()
    menu3 = menu2.split("\n")
    menu.close()
    menu4 = []                     
    while menu3 != []:
        menu4.append(menu3[:4])    ##tranformando menu em lista organizada
        menu3 = menu3[4:]
    for linha in range(len(menu4)):
        for coluna in range(4):
            print("%2s" %(menu4[linha][coluna]),end=' ')
        print()
    CPFpedido = ("%s.txt"%(CPF))
    try:                                  ##código de verificação para verificar se o pedido existe
        pedido = open(CPFpedido,"a")
    except FileNotFoundError:
        print("Pedido não existe!\nCrie um usando Novo Pedido!")
        return
    while True:
        
        cd = int(input("Código do produto desejado: "))  ##input do codigo do pedido
        while cd > len(menu4) or cd <= 0 or cd == string:
            print("Código inválido.\nUse um dos códigos providenciados")
            cd = int(input("Código do produto desejado: "))
        qt = int(input("Quantidade do produto: "))   ##quantidade de itens
        while qt <= 0 or cd == string:
            print("Quantidade inválida.\nUse numeros positivos")
            qt = int(input("Quantidade do produto: "))
        pedido.write("%s\n%s\n" %(cd,qt))
        
        
        
        cont = input("Deseja adicionar mais algun item?\nSe sim digite 1, se não, digite 0: ")  ##pergunta se deseja adicionar mais itens ou não
        if cont == "0":
            print("Voltando ao menu principal")
            pedido.close()
            break
        if cont == "1":
            print("Código  Produto  Preço")
            for linha in range(len(menu4)):
                for coluna in range(4):
                    print("%2s" %(menu4[linha][coluna]),end=' ')
                print()
        

        
            
        
        
            
        

def validação():   ## cria a lista utilizada para verificar as informações de login
    info = open("info.txt","r")
    info2 = info.read()
    info3 = info2.split("\n")  ##abre o arquivo que contém todos os logins e os transforma em uma lista
    info4 = []
    info.close()
    while info3 !=[]:           
        info4.append(info3[:3]) # info4 agora é uma matriz, onde cada linha são as informações de 1 login, sendo assim
        info3 = info3[3:]       # posso utilizá-la para confirmar senhas e CPF.
    info4.pop(-1)               
    return(info4)              
                                
def novopedido(): ##código da opção 1
    E = 3         ##E serve para checar se o login é válido ou não, E = 1 é invalido, E = 0 é válido
    info = open("info.txt","r")
    info2 = info.read()
    info3 = info2.split("\n")
    info.close()
    cont = input("Já possui conta?\nSe sim digite 1, se não, digite 0: ")
    if cont == "1":
        E = 1
        info4 = validação()
        
        CPF = input("CPF: ")
        Senha = input("Senha: ")
        CPFpedido = ("%s.txt"%(CPF))
        if os.path.exists(CPFpedido):  ## código para não permitir a criação de 2 .txt de pedido
            print("Pedido Já existe!")
            return
        for linha in range(len(info4)): ##código utilizado várias vezes para checar se o CPF e senha estão corretos
            if CPF == info4[linha][1]:
                if Senha != info4[linha][1]:
                    print("Senha incorreta!")
                    return
                if Senha == info4[linha][2]:
                    E = 0
                    menupedido(CPF)
                    return
    if E == 1: ## código para não deixar logins incorretos continuar
        print("CPF não cadastrado!")
        return
    Nome = input("Nome: ")
    while Nome == "":
        print("Insira seu nome!")
        Nome = input("Nome: ")
    CPF = input("CPF: ")
    while CPF == "":
        print("Insira seu CPF!")
        CPF = input("CPF: ")
    Senha = input("Senha: ")
    while Senha == "":
        print("Insira uma senha!")
        Senha = input("Senha: ")
    for linha in range(len(info3)):
        if info3[linha] == CPF:
            print("Já existe uma conta com esse CPF")
            return
    info = open("info.txt","a")
    info.write("%s\n"%(Nome)) 
    info.write("%s\n"%(CPF))
    info.write("%s\n"%(Senha))
    info.close()
    menupedido(CPF)


def cancelarpedido(): ##código para opção 2 - Cancela Pedido. Serve para deletar a .txt do pedido
    info4 = validação()               
    
    CPF = input("CPF: ")
    Senha = input("Senha: ")
    
    
    
    
    for linha in range(len(info4)):    ## usa a lista info4 para verificar se as info. do login estão corretas
        if CPF == info4[linha][1]:
            if Senha != info4[linha][2]:
                print("Senha incorreta!")
                return
            if Senha == info4[linha][2]:
                E = mostrarpedido(CPF)  
                if E == 1:   ## retorna quando arquivo é inválido
                    return
                conf = input("Certeza que gostaria de deletar o pedido?\nSe sim digite 1, se não, digite 0: ")
                if conf == "0":
                    print("Voltando ao menu principal")
                    return
                if conf == "1":
                    CPFpedido = ("%s.txt"%(CPF))
                    try:
                        os.remove(CPFpedido)
                        print("Pedido Deletado!")
                        return
                    except FileNotFoundError:
                        print("Pedido Já Deletado!")
                        return
                   
    print("CPF não cadastrado!") 

def insereproduto(): ## código para a opção 3
    info4 = validação()
    
    CPF = input("CPF: ")
    Senha = input("Senha: ")
    for linha in range(len(info4)):
        if CPF == info4[linha][1]:
            if Senha != info4[linha][2]:
                print("Senha incorreta!")
                return
            if Senha == info4[linha][2]:
                conf = 1
                if conf == 1:
                    E = mostrarpedido(CPF) ## se usa o mostrarpedido() para ver se o arquivo existe
                    if E == 1:
                        return
                    menupedido(CPF)
                    return
    print("CPF não cadastrado!")

def cancelarproduto(): ##código para opção 4, não descobri um jeito de fazer com que se possa apenas remover itens já existentes. (então ficou meio nas coxas)
    info4 = validação()
    
    CPF = input("CPF: ")
    Senha = input("Senha: ")
    for linha in range(len(info4)):
        if CPF == info4[linha][1]:
            if Senha != info4[linha][2]:
                print("Senha incorreta")
                return
            if Senha == info4[linha][2]:
                conf = 1
                if conf == 1:
                    E = mostrarpedido(CPF)
                    if E == 1:
                        print("CPF não cadastrado!")
                        return
                    print("Código  Produto  Preço") ##mostra o menu
                    menu = open("menu.txt","r")
                    menu2 = menu.read()
                    menu3 = menu2.split("\n")
                    menu.close()
                    menu4 = []                     
                    while menu3 != []:
                        menu4.append(menu3[:4])
                        menu3 = menu3[4:]
                    for linha in range(len(menu4)):
                        for coluna in range(4):
                            print("%2s" %(menu4[linha][coluna]),end=' ')
                        print()
                    CPFpedido = ("%s.txt"%(CPF))
                    try:
                        pedido = open(CPFpedido,"r") ########!!!!!!!!!!!!COLOCAR "a" DEPOIS!!!!!!
                    except FileNotFoundError:
                        print("Pedido não existe! Crie um usando Novo Pedido!")
                        return
                    pedido2 = pedido.read()
                    pedido.close()
                    pedido3 = pedido2.split("\n")     ##transforma o arquivo em uma lista desorganizada
                    pedido4 = []
                    while pedido3 != []:
                        pedido4.append(pedido3[:2])    ##transforma a lista desorganizada em uma lista que contém código e quantidade
                        pedido3 = pedido3[2:]
                    pedido4.pop(-1)
                    pedido = open(CPFpedido,"a")
                    while True:
                        C = 0
                        
                        
                            

        
                        cd = int(input("Código do produto que deseja remover: "))  ## código de verificação se o pedido tem esse código
                        for linha in range(len(pedido4)):
                            if cd == int(pedido4[linha][0]):
                                C = 1
                        while C == 0 or C == string:
                            print("Código invalido! Use um código dentro do pedido!")
                            cd = int(input("Código do produto que deseja remover: "))
                            for linha in range(len(pedido4)):
                                if cd == int(pedido4[linha][0]):
                                    C = 1




                        
                        
                        quantidade = 0
                        qt = int(input("Quantidade a ser removida, 0 para não modificar: ")) ### código de verificação se o pedido com esse código, tem quantidade o suficiente
                        for linha in range(len(pedido4)):
                            if cd == int(pedido4[linha][0]):
                                quantidade += int(pedido4[linha][1])
                        while qt > quantidade or qt < 0 or qt == string:  
                            quantidade = 0
                            print("Quantidade inválida! Não se pode ter quantidades negativas nem menor que as no pedido!")
                            qt = int(input("Quantidade a ser removida: ")) 
                            for linha in range(len(pedido4)):
                                if cd == int(pedido4[linha][0]):
                                    quantidade += int(pedido4[linha][1])

                                


                        
                        pedido.write("%s\n%s\n" %(cd,qt * -1)) ##qt negativa pois é remoção
        
        
        
                        cont = input("Deseja retirar mais algun item?\nSe sim digite 1, se não, digite 0: ")
                        if cont == "0":
                            print("Voltando ao menu principal")
                            pedido.close()
                            break
                        if cont == "1":
                            mostrarpedido(CPF)
                            print("Código  Produto  Preço")
                            for linha in range(len(menu4)):
                                for coluna in range(4):
                                    print("%2s" %(menu4[linha][coluna]),end=' ')
                                print()
    print("CPF não cadastrado!")

def valorproduto(): ##código para a opção 5
    info4 = validação()
    
    CPF = input("CPF: ")
    Senha = input("Senha: ")
    for linha in range(len(info4)):
        if CPF == info4[linha][1]:
            if Senha != info4[linha][2]:
                print("Senha incorreta!")
                return
            if Senha == info4[linha][2]:
                cont = 1
                CPFpedido = ("%s.txt"%(CPF))
                try:
                    pedido = open(CPFpedido,"r")
                    pedido.close()
                except FileNotFoundError:
                    print("Pedido não existe! Crie um usando Novo Pedido!")
                    return

                while cont == 1:
                
                
                    preço = mostrarpedido(CPF,1) ##utiliza a parte de mostrarpedido() que calcula o total
                    
                    

                    print("Valor total do pedido é: R$ %.2f"%(preço))
                    cont = 0 

                
                    
                print("Voltando ao menu principal")
                return
    print("CPF não cadastrado!")
    
def extratopedido(): #código para a opção 6
    info4 = validação()
    
    CPF = input("CPF: ")
    Senha = input("Senha: ")
    for linha in range(len(info4)):
        if CPF == info4[linha][1]:
            if Senha != info4[linha][2]:
                print("Senha incorreta!")
                return
            if Senha == info4[linha][2]:
                cont = 1
                CPFpedido = ("%s.txt"%(CPF))
                try:
                    pedido = open(CPFpedido,"r")
                    pedido.close()
                except FileNotFoundError:
                    print("Pedido não existe! Crie um usando Novo Pedido!")
                    return
                while cont == 1:
                    now = datetime.datetime.now() ##tempo
                    
                    print("Nome: %s"%(info4[linha][0])) ##nome de acordo com o arquivo
                    print("CPF: %s"%(info4[linha][1])) ##CPF de acordo com o arquivo
                    print("Data: %.19s"%(now)) ##horário sem milisegundos
                    preço = mostrarpedido(CPF,1)
                    print("Valor total do pedido é: R$ %.2f"%(preço))
                    cont = 0
                print("Voltando ao menu principal")
                return
    print("CPF não cadastrado!")
    



while True:
    print("1- Novo Pedido\n2- Cancela Pedido\n3- Insere produto\n4- Cancela Produto\n5- Valor do pedido\n6- Extrato do pedido\n0- Sair")
    option = input("Opção: ")
    if option == "1":
        novopedido()
    if option == "2":
        cancelarpedido()
    if option == "3":
        insereproduto()
    if option  == "4":
        cancelarproduto()
    if option == "5":
        valorproduto()
    if option == "6":
        extratopedido()
    if option == "0":
        break