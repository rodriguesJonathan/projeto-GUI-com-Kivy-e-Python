from distutils.command.build import build
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView
import db


class ListaScreen(BoxLayout):
	def on_press_voltar(self):
		window.root_window.remove_widget(window.root)
		window.root_window.add_widget(FirstScreen())

class RV(RecycleView):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		print(kwargs)
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

	def on_press_salvar(self):
		nomeAlbum     = self.ids.nomeAlbum.text
		anoLancamento = self.ids.anoLancamento.text
		bandaArtista  = self.ids.bandaArtista.text
		lancamentoAB  = self.checkBoxSelect
		
		db.inserirNoBanco(nomeAlbum, anoLancamento, bandaArtista, lancamentoAB)

		self.ids.nomeAlbum.text, self.ids.anoLancamento.text, self.ids.bandaArtista.text, self.ids.lancamentoAB.text = "","","",""

	def on_press_lista(self):
		window.root_window.remove_widget(window.root)
		window.root_window.add_widget(ListaScreen())


class GUIApp(App):
	pass

if __name__ == "__main__":
	window = GUIApp()
	window.run()