
def validar_opcion (num_min: int, num_max: int)->int: 
    """_summary_
    Args:
        num_min (int): _description_
        num_max (int): _description_
    Returns:
        int: _description_
    """
    
    opcion = input (f"ingrese una opcion entre {num_min} y {num_max}: ")
    if not opcion or not opcion.isdigit() or not (num_min <= int(opcion) <= num_max): #NOT OPCION: verifica que la varible no este vacia
        return (validar_opcion(num_min, num_max))  #Usamos una funcion recursiva, por lo que no hace falta usar un while para volver a pedir datos
    else:
        opcion = int(opcion) 
        return opcion
    
