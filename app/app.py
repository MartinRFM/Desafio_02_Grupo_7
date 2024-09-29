from funciones.salida_consola import mostrarmenu
from UTN_Heroes_Dataset.utn_funciones import saludo, clear_console, play_sound
from validaciones.validaciones import validar_opcion
from UTN_Heroes_Dataset.utn_matrices import matriz_data_heroes 


def utn_heroes_app ():

    matriz_data_heroes
    while True:
        mostrarmenu()
        opcion = validar_opcion(1,10)
        
        match opcion:
            case 1:
                pass
            case 2:
                pass
            case 3: 
                pass
            case 4: 
                pass
            case 5: 
                pass
            case 6:
                pass
            case 7:
                pass
            case 8: 
                pass
            case 9: 
                pass
                
            case 10: 
                pass
            case 11:
                pass
            case 12: 
                pass
            case 13:
                break
        play_sound()
        clear_console()

if __name__  == "__main__": #Usamos esta condicion que se ejecutara solo cuando compilemos desde el main original
    utn_heroes_app(matriz_data_heroes)