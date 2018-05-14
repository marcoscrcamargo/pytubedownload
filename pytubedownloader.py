import tkinter as tk

from pytube import YouTube
from pydub import AudioSegment

class Application:
	def __init__(self, master=None):
		self.main_widget = tk.Frame(master)
		self.main_widget.pack()
		self.insert_link = tk.Label(self.main_widget, text="Insira o link do YouTube:")
		self.insert_link["font"] = ("Verdana", "10", "italic", "bold")
		self.insert_link.pack()

		self.link_field = tk.Entry(self.main_widget)
		self.link_field.pack()

		self.download = tk.Button(self.main_widget, command = self.download_youtube)
		self.download["text"] = "Download"
		self.download["font"] = ("Calibri", "10")
		self.download["width"] = 8
		self.download.pack()

	def download_youtube(self):
		link = self.link_field.get()
		if(link == ""):
			tk.messagebox.showinfo("Erro", "Link vazio")
			return

		video = YouTube(link)
		# print("Baixando " + str(video.title) + " ...")
		stream = video.streams.filter(only_audio=True).first()

		# Faz download da stream
		stream.download(filename="temp")

		# print("Convertendo para mp3 ...")
		# Convertendo mp4 para mp3
		f_name = stream.player_config_args["title"]
		extention = stream.subtype

		# Abre o arquivo stream baixado
		stream_file = AudioSegment.from_file(file=str("temp." + extention), format=extention)
		# Convertendo e salvando arquivo mp3
		stream_file.export(out_f=f_name+".mp3", format="mp3")
		# print("Done.")
		tk.messagebox.showinfo("Sucesso", "Baixado com sucesso!")


root = tk.Tk()
Application(root)
root.mainloop()


