import os

class Sustancia:
    def __init__(self, serial, ubicacion, acess_student, danger):
        self.__serial = serial
        self.__ubicacion = ubicacion
        self.__acess_student = acess_student
        self.__danger_human = danger

    def verSerial(self):
        return self.__serial
    def verUbicacion(self): 
        return self.__ubicacion
    def verAcessStudent(self):
        return self.__acess_student
    def verDanger(Self):
        return Self.__danger_human
    
    def asignarSerial(self,serial):
        self.__serial = serial
    def asignarUbicacion(self,ubicacion):
        self.__ubicacion = ubicacion
    def asignarAcess_student(self,acess_student):
        self.__acess_student = acess_student
    def asignarDanger_human(self,danger):
        self.__danger_human = danger

class Acidos_Bases(Sustancia):
    def __init__(self, concentracion, descripcion, etiqueta):
        self.__concentracion = concentracion
        self.__descripcion = descripcion
        self.__etiqueta = etiqueta

    def __str__(self):
        return f"""/ Informacion sobre la sustancia {self.verEtiqueta()}.
\n| - ID: {self.verSerial()} - Ubicacion: {self.verUbicacion()}         
| - {self.verAcessStudent()} 
| - {self.verDanger()}
| - Concentracion: {self.verConcentracion()}
| - Descripcion de la sustancia:
| {self.verDescripcion()}       
        """

    def verConcentracion(self):
        return self.__concentracion
    def verDescripcion(self):
        return self.__descripcion
    def verEtiqueta(self):
        return self.__etiqueta

    def asignarConcentracion(self, concentracion):
        self.__concentracion = concentracion
    def asignarDescripcion(self, descripcion):
        self.__descripcion = descripcion
    def asignarEtiqueta(self, etiqueta):
        self.__etiqueta = etiqueta

class Alcoholes(Sustancia):
    def __init__(self, ebullicion, arder, etiqueta):
        self.__ebullicion = ebullicion
        self.__arder = arder
        self.__etiqueta = etiqueta

    def __str__(self):
        return f"""/ Informacion sobre la sustancia {self.verEtiqueta()}.
\n| - ID: {self.verSerial()} - Ubicacion: {self.verUbicacion()}         
| - {self.verAcessStudent()} 
| - {self.verDanger()}
| - Temperatura de ebullicion: {self.verEbullicion()}
| - Temperatura al arder: {self.verArder()}"""

    def verEbullicion(self):
        return self.__ebullicion
    def verArder(self):
        return self.__arder
    def verEtiqueta(self):
        return self.__etiqueta

    def asignarEbullicion(self, ebullicion):
        self.__ebullicion = ebullicion
    def asignarArder(self, arder):
        self.__arder = arder
    def asignarEtiqueta(self, etiqueta):
        self.__etiqueta = etiqueta

class Solventes(Sustancia):
    pass

class Otras_Sustancias(Sustancia):
    pass

class Menu:
    def __init__(self):
        self.opciones = {
            "1": self.agregar_sustancia,         
            "2": self.imprimir_sustancias,
            "3": self.eliminar_sustancia,
            "4": self.salir,
            "*": self.len_sustancias,
            "+": self.activar_negrita,
            "-": self.desactivar_negrita,
            "add": self.cargar_informacion
        }
        self.bd_sustancia = {}
        
    def mostrar_menu(self):
        print("-"*60)
        print("\nBienvenido al sistema de registros de sustancias Bioquimicas.")
        print("\n| 1. Ingresar sustancia.                      |write(add)generarArchivo.txt")
        print("| 2. Imprimir sustancias.                     |press(+)activarNegrita")
        print("| 3. Eliminar Sustancia.                      |press(-)desactivarNegrita")
        print("| 4. Salir del sistema.                       |press(*)vercantidadSustancias.")
        print("")
 
    def ejecutar_opcion(self, opcion):
        if opcion in self.opciones:
            self.opciones[opcion]()
        else:
            print("Opción inválida")
    
    def agregar_sustancia(self): 
        while True:
            buscar_serial = self.verificar_codigo()
            cargar = self.bd_sustancia.get(buscar_serial, None)
            if cargar:
                print("-"*60)
                print(f"Ya existe una sustancia N°-{buscar_serial} en el sistema !!!")
                break
            else:
                print("Ingresa los datos de Numero de fila y columna en el gabinete.")
                fila = input("Ingrese la fila: ")
                columna = input("Ingrese la columna: ")
                ubicacion = f"|N°Fila = {fila}| N°Columna = {columna}|"
                print("¿La sustancia de libre acceso para estudiantes? \n1. Si - 2. No.")
                acceso = self.verificar_1_0_2()
                if acceso == "1":
                    acceso = "¿Es de libre acceso para estudiantes? Si."
                elif acceso == "2":
                    acceso = "¿Es de libre acceso para estudiantes? No."
                print("¿La sustancia es peligrosa para la salud humana? \n1. Si - 2. No: ")
                danger = self.verificar_1_0_2()
                if danger == "1":
                    danger = "¿Es peligrosa para la salud humana? Si."
                elif danger == "2":
                    danger = "¿Es peligrosa para la salud humana? No."  
                sustancia = Sustancia("", "", "", "")
                sustancia.asignarSerial(buscar_serial)
                sustancia.asignarUbicacion(ubicacion)
                sustancia.asignarAcess_student(acceso)
                sustancia.asignarDanger_human(danger)             
                print("""\nSelecciona el tipo de sustancia:
1. Acidos y bases.
2. Alcoholes.
3. Solventes.
4. Otras sustancias.""")
                opcion = self.verificar_opcion_sustancia()
                if opcion == "1":  
                    self.agregar_acido_base(sustancia)
                    break
                elif opcion == "2":
                    self.agregar_Alcoholes(sustancia)
                    break
                  
    def agregar_acido_base(self, sustancia):
        acido = Acidos_Bases("", "", "")
        acido.asignarSerial(sustancia.verSerial())
        acido.asignarUbicacion(sustancia.verUbicacion())
        acido.asignarAcess_student(sustancia.verAcessStudent())
        acido.asignarDanger_human(sustancia.verDanger())  
        print("\nIngresa la concentracion de la sustancia en Moles.")
        valor = self.verificar_valor()
        concentracion = f"{valor} M"
        descripcion = input("Describa los efectos a la salud que puede generar la sustancia.\n: ")
        acido.asignarEtiqueta("Acidos-Bases")
        acido.asignarConcentracion(concentracion)
        acido.asignarDescripcion(descripcion)
        self.bd_sustancia[acido.verSerial()] = acido
        return True
    
    def agregar_Alcoholes(self, sustancia):
        alcohol = Alcoholes("", "", "")
        alcohol.asignarSerial(sustancia.verSerial())
        alcohol.asignarUbicacion(sustancia.verUbicacion())
        alcohol.asignarAcess_student(sustancia.verAcessStudent())
        alcohol.asignarDanger_human(sustancia.verDanger())  
        print("\nIngresa la temperatura de ebullicion.")
        temp_abulli = self.verificar_valor()
        abullicion = f"{temp_abulli} °C"
        print("\nIngresa la temperatura al arder.")
        temp_arder = self.verificar_valor()
        arder = f"{temp_arder} °C"
        alcohol.asignarEtiqueta("Alcoholes")
        alcohol.asignarEbullicion(abullicion)
        alcohol.asignarArder(arder)
        self.bd_sustancia[alcohol.verSerial()] = alcohol
        return True

    def eliminar_sustancia(self):
        while True:
            print("Ingrese el serial a eliminar.")
            buscar_serial = self.verificar_codigo()
            id = self.bd_sustancia.get(buscar_serial, None )
            if not id:
                print("-"*60)
                print(f"No encontre la sustancia N°-{buscar_serial} en la Base de datos.")
                break
        
            else:
                del self.bd_sustancia[id.verSerial()] 
                print("-"*60)
                print("Operacion exitosa.... Sustancia eliminada.")
                break
    
    def imprimir_sustancias(self):
        while True:
            print("Ingresa el serial a buscar.")
            codigo = self.verificar_codigo()
            if codigo in self.bd_sustancia.keys():
                cargar = self.bd_sustancia.get(codigo, None )
                print(f"\n<> Sustancia:\n{cargar}")
                print("\n1. Volver al menu principal.\n2. Salir.")
                opcion = self.verificar_1_0_2()
                if opcion == "1":
                    break
                elif opcion == "2":
                    self.salir()
            else:
                print("-"*60)
                print(f'No encontre la sustancia N°-{codigo} en la Base de datos.')
                break
    
    def verificar_valor(self):
        while True:
            codigo = input(": ")
            try:
                codigo = float(codigo)
                if codigo <= 0:
                    print("\n°°° El valor debe ser > que 0") 
                    continue
            except ValueError:
                print("El valor debe ser un número flotante.")    
                continue
            return codigo 
        
    def verificar_codigo(self):
        while True:
            codigo = input("Ingrese el N° de serial: ")
            if codigo.isdigit() and len(codigo) >= 7 and len(codigo) <= 10:
                codigo = int(codigo)
                return codigo
            else:
                print("El serial ingresado no es valido. Por favor, ingrese un id de 7 a 10 dígitos.\n")

    def verificar_1_0_2(self):
        while True:
            codigo = input(": ")
            if codigo.isdigit() and (codigo) == "1" or (codigo) == "2":
                codigo = (codigo)
                return codigo
            else:
                print("Ingresa una opcion correcta.\n")
    
    def verificar_opcion_sustancia(self):
        while True:
            codigo = input(": ")
            if codigo.isdigit() and (codigo) == "1" or (codigo) == "2" or (codigo) == "3" or (codigo) == "4":
                codigo = (codigo)
                return codigo
            else:
                print("Ingresa una opcion correcta.\n")

    def salir(self):
        print()
        print("\nSaliendo del programa...")
        exit()
            
    def len_sustancias(self):
        cantidad = len(self.bd_sustancia.values())
        print("-"*60)
        print(f"El sistema tiene almacenado #{cantidad} sustancia.")
    
    def activar_negrita(self):
        print('\033[1m')
    
    def desactivar_negrita(self):
        print('\033[0m')
    
    def cargar_informacion(self):
        codigo = self.verificar_codigo()
        if codigo in self.bd_sustancia.keys():
            for busca in self.bd_sustancia.values():
                nombre_archivo = f"Sustancia{str(codigo)}.txt"
                archivo = open(nombre_archivo, "w")
                archivo.write("Archivo de texto genereado automaticamente por el sistema.")
                archivo.write("\nInformacion de la sustancia:\n")
                archivo.write("\n- Sustancia: \n-{}\n".format(busca))
                ruta_archivo = os.path.dirname(os.path.abspath(__file__)) + "/Sustancia" + str(codigo)
                print("-"*60)
                print(f"\nHe creado el archivo: {nombre_archivo} en la siguiente ruta:\n {ruta_archivo}")
                
            archivo.close()
        else:
            print("-"*60)
            print(f"No se encuentra en la base de datos: {str(codigo)}")

menu = Menu()
while True:
    menu.mostrar_menu()
    opcion = input("\nIngrese una opción: ")
    menu.ejecutar_opcion(opcion)
