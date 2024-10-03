from .auxiliares import  (filtrar_cant_heroes_genero, mostrar_listas_formateada, filtrar_poder, cambiar_lista_1erLetra_mayuscula, \
                        mostrar_lista_matriz, mostrar_lista_matriz_dos, filtrar_matriz)
from UTN_Heroes_Dataset.utn_matrices import matriz_data_heroes
"""
Nota: Mostrar a X heroe, implica mostrar todos sus datos, formateados en columnas como si de una planilla se tratar

"""



def utn_mostrar_cantidad_heroes_fememinos (matriz_de_datos:list[list])->None:
    """_summary_ filtra la cantidad de heroes femeninos de una matriz y la muestra.

    Args:
        matriz_de_datos (list[list]): matriz de datos
    """
    matriz_filtrada = filtrar_cant_heroes_genero(matriz_de_datos, "Femenino")
    mostrar_listas_formateada(matriz_filtrada)

def utn_mostrar_cantidad_heroes_masculinos (matriz_de_datos:list[list])->None:
    """_summary_ filtra la cantidad de heroes masculinos de una matriz y la muestra.

    Args:
        matriz_de_datos (list[list]): matriz dde datos
    """
    matriz_filtrada = filtrar_cant_heroes_genero(matriz_de_datos, "Masculino")
    mostrar_listas_formateada(matriz_filtrada)

def utn_mostrar_heroes_mas_75_poder (matriz_de_datos:list[list])->None:
    """_summary_ filtra la cantidad de heroes con poder mayor al 75

    Args:
        matriz_de_datos (list[list]): _description_
    """
    matriz_filtrada = filtrar_poder (matriz_de_datos, "mayor", 75)
    mostrar_listas_formateada(matriz_filtrada)

def cuarto_punto():
    """_summary_ muestra los heroes con altura mayor a 160

    """
    def altura_metro_sesenta():
        
        def criterio_altura(altura):
            return altura > 160
            
        matriz_filtrada = filtrar_matriz(matriz_data_heroes, 5, criterio_altura)
        return matriz_filtrada
        
    matriz_filtrada = altura_metro_sesenta()
    mostrar_lista_matriz_dos(matriz_filtrada)
    return matriz_filtrada

def quinto_punto():
    """ muestra los heroes femeninos con mas de 60 de poder.
    
    """
    def heroes_femeninos():
        
        def criterio_genero(genero):
            return genero == "Femenino"
        
        matriz_filtrada = filtrar_matriz(matriz_data_heroes, 3, criterio_genero)
        
        def mas_poder():
            def criterio_poder(poder):
                return poder > 60
            
            matriz_filtrada_poder = filtrar_matriz(matriz_filtrada, 4, criterio_poder)
            return matriz_filtrada_poder
        
        matriz_filtrada = mas_poder()
        mostrar_lista_matriz_dos(matriz_filtrada)
        return matriz_filtrada
    
    matriz_filtrada = heroes_femeninos()
    mostrar_lista_matriz_dos(matriz_filtrada)
    
    return matriz_filtrada

def sexto_punto():
    """_summary_ muestra los heroes masculinos con menos de 60 de poder.
    """
    def heroes_masculinos():
        
        def criterio_genero(genero):
            return genero == "Masculino"
        
        matriz_filtrada = filtrar_matriz(matriz_data_heroes, 3, criterio_genero)
        
        def mas_poder():
            def criterio_poder(poder):
                return poder < 60
            
            matriz_filtrada_poder = filtrar_matriz(matriz_filtrada, 4, criterio_poder)
            return matriz_filtrada_poder
        
        matriz_filtrada = mas_poder()
        mostrar_lista_matriz_dos(matriz_filtrada)
        return matriz_filtrada
    
    matriz_filtrada = heroes_masculinos()
    mostrar_lista_matriz_dos(matriz_filtrada)
    
    return matriz_filtrada

def septimo_punto():
    """
    muestra los heroes no-binarios entre 10 y 5o de poder.
    """
    def heroes_nob():
        
        def criterio_genero(genero):
            return genero == "No-Binario"
        
        matriz_filtrada = filtrar_matriz(matriz_data_heroes, 3, criterio_genero)
        
        def mas_poder():
            def criterio_poder(poder):
                return 10 <= poder <= 50
            
            matriz_filtrada_poder = filtrar_matriz(matriz_filtrada, 4, criterio_poder)
            return matriz_filtrada_poder
        
        matriz_filtrada = mas_poder()
        mostrar_lista_matriz_dos(matriz_filtrada)
        return matriz_filtrada
    
    matriz_filtrada = heroes_nob()
    mostrar_lista_matriz_dos(matriz_filtrada)
    
    return matriz_filtrada

def octavo_punto():
    """
    muestra la cantidad de heroes con el minimo de poder.
    """
    def encontrar_minimo_poder(matriz_data_heroes):
        lista_poderes = matriz_data_heroes[4] 
        minimo_poder = min(lista_poderes)
        return minimo_poder
    minimo_poder = encontrar_minimo_poder(matriz_data_heroes)
    def contar_heroes_con_minimo_poder(matriz_data_heroes):
        minimo_poder = encontrar_minimo_poder(matriz_data_heroes)
        lista_poderes = matriz_data_heroes[4]
        cantidad_heroes_minimo_poder = lista_poderes.count(minimo_poder)
        return cantidad_heroes_minimo_poder
    cantidad_heroes_minimo_poder = contar_heroes_con_minimo_poder(matriz_data_heroes)
    return print(f"La cantidad de héroes con el mínimo poder es: {cantidad_heroes_minimo_poder}")

def noveno_punto():
    """_summary_ muestra la cantidad de heroes con maxima altura.
    """
    def encontrar_max_altura(matriz_data_heroes):
        lista_altura = matriz_data_heroes[5] 
        max_altura = max(lista_altura)
        return max_altura
    max_alturas = encontrar_max_altura(matriz_data_heroes)
    def contar_heroes_con_max_altura(matriz_data_heroes):
        max_altura = encontrar_max_altura(matriz_data_heroes)
        lista_altura = matriz_data_heroes[5]
        cantidad_heroes_max_altura = lista_altura.count(max_altura)
        return cantidad_heroes_max_altura
    cantidad_heroes_max_altura = contar_heroes_con_max_altura(matriz_data_heroes)
    return print(f"La cantidad de héroes con la maxima altura es: {cantidad_heroes_max_altura}")

def utn_ordenar_nombres_alfabeticamente_asc(matriz:list[list])-> None:
    """_summary_ ordena los apodos de manera ascendente dentro de la matriz pasada como parametro

    Args:
        matriz (list[list]): matriz de datos
    """
    lista_nombres = matriz[0]
    lista_identidades =matriz[1]
    lista_apodos = matriz[2]
    lista_generos = matriz[3]
    lista_poderes = matriz[4]
    lista_altura = matriz[5]
    for indice in range(len(lista_nombres) - 1):
        for sub_indice in range(indice + 1, len(lista_nombres)):
            if lista_nombres[indice] > lista_nombres[sub_indice]:
                lista_nombres[indice], lista_nombres[sub_indice] = lista_nombres[sub_indice], lista_nombres[indice]
                lista_identidades[indice], lista_identidades[sub_indice] = lista_identidades[sub_indice], lista_identidades[indice]
                lista_apodos[indice], lista_apodos[sub_indice] = lista_apodos[sub_indice], lista_apodos[indice]
                lista_generos[indice], lista_generos[sub_indice] = lista_generos[sub_indice], lista_generos[indice]
                lista_poderes[indice], lista_poderes[sub_indice] = lista_poderes[sub_indice], lista_poderes[indice]
                lista_altura[indice], lista_altura[sub_indice] = lista_altura[sub_indice], lista_altura[indice]
    mostrar_listas_formateada([lista_nombres, lista_identidades, lista_apodos, lista_generos, lista_poderes , lista_altura])

def utn_ordenar_apodos_alfabeticamente_des(matriz:list[list])-> None:
    """_summary_ ordena los apodos de manera descendente dentro de la matriz pasada como parametro

    Args:
        matriz (list[list]): matriz de datos
    """
    lista_nombres = matriz[0]
    lista_identidades = matriz[1]
    lista_apodos = matriz[2]
    lista_generos = matriz[3]
    lista_poderes = matriz[4]
    lista_altura = matriz[5]
    lista_apodos = cambiar_lista_1erLetra_mayuscula(lista_apodos)
    for indice in range(len(lista_apodos) - 1):
        for sub_indice in range(indice + 1, len(lista_apodos)):
            if lista_apodos[indice] < lista_apodos[sub_indice]:
                lista_apodos[indice], lista_apodos[sub_indice] = lista_apodos[sub_indice], lista_apodos[indice]
                lista_nombres[indice], lista_nombres[sub_indice] = lista_nombres[sub_indice], lista_nombres[indice]
                lista_identidades[indice], lista_identidades[sub_indice] = lista_identidades[sub_indice], lista_identidades[indice]
                lista_generos[indice], lista_generos[sub_indice] = lista_generos[sub_indice], lista_generos[indice]
                lista_poderes[indice], lista_poderes[sub_indice] = lista_poderes[sub_indice], lista_poderes[indice]
                lista_altura[indice], lista_altura[sub_indice] = lista_altura[sub_indice], lista_altura[indice]
    mostrar_listas_formateada([lista_nombres, lista_identidades, lista_apodos, lista_generos, lista_poderes , lista_altura])


def utn_ordenar_heroes_altura_asc_des(matriz:list[list])->None:
    """_summary_ recibe una lista como parametro y dependiendo lo que el usuario elija, la lista de altura se ordenara de manera ascendente o descendente.

    Args:
        matriz (list[list]): matriz de datos
    """
    lista_nombres = matriz[0]
    lista_identidades = matriz[1]
    lista_apodos = matriz[2]
    lista_generos = matriz[3]
    lista_poderes = matriz[4]
    lista_altura = matriz[5]
    respuesta = input("Ingrese de que modo desea ordenar la lista de alturas, ascendente(asc) o descendente(des): ")
    match respuesta:
        case "asc": 
            for indice_Uno in range(len(lista_altura)-1):
                indice_minimo = indice_Uno 
                for indice_Dos in range(indice_Uno + 1, len(lista_altura)):
                    if lista_altura[indice_Dos]<lista_altura[indice_minimo]:
                        indice_minimo = indice_Dos
                    if indice_minimo != indice_Uno:
                        lista_altura[indice_Uno], lista_altura[indice_minimo] = lista_altura[indice_minimo], lista_altura[indice_Uno]
                        lista_apodos[indice_Uno], lista_apodos[indice_minimo] = lista_apodos[indice_minimo], lista_apodos[indice_Uno]
                        lista_nombres[indice_Uno], lista_nombres[indice_minimo] = lista_nombres[indice_minimo], lista_nombres[indice_Uno]
                        lista_identidades[indice_Uno], lista_identidades[indice_minimo] = lista_identidades[indice_minimo], lista_identidades[indice_Uno]
                        lista_generos[indice_Uno], lista_generos[indice_minimo] = lista_generos[indice_minimo], lista_generos[indice_Uno]
                        lista_poderes[indice_Uno], lista_poderes[indice_minimo] = lista_poderes[indice_minimo], lista_poderes[indice_Uno]
            mostrar_listas_formateada([lista_nombres, lista_identidades, lista_apodos, lista_generos, lista_poderes , lista_altura])
        case "des":
            for indice_Uno in range(len(lista_altura)-1):
                indice_minimo = indice_Uno 
                for indice_Dos in range(indice_Uno + 1, len(lista_altura)):
                    if lista_altura[indice_Dos]>lista_altura[indice_minimo]:
                        indice_minimo = indice_Dos
                    if indice_minimo != indice_Uno:
                        lista_altura[indice_Uno], lista_altura[indice_minimo] = lista_altura[indice_minimo], lista_altura[indice_Uno]
                        lista_apodos[indice_Uno], lista_apodos[indice_minimo] = lista_apodos[indice_minimo], lista_apodos[indice_Uno]
                        lista_nombres[indice_Uno], lista_nombres[indice_minimo] = lista_nombres[indice_minimo], lista_nombres[indice_Uno]
                        lista_identidades[indice_Uno], lista_identidades[indice_minimo] = lista_identidades[indice_minimo], lista_identidades[indice_Uno]
                        lista_generos[indice_Uno], lista_generos[indice_minimo] = lista_generos[indice_minimo], lista_generos[indice_Uno]
                        lista_poderes[indice_Uno], lista_poderes[indice_minimo] = lista_poderes[indice_minimo], lista_poderes[indice_Uno]
            mostrar_listas_formateada([lista_nombres, lista_identidades, lista_apodos, lista_generos, lista_poderes , lista_altura])
        case _:
            print ("ERROR, ingrese asc o des")
            utn_ordenar_heroes_altura_asc_des(matriz_data_heroes)

