import random

def firstPic(filename,length,width,scale,thePic):
    add = "P3\n" + str(length) + " " + str(width) + "\n" + str(scale) + "\n"
    newFile = open(filename + ".ppm",'w')
    looky = open("lookey.txt",'w');
    newFile.write(add+thePic)
    looky.write(add+thePic)
    looky.close()
    newFile.close();

def theGoods():
    ans = ""
    for r in range (0,500*500):
        for c in range (0,3):
            color = random.randint(0,256)
            ans += str(color) + " "
    return ans
    
firstPic("c0l0r",500,500,255,theGoods())
