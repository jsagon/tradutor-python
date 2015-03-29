#coding: utf-8

#  
#  @JSagon - Jhonatan dos S. Gonçalves
#  http://www.jsagon.com
#
#  Classe responsável pela parte visual do programa
#  Versão 1.0
#

import sys

class Visual(object):

	def __init__ (self) :
		self.entrada = "> "
		self.pedido_entrada = "Entre com a opção desejada"

	def mostrar_ateristicos (self) :
		print ("*" * 70)

	def mostrar_texto (self, texto) :
		print (" %s" % texto)
		

	def tela_inicial (self) :
		self.mostrar_ateristicos()
		self.mostrar_texto("\t\tjTradutor - JSagon")
		self.mostrar_ateristicos()

	def creditos (self) :
		self.mostrar_ateristicos()
		self.mostrar_texto("\t\tCréditos - JSagon")
		self.mostrar_texto("")
		self.mostrar_texto("- Desenvolvedor : Jhonatan dos S. Gonçalves")
		self.mostrar_texto("- Linguagem : Python")
		self.mostrar_texto("- Sobre : Programa de tradução de palavras nos idiomas disponiveis")
		self.mostrar_texto("- Versao 1.0")
		self.mostrar_texto("- Site : www.jsagon.com")
		self.mostrar_texto("")
		self.mostrar_ateristicos()

	def menu_principal (self) :
		self.mostrar_texto(" \t\t MENU")
		self.mostrar_texto("")
		self.mostrar_texto("1  - Português > Inglês")
		self.mostrar_texto("2  - Inglês > Português")
		self.mostrar_texto("10 - Créditos")
		self.mostrar_texto("xxx - Para sair")

	def menu_traducao (self) :
		self.mostrar_texto("")
		self.mostrar_texto("Digite a palavra desejada ou (xxx) para voltar para o menu")

	def pegar_entrada (self) :
		self.mostrar_texto("")
		self.mostrar_texto(self.pedido_entrada)
		
		if sys.version_info >= (3, 0, 0) :
			return input("  %s" % self.entrada)
		else :
			return raw_input("  %s" % self.entrada)
