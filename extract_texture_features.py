from skimage import io
from numpy import *
from math import sqrt

gray_level = 16

def F(x,y,img):
    if(len(img.shape)==2):
        return int(img[x,y])
    return int(0.3*int(img[x,y,0])+0.59*int(img[x,y,1])+0.11*int(img[x,y,2]))

def GetP(string,d_x,d_y):
    # print(string)
    img = io.imread(string)
    x = img.shape[0]
    y = img.shape[1]
    max_gray = 0
    for i in range(x):
        for j in range(y):
            if F(i,j,img) > max_gray:
                max_gray = F(i,j,img)
    P = zeros((gray_level+1,gray_level+1),int)
    if max_gray > gray_level:
        for i in range(1,x-1):
            for j in range(1,y-1):
                P[int(F(i,j,img)*gray_level / max_gray)][int(F(i+d_x,j+d_y,img)*gray_level / max_gray)] += 1
    else:
        for i in range(1,x-1):
            for j in range(1,y-1):
                P[F(i,j,img)][F(i+d_x,j+d_y,img)] += 1
    return P

def Get_mean_value(x):
    return mean(x)

def Get_standard_deviation(x):
    m = mean(x)
    sum = 0
    for i in range(len(x)):
        sum = (x[i]-m)**2
    return sqrt(sum/(len(x)-1))

def Getfeature(P):          #对比度的纹理特征
    COM = 0
    ASM = 0
    REL = 0
    ENG = 0
    for i in range(P.shape[0]):
        for j in range(P.shape[1]):
            COM += (i-j)**2*P[i][j]
            ASM += P[i][j]*P[i][j]
            if Get_standard_deviation(P[i])*Get_standard_deviation(P[j]) != 0:
                REL +=((i-Get_mean_value(P[i,:]))*(j-Get_mean_value(P[:,j]))*P[i][j])/(Get_standard_deviation(P[i])*Get_standard_deviation(P[j]))
            if P[i][j]>0.0:
                ENG += P[i][j]*math.log(P[i][j])
    return COM,ASM,REL,ENG


def Write_to_file():
    fl = open('../feats/texture3.txt','w')
    f2 = open('pictuer_path.txt')
    pict_paths = f2.readlines()[2570+5970:]
    for pictpath in pict_paths:
        pictpath = pictpath.rstrip('\n')
        com = []
        asm = []
        rel = []
        eng = []

        P = GetP(pictpath,1,0)
        COM,ASM,REL,ENG = Getfeature(P)
        com.append(COM)
        asm.append(ASM)
        rel.append(REL)
        eng.append(ENG)
        P = GetP(pictpath,0,1)
        COM,ASM,REL,ENG = Getfeature(P)
        com.append(COM)
        asm.append(ASM)
        rel.append(REL)
        eng.append(ENG)
        P = GetP(pictpath,1,1)
        COM,ASM,REL,ENG = Getfeature(P)
        com.append(COM)
        asm.append(ASM)
        rel.append(REL)
        eng.append(ENG)
        P = GetP(pictpath,-1,1)
        COM,ASM,REL,ENG = Getfeature(P)
        com.append(COM)
        asm.append(ASM)
        rel.append(REL)
        eng.append(ENG)
        fl.write(pictpath+'\t')
        fl.write(str(Get_mean_value(com)))
        fl.write(',')
        fl.write(str(Get_mean_value(asm)))
        fl.write(',')
        fl.write(str(Get_mean_value(rel)))
        fl.write(',')
        fl.write(str(Get_mean_value(eng)))
        fl.write(',')
        fl.write(str(Get_standard_deviation(com)))
        fl.write(',')
        fl.write(str(Get_standard_deviation(asm)))
        fl.write(',')
        fl.write(str(Get_standard_deviation(rel)))
        fl.write(',')
        fl.write(str(Get_standard_deviation(eng)))
        fl.write('\n')
    fl.close()
    f2.close()

# if __name__ == '__main__':
#     Write_to_file()