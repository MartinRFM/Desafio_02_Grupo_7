from UTN_Heroes_Dataset.utn_matrices import matriz_data_heroes
from UTN_Heroes_Dataset.utn_funciones.auxiliares import color_text

def validar_opcion (num_min: int, num_max: int)->int: 
    
    
    
    opcion = input (f"ingrese una opcion entre {num_min} y {num_max}: ")
    if not opcion or not opcion.isdigit() or not (num_min <= int(opcion) <= num_max): #NOT OPCION: verifica que la varible no este vacia
        return (validar_opcion(num_min, num_max))  #Usamos una funcion recursiva, por lo que no hace falta usar un while para volver a pedir datos
    else:
        opcion = int(opcion)  #parseamos la opcion 
        return opcion




if __name__  == "__main__": #Usamos esta condicion que se ejecutara solo cuando compilemos desde el main original
    print (validar_opcion(3,10))