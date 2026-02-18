def askStr(msj):
    m=str(input(msj))
    return(m)

def askNumber(msj):
    n=float(input(msj))
    return (n)

def finalMsg():
    print("\nTAREA FINALIZADA")

def suma (a,b):
    return(a+b)

def difference (a,b):
    return (a-b)

def division (a,b):
    if (b!=0):
        return (a/b)
    else:
        return ("No es válida la división por 0.")

def multip (a,b):
    return(a*b)

def menu ():
    print("***********************")
    print("CALCULADORA")
    print("***********************")
    print("Según la operacion a realizar, ingrese el signo que se encuentra al inicio:")
    print ("+. Sumar")
    print ("-. Restar")
    print ("*. Multiplicar")
    print ("/. Dividir")
    print ("5. Salir")
    opc=7
    while (opc!= "+" and opc!="-" and opc!="/" and opc!="*"):
        opc= askStr("\n Ingrese una opción del menú: ")
        if (opc== "+" or opc=="-" or opc=="/" or opc=="*"):
            return(opc)
        else:
            return(5)
        
def operaciones(n, a, b):
    if (n=="+"):
        s=suma(a,b)
        print("\n El resultado es:", s)
    if (n=="-"):
        d=difference(a,b)
        print("\n El resultado es:", d)
    if (n=="*"):
        m=multip(a,b)
        print("\n El resultado es:", m)
    if (n=="/"):
        d=division(a,b)
        print("\n El resultado es:", d)
    if (n=="5"):
        print("\n Ok, tenga buen día.")

def main():
    while 1:
        opc= menu()
        if opc=="5":
            print("\n Ok, tenga buen día.")
            break
        if opc in ["+", "-", "*", "/"]:
            a= askNumber("\n Ingrese a:")
            b= askNumber("\n Ingrese b:")
            operaciones(opc, a, b)
    finalMsg()
main()