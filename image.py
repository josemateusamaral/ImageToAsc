import os
from PIL import Image
from PIL import ImageTk
import sys
from tkinter import Label,Tk

INIT_SCREEN = '''
CONVERSOR DE IMAGEM PARA ASCII ART\n\n
[1] Selecionar imagem\n		
[0] Sair\n\n
[ option ] :  '''

class Image_To_AscIIART:
		
	def selectImage(self):
		dir = os.getcwd()
		while True:
			print('\n'*400)
			try: osDirList = os.listdir(dir)
			except:
				input('Voce nao pode acessar este diretorio\n[ENTER] para continuar')
				dir = os.getcwd()
				continue
			newList = []
			for entry in osDirList:
				ok = False
				if '.' not in entry: 
					ok = True
				for fileType in ['.jpg','.jpge','.gif','.tiff','.png']:
					if fileType in entry[-5:]:
						ok = True
						continue
				if ok: newList.append(entry)
			osDirList = newList
			print('\n\nDIR: ',dir,'\n')
			for index,i in enumerate(osDirList): print('\n[',index,']\t',i)
			option = input('\noption: ')
			if option == '<':
				os.chdir('..')
				dir = os.getcwd()
				continue
			esc = osDirList[int(option)]
			if '.' in esc:
				print('\n'*400)
				return f'{dir}\\{esc}'
			else: dir += f'\{esc}'
			
	def renderAscImage(self,file,sx,sy):
		print('\n'*400)
		chars = """$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'."""
		image = Image.open(file)
		imageResized = image.resize((sx,sy))
		imageRecolored = imageResized.convert('L')
		pixelsList = imageRecolored.load()
		for x in range(1,sy):
			for y in range(1,sx):
				char = int( pixelsList[y,x] / 3.7 )
				print(chars[char],end='')
			print()
		print(f'''\n
		IMAGE: {file}
		SIZE: {sx}  X  {sy}\n\n
		[ENTER] to continue''')
		self.showOriginalImage(file)
		self.app()

	def showOriginalImage(self,image):
		self.window = Tk()
		self.window.title('original image - ' + image)
		n = int(self.window.winfo_screenheight()/3)
		self.window.geometry(f'{n}x{n}+{n}+{n}')
		tkImage = ImageTk.PhotoImage(Image.open(image))
		Label(master=self.window,image=tkImage).pack()
		self.window.mainloop()

	def app(self):
		print('\n'*400)
		option = input(INIT_SCREEN)
		if option == '1':
			file = self.selectImage()
			print('IMAGE: ',file)
			sx = int(input('size X: '))
			sy = int(input('size Y: '))
			self.renderAscImage(file,sx,sy)
		elif option == '0': sys.exit()
		return 

Image_To_AscIIART().app()