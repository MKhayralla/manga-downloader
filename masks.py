from PIL import Image
colors = {
    'red' : (255, 0, 0),
    'green' : (0, 255, 0),
    'blue' : (0, 0, 255),
    'yellow' : (250, 218, 94)
}
def color_mask(img, color):
    mask = Image.new('RGB',img.size,colors[color])
    alpha = Image.new('RGBA',img.size,(0,0,0,220))
    return Image.composite(img,mask,alpha).convert('RGB')