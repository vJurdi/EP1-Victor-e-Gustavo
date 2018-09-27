# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 17:48:58 2018

@author: victo
"""

import tkinter as tk


class restaurante:
        
    def __init__(self):
        
        self.window=tk.Tk()
        self.window.geometry("300x200+100+100")
        self.window.rowconfigure(0, minsize=150, weight=1)
        self.window.rowconfigure(1, weight=1)
        self.window.columnconfigure(0, minsize=120, weight=1)
        self.window.columnconfigure(1, weight=1)
        self.texto = 'Menu do restaurante:'
        
        #escrita na tela       
        self.conteudo_label = tk.StringVar()
        self.label = tk.Label(self.window)
        self.label.configure(textvariable=self.texto)
        self.label.configure(font="Courier 20 bold")
        self.label.grid(row=0, column=0, columnspan=2, sticky="nsew") 
        
        #caixa de texto
        self.escolha_menu = tk.StringVar()
        
        caixa_texto = tk.Entry(self.window)
        caixa_texto.configure(textvariable=self.escolha_menu)
        caixa_texto.grid(row=1, column=0, padx=20, sticky="ew")
        
        caixa_texto.bind("<Return>", self.apertou_enter)
        
        #botão "Menu do Restaurante"
        self.botao=tk.Button(self.window)
        self.botao.grid()
        self.botao.configure(text='Menu do Restaurante')
        self.botao.configure(command=self.Menu_Restaurante)
    
    
    def iniciar(self):
        self.window.mainloop()
        
    
    
    def Menu_Restaurante(self):
        self.label.configure(text="oi")
    
        print('Menu do restaurante:')
        print('0 - sair')
        print('1 - adicionar comanda')
        print('2 - acessar comanda')
        print('3 - Alterar cardápio')
        print('4 - imprimir cardápio')
        
    def Comanda_eletronica(self):
        print('Comanda eletrônica')
        print('0 - voltar')
        print('1 - adicionar item')
        print('2 - remover item')
        print('3 - imprimir comanda')
        
    def Alterar_cardapio(self):
        print('0 - voltar')
        print('1 - adicionar item ao cardápio')
        print('2 - remover item do cardápio')
        print('3 - alterar o preço de um produto no cardápio')
        
    def apertou_enter(self, event):
        self.enter()
        
    def enter(self):
        self.conteudo_label.set(self.escolha_menu.get())
    
               
app=restaurante()
app.iniciar()