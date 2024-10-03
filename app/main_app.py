
from UTN_Heroes_Dataset.utn_funciones import clear_console, play_sound, saludo
from UTN_Heroes_Dataset.utn_matrices import matriz_data_heroes 
from funciones import (mostrar_menu, utn_mostrar_cantidad_heroes_fememinos, utn_mostrar_cantidad_heroes_masculinos,\
                        utn_mostrar_heroes_mas_75_poder, cuarto_punto, quinto_punto, sexto_punto, septimo_punto, octavo_punto, noveno_punto,\
                        utn_ordenar_apodos_alfabeticamente_des, utn_ordenar_heroes_altura_asc_des, utn_ordenar_nombres_alfabeticamente_asc)
from validaciones import validar_opcion

def utn_heroes_app (matriz_data_heroes: list[list]):

    
    while True:
        saludo()
        mostrar_menu()
        opcion = validar_opcion(1,13)
        
        match opcion:
            case 1:
                utn_mostrar_cantidad_heroes_fememinos(matriz_data_heroes)
            case 2:
                utn_mostrar_cantidad_heroes_masculinos(matriz_data_heroes)
            case 3: 
                utn_mostrar_heroes_mas_75_poder(matriz_data_heroes)
            case 4: 
                cuarto_punto()
            case 5: 
                quinto_punto()
            case 6:
                sexto_punto()
            case 7:
                septimo_punto()
            case 8: 
                octavo_punto()
            case 9: 
                noveno_punto()
            case 10: 
                utn_ordenar_nombres_alfabeticamente_asc(matriz_data_heroes)
            case 11:
                utn_ordenar_apodos_alfabeticamente_des(matriz_data_heroes)
            case 12: 
                utn_ordenar_heroes_altura_asc_des(matriz_data_heroes)
            case 13:
                break
        play_sound()
        clear_console()
