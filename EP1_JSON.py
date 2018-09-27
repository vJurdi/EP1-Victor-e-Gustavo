# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 16:37:45 2018

@author: Victor Jurdi & Gustavo Pierre

EP1-Design de Sofware
"""



import json

with open ('cardapioecomandas.json', 'r+') as arquivo:
    texto = arquivo.read()
cardapio_comandas = json.loads(texto)

#arquivo cardápio
with open ('cardapio.json','r+') as arquivo:
    texto = arquivo.read()
cardapio = json.loads(texto)

#arquivo comanda
with open ('comanda.json','r+') as arquivo1:
    texto1=arquivo1.read()
comandas = json.loads(texto1)





y=True
while y == True:
    print('Menu do restaurante:')
    print('0 - sair')
    print('1 - adicionar comanda')
    print('2 - acessar comanda')
    print('3 - Alterar cardápio')
    print('4 - imprimir cardápio')
    
    escolha_menu=int(input('Faça sua escolha:'))
    if escolha_menu ==0:
        print ('Até mais!')
        y=False

    elif escolha_menu == 1:
        
        g=True
        while g == True:
            comanda_adicionar=str(input('Numero da mesa para qual deseja adicionar a comanda:'))
            if comanda_adicionar not in comandas: 
                comandas[comanda_adicionar]={}
                g=False
                y=True
            else:
                print ('Esta comanda ja existe')
                g=True
        
        
    elif escolha_menu==2:
        
        comanda_desejada=str(input('Digite o numero da comanda que deseja acessar:'))       
        if comanda_desejada in comandas:
            comanda=comandas[comanda_desejada]
            i=True
            while i == True:
                print('Comanda eletrônica')
                print('0 - voltar')
                print('1 - adicionar item')
                print('2 - remover item')
                print('3 - imprimir comanda')
            
                escolha=int(input('Faça sua escolha:'))
                
                if escolha == 0:
                    i=False
                
                
                elif escolha == 1:
                    item_desejado=str(input('Nome do produto:'))
                    if item_desejado in cardapio:
                        
                        quantidade=int(input('Qual a quantidade de {0} que você gostaria adicionar?'.format(item_desejado)))
                      
                            
                        if quantidade > 0:
                                                                                   
                            if item_desejado in comanda:
                                
                                comanda[item_desejado]+=(quantidade*cardapio[item_desejado])
                                print('quantidade atual de {0} : {1}'.format(item_desejado,int(comanda[item_desejado]/cardapio[item_desejado])))
                            else:
                                comanda[item_desejado]=(quantidade*cardapio[item_desejado])
                                print('quantidade atual de {0} : {1}'.format(item_desejado,int(comanda[item_desejado]/cardapio[item_desejado])))
                            
                            j=False
                        else:
                            print('digite uma quatidade maior que zero')
                            j=True
                    else:
                        print('O item {0} não está no cardápio.'.format(item_desejado))
                    i=True   
                elif escolha == 2:
                    p=True
                    while p==True:
                        item_remover=str(input('Nome do produto que deseja remover:'))
                        if item_remover in comanda:
                            j=True
                            while j == True:
                                quantidadeR=int(input('Quantidade a remover:'))
                                if quantidadeR >=0:
                                    #quantidade na comanda
                                    if (comanda[item_remover] / cardapio[item_remover]) > quantidadeR:
                                        comanda[item_remover]=comanda[item_remover]-(quantidadeR*cardapio[item_remover])
                                        print('Removendo {0} {1} da comanda...'.format( quantidadeR, item_remover))
                                        print('Quantidade atual de {0} na comanda: {1}'.format(item_remover,int(comanda[item_remover]/cardapio[item_remover])))
                                        j=False
                                    elif (comanda[item_remover] / cardapio[item_remover]) == quantidadeR: 
                                        print('Removendo {0} {1} da comanda...'.format( quantidadeR, item_remover))
                                        del comanda[item_remover]
                                        print('Quantidade atual da comanda: 0')
                                        j=False
                                    else:
                                        print('Não é possível remover mais do que a quantidade presente na comanda')
                                        j=True
                                else:
                                    print('Não é possível remover quantidade não positiva')
                                    j=True
                                p=False
                        else:
                            print('O produto não está na comanda.')
                            p=True
                        i=True
                elif escolha == 3:
                    if len(comanda)==0:
                        print('A comanda está vazia!')
                        i=True
                    elif len(comanda)>0:
                        conta_total=0
                        for produto in comanda:
                            print ('{0}:{1}'.format(produto,int(comanda[produto]/cardapio[produto])))
                            print ('Preço unitário: R${0}'.format(cardapio[produto]))
                            print ('preço total: R${0}'.format(comanda[produto]))
                            conta_total+=comanda[produto]
                        print('TOTAL: R${0}'.format(conta_total))
                        servico=conta_total*0.1
                        print('TOTAL (c/ 10%): R${0}'.format(conta_total + servico))
                            
                        i=True
                                   
                    
                else:
                    print('Faça uma escolha entre 0 e 4')
                    i=True
        
        else:
            print('digite uma comanda existente')
            y=False
        
    elif escolha_menu == 3:
        e=True
        while e == True:
            print('0 - voltar')
            print('1 - adicionar item ao cardápio')
            print('2 - remover item do cardápio')
            print('3 - alterar o preço de um produto no cardápio')
            
            escolha_alterar= int(input('Faça sua escolha:'))
            if escolha_alterar == 0:
                e=False
                j=True
               
            elif escolha_alterar == 1:
                l=True
                while l ==True:
                
                    item_adicionar=str(input('Nome do produto que deseja adicionar:'))
                    
                    if item_adicionar not in cardapio:
                        preco_adicionar=float(input('Preço do produto novo:'))
                        cardapio[item_adicionar]= preco_adicionar
                        print ('O item {0} foi adicionado ao cadápio com o preço de R${1}'.format(item_adicionar,preco_adicionar))
                        l=False
                        e=True
                        
                    else:
                        print ('O item "{0}" já está no cardápio'.format(item_adicionar))
                        l=True
                    
                
            elif escolha_alterar == 2:
                item_remover1=str(input('Nome do produto que deseja remover:'))
                if item_remover1 in cardapio:
                    del cardapio[item_remover]
                    print (cardapio)
                else:
                    print('Este item não está no cardápio')
                e=True
            elif escolha_alterar == 3:
                item_preco=str(input('Nome do produto do qual você gostaria de alterar o preço:'))
                preco_novo=float(input('Preço novo que deseja atribuir ao produto:'))
                if item_preco in cardapio:
                    cardapio[item_preco]=preco_novo
                    print('Preço novo do(a) {0} : {1}'.format(item_preco,preco_novo))
                else:
                    print('Este item não está no cardápio')
                e=True            
            else:
                print('Faça uma escolha entre 0 e 3')
                e=True
                
    elif escolha_menu == 4:
        print ('O cardápio possui os seguintes itens:')
        for item in cardapio:                       
            print ('-{0}:R${1}'.format(item,float(cardapio[item])))
        y=True
        
    else:
        print('Faça uma escolha entre 0 e 4')
        y=True


for key in comandas:
    for produto in comandas[key]:
        comandas[key][produto] = int(comandas[key][produto] / cardapio[produto])
 

cardapio_comandas['comandas'] = comandas
cardapio_comandas['cardapio']= cardapio     
           
novo_cardapio = json.dumps(cardapio, sort_keys = True, indent = 4)
with open ('cardapio.json','w') as arquivo:
    arquivo.write(novo_cardapio)
    
novo_comandas = json.dumps(comandas, sort_keys = True, indent = 4)
with open ('comanda.json','w') as arquivo1:
    arquivo1.write(novo_comandas)
 
novo_cardapio_comandas= json.dumps(cardapio_comandas,sort_keys = True ,indent =4)
with open ('cardapioecomandas.json', 'w') as arquivo:
    arquivo.write(novo_cardapio_comandas)
    
    
    

  
    
    
    
    