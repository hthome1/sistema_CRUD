#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 18:13:35 2018

@author: h.t
"""
import json
with open ('arquivo_texto.json','r') as arquivo:
    texto = arquivo.read()
dicionario = json.loads(texto)
x = True
estoque = 'Estoque'
preco = 'Preco'
while x == True:
    print("Controle de estoque\n")
    print("0 - Sair\n")
    print("1 - Adicionar Item\n")
    print("2 - Remover Item\n")
    print("3 - Alterar Item\n")
    print("4 - Informações sobre estoque\n")
    escolha = int(input("faça sua escolha:"))
    if escolha == 0:
        print("Até mais!\n")
        x = False
    if escolha == 1:
        produto = input("Nome do produto:").upper()
        if produto in dicionario:
            print("Produto já esta cadastrado\n")
        else:
            quantidade = int(input("Quantidade Inicial:"))
            preco_unitario = float(input("Preço unitário do produto:"))
            while quantidade < 0 or preco_unitario < 0:
                print("A quantidade inicial e o preço não podem ser negativos\n")
                quantidade = int(input("Quantidade Inicial:"))
                preco_unitario = int(input("Preço unitário do produto:"))
            dicionario[produto] = {}
            dicionario[produto][estoque] = quantidade
            dicionario[produto][preco] = preco_unitario
            print(dicionario[produto])
    if escolha == 2:
        produto_a_remover = input("Nome do Produto:").upper()
        if produto_a_remover not in dicionario:
            print("Elemento não encontrado\n")
        else:
            del dicionario[produto_a_remover]
    if escolha == 3:
        produto_alterado = input("Nome do Produto:").upper()
        if produto_alterado in dicionario:
            escolha_2 = int(input("1 - alterar o estoque\n2 - alterar o preço\nFaça sua escolha:"))
            if escolha_2 == 1:
                quantidade = int(input("Quantidade:"))
                dicionario[produto_alterado][estoque] += quantidade
                print("novo estoque de {0}: {1}\n".format(produto_alterado, dicionario[produto_alterado][estoque]))
            if escolha_2 == 2:
                novo_preco = float(input("novo preço:"))
                while novo_preco < 0:
                    print("O preço não pode ser negativo")
                    novo_preco = int(input("Quantidade:"))
            dicionario[produto_alterado][preco] = novo_preco
        else:
            print("Elemento não encontrado")
    if escolha == 4:
        escolha_3 = int(input("1 - imprimir estoque\n2 - Produtos com estoques negativos\n3 - Valor monetário\nFaça sua escolha:"))
        if escolha_3 == 1:
            for key in dicionario:
                print("\n{0}: {1}\n".format(key, dicionario[key][estoque]))
        if escolha_3 == 2:
            lista_prod_neg = []
            for key in dicionario:
                if dicionario[key][estoque] < 0:
                    lista_prod_neg.append(key)
                    for i in lista_prod_neg:
                        print(i)
        if escolha_3 == 3:
            resultado = 0
            for key in dicionario:
                if dicionario[key][estoque] > 0:
                    resultado += dicionario[key][estoque] * dicionario[key][preco]
            print("\nSeu estoque tem o valor de {0}\n".format(resultado))
            
novo_dicionario = json.dumps(dicionario, sort_keys = True, indent = 4)
with open ('arquivo_texto.json','w') as arquivo:
    arquivo.write(novo_dicionario)  
    