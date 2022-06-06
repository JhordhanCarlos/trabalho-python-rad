from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import *

##----------CORES----------

co0 = "#000000"
co1 = "#FEFFFF"
co2 = "#4FA882"
co3 = "#38576B"
co4 = "#403D3D"
co5 = "#E06636"
co6 = "#038CFC"
co7 = "#EF5350"
co8 = "#4FA889"
co9 = "#CCCCCC"

##---------- Janela ----------

janela = Tk()
janela.title("Controle de Histórias em Quadrinhos")
janela.geometry('1043x453')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

##  Frames da esquerda 

##---------- Header ----------

headerLeft = Frame(janela, width=310, height=50, bg=co2, relief='flat')
headerLeft.grid(row=0, column=0)

titleForm = Label(headerLeft, text="Cadastre uma História em Quadrinhos", anchor=NW, font="Ivy 12 bold", bg=co2, fg=co1, relief='flat')
titleForm.place(x=10, y=15)

choice = int 

def inserirUm():
    titulo =    tituloInput.get()
    publisher = publisherInput.get()
    editor =    editorInput.get()

    status = bool
    if(choice == 0):
        status = False
    else:
        status = True

    comment = commentInput.get()

    if(titulo == ''):
        messagebox.showerror("Preencha o campo", "O campo 'Título' é obrigatório!")

    if(publisher == ''):
        messagebox.showerror("Preencha o campo", "O campo 'Publicadora' é obrigatório!")
    
    if(editor == ''):
        messagebox.showerror("Preencha o campo", "O campo 'Editora' é obrigatório!")

    else:
        novaHq =[titulo ,publisher ,editor ,status , comment]
        inserir(novaHq)
        messagebox.showinfo("HQ adicionada com sucesso", "Uma nova História Em Quarinhos foi adicionada!")

        tituloInput.delete(0, 'end')
        publisherInput.delete(0, 'end')
        editorInput.delete(0, 'end')
        commentInput.delete(0, 'end')

    for i in bodyRight.winfo_children():
        i.destroy()

    show()
##---------- Body ----------

bodyLeft = Frame(janela, width=310, height=403, bg=co1, relief='flat')
bodyLeft.grid(row=1, column=0, padx=0, pady=1, sticky=NSEW)


tituloLabel = Label(bodyLeft, text="Título", anchor=NW, font="Ivy 10 bold", bg=co1, fg=co4, relief='flat')
tituloLabel.place(x=10, y=10)

tituloInput = Entry(bodyLeft, width=45, justify='left', relief='solid')
tituloInput.place(x=15, y=40)


publisherLabel = Label(bodyLeft, text="Publicadora", anchor=NW, font="Ivy 10 bold", bg=co1, fg=co4, relief='flat')
publisherLabel.place(x=10, y=70)

publisherInput = Entry(bodyLeft, width=45, justify='left', relief='solid')
publisherInput.place(x=15, y=100)


editorLabel = Label(bodyLeft, text="Editora", anchor=NW, font="Ivy 10 bold", bg=co1, fg=co4, relief='flat')
editorLabel.place(x=10, y=130)

editorInput = Entry(bodyLeft, width=45, justify='left', relief='solid')
editorInput.place(x=15, y=160)


statusLabel = Label(bodyLeft, text="Já leu esta HQ?", anchor=NW, font="Ivy 10 bold", bg=co1, fg=co4, relief='flat')
statusLabel.place(x=10, y=190)


statusTrueRadio = Radiobutton(bodyLeft, text="Sim", variable=choice, value=1)
statusTrueRadio.place(x=15, y=220)
choice = 1

statusFalseRadio = Radiobutton(bodyLeft, text="Não", variable=choice, value=0)
statusFalseRadio.place(x=70, y=220)
choice = 0

commentLabel = Label(bodyLeft, text="Comentário", anchor=NW, font="Ivy 10 bold", bg=co1, fg=co4, relief='flat')
commentLabel.place(x=10, y=250)

commentInput = Entry(bodyLeft, width=45, justify='left', relief='solid')
commentInput.place(x=15, y=280)


saveButton = Button(bodyLeft, command= inserirUm, width=38, text ="Salvar", justify='left', bg=co8, fg=co1, relief='flat')
saveButton.place(x=15, y=310)

updateButton = Button(bodyLeft, width=38, text ="Atualizar", justify='left', bg=co6, fg=co1, relief='flat')
updateButton.place(x=15, y=340)

deleteButton = Button(bodyLeft, width=38, text ="Excluir", justify='left', bg=co7, fg=co1, relief='flat')
deleteButton.place(x=15, y=370)

##  Frame da Direita
bodyRight = Frame(janela, width=588, height=403, bg=co1, relief='solid')
bodyRight.grid(row=0, column=1, rowspan=2, padx=1, pady=0 ,sticky=NSEW)

gridHeader = ['ID', 'Título', 'Publicadora', 'editora', 'Status', 'Comentário']
def show():
    gridContent = listar()

    tree = ttk.Treeview(bodyRight, selectmode='extended', columns=gridHeader, show="headings")
    verticalScroll = ttk.Scrollbar(bodyRight, orient="vertical", command=tree.yview)
    horizontalScroll = ttk.Scrollbar(bodyRight, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=verticalScroll.set, xscrollcommand=horizontalScroll.set)

    tree.grid(row=0, column=0,sticky='nsew')
    verticalScroll.grid(row=1, column=0,sticky='ns')
    horizontalScroll.grid(row=0, column=1,sticky='ew')

    bodyRight.grid_rowconfigure(0, weight=12)

    h=[30,120,100,100,70,300]
    n=0

    for col in gridHeader:
        tree.heading(col, text=col.title(), anchor=CENTER)
        tree.column(col, width=h[n], anchor="nw")
        n+=1

    for item in gridContent:
        print(item)
        if item == 0:
            tree.insert('', 'end', values="NÃO LIDO")
        elif item == 1:
            tree.insert('', 'end', values="LIDO")
        else: 
            tree.insert('', 'end', values=item)

show()
janela.mainloop()