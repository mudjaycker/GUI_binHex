##########################################################################
############################# Convert to #################################
############################## Binary ###################################
##########################################################################
def varToBin(variable):
    
    tabBin = [int(ord(i)) for i in variable]
    binaire = [bin(i)[2:] for i in tabBin]
    binary = ' '.join(str(i) for i in binaire)
    
    return binary

def VarToHex(variable):
    tabHex = [int(ord(i)) for i in variable]
    hexadecimal = [format(i,'X') for i in tabHex]
    hexa = ' '.join(str(i) for i in hexadecimal)
    return hexa
    
    

##########################################################################
############################# Graphique #################################
############################## Binary ###################################
############################### HEXA ####################################

from tkinter import *
############################## Fonctions de conversion ###################################
def hexBinUpdate(*args):
        toConvert = valueInput.get()
        
        binOutput.set(varToBin(toConvert))
        hexOutput.set(VarToHex(toConvert))
        if toConvert == "":
            binOutput.set("")
            hexOutput.set("")

def onCenter(root:str, W:int, H:int):
    screenX = root.winfo_screenwidth()
    scrennY = root.winfo_screenheight()

    positionX = (screenX//2) - W//2
    positionY = (scrennY//2) - H//2
    geo = (f'{W}x{H}+{positionX}+{positionY}')

    return root.geometry(geo)

root = Tk()
W= 760
H = 365
onCenter(root, W, H)
root.resizable(False,False)



valueInput = StringVar()
valueInput.trace('w',hexBinUpdate)
entry = Entry(root,width=80,textvariable=valueInput).place(y=80,x=50)

labBinPos = W/3.415
binOutput = StringVar()
labelBin  = Label(root,bg="#deb887",width=80,textvariable=binOutput)
labelBin.config(font=('Andika',11))
labelBin.place(y=labBinPos,x=15)


labHexPos = W/2.732

hexOutput = StringVar()
labelHex = Label(root,bg="#a9a9a9",width=80,textvariable=hexOutput)
labelHex.config(font=('Andika',11))
labelHex.place(y=labHexPos,x=15)



################### Fonctions to copy ######################
from tkinter import messagebox

def copyBin():
    value = valueInput.get()
    root.clipboard_clear()
    root.clipboard_append(varToBin(value))
    messagebox.showinfo("Binary copied!","{} copied".format(varToBin(value)))

def copyHex():
    value = valueInput.get()
    root.clipboard_clear()
    root.clipboard_append(VarToHex(value))
    messagebox.showinfo("Hexadecimal copied!","{} copied".format(VarToHex(value)))




butY=int(H/(H/310))
but = int(W/(W/20))
butBin = Button(root,width=2,height=1,bg='#deb887',command=copyBin,
                text="copy").place(y=butY,x=but)

butX=int(W/(W/650))
butHex = Button(root,width=2,height=1,bg='#a9a9a9',command=copyHex,
                text="copy").place(y=butY, x=butX)


root.mainloop()