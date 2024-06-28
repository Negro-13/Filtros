from PIL import Image

print('Hola, pon la ruta de la imagen desea cortar')
image = input()
resolucion = image.size
print(f'Esta es la resolucion de su imagen: {resolucion} ')
print('Selecione las cordenadas en las q quiera cortar su imagen:')
bi = int(input())
bis = int(input())
bd = int(input())
bdi = int(input())
pokeimg = Image.open(image)
cutpoke = pokeimg.crop((bi, bis, bd, bdi))
cutpoke.save('Guia 1\Recortes\pokecut.png')
cutpoke.show()