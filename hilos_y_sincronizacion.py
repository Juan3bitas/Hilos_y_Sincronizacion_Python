import threading;
import time;

semaforo = threading.Semaphore(1)

#Clase empleado
class Empleado:
    def __init__(self, nombre, documento):
        self.nombre = nombre
        self.documento = documento

#Clase impresora
class Impresora:
    def __init__(self):
        self.empleados = []
    
    #Método para agregar empleados que van a usar la impresora
    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)
    
    #Método para remover empelados que ya usaron la impresora
    def remover_empleado(self, empleado):
        self.empleados.remove(empleado)

    def imprimir(self, empleado):
        with semaforo:
            #Simula la impresión del empleado
            print(f"{empleado.nombre} está imprimiendo {empleado.documento}.")
            time.sleep(5)

            print(f"{empleado.nombre} terminó de imprimir.\n")
            self.remover_empleado(empleado)

    def gestionarImpresiones(self):
        hilos = []

        for empleado in self.empleados:
            hilo = threading.Thread(target=self.imprimir, args=(empleado,))
            hilos.append(hilo)
            hilo.start()

        for hilo in hilos:
            hilo.join()
        
        print("Todos los empleados ya imprimieron sus documentos.\n")

def main():
    impresora = Impresora()

    #Agregar los empleados a la lista de la impresora

    impresora.agregar_empleado(Empleado("Angie Bonilla","Tralalero_tralala.png"))
    impresora.agregar_empleado(Empleado("Celeste Buitrago","Albaricoque.docx"))
    impresora.agregar_empleado(Empleado("Juan Diego","Acta_de_matrimonio.pdf"))
    impresora.agregar_empleado(Empleado("Angie Grajales","Allosaurus.png"))
    impresora.agregar_empleado(Empleado("David Gómez","Brawlhalla_stats.png"))
    impresora.agregar_empleado(Empleado("Juan Sebastián","Principe_gris_zote.pdf"))

    #Gestionar las impresiones de los empleados
    impresora.gestionarImpresiones()

if __name__ == "__main__":
    main()