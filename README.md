# Reto 1
<p>
1. Crear una función que realice operaciones básicas (suma, resta, multiplicación, división) entre dos números, según la elección del usuario, la forma de entrada de la función será los dos operandos y el caracter usado para la operación. entrada: (1,2,"+"), salida (3).
</p>

- **Solución**:
```python
		#Los comentarios indicarán cómo se llegó a la solución

		#Modularmente, se definen funciones para tareas como pedir número, mensajes de bienvenida/despedida
		def askStr(msj):
			m=str(input(msj))
			return(m)

		def askNumber(msj):
			n=float(input(msj))
			return (n)

		def finalMsg():
			print("\nTAREA FINALIZADA")

		#Se definen modularmente las operaciones
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

		#Se crea un menú donde el usuario podrá escoger la operación a realizar, se tiene en cuenta el caso donde la opción sea equivocada-
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

		#Operaciones básicas        
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

		#Se agrupa todo en el main
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
```
<p>
2. Realice una función que permita validar si una palabra es un palíndromo. Condición: No se vale hacer slicing para invertir la palabra y verificar que sea igual a la original.
</p>

- **Solución**:
```python
		def ask_str(msj):
			m=str(input(msj))
			return m
		#Se recorre la palabra y se verifica de atrás hacia adelante si coincide con la debida letra, algo así como un proceso espejo.
		def check_word(w):
			l=len(w)  
			for x in range(l):
				if w[x]!=w[l-x-1]:
					return False
			return True

		def msg(a,w):
			if a:
				print("La palabra",w, "es palíndroma.")
			else:
				print("La palabra",w, "no es palíndroma.")

		def initial_msg():
			print("Buen día, ingrese una palabra y le diré si es palíndroma o no.")

		def final_msg():
			print("Programa finalizado, hasta pronto.")

		#Se une todo en el main
		def main():
			initial_msg()
			w=ask_str("Ingrese la palabra a continuación: ")
			cond=check_word(w)
			msg(cond, w)
			final_msg()
		main()
```
<p>
3.  Escribir una función que reciba una lista de números y devuelva solo aquellos que son primos. La función debe recibir una lista de enteros y retornar solo aquellos que sean primos.
</p>
- **Solución:**

```python
#Se define modularmente los mensajes y solicitud de número
def initial_msg():
    print("Buen día, recibo una lista de números enteros y le indico cuáles de ellos son primos")

def final_msg():
    print("Programa finalizado, hasta pronto.")

def ask_num(msg):
    n = int(input(msg))
    while n < 0:
        print("Recuerde, debe ser un número positivo válido.")
        n = int(input(msg))
    return n
#Se crea una lista según la cantidad de números que el usuario afirma querer ingresar
def create_list():
    lista = ask_num("¿Cuántos números va a ingresar? ")  
    li = []
    for x in range(lista):
        num = ask_num(f"Número # {x+1}: ")
        li.append(num)
    return li

#Para ver si el número es o no primo, se evalúa en el for si tiene algún divisor distinto de sí mismo y 1, rompiendo en caso de que ocurra. De lo contrario, se inserta en la lista previamente creada y se retorna.
def check_prime(li):
    final=[]
    for x in range(len(li)):
        if li[x]>1:
            for i in range (2,li[x]):
                if li[x]%i==0:
                    break
            else:
                final.append(li[x])
    return (final)

def give_info(info):
    print("Los números primos encontrados son: ", info)

#Se agrupa todo en el main
def main():
    initial_msg()
    li = create_list()
    info = check_prime(li)
    give_info(info)
    final_msg()
main()
```
<p>
4. Escribir una función que reciba una lista de números enteros y retorne la mayor suma entre dos elementos consecutivos.
</p>

```python
#Se define modularmente los mensajes de bienvenida y solicitud de número
def initial_msg():
    print("Buen día, recibo una lista de números enteros y le indico cuál es la mayor suma entre dos elementos consecutivos.")

def final_msg():
    print("Programa finalizado, hasta pronto.")

def ask_num(msg):
    n=int(input(msg))
    while n<0:
        print("Recuerde, debe ser un número positivo válido.")
        n=int(input(msg))
    return n

#Dado que el ejercicio retorna la mayor suma entre dos elementos consecutivos, es necesario verificar que al menos se ingresen 2 números
def create_list():
    lista=ask_num("¿Cuántos números va a ingresar? ")  
    while lista<2:
        print("Debe ingresar al menos 2 números.")
        lista=ask_num("¿Cuántos números va a ingresar?: ")
    li = []
    for x in range(lista):
        num=ask_num(f"Número # {x+1}: ")
        li.append(num)
    return li

#Se recorre la lista tomando los primeros dos elementos. Si existen una suma de otros dos números mayor que la anterior, se reeemplaza.
#La función devuelve los dos números y su respectiva suma
def check_sum(li):
    i=li[0]+li[1]
    num1=li[0]
    num2=li[1]
    for x in range(len(li)-1):
        suma=li[x]+li[x+1]
        if suma>i:
            i=suma
            num1=li[x]
            num2=li[x+1]
    return (i, num1, num2)

def give_info(info):
    print("La mayor suma encontrada corresponde a ", info[0],", la cual resulta de los números", info[1], "y", info[2], ".")
#Se agrupa todo en un main
def main():
    initial_msg()
    li = create_list()
    info = check_sum(li)
    give_info(info)
    final_msg()
main()
```

<p>
5. Escribir una función que reciba una lista de string y retorne unicamente aquellos elementos que tengan los mismos caracteres. e.g. entrada: ["amor", "roma", "perro"], salida ["amor", "roma"]
</p>

```pyhton
	#Se define modularmente los mensajes de bienvenida, solicitud de número y string.
	def initial_msg():
	    print("Buen día. De una lista de palabras que ingrese, le indico cuáles de ellas contienen las mismas letras.")
	
	def final_msg():
	    print("Programa finalizado, hasta pronto.")
	
	def ask_str(msg):
	    m=str(input(msg))
	    return m
	
	def ask_num(msg):
	    n=int(input(msg))
	    while n<0:
	        print("Recuerde, debe ser un número positivo válido.")
	        n=int(input(msg))
	    return n
	
	#Se insertan las palabras en una lista
	def create_list():
	    lista=ask_num("¿Cuántas palabras va a ingresar? ")
	    li=[]
	    for x in range(lista):
	        w=ask_str(f"Palabra # {x+1}: ")
	        li.append(w)
	    return li
	
	#Se recorre la lista y palabra. Sorted es la clave, pues ordena los caracteres alfabéticamente y se permite su comparación
	#Hay doble for, pues recorre todas las posibles combinaciones que existan dentro de la lista
	#Devuelve la lista de palabras que contienen las mismas letras
	def check_word(li):
	    final=[]
	    l=len(li)
	    for x in range(l):
	        for y in range(x+1, len(li)):
	                if sorted(li[x])==sorted(li[y]):
	                    final.append((li[x], li[y]))
	    return final
	
	#Se agrupa todo en el main
	def main():
	    initial_msg()
	    lista = create_list()
	    resultado = check_word(lista)
	    if len(resultado) == 0:
	        print("No hay palabras que contengan las mismas letras.")
	    else:
	        print("Las palabras que contienen las mismas letras son:")
	        for par in resultado:
	            print(par[0], "y", par[1])
	    final_msg()
	main()
```
