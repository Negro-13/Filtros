from PIL import Image
image = input('Hola, ponla ruta de la imagen q desee saber datos')
pokeimg = Image.open(image)
pokeimg.show()
pokeimg.save('Guia 1\Imgs\img_Selecionado.png')