from PIL import Image

print('Hola, pon la ruta de la imagen desea cortar')
image = input()
pokeimg = Image.open(image)
resolucion = pokeimg.size
width , height = pokeimg.size
print(f'Esta es la resolucion de su imagen: {resolucion} ')
print('Selecione las cordenadas en las q quiera cortar su imagen:')
bi = int(input())
bis = int(input())
bd = int(input())
bdi = int(input())
while True:
    if bi > 0 and bi < width and bd > 1 and bd < width and bis > 0 and bis < height and bdi > 1 and bdi < height:
        cutpoke = pokeimg.crop((bi, bis, bd, bdi))
        break
    else:
        print('Selecione cordenadas validas')
        bi = int(input())
        bis = int(input())
        bd = int(input())
        bdi = int(input())
        
cutpoke.save('Recortes\imgcut.png')
cutpoke.show()
