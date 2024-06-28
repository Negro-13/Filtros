from PIL import Image

print('Hola, pon la ruta la imagen q desee saber datos')
image = input()
pokeimg = Image.open(image)
nombre = pokeimg.filename
ext = pokeimg.format
resolucion = pokeimg.size
width, height = pokeimg.size
pixels = width * height

print(f'El nombre de la img es: {nombre}')
print(f'La extension es de: .{ext}')
print(f'La resolucion es de : {resolucion}')
print(f'La cantidad de pixels es: {pixels}')
print(f'La ruta de la img es: {pokeimg.filename}')
