#!/usr/bin/env python
# coding: utf-8

EJERCICIO 1
# In[40]:


x="Mirthala Nallely"
matricula= 1614768

print(x+str(matricula))


EJERCICIO 2:
# In[3]:


x = int(input("Ingrese un numero:"))
y = int(input("Ingrese un segundo numero:"))

z=x+y
r=x-y
s=x*y
t=x/y
u=x**y

print()
print ("La suma de los dos numeros ingresados es:", z)
print ("La resta de los dos numeros ingresados es: ", r)
print ("La multiplicacion de los dos numeros ingresados es: ", s)
print ("La division de los dos numeros ingresados es: ", t)
print ("El resultado del primer numero elevado al segundo como potencia es: ", u)


EJERCICIO 3:

# In[5]:


cont=0
lista=[i*3 for i in range(1,11)]
print (lista)

for i in range(len(lista)):
    cont=cont+lista[i]
    
    print()
    print("La suma de los numeros es:", cont)
    

    EJERCICIO 4:

# In[11]:


x = int(input ("Ingrese un numero: "))

if x%2==0:
    print()
    print ("El numero ingresado es par")
    
else:
    print()
    print ("El numero ingresado es impar")
        

        EJERCICIO 5:

# In[39]:


num = int(input("Ingrese un numero: "))
cont = 0

for n in range(1, num + 1):
    if num%n == 0:
    cont=cont+1
    
if cont == 2:
    print()
    print ("El numero ingresado es primo")
else:
    print()
    print ("El numero ingresado no es primo")
        
EJERCICIO 6:

# In[25]:


def Suma(x,y):
    z=x+y
    return z
def Resta(x,y):
    z=x-y
    return z
def Multiplicacion(x,y):
    z=x*y
    return z
def Division(x,y):
    z=x/y
    return z
def Exponente(x,y):
    z=x**y
    return z

def Opciones():
    print ("Opciones\n\n1.Suma\n2.Resta\n3.Multiplicacion\n4.Division\n5.Exponente\n6.Salir")
def Calculadora():
    Opciones()
    print()
    opc = int(input("Ingrese la opcion a realizar: " ))
    print()
    x = int(input("Ingrese un numero: "))
    y = int(input("Ingrese otro numero: "))
    while (opc >0 and opc <6):
        if (opc==1):
            print()
            print ("Suma = ",Suma(x,y))
            break
        elif(opc==2):
            print()
            print ("Resta =",Resta(x,y))
            break
        elif(opc==3):
            print()
            print ("Multiplicacion =",Multiplicacion(x,y))
            break
        elif(opc==4):
            print()
            print("Division =",Division(x,y))
            break
        elif(opc==5):
            print()
            print("Exponente =",Exponente(x,y))
            break
        
    Calculadora()
    
    
            
                
                
EJERCICIO 7:

# In[28]:


flotante = 0.5
integer = 10
booleana = False
compleja = 2+2j

print()
print(type(flotante))
print(type(integer))
print(type(booleana))
print(type(compleja))


EJERCICIO 8:
# In[29]:


x=[2,4,5,8,9,2,2,4,3,8]

x=tuple(x)
pnum = x[0]
unum = x[-1]

print("Primer numero: ",pnum)
print("Ultimo numero: ",unum)

print()
print(x+('hey', 'Tarea', 'Nalle'))

6 in x


EJERCICIO 9:
# In[34]:


import random as x

lista=[x.randint(1,20) for i in range(40)]
print (lista)

def numPI(lista):
    imp=[]
    par=[]
    for i in range(len(lista)):
        if lista[i]%2==0:
            par.append(lista[i])
        else:
                imp.append(lista[i])
    return par,imp

par,imp=numPI(lista)
print()
print("Lista de pares: ", par)
print()
print("Lista de impares: ", imp)
            
lp=len(par)
print()
print("Numero de pares: ", lp)
            
li=len(imp)
print()
print("Numero de impares: ", li)
            
lista[0]=2
print()
print(lista)
            
print()
print(lista[4:8])
            
print()
lista.insert(1,6)
print(list)
            
print()
lista.append(11)
print(lista)
            
            
            
EJERCICIO 10:

# In[37]:


diccionario ={"Ernesto":28,"Patricio":3,"Mirthala":47,"Mauricio":1,"Eliza":25,"Sergio":48}

Edad = [i for i in diccionario.values()]
print(Edad)

print()
Edad.sort()
print(Edad)

print()
for i in diccionario:
    print (i)
    
print()
diccionario["Danna"]=10
diccionario["Alexa"]=6
    
print(diccionario)


EJERCICIO 11:
# In[38]:


import random as r

x={r.randint(1,25) for i in range(100)}
print(x)

print()
print(len (x))

print()
y=[r.randint(1,10) for i in range(5)]
print(y)

print()
for i in range(len(y)):
    print("Existe: ", y[i], y[i] in x)


# In[ ]:




