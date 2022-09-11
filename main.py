import sys
from PIL import Image
import time
from tqdm import tqdm 
import colorama
from math import sqrt
colorama.init()
COLOR = [(139,69,19),(222,171,190),(0,0,0),(58,150,221),(0,55,218),(19,161,14),(118,118,188), (97,214,214), (22,198,12),(180,0,158), (231,72,86),(231,72,86),(249,241,165),(59,120,255),(193,156,0),(136,23,152),(197,15,31),(204,204,204)]
COLORS = {
    "(0,0,0)":colorama.Back.RESET+" "+colorama.Back.RESET,
    "(139,69,19)":colorama.Back.BLACK+" "+colorama.Back.RESET,
    "(58,150,221)":colorama.Back.CYAN+" "+colorama.Back.RESET,
    "(0,55,218)":colorama.Back.BLUE+" "+colorama.Back.RESET,
    "(19,161,14)":colorama.Back.GREEN+" "+colorama.Back.RESET
    ,"(118,118,188)":colorama.Back.LIGHTBLACK_EX+" "+colorama.Back.RESET
    ,"(97,214,214)":colorama.Back.LIGHTCYAN_EX+" "+colorama.Back.RESET
    ,"(22,198,12)": colorama.Back.LIGHTGREEN_EX+" "+colorama.Back.RESET
   ,"(180,0,158)":colorama.Back.LIGHTMAGENTA_EX+" "+colorama.Back.RESET
    ,"(231,72,86)":   colorama.Back.LIGHTRED_EX+" "+colorama.Back.RESET
    ,"(222,171,190)": colorama.Back.LIGHTWHITE_EX +" "+colorama.Back.RESET,"(249,241,165)":colorama.Back.LIGHTYELLOW_EX+" "+colorama.Back.RESET,"(59,120,255)":colorama.Back.LIGHTBLUE_EX+" "+colorama.Back.RESET,"(193,156,0)":        colorama.Back.YELLOW+" "+colorama.Back.RESET,
        "(136,23,152)": colorama.Back.MAGENTA+" "+colorama.Back.RESET
   ,"(197,15,31)": colorama.Back.RED+" "+colorama.Back.RESET,"(204,204,204)": colorama.Back.WHITE+" "+colorama.Back.RESET,
}
def closest_color(rgb):
    r, g, b = rgb
    color_diffs = []
    for color in COLOR:
        cr, cg, cb = color
        color_diff = sqrt((r - cr)**2 + (g - cg)**2 + (b - cb)**2)
        color_diffs.append((color_diff, color))
    coll = min(color_diffs)[1]
    coll = (",".join([str(value) for value in coll]))
    return COLORS["("+coll+")"]
def imageToASCII(size,pixel):
  
    ll  = []
    text = ""
    list2 = []
    t = time.time()
    for y in tqdm(range(size[1])):
        for x in range(size[0]):
            color = pixel[x,y]
            text= text + (closest_color((color[0],color[1],color[2])))
        ll.append(text)
        text = ""
    list2.append("\n".join(ll))
    for i in list2:
        sys.stdout.writelines(i)    

def main():
    args = sys.argv
    if len(args)==3:
        path = str(args[1])
        new_width = int(args[2])
        if path != None:

            img = Image.open(path)
            width, height = img.size
            aspect_ratio = height/width
            new_height = aspect_ratio * new_width * 0.35
            im = img.resize((new_width, int(new_height)))
            size = im.size
            pixel = im.load()
            imageToASCII(size,pixel)

if __name__=="__main__":
    main()



