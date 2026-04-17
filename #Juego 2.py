#Juego

print("--- SUPERVIVENCIA EN LA SELVA DEL AMAZONAS ---")
print("Tu avioneta se ha estrellado. Entre los restos ves un MACHETE y un ENCENDEDOR.")

opcion1 = input("Que decides tomar? (MACHETE / ENCENDEDOR): ").strip().lower()

# nivel 1
if opcion1 == "machete":
    print("Con el machete te abres paso entre la maleza. Llegas a un claro con tres caminos: CUEVA, RIO o RUINAS.")
    
    # Nivel 2
    opcion2 = input("Que camino eliges? (CUEVA / RIO / RUINAS):").strip().lower()
    
    if opcion2 == "ruinas":
        print("Encuentras un templo azteca! En la entrada hay tres estatuas: JAGUAR, AGUILA o SERPIENTE.")
        
        # nivel 3
        opcion3 = input("A que estatua le pides permiso para pasar? (JAGUAR / AGUILA / SERPIENTE): ").strip().lower()
        if opcion3 == "jaguar":
            print("Se abre una puerta secreta. Dentro hay tres objetos: ÍDOLO, CALIZ o MASCARA.")
            
            # Nivel 4
            opcion4 = input("Que objeto sagrado tomas? (IDOLO / CALIZ / MASCARA): ").strip().lower()
            if opcion4 == "mascara":
                print("Al ponertela, ves un mapa espiritual con tres destinos: VOLCAN, ALDEA o CASCADA.")
                
                # Nivel 5 
                opcion5 = input("Hacia donde te diriges? (VOLCAN / ALDEA / CASCADA): ").strip().lower()
                if opcion5 == "aldea":
                    print("Llegas a una tribu que te recibe como un dios. Tienes tres ofrendas: COMER, CANTAR o BAILAR.")
                    
                    # Nivel 6 
                    opcion6 = input("Que haces para ganarte su respeto? (COMER / CANTAR / BAILAR): ").strip().lower()
                    if opcion6 == "bailar":
                        print("Felicidades! Tu baile impresiona al jefe y te ayudan a volver a la civilización. VICTORIA!")
                    elif opcion6 == "comer":
                        print("La comida era demasiado picante para un turista. FIN DEL JUEGO.")
                    elif opcion6 == "cantar":
                        print("Cantas tan mal que creen que eres un espiritu maligno. FIN DEL JUEGO.")
                    else:
                        print("Te quedas mudo y te expulsan de la aldea.")
                else:
                    print("Te pierdes en la inmensidad de la selva. FIN DEL JUEGO.")
            else:
                print("El objeto tenia una maldicion de flechas venenosas. FIN DEL JUEGO.")
        else:
            print("La estatua cobra vida y te ataca. FIN DEL JUEGO.")
            
    elif opcion2 == "rio":
        print("Intentas cruzar, pero las pirañas tienen hambre. FIN DEL JUEGO.")
    elif opcion2 == "cueva":
        print("Esta llena de murcielagos rabiosos. FIN DEL JUEGO.")
    else:
        print("Te quedas parado y un mosquito gigante te pica. FIN DEL JUEGO.")

elif opcion1 == "encendedor":
    print("Usas el fuego para ahuyentar a las bestias, pero el humo atrae algo peor.")
    print("Ves una sombra moviéndose: ¿Prefieres CORRER, TREPAR o LUCHAR?")
    
    # Nivel 2
    opcion2b = input("Que decides? (CORRER / TREPAR / LUCHAR): ").strip().lower()
    if opcion2b == "trepar":
        print("Desde lo alto de un arbol ves tres señales de humo: BLANCO, NEGRO o AZUL.")
        
        # Nivel 3
        opcion3b = input("A cual te diriges? (BLANCO / NEGRO / AZUL): ").strip().lower()
        if opcion3b == "blanco":
            print("Es un campamento de rescate. Tienen tres vehiculos: HELICOPTERO, JEEEP o CANOA.")
            
            # Nivel 4
            print("(Continuara en la siguiente expansion...)")
        else:
            print("Era un incendio forestal. FIN DEL JUEGO.")
    else:
        print("Un jaguar fue más rápido que tu. FIN DEL JUEGO.")

else:
    print("El panico te domina y no tomas nada. La selva te consume rapidamente.")