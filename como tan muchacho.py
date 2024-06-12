import csv
lista=[]
def imprimir_lista(lis):
    for x in lis:
        print("ID : ",x["id"])
        print("nombre : ",x["detalle"])
        print("Precio : ",x["precio"])
        print("-------")
def menu():
    print("-."*20)
    print(".-.-.-.-.-.Menu auto motris.-.-.-.")  
    print("1.-agregar producto")
    print("2.-lista de todos los productos ")
    print("3.-eleminar prodicto por id")
    print("4.-generar archivo cvs")
    print("5.-cargar archivo csv")
    print("6.-estadisticas")
    print("0.-salir")
    print("/-/"*20)
    
    
    op=int(input("ingrese una opcion : "))

    
    if op==1:
        print(":_:_:_:_Agregar un auto:__:_:_:_:_")
    elif op==2:
        print(".-.--.-.-.-.-.-.-.lista de los autos.--.-.-.-.-.")
        print(lista)
    elif op==3:
        lista=[("id":1,"detalle":'escritorio',"precio":30000)]
    elif op==4:
        print("generar archivo con cvs")
    elif op==5:
        print("c")
    elif op==6:
        print("d")
    elif op==0:
        print("")
        print(" ADIOS WACHIN ")
        break
    else:
        print("")
        print("no selecciono ninguna opcion....")
        print("vuelva ingresar una opcion")
        print("\n"*3)
