#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 18:13:35 2018

@author: h.t
"""
x = True
dicionario = {}
while x == True:
    print("Controle de estoque\n")
    print("0 - Sair\n")
    print("1 - Adicionar Item\n")
    print("2 - Remover Item\n")
    print("3 - Alterar Item\n")
    print("4 - Imprimir Estoque\n")
    escolha = int(input("faça sua escolha:"))
    if escolha == 0:
        print("Até mais!\n")
        x = False
    if escolha == 1:
        produto = input("Nome do produto:")
        if produto in dicionario:
            print("Produto já esta cadastrado\n")
        else:
            quantidade = int(input("Quantidade Inicial:"))
            while quantidade < 0:
                print("A quantidade inicial não pode ser negativa\n")
                quantidade = int(input("Quantidade Inicial:"))
            dicionario[produto] = quantidade
            print(dicionario[produto])
    if escolha == 2:
        produto_a_remover = input("Nome do Produto:")
        if produto_a_remover not in dicionario:
            print("Elemento não encontrado\n")
        else:
            del dicionario[produto_a_remover]
    if escolha == 3:
        produto_alterado = input("Nome do Produto:")
        while produto_alterado not in dicionario:
            print("Elemento não encontrado\n")
            produto_alterado = input("Nome do Produto:")
        quantidade = int(input("Quantidade:"))
        dicionario[produto_alterado] += quantidade
        print("novo estoque de {0}: {1}\n".format(produto_alterado, dicionario[produto_alterado]))
    if escolha == 4:
        for key,values in dicionario.items():
            print("\n{0}: {1}\n".format(key, values))
            

        
  
     