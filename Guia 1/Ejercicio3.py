from PIL import Image

print('Hola, pon el nobre de la imagen q desee saber datos')
image = input()
print('Cuantos grados quiere rotar la imagen:')
angulos = int(input())
pokeimg = Image.open(f"Guia 1\Imgs\{image}.png")
imgrotate = pokeimg.rotate(angulos).save(f'Guia 1\Rotateimg\{image}rot.png')
imgrotate.show()
