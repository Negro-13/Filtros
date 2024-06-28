from PIL import Image
import os
## https://wiki.p-insurgence.com/images/1/16/330.png
print('Hola, pon el nobre de la imagen q desee saber datos')
image = input()
pokeimg = Image.open('./Imgs/zekrom.png')

print(f'La cantidad de pixels de la imagen son: {pokeimg.size}')