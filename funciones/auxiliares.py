from UTN_Heroes_Dataset.utn_matrices import  matriz_data_heroes
from UTN_Heroes_Dataset.utn_funciones.auxiliares import color_text

def mostrar_listas_formateada (matriz_data_heroes: list[list]):
    """_summary_ recibe una matriz con datos y formatea las listas de modo que sea mas legible

    Args:
        matriz (list): matriz de listas a mostrar
    """
    cantidad_columnas = len(matriz_data_heroes[0])
    cantidad_filas = len(matriz_data_heroes)
    for indice in range(cantidad_columnas):
        texto = ""
        for sub_indice in range(cantidad_filas):
            
            if type(matriz_data_heroes[sub_indice][indice]) == str:
                
                if len(matriz_data_heroes[sub_indice][indice]) >= 20:
                    texto_original = matriz_data_heroes[sub_indice][indice]
                    texto_saneado = texto_original[:19]
                    texto += f"{texto_saneado:20} | "
                else:
                    texto += f"{matriz_data_heroes[sub_indice][indice]:20} | "
                
            elif type(matriz_data_heroes[sub_indice][indice]) == int:
                texto += f"{matriz_data_heroes[sub_indice][indice]:03} | "
                
            elif type(matriz_data_heroes[sub_indice][indice]) == float:
                texto += f"{matriz_data_heroes[sub_indice][indice]:8.2f} | "
                
            else:
                texto += f"{matriz_data_heroes[sub_indice][indice]} | "
                
                
        texto = texto[0 : -3]
        print(texto)

def filtrar_cant_heroes_genero(matriz_datos:list[list], genero: str)->list[list]:
    """_summary_ recibe una matriz de datos y busca el genero que se le pase por parametro

    Args:
        matriz_datos (list[list]): matriz de datos
        genero (str): nombre del genero a buscar, debe ser exactamente igual al de la lista generos
    """
    lista_nombres = matriz_datos[0]
    lista_identidades =matriz_datos[1]
    lista_apodos = matriz_datos[2]
    lista_generos = matriz_datos[3]
    lista_poderes = matriz_datos[4]
    lista_altura = matriz_datos[5]
    matriz_genero_filtrado = [[],[],[],[],[],[]]
    for indice in range(len(lista_generos)):
        if lista_generos[indice] == genero: 
            matriz_genero_filtrado[0].append (lista_nombres[indice])
            matriz_genero_filtrado[1].append (lista_identidades[indice])
            matriz_genero_filtrado[2].append(lista_apodos[indice])
            matriz_genero_filtrado[3].append(lista_generos[indice])
            matriz_genero_filtrado[4].append(lista_poderes[indice])
            matriz_genero_filtrado[5].append(lista_altura[indice])
    return matriz_genero_filtrado

def filtrar_poder(matriz_datos:list[list], rango:str, num:int, num_max:int = None,)->list[list]:
    """_summary_ recibe la matriz, toma la lista poder y dependiendo del parametro que se las pase filtra si es \
                    por mayor, menor o el poder debe estar entre un rango de numeros. si no encuntra nada devuelve una lista vacia

    Args:
        rango string que indica el rango a filtrar.
        num numero por el cual se decide comparar.
        num_max: opcional, llenar si se desea buscar entre el primer numero ingresado y este. 
        
    """
    lista_nombres = matriz_datos[0]
    lista_identidades =matriz_datos[1]
    lista_apodos = matriz_datos[2]
    lista_generos = matriz_datos[3]
    lista_poderes = matriz_datos[4]
    lista_altura = matriz_datos[5]
    matriz_poder_filtrado = [[],[],[],[],[],[]]

    match rango:
        case "menor":
            for indice in range(len(lista_poderes)):
                if lista_poderes[indice]<= num:
                    matriz_poder_filtrado[0].append (lista_nombres[indice])
                    matriz_poder_filtrado[1].append (lista_identidades[indice])
                    matriz_poder_filtrado[2].append(lista_apodos[indice])
                    matriz_poder_filtrado[3].append(lista_generos[indice])
                    matriz_poder_filtrado[4].append(lista_poderes[indice])
                    matriz_poder_filtrado[5].append(lista_altura[indice])
        case "mayor":
            for indice in range(len(lista_poderes)):
                if lista_poderes[indice] >= num:
                    matriz_poder_filtrado[0].append (lista_nombres[indice])
                    matriz_poder_filtrado[1].append (lista_identidades[indice])
                    matriz_poder_filtrado[2].append(lista_apodos[indice])
                    matriz_poder_filtrado[3].append(lista_generos[indice])
                    matriz_poder_filtrado[4].append(lista_poderes[indice])
                    matriz_poder_filtrado[5].append(lista_altura[indice])
        case "intervalo":
            if num_max is not None:
                for indice in range(len(lista_poderes)):
                    if num <= lista_poderes[indice] <= num_max:
                        matriz_poder_filtrado[0].append (lista_nombres[indice])
                        matriz_poder_filtrado[1].append (lista_identidades[indice])
                        matriz_poder_filtrado[2].append(lista_apodos[indice])
                        matriz_poder_filtrado[3].append(lista_generos[indice])
                        matriz_poder_filtrado[4].append(lista_poderes[indice])
                        matriz_poder_filtrado[5].append(lista_altura[indice])
    return matriz_poder_filtrado


def cambiar_lista_1erLetra_mayuscula(lista:list[str])->list:
    for indice in range(len(lista)):
        lista[indice] = lista[indice].title()
    return lista


def mostrar_lista_matriz ():
    cantidad_columnas = len(matriz_data_heroes[0])
    cantidad_filas = len(matriz_data_heroes)
    for indice in range(cantidad_columnas):
        texto = ""
        for sub_indice in range(cantidad_filas):
            
            if type(matriz_data_heroes[sub_indice][indice]) == str:
                
                if len(matriz_data_heroes[sub_indice][indice]) >= 20:
                    texto_original = matriz_data_heroes[sub_indice][indice]
                    texto_saneado = texto_original[:19]
                    texto += f"{texto_saneado:20} | "
                else:
                    texto += f"{matriz_data_heroes[sub_indice][indice]:20} | "
                
            elif type(matriz_data_heroes[sub_indice][indice]) == int:
                texto += f"{matriz_data_heroes[sub_indice][indice]:03} | "
                
            elif type(matriz_data_heroes[sub_indice][indice]) == float:
                texto += f"{matriz_data_heroes[sub_indice][indice]:8.2f} | "
                
            else:
                texto += f"{matriz_data_heroes[sub_indice][indice]} | "
                
                
        texto = texto[0 : -3]
        print(texto)

def mostrar_lista_matriz_dos (matriz_filtrada):
    cantidad_columnas = len(matriz_filtrada[0])
    cantidad_filas = len(matriz_filtrada)
    for indice in range(cantidad_columnas):
        texto = ""
        for sub_indice in range(cantidad_filas):
            
            if type(matriz_filtrada[sub_indice][indice]) == str:
                
                if len(matriz_filtrada[sub_indice][indice]) >= 20:
                    texto_original = matriz_filtrada[sub_indice][indice]
                    texto_saneado = texto_original[:19]
                    texto += f"{texto_saneado:20} | "
                else:
                    texto += f"{matriz_filtrada[sub_indice][indice]:20} | "
                
            elif type(matriz_filtrada[sub_indice][indice]) == int:
                texto += f"{matriz_filtrada[sub_indice][indice]:03} | "
                
            elif type(matriz_filtrada[sub_indice][indice]) == float:
                texto += f"{matriz_filtrada[sub_indice][indice]:8.2f} | "
                
            else:
                texto += f"{matriz_filtrada[sub_indice][indice]} | "
                
                
        texto = texto[0 : -3]
        print(color_text(texto, "Info"))

def filtrar_matriz(matriz_data_heroes, indice, criterio):

    lista_a_filtrar = matriz_data_heroes[indice]
    indices_filtrados = [i for i, dato in enumerate(lista_a_filtrar) if criterio(dato)]
    matriz_filtrada = [[fila[info] for info in indices_filtrados] for fila in matriz_data_heroes]
    return matriz_filtrada
