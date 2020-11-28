import tkinter as tk

operator=''
def btn(numbers):
    global operator
    operator=operator+str(numbers)
    txt_input.set(operator)

def clear():
    global operator
    operator=''
    txt_input.set('')
    display.insert(0,'Start Calculating..')


def equal():
    global operator
    sumup=float(eval(operator))
    txt_input.set(sumup)
    operator=''


root=tk.Tk()
root.title("Simple Calculator")

txt_input=tk.StringVar(value="Start Calculating..")

# ==================================Screen==============================================
display=tk.Entry(root,font=('arial',30,'bold'),fg='white',bg='green',justify='right',bd=30,textvariable=txt_input)
display.grid(columnspan=4)

# ====================================Row1==================================================
tk.Button(root,text='7',padx=30,pady=15,font=('arial',30,'bold'),fg='black',bd=8,command=lambda : btn(7)).grid(row=1,column=0)
tk.Button(root,text='8',padx=30,pady=15,font=('arial',30,'bold'),fg='black',bd=8,command=lambda : btn(8)).grid(row=1,column=1)
tk.Button(root,text='9',padx=30,pady=15,font=('arial',30,'bold'),fg='black',bd=8,command=lambda : btn(9)).grid(row=1,column=2)
tk.Button(root,text='C',padx=30,pady=15,font=('arial',30,'bold'),fg='black',bg='green',bd=8,command=clear).grid(row=1,column=3)

# ====================================Row2==================================================
tk.Button(root,text='4',padx=30,pady=15,font=('arial',30,'bold'),fg='black',bd=8,command=lambda : btn(4)).grid(row=2,column=0)
tk.Button(root,text='5',padx=30,pady=15,font=('arial',30,'bold'),fg='black',bd=8,command=lambda : btn(5)).grid(row=2,column=1)
tk.Button(root,text='6',padx=30,pady=15,font=('arial',30,'bold'),fg='black',bd=8,command=lambda : btn(6)).grid(row=2,column=2)
tk.Button(root,text='+',padx=33,pady=15,font=('arial',30,'bold'),fg='black',bg='orange',bd=8,command=lambda : btn('+')).grid(row=2,column=3)

# ====================================Row3==================================================
tk.Button(root,text='1',padx=30,pady=15,font=('arial',30,'bold'),fg='black',bd=8,command=lambda : btn(1)).grid(row=3,column=0)
tk.Button(root,text='2',padx=30,pady=15,font=('arial',30,'bold'),fg='black',bd=8,command=lambda : btn(2)).grid(row=3,column=1)
tk.Button(root,text='3',padx=30,pady=15,font=('arial',30,'bold'),fg='black',bd=8,command=lambda : btn(3)).grid(row=3,column=2)
tk.Button(root,text='-',padx=38,pady=15,font=('arial',30,'bold'),fg='black',bg='orange',bd=8,command=lambda : btn('-')).grid(row=3,column=3)

# ====================================Row4==================================================
tk.Button(root,text='0',padx=30,pady=15,font=('arial',30,'bold'),fg='black',bd=8,command=lambda : btn(0)).grid(row=4,column=0)
tk.Button(root,text='.',padx=35,pady=15,font=('arial',30,'bold'),fg='black',bg='orange',bd=8,command=lambda : btn('.')).grid(row=4,column=1)
tk.Button(root,text='/',padx=36,pady=15,font=('arial',30,'bold'),fg='black',bg='orange',bd=8,command=lambda : btn('/')).grid(row=4,column=2)
tk.Button(root,text='x',padx=34,pady=15,font=('arial',30,'bold'),fg='black',bg='orange',bd=8,command=lambda : btn('*')).grid(row=4,column=3)

# ====================================Row5==================================================
tk.Button(root,text='=',padx=90,pady=15,font=('arial',30,'bold'),fg='black',bg='green',bd=8,command=equal).grid(row=5,column=0,columnspan=2)
tk.Button(root,text='(',padx=35,pady=15,font=('arial',30,'bold'),fg='black',bg='orange',bd=8,command=lambda : btn('(')).grid(row=5,column=2)
tk.Button(root,text=')',padx=38,pady=15,font=('arial',30,'bold'),fg='black',bg='orange',bd=8,command=lambda : btn(')')).grid(row=5,column=3)


root.mainloop()