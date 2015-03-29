#coding: utf-8

#  
#  @JSagon - Jhonatan dos S. Gonçalves
#  http://www.jsagon.com
#
#  Classe principal para controle das funcionalidades do programa
#  Versão 1.0
#

import visual_controller as v_controller
import arquivo_controller as arq_controller

class Programa (object) :

	def __init__(self) :
		visual = v_controller.Visual()
		visual.tela_inicial()
		visual.menu_principal()
		self.visual = visual
		self.arquivo = None
		self.iniciar_menu_1()

	def iniciar_menu_1 (self) : 

		while True :
			comando = self.visual.pegar_entrada()

			if comando == "xxx":
				self.visual.mostrar_texto("\n  Até mais... fechado")
				break

			if comando == '1' :
				self.iniciar_menu_2(1)
			
			elif comando == '2' :
				self.iniciar_menu_2(2)

			elif comando == '10' :
				self.visual.creditos()
				self.visual.mostrar_texto("\n  Digite qualquer coisa para voltar...")
				self.visual.pegar_entrada()
				self.visual.mostrar_ateristicos()
				self.visual.menu_principal()
			
			else : 
				self.visual.mostrar_texto("Opção inválida")

	def iniciar_menu_2 (self, indice) :
		self.visual.mostrar_ateristicos()
		
		if indice == 1 :
			self.arquivo = arq_controller.Arquivo("idiomas_arq/pt_eng.txt")
			self.visual.mostrar_texto("\n\t\tTradução Português - Inglês\n")

		elif indice == 2 : 
			self.arquivo = arq_controller.Arquivo("idiomas_arq/eng_pt.txt")
			self.visual.mostrar_texto("\n\t\tTradução Inglês - Português\n")

		self.arquivo.abrir_arquivo_leitura()

		self.visual.menu_traducao()
		
		while True:
			comando = self.visual.pegar_entrada()

			if comando == "xxx":
				self.visual.mostrar_ateristicos()
				self.visual.menu_principal()
				break

			texto = self.arquivo.pegar_ocorrencia_linhas(comando)

			cont = 0
			for l in texto :
				cont+=1
				self.visual.mostrar_texto("\n  "+ str(cont) +" - " + l + "\n")
			self.visual.mostrar_ateristicos()

