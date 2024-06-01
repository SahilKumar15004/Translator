from tkinter import ttk
from tkinter import*
from googletrans import Translator,LANGUAGES

root=Tk()
root.attributes('-fullscreen',"true")

#ADDING IMAGE
bg=PhotoImage(file="cy.png")
lbl=Label(root,image=bg,bg="cyan")
lbl.place(x=575,y=220)

#TRANSLATION BUTTON FUNCTION
def Translated():
 translate=Translator()
 translation=translate.translate(text=input.get(1.0,END),src=src_lang.get(),dest=dest_lang.get())
 output.delete(1.0,END)
 output.insert(END,translation.text)

#CLEAR BUTTON FUNCTION 
def delete():
 input.delete(1.0,'end')
 output.delete(1.0,'end')

#SCREEN ADJUSTING OR EDITING
root.geometry("1400x900")
root.resizable(0,0)

#CREATING A SCREEN TITLE
root.title("language translator")

#ADDING BG COLOR TO THE SCREEN
root["bg"]="cyan"

#CREATING A HEADING
Label(root,text="            L    A    N    G    U    A    G    E           T    R    A    N    S    L    A    T    O    R          ",font=("Garamond 30 bold"),bd="7",bg="#8576FF",border="10",width="61",activeforeground="black",fg="white").place(x=30,y=17)

#CREATING AN INPUT LABEL
Label(root,text="I N P U T",font="times 30 bold",fg="black",bg="cyan").place(x=30,y=99)

#CREATING AN INPUT BOX
input=Text(root,font="garamond 23 bold",bg="grey",fg="white",height="13.520",wrap=WORD,padx=5,pady=10,bd=1,width=35)
input.place(x=30,y=158)


#CREATING AN OUTPUT LABEL
Label(root,text="O U T P U T",font="times 30 bold ",fg="black",bg="cyan").place(x=947,y=99)

#CREATING AN OUTPUT BOX
output=Text(root,font="roman 19 bold ",bg="grey",height="16.55",fg="white",wrap=WORD,padx=6,pady=10,width=46)
output.place(x=950,y=158)

#INPUT LANGUAGE SELECTOR
language=list(LANGUAGES.values())
src_lang=ttk.Combobox(root,values=language,height=20,width=55)
src_lang.place(x=215,y=115)
src_lang.set('Choose Input Language')

#OUTPUT LANGUAGE SELECTOR
language=list(LANGUAGES.values())
dest_lang=ttk.Combobox(root,values=language,height=20,width=50)
dest_lang.place(x=1190,y=115)
dest_lang.set('Choose Output Language')

#CREATION OF TRANSLATE BUTTON
translate_btn=Button(root,text="TRANSLATE",font="georgia 30 bold",bd="5",command=Translated,bg="navy blue",activebackground="sky blue",fg="white")
translate_btn.place(x=600,y=586)

#CREATION OF CLEAR BUTTON
btn=Button(root,text="DELETE",font="georgia 30 bold",bd="5",command=delete,bg="#D862BC",activebackground="light blue",fg="white")
btn.place(x=639,y=700)

#HOLD THE SCREEN
mainloop()