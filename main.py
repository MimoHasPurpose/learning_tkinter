




from tkinter import *
def study():
    label=Label(root,text="Study for an hour!")
    label.grid(row=2,column=3)
root=Tk()
root.title('to-do app')
root.iconbitmap('data/billu.ico')
root.configure(bg='pink')
bg=PhotoImage(file='data/kanyewest.png')

label1=Label(root,image=bg)
label1.grid(row=1,column=3)

label2=Label(root,text="Enter your Task!!")
label2.grid(row=3,column=3)


#introducing buttons for input text
studyButton=Button(root,text="blue is for study!",command=study)
studyButton.grid(row=4,column=3)

#=Entry for user name
e=Entry(root,width=50)
e.grid(row=5,column=3)
#function to get username
def userName():
    name=Label(root,text="Hello "+e.get())
    name.grid(row=5,column=3)
    e.delete(0,END)


userName=Button(root,text="Enter user name: ",width=50,command=userName)
userName.grid(row=6,column=3)
print(userName)
root.geometry("400x500")

root.mainloop()