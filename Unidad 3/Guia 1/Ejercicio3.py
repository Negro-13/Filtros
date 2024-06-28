from PIL import Image

print('Hola, pon la ruta de la imagen q desee rotar:')
image = input()
print('Cuantos grados quiere rotar la imagen:')
angulos = int(input())
pokeimg = Image.open(image)
imgrotate = pokeimg.rotate(angulos)
imgrotate.save(image)
imgrotate.show()
