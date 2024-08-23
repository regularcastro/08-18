from rembg import remove
# fornece ao interpretador python recursos de edição de imagem
from PIL import Image

img_entrada = 'images.jpg'
img_saida = 'images.png'
input = Image.open(img_entrada)
output = remove(input)
#salvando a imagem
output.save(img_saida)