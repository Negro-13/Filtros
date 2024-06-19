from PIL import Image

print('Hola, pon el nobre de la imagen q desee saber datos')
image = input()
pokeimg = Image.open(f'Guia 1\Imgs\{image}.png')
nombre = pokeimg.filename
ext = pokeimg.format
resolucion = pokeimg.size
width, height = pokeimg.size
pixels = width * height

print(f'El nombre de la img es: {image}')
print(f'La extension es de: .{ext}')
print(f'La resolucion es de : {resolucion}')
print(f'La cantidad de pixels es: {pixels}')
print(f'La ruta de la img es: {pokeimg.filename}')
