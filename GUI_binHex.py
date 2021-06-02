##########################################################################
############################# Convert to #################################
############################## Binary ###################################
##########################################################################
def intToBin(variable):
    
    tabBin = [int(ord(i)) for i in variable]
    binaire = [bin(i)[2:] for i in tabBin]
    binary = ' '.join(str(i) for i in binaire)
    
    return binary

def intTohex(variable):
    tabHex = [int(ord(i)) for i in variable]
    hexadecimal = [format(i,'X') for i in tabHex]
    hexa = ' '.join(str(i) for i in hexadecimal)
    return hexa
    
    

##########################################################################
############################# Graphique #################################
############################## Binary ###################################
############################### HEXA ####################################

from tkinter import *
############################## Fonctions d'ecriture ###################################
def hexBinUpdate(*args):
        toConvert = valueInput.get()
        
        binOutput.set(intToBin(toConvert))
        hexOutput.set(intTohex(toConvert))
        if toConvert == "":
            binOutput.set("")
            hexOutput.set("")


root = Tk()
W = root.winfo_screenwidth()//2
H = root.winfo_screenheight()//2


screenX = root.winfo_screenwidth()
windowX = W
scrennY = root.winfo_screenheight()
windowY = H


positionX = (screenX//2) - (windowX//2)
positionY = (scrennY//2) - (windowY//2)


geo = (f'{windowX}x{windowY}+{positionX}+{positionY}')
root.geometry(geo)
root.title("Convertisseur Binaire et Hexadecimale")
root.resizable(False,False)

valueInput = StringVar()
valueInput.trace('w',hexBinUpdate)
entryBin = Entry(root,width=80,textvariable=valueInput).place(y=80,x=15)
#okButt = Button(root,width=5,height=5,bg='red',command=hexBinUpdate).pack()

labBinPos = W/3.415
binOutput = StringVar()
labelBin  = Label(root,bg="#deb887",width=80,textvariable=binOutput)
labelBin.config(font=('Andika',11))
labelBin.place(y=labBinPos,x=1)


labHexPos = W/2.732

hexOutput = StringVar()
labelHex = Label(root,bg="#a9a9a9",width=80,textvariable=hexOutput)
labelHex.config(font=('Andika',11))
labelHex.place(y=labHexPos,x=1)



################### Fonctions to copy ######################
from tkinter import messagebox

def copyBin():
    value = valueInput.get()
    root.clipboard_clear()
    root.clipboard_append(intToBin(value))
    messagebox.showinfo("Binary copied!","{} copied".format(intToBin(value)))

def copyHex():
    value = valueInput.get()
    root.clipboard_clear()
    root.clipboard_append(intTohex(value))
    messagebox.showinfo("Hexadecimal copied!","{} copied".format(intTohex(value)))




butY=int(H/(H/300))
but = int(W/(W/20))
butBin = Button(root,width=2,height=1,bg='#deb887',command=copyBin,
                text="copy").place(y=butY,x=but)

butX=int(W/(W/600))
butHex = Button(root,width=2,height=1,bg='#a9a9a9',command=copyHex,
                text="copy").place(y=butY, x=butX)


root.mainloop()