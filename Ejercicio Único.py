class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaCircular:
    def __init__(self):
        self.primero = None

    def esta_vacia(self):
        return self.primero is None

    def agregar_elemento(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.primero = nuevo_nodo
            nuevo_nodo.siguiente = self.primero
        else:
            actual = self.primero
            while actual.siguiente != self.primero:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = self.primero

    def mostrar_lista(self):
        if self.esta_vacia():
            print("La lista está vacia")
            return

        actual = self.primero
        while True:
            print(actual.dato, end = " -> ")
            actual = actual.siguiente
            if actual == self.primero:
                break
        print()
    def eliminar_elemento(self, dato):
        if self.esta_vacia():
            print("La lista está vacía")
            return

        actual = self.primero
        anterior = None
        while True:
            if actual.dato == dato:
                if anterior:
                    anterior.siguiente = actual.siguiente
                    if actual == self.primero:
                        self.primero = actual.siguiente
                    actual = None
                    return
                else:
                    siguiente_nodo = actual.siguiente
                    while actual.siguiente != self.primero:
                        actual = actual.siguiente
                    actual.siguiente = siguiente_nodo
                    self.primero = siguiente_nodo
                    return
            if actual.siguiente == self.primero:
                print(f"El elemento {dato} no está en la lista.")
                return
            anterior = actual
            actual = actual.siguiente

    def eliminar(self, valor):
        if self.esta_vacia():
            print("La lista está vacía.")
            return
        
        if self.primero.dato == valor:
            actual = self.primero
            while actual.siguiente !=self.primero:
                actual = actual.siguiente
            if self.primero == self.primero.siguiente:
                self.primero = None
            else:
                actual.siguiente = self.primero.siguiente
        else:
            actual = self.primero
            prev = None
            while True:
                if actual.dato == valor:
                    prev.siguiente = actual.siguiente
                    break
                prev = actual
                actual = actual.siguiente
                if actual == self.primero:
                    break

    def buscar_elemento(self, dato):
        if self.esta_vacia():
            print("Vacia")
            return False

        actual = self.primero
        while True:
            if actual.dato == dato:
                print(f"El elemento {dato} está en la lista")
                print(dato)
                return True
            actual = actual.siguiente
            if actual == self.primero:
                print(f"El elemento {dato} no está en la lista")
                return False

class Polinomio_a:
    def __init__(self, poli_a):
        self.poli_a = poli_a
   
    def imprimir(self):
        print("Primer polinomio: ",self.poli_a)

class Polinomio_b:
    def __init__(self, poli_b):
        self.poli_b = poli_b
   
    def imprimir(self):
        print("Segundo polinomio: ",self.poli_b)
        
class Menu:
    def __init__(self, lista_polinomios):
        self.lista_polinomios = lista_polinomios
        self.incognita = 0
        self.mostrar_menu()
        
    def suma_polinomios(self):
        self.grado_3T = self.grado_3b
        self.grado_2T = self.grado_2 + self.grado_2b
        self.grado_1T = self.grado_1
        self.grado_0T = self.grado_0 + self.grado_0b
        self.suma_de_polinomios = self.grado_3T, self.grado_2T, self.grado_1T, self.grado_0T
        self.lista_polinomios.agregar_elemento(self.suma_de_polinomios)
        self.lista_polinomios.buscar_elemento(self.suma_de_polinomios)
    
    def resta_polinomios(self):
        self.grado_3TR = self.grado_3b
        self.grado_2TR= self.grado_2 + self.grado_2b
        self.grado_1TR = self.grado_1
        self.grado_0TR = self.grado_0 + self.grado_0b
        self.resta_de_polinomios = self.grado_3TR, self.grado_2TR, self.grado_1TR, self.grado_0TR
        self.lista_polinomios.agregar_elemento(self.resta_de_polinomios)
        self.lista_polinomios.buscar_elemento(self.resta_de_polinomios)
    
    def mostrar_menu(self):
        while True:
            print("CALCULADORA DE POLINOMIOS")
            print("1. Ingresar componentes a un polinomio.")
            print("2. Adición y sustracción.")
            print("3. Evaluar polinomios.")
            print("0. Salir.")
            opcion = input("Ingrese su opción: ")
            
            if opcion == "1":
                polinomio = input("Ingrese a cuál polinomio desea agregar sus datos (a/b): ")
                if polinomio == "a":
                    self.grado_2 = int(input("Ingrese el coeficiente del grado 2: "))
                    self.grado_1 = int(input("Ingrese el coeficiente del grado 1: "))
                    self.grado_0 = int(input("Ingrese el coeficiente del grado 0: "))
                    self.polimio_a = self.grado_2*(self.incognita)**2, self.grado_1*(self.incognita)**1, self.grado_0
                    self.polinomio_a = Polinomio_a(self.polimio_a)
                    self.lista_polinomios.agregar_elemento(self.polinomio_a)
                elif polinomio == "b":
                    self.grado_3b = int(input("Ingrese el coeficiente del grado 3: "))
                    self.grado_2b = int(input("Ingrese el coeficiente del grado 2: "))
                    self.grado_0b = int(input("Ingrese el coeficiente del grado 0: "))
                    self.polimio_b = self.grado_3b*(self.incognita)**3, self.grado_2b*(self.incognita)**2, self.grado_0b
                    self.polinomio_b = Polinomio_b(self.polimio_b)
                    self.lista_polinomios.agregar_elemento(self.polinomio_b)
                else:
                    print("Opción no válida.")
            elif opcion == "2":
                operacion = input("Ingrese el tipo de operación que desea efectuar: (suma/resta)").lower()
                if operacion == "suma".lower():
                    self.suma_polinomios()
                elif operacion == "resta".lower():
                    self.resta_polinomios()
                else:
                    print("Opción no válida.")
            elif opcion == "3":
                x = int(input("Ingrese la incognita de los polinomios: "))
                self.incognita = x
            elif opcion == "0":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida.")

lista_polinomio = ListaCircular()
menu = Menu(lista_polinomio)