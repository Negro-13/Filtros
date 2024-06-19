from PIL import Image

print('Hola, pon el nobre de la imagen q desee saber datos')
image = input()
pokeimg = Image.open(f"Guia 1\Imgs\{image}.png")
pokeimg.show()
pokeimg.save('Guia 1\Imgs\Pokemon_Selecionado.png')