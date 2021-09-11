from skimage import io,transform
from numpy import *

def F(x, y, img):          #灰度分布
    if len(img.shape)== 3:
        return 0.3*img[x,y,0]+0.59*img[x,y,1]+0.11*img[x,y,2]
    else:
        return img[x,y]

def General_Matrix(p,q,img):            #笛卡尔系几何矩
    m = 0
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            m += (x**p)*(y**q)*(F(x, y, img))
    return m

def I0(img):
    return General_Matrix(1,0,img)/General_Matrix(0,0,img)

def J0(img):
    return General_Matrix(0,1,img)/General_Matrix(0,0,img)

def Central_Matrix(m,n,img):            #中心矩
    u = 0
    I_0 = I0(img)
    J_0 = J0(img)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            u += F(i,j,img)*((i-I_0)**m)*((j-J_0)**n)
    return u

def Standardized_central_moment(m,n,img):
    return Central_Matrix(m,n,img)/((General_Matrix(0,0,img))**((m+n+2)/2))

def Hu_Invariant_Moment(img):
    I20 = Standardized_central_moment(2,0,img)
    I02 = Standardized_central_moment(0,2,img)
    I11 = Standardized_central_moment(1,1,img)
    I30 = Standardized_central_moment(3,0,img)
    I12 = Standardized_central_moment(1,2,img)
    I21 = Standardized_central_moment(2,1,img)
    I03 = Standardized_central_moment(0,3,img)
    C1 = I20+I02
    # print(C1)
    C2 = (I20-I02)**2+4*I11**2
    # print(C2)
    C3 = (I30-3*I12)**2+(3*I21-I03)**2
    # print(C3)
    C4 = (I30+I12)**2+(I21+I03)**2
    # print(C4)
    C5 = (I30-3*I12)*(I30+I12)*((I30+I12)**2-3*(I21+I03**2))+(3*I21-I03)*(I21+I03)*(3*(I30+I12)**2-(I21+I03)**2)
    # print(C5)
    C6 = (I20-I02)*((I30+I12)**2-(I21+I03)**2)+4*I11*(I30+I12)*(I21+I03)
    # print(C6)
    C7 = (3*I21-I03)*(I30+I12)*((I30+I12)**2-3*(I21+I03)**2)-(I30-3*I12)*(I21+I03)*(3*(I03+I12)**2-(I21+I03)**2)
    # print(C7)
    return C1,C2,C3,C4,C5,C6,C7

def extract_shape_feature():
    fl = open('../feats/shape3.txt','w')
    f2 = open('pictuer_path.txt','r')
    paths = f2.readlines()[6617:]
    for path in paths:
        path = path.rstrip('\n')
        print(path)
        img = io.imread(path)
        img = transform.resize(img, (128, 128))
        C1,C2,C3,C4,C5,C6,C7 = Hu_Invariant_Moment(img)
        fl.write(path+'\t')
        fl.write(str(C1)+',')
        fl.write(str(C2)+',')
        fl.write(str(C3)+',')
        fl.write(str(C4)+',')
        fl.write(str(C5)+',')
        fl.write(str(C6)+',')
        fl.write(str(C7))
        fl.write('\n')
    fl.close()

# if __name__ == '__main__':
    # extract_shape_feature()