from tkinter import *
import numpy as np
import pandas as pd
import math as m
import matplotlib.pyplot as plt
from IPython.core.display import HTML
from sympy import Symbol, Derivative
from scipy.misc import derivative
%matplotlib inline
%config InlineBackend.figure_format = 'retina'
window = Tk() 
window.title("Welcome to Root Finding Methods")
window.geometry('650x650')
window.resizable(width=False, height=False)
bg_image = PhotoImage(file ="bg.png")
x = Label (image = bg_image)
x.grid(row = 0, column = 0)
selected = DoubleVar()

RF=0
NR=0
SC=0
BM=0


def func( x ): 
    return ((x**2)+(2*x)-10); 
 

def derivFunc( x ):
    h=(derivative(func,x))
    return h

def f(x): 
    f = func(x) 
    return f; 
  
  
def newtonRaphson( x ,E, n):
    print("----------Newton Rephson-------------")
    global NR
    newtonCount=0;
    mylist=[]
    h = func(x) / derivFunc(x) 
    while abs(h) >= E: 
        
        if(derivFunc(x)==0):
            print("Not Possible")
            break;
        else:
            h = func(x)/derivFunc(x) 
            mylist.append(h)
            x = x - h 
            
            newtonCount=newtonCount+1;
             
        if(newtonCount>n):
            break
        
    
    if(newtonCount>n):
        print("Could Not Found Solution even in ",n, "iterations")
        NR=0
    else:
        NR=newtonCount
        print("The value of the root By Newton rephson method is : ", "%.4f"% x) 
        print("Counts : ",newtonCount)
        
   
     
    plt.plot(mylist, color='g')
    plt.xlabel('No. of iteration')
    plt.ylabel('Tolerence')
   
    plt.title('Graph - NewtonRephson')
    plt.show()
    return
        
        

def bisection(a,b,E, n):
    print("----------Bisection-------------")
    global BM
    bisectionCount=0;
    mylist=[]
    if (func(a) * func(b) >= 0):
        print("Here f(a)>0 and f(b)>0 So, Solution is not possible. Try Again...")
        return
   
    c = a 
    while ((b-a) >= E): 
        
        mylist.append((b-a)) 
        c = (a+b)/2
   
        if (func(c) == 0.0): 
            break
   
        if (func(c)*func(a) < 0): 
            b = c 
        else: 
            a = c 
        bisectionCount=bisectionCount+1
        
        if(bisectionCount>n):
            break;
    
   
    
    if(bisectionCount>n):
        BM=0
        print("Could Not Found Solution even in ",n, "iterations")
    else:
        BM=bisectionCount
        print("The value of root is : ","%.4f"%c) 
        print("Counts : ",bisectionCount)
    
    plt.plot(mylist, color='g')
    plt.xlabel('No. of iteration')
    plt.ylabel('Tolerence')
    plt.title('Graph - Bisection')
    plt.show()
    return

def regulaFalsi(a,b,TOL,N):
    print("----------Regula Falsi-------------")
    global RF
    mylist=[]
    i = 1
    FA = f(a)
     
    if(f(a)*f(b)<0):

        while True:
            p = (a*f(b)-b*f(a))/(f(b) - f(a))
            FP = f(p)

            if(FP == 0 or np.abs(f(p)) < TOL):
                break
            mylist.append(np.abs(f(p)))


            i = i + 1

            if(FA*FP > 0):
                a = p
            else:
                b = p
            
            if(i>N):
                break
        
        if(i>N):
            print("Could Not Found Solution even in ",nn, "iterations")
            RF=0
        else:
            print("The value of root is : " , '%.4f'%a)
            print("Count : ",i)
            RF=i;
        
       
        
    else:
        print("Here f(a)>0 and f(b)>0 So, Solution is not possible. Try Again...")
    
    plt.plot(mylist, color='g')
    plt.xlabel('No. of iteration')
    plt.ylabel('Tolerence')
    plt.title('Graph - Regula Falsi')
    plt.show()
    return

def secant(x1, x2, E, nn): 
    print("----------Secant-------------")
    global SC
    n = 0; xm = 0; x0 = 0; c = 0;  
    mylist=[]
    if(f(x1)*f(x2)<0):
        while True:  

            x0 = ((x1 * f(x2) - x2 * f(x1)) / 
                            (f(x2) - f(x1)));  

            c = f(x1) * f(x0);  

            x1 = x2;  
            x2 = x0;  

            n += 1; 
            
            if(n>nn):
                break;

            if (c == 0):  
                break;  
            xm = ((x1 * f(x2) - x2 * f(x1)) / 
                            (f(x2) - f(x1))); 

            if(abs(xm - x0) < E): 
                break; 
            mylist.append(abs(xm - x0))

        SC=n
        
        if(n>nn):
            print("Could Not Found Solution even in ",nn, "iterations")
            SC=0
        else:
            print("Root of the given equation =",  
                                   round(x0, 4));  
            print("No. of iterations = ", n);  
    
    else:
        print("Here f(a)>0 and f(b)>0 So, Solution is not possible. Try Again...")
  
    plt.plot(mylist, color='g')
    plt.xlabel('No. of iteration')
    plt.ylabel('Tolerence')
    plt.title('Graph - Secant')
    plt.show()
    return


def draw_Graph():
    
    MethodName = ['Bisection Method','Regula Falsi','Newton Rephson','Secant Method']
   
    Count = [BM,RF,NR, SC]
     
    plt.plot(MethodName, Count, color='g')
    plt.xlabel('Method Name')
    plt.ylabel('No. of iteration')
    plt.title('Comparision of root finding Methods')
    plt.show()
    return


def draw_Bar_Graph():
    
    s = pd.Series(
        [BM,RF,NR, SC],
        index = ['Bisection Method','Regula Falsi','Newton Rephson','Secant Method']
        )


    plt.title("Comparision of Root Finding Methods")
    plt.ylabel('No of Iteration')
    plt.xlabel('Mathod Name')


    ax = plt.gca()
    ax.tick_params(axis='x', colors='blue')
    ax.tick_params(axis='y', colors='red')
   
    my_colors = 'Black'  

    s.plot( 
        kind='bar',
        color=my_colors,

    )

    plt.show()
    return

def a():
    
   
    
    a=txt2.get()
    b=txt3.get()
    E=selected.get()
    N=txt1.get()
    bisection(float(a),float(b),E,int(N))
   
    
def b():
    
   
    
    a=txt2.get()
    b=txt3.get()
    E=selected.get()
    N=txt1.get()
    newtonRaphson(float(a),E,int(N))
  

def c():
    
   
    
    a=txt2.get()
    b=txt3.get()
    E=selected.get()
    N=txt1.get()
   
    regulaFalsi(float(a),float(b),E,int(N))

def d():
    
   
    
    a=txt2.get()
    b=txt3.get()
    E=selected.get()
    N=txt1.get()
   
    secant(float(a),float(b),E,int(N))

def allF():
    
   
    
    a=txt2.get()
    b=txt3.get()
    E=selected.get()
    N=txt1.get()
    print("    ")
    print("  ---  ")
    print("    ")
    bisection(float(a),float(b),E,int(N))
    newtonRaphson(float(a),E,int(N))
    regulaFalsi(float(a),float(b),E,int(N))
    secant(float(a),float(b),E,int(N))
    
    draw_Bar_Graph()
    draw_Graph()


    
    
    
lbl = Label(window, text="Max Iterations")

lbl.place(x=15,y=70)

lbl.config(bg="white")

txt1 =Entry(window,bd=5,width="30")

txt1.place(x=115,y=70)

lbl = Label(window, text="Enter a")

lbl.place(x=15,y=115)

lbl.config(bg="white")

txt2 =Entry(window,bd=5,width="30")

txt2.place(x=115,y=115)

lbl = Label(window, text="Enter b")

lbl.place(x=15,y=160)

lbl.config(bg="white")

txt3 =Entry(window,bd=5,width="30")

txt3.place(x=115,y=160)

lbl = Label(window, text="Select Tolerance")

lbl.place(x=15,y=250)

lbl.config(bg="white")

rad1 = Radiobutton(window,text='0.1', value=0.1, variable=selected)

rad2 = Radiobutton(window,text='0.01', value=0.01, variable=selected)

rad3 = Radiobutton(window,text='0.001', value=0.001, variable=selected)

rad4 = Radiobutton(window,text='0.0001', value=0.0001, variable=selected)

rad5 = Radiobutton(window,text='0.00001', value=0.00001, variable=selected)

rad6 = Radiobutton(window,text='0.000001', value=0.000001, variable=selected)

rad1.place(x=115, y=250)

rad1.config(bg="white")
 
rad2.place(x=185, y=250)

rad2.config(bg="white")
 
rad3.place(x=255, y=250)

rad3.config(bg="white")

rad4.place(x=325, y=250)

rad4.config(bg="white")

rad5.place(x=395, y=250)

rad5.config(bg="white")

rad6.place(x=465, y=250)

rad6.config(bg="white")
btn = Button(window, text="Bisection", height="2", width="20", command=a)
 
btn.place(x=100,y=300)

btn = Button(window, text="Newton Rephson", height="2", width="20", command=b)
 
btn.place(x=100,y=350)

btn = Button(window, text="Regula", height="2", width="20", command=c)
 
btn.place(x=100,y=400)

btn = Button(window, text="Secant", height="2", width="20", command=d)
 
btn.place(x=100,y=450)

btn = Button(window, text="Compare All", height="2", width="20", command=allF)
 
btn.place(x=100,y=500)






window.mainloop()