from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.dropdown import DropDown
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.lang.builder import Builder

import domain

stringHeader = """
<CustomDropDown>:
"""


model = """
	Button:
		text: '{0}'
		size_hint_y: None
		height: 44
		on_release: root.select('{0}')
"""
for ano in range(1990,2023):
    stringHeader += model.format(ano)

stringBuilder = Builder.load_string(stringHeader)

class CustomDropDown(DropDown):
    def build():
        return stringBuilder


class DropdownDemo(FloatLayout):
	anoEscolhido = 0
	def __init__(self, **kwargs):
		super(DropdownDemo, self).__init__(**kwargs)
		self.dropdown = CustomDropDown()
		self.mainbutton = Button(text ='Escolha o Ano',
								size_hint = (1., 1.),
								pos_hint = {"top":1., "center_x":.5})
		self.add_widget(self.mainbutton)
		self.mainbutton.bind(on_release = self.dropdown.open)
		self.dropdown.bind(on_select = lambda\
						instance, x: setattr(self.mainbutton, 'text', x))
		self.dropdown.bind(on_select = self.callback)

	def callback(self, instance, ano):
		self.anoEscolhido = int(ano)

class RVAnoScreen(RecycleView):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.data = []

class BuscaPorAnoScreen(BoxLayout):
	checkBoxSelect = 0

	def showDataAno(self):
		lista = []
		model = "Numero:\n%d\nNome do Album:\n%s\nAno do lancamento:\n%s\nBanda/Artista:\n%s\nAlbum lancamento do artista:\n%s\n"
		listaNomes = domain.buscarPorAnoBanda(self.ids.dropdown.anoEscolhido, self.checkBoxSelect)

		for linha in listaNomes:
			num, nomeAlbum, anoLancamento, bandaArtista, lancamentoAB = linha
			lista.append( model%(num,nomeAlbum, anoLancamento, bandaArtista, lancamentoAB))
		self.ids.recycleBuscaAno.data = [{'text': text} for text in lista]

	def checkBoxClick(self, instace, value, condicao):
		if value == True:
			self.checkBoxSelect = condicao
			print(f"{condicao} ativo")
	
class RVNomeScreen(RecycleView):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.data = []

class BuscaPorNomeScreen(BoxLayout):
	def showData(self):
		nome = self.ids.nomeParaBusca.text
		lista = []
		model = "Numero:\n%d\nNome do Album:\n%s\nAno do lancamento:\n%s\nBanda/Artista:\n%s\nAlbum lancamento do artista:\n%s\n"
		listaNomes = domain.buscarPorNomeArtistaBanda(nome)


		for linha in listaNomes:
			num, nomeAlbum, anoLancamento, bandaArtista, lancamentoAB = linha
			lista.append( model%(num,nomeAlbum, anoLancamento, bandaArtista, lancamentoAB))
		
		
		self.ids.recycleBuscaNome.data = [{'text': text} for text in lista]

class ListaScreen(BoxLayout):
	pass

class RVListaScreen(RecycleView):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		modelList = []
		model = "Numero:\n%d\nNome do Album:\n%s\nAno do lancamento:\n%s\nBanda/Artista:\n%s\nAlbum lancamento do artista:\n%s\n"
		num = 1
		for linha in db.lerTodoBancoDeDados():
			nomeAlbum, anoLancamento, bandaArtista, lancamentoAB = linha
			modelList.append( model%(num,nomeAlbum, anoLancamento, bandaArtista, lancamentoAB))
			num += 1
		
		
		self.data = [{'text': text} for text in modelList]

class FirstScreen(BoxLayout):
	checkBoxSelect = "Dado não informado"

	def checkBoxClick(self, instace, value, text):
		if value == True:
			self.checkBoxSelect = f'{text}'
			print(f"{text} ativo")

	def onPressSalvar(self):
		nomeAlbum     = self.ids.nomeAlbum.text
		anoLancamento = self.ids.anoLancamento.text
		bandaArtista  = self.ids.bandaArtista.text
		lancamentoAB  = self.checkBoxSelect
		
		domain.salvarDados(nomeAlbum, anoLancamento, bandaArtista, lancamentoAB)

		self.ids.nomeAlbum.text, self.ids.anoLancamento.text, self.ids.bandaArtista.text, self.ids.lancamentoAB.text = "","","",""

	def onPressLista(self):
		window.root_window.remove_widget(window.root)
		window.root_window.add_widget(ListaScreen())
	
	def onPressBuscaNome(self):
		window.root_window.remove_widget(window.root)
		window.root_window.add_widget(BuscaPorNomeScreen())
	
	def onPressBuscaAno(self):
		window.root_window.remove_widget(window.root)
		window.root_window.add_widget(BuscaPorAnoScreen())



class GUIApp(App):
	def onPressVoltar(self):
		window.root_window.remove_widget(window.root)
		window.root_window.add_widget(FirstScreen())

if __name__ == "__main__":
	window = GUIApp()
	window.run()