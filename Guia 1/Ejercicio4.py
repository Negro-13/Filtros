from PIL import Image

print('Hola, pon el nobre de la imagen q desee saber datos')
image = input()
print('Cuantos grados quiere rotar la imagen:')
angulos = int(input())
pokeimg = Image.open(f"Guia 1\Imgs\{image}.png")
cutpoke = pokeimg.crop((335, 345, 565))