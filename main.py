import os
from PIL import Image
from PIL import ImageTk
import sys
from tkinter import Label,Tk,filedialog
from threading import Thread
from functools import partial

INIT_SCREEN = '''
CONVERSOR DE IMAGEM PARA ASCII ART\n\n
[1] Selecionar imagem\n		
[0] Sair\n\n
[ option ] :  '''

FILE_SELECTOR = '''
\n\n\t[FILE SELECTOR]
\n\n	Select a file to convert to ASCII_ART\n
	Enter [ < ] to go back on the folders tree\n
	Enter [ number ] to select a image or open a folder\n
	Enter [ x ] to close the program\n
\n\nFOLDER> '''

class ImageSelector:
      
    def terminal(self):
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
                if '.' not in entry: ok = True
                else: ok = False
                for fileType in ['.jpg','.jpge','.gif','.tiff','.png']:
                    if fileType in entry[-5:]:
                        ok = True
                if ok: newList.append(entry)
            osDirList = newList
            print(FILE_SELECTOR,dir,'\n')
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
    
    def tkinter(self):
        file = filedialog.askopenfilename()
        return file

class Image_To_AscIIART:

    def __init__(self,interface):
        self.interface = interface
    
    def generateAscII_ART(self,file,sx,sy):
        print('\n'*400)
        chars = """$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'."""
        image = Image.open(file)
        imageResized = image.resize((sx,sy))
        imageRecolored = imageResized.convert('L')
        pixelsList = imageRecolored.load()
        ascII_ART = ''
        for x in range(1,sy):
            for y in range(1,sx):
                char = int( pixelsList[y,x] / 3.7 )
                ascII_ART += chars[char]
            ascII_ART += '\n'
        return ascII_ART
        
    def saveArt(self,art,path='ascII_ART.txt'):
        with open(path,'w') as file:
            file.write(art)
    
    def app(self):
        file = None
        
        if self.interface == 'tkinter':
            file = ImageSelector().tkinter()
            
        elif self.interface == 'terminal':
            print('\n'*400)
            option = input(INIT_SCREEN)
            if option == '1':
                file = ImageSelector().terminal()        
            elif option == '0': sys.exit()
        
        print('IMAGE: ',file)
        sx = int(input('size X: '))
        sy = int(input('size Y: '))
        ascII_ART = self.generateAscII_ART(file,sx,sy)
        self.saveArt(art=ascII_ART)
        print('\n'*400)
        Image.open(file).show()
        print(ascII_ART)
        
        if self.interface == 'terminal':
            input(f'''\nIMAGE: {file}\n\nSIZE: {sx}  X  {sy}\n\n\n[ENTER] to continue''')
        else:
            print(f'''\nIMAGE: {file}\n\nSIZE: {sx}  X  {sy}\n\n\n''')
        
        return self.app()

modes = ['terminal','tkinter']

if __name__ == '__main__':
    Image_To_AscIIART(modes[0]).app()