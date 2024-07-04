from PIL import Image
print('Hola, ponla ruta de la imagen q desee saber datos')
image = input()
pokeimg = Image.open(image)
print('Coloque la drieccion de la imagen a poner como marca de agua')
imagua = input()
imagepaste = Image.open(imagua)

print(f'Su rango de cordenadas de largo es {width}, y su altura es de {height}')
while True:
    print('Selecione cordenada del borde superior izquierdo:')
    bsi = int(input())
    print('Selecione cordenada del borde superior derecho:')
    bsd = int(input())
    print('Selecione cordenada del borde inferior izquierdo:')
    bii = int(input())
    print('Selecione cordenada del borde inferior derecho:')
    bid = int(input())
    if bsi > 50 and bsi < (width - 49) and bsd > 51 and bsd < (width - 50) and bii > 50 and bii < (height - 49) and bid > 51 and bid < (height - 50):
        image
        
