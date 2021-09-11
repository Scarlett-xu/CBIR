from tkinter import *
import tkinter.filedialog
from PIL import Image, ImageTk
import time
from test import *

#总框架
root = Tk()
root.title('图像检索系统')
root.geometry('960x520') # 这里的乘号不是 * ，而是小写英文字母 x

col_count, row_count = root.grid_size()
for col in range(col_count):
    root.grid_columnconfigure(col, minsize=20)

choose1 =StringVar()
query = StringVar()
messagevar = StringVar()

def func2():
    filename=tkinter.filedialog.askopenfilename()

    messagevar.set("文件路径："+filename)
    if filename != '':
        component22['text'] = filename
        image = Image.open(filename)
        query.set(filename)
        image = image.resize((200,100))
        pyt = ImageTk.PhotoImage(image)
        component1.config(image=pyt)
        component1.image = pyt
    else:
        component22['text'] = "您还未上传文件！"
        component1.config(text='您没有选择任何文件')






#lb：1
component1 = Label(root,text='')
background = Image.open('background.png')
background = background.resize((200, 100))
pyt = ImageTk.PhotoImage(background)
component1.config(image=pyt)
component1.grid(row = 0, column = 0,padx=20, pady=20)

component2 = Frame(root,relief=RAISED)
component2.grid(row = 1, column = 0,ipady = 1)


component21 = Button(component2,text="     上传文件    ",command=func2)
component21.pack(fill = X)

component22 = Label(component2, text='图片库共9145张图片', fg="red", bg="white", height=2, width=30,
                    anchor="nw")
component22.pack(fill = X)


component3 = Frame(root,relief=RAISED)
component3.grid(row = 2, column = 0,padx=20, pady=1)

def myPrint(self):
    choose1.set(Chooses.get(Chooses.curselection()))

Chooses = Listbox(component3)

for item in ["颜色直方图","纹理特征","形状特征","哈希算法","VGG模型"]:
    Chooses.insert("end",item)
Chooses.pack(side = RIGHT)



Chooses.bind("<Double-Button-1>",myPrint)


def chuliimg(path):
    image = Image.open(path)
    image = image.resize((220, 100))
    pyt = ImageTk.PhotoImage(image)
    return pyt


def showimageincom5(files):
    path1 = files[0]
    pyt = chuliimg(path1)
    component51.config(image=pyt)
    component51.image = pyt

    path2 = files[1]
    pyt = chuliimg(path2)
    component52.config(image=pyt)
    component52.image = pyt

    path3 = files[2]
    pyt = chuliimg(path3)
    component53.config(image=pyt)
    component53.image = pyt

    path4 = files[3]
    pyt = chuliimg(path4)
    component54.config(image=pyt)
    component54.image = pyt

    path5 = files[4]
    pyt = chuliimg(path5)
    component55.config(image=pyt)
    component55.image = pyt

    path6 = files[5]
    pyt = chuliimg(path6)
    component56.config(image=pyt)
    component56.image = pyt

    path7 = files[6]
    pyt = chuliimg(path7)
    component57.config(image=pyt)
    component57.image = pyt

    path8 = files[7]
    pyt = chuliimg(path8)
    component58.config(image=pyt)
    component58.image = pyt

    path9 = files[8]
    pyt = chuliimg(path9)
    component59.config(image=pyt)
    component59.image = pyt

def func4():
    select = choose1.get()
    qu = query.get()
    t = time.perf_counter()


    if select == "颜色直方图":
        paths = zft_result(qu)
        text = "花费时间:" + str('%.4f' % (time.perf_counter() - t)) + "s"
        showimageincom5(paths)
        component6['text'] = text

    if select == "纹理特征":
        paths = texture_result(qu)
        text = "花费时间:" + str('%.4f' % (time.perf_counter() - t)) + "s"
        showimageincom5(paths)
        component6['text'] = text

    if select == "哈希算法":
        paths = phash_result(qu)
        text = "花费时间:" + str('%.4f' %(time.perf_counter() - t))+"s"
        showimageincom5(paths)
        component6['text'] = text

    if select == "VGG模型":
        paths = vgg_model_result(qu)
        text = "花费时间:" + str('%.4f' % (time.perf_counter() - t)) + "s"
        showimageincom5(paths)
        component6['text'] = text

    if select == "形状特征":
        paths = shape_results(qu)
        text = "花费时间:" + str('%.4f' % (time.perf_counter() - t)) + "s"
        showimageincom5(paths)
        component6['text'] = text


component4 = Button(root,text='   开始检测   ',command=func4)
component4.grid(row = 3, column = 0,padx=20, pady=10)


background2 = Image.open('background2.png')
background2 = background2.resize((220, 100))
pyt2 = ImageTk.PhotoImage(background2)


component51 = Label(root,text='')
component51.config(image=pyt2)
component51.grid(row = 0, column = 1)

component52 = Label(root,text='')
component52.config(image=pyt2)
component52.grid(row = 0, column = 2)

component53 = Label(root,text='')
component53.config(image=pyt2)
component53.grid(row = 0, column = 3)

component54 = Label(root,text='')
component54.config(image=pyt2)
component54.grid(row = 1, column = 1)

component55 = Label(root,text='')
component55.config(image=pyt2)
component55.grid(row = 1, column = 2)

component56 = Label(root,text='')
component56.config(image=pyt2)
component56.grid(row = 1, column = 3)


component57 = Label(root,text='')
component57.config(image=pyt2)
component57.grid(row = 2, column = 1)

component58 = Label(root,text='')
component58.config(image=pyt2)
component58.grid(row = 2, column = 2)

component59 = Label(root,text='')
component59.config(image=pyt2)
component59.grid(row = 2, column = 3)

component6 = Label(root, text='花费时间', bg="white", height=3, width=80,
                    anchor="nw")
component6.grid(row = 3, column = 1,columnspan  = 3)

root.mainloop()