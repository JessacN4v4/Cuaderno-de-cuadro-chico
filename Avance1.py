
# Matriz de criaturas y su tipo correspondiente
criaturas_ataques = [
    ["Volcano", "fuego","1:Rueda de fuego / 2:Embestida / 3:Abrazo fugaz"],
    ["Flayer", "aereo","1:Vendaval / 2:Embestida / 3:Aire afilado"],
    ["Grasso", "planta","1:Lluvia floral / 2:Embestida / 3:Navahojazo"],
    ["Elektro", "electrico","1:Rayo / 2:Embestida / 3:Chispazo"],
    ["Solbrick", "piedra","1:Deslave / 2:Embestida / 3: Pedrada "],
    ["Mr.Plane", "aereo","1:Vendaval / 2:Embestida / 3:Aire afilado"],
    ["Wettie", "agua","1:Ola / 2:Embestida / 3:Goteo"],
    ["Rhayman", "electrico","1:Rayo / 2:Embestida / 3:Chispazo"],
    ["Vaioleta", "planta","1:Lluvia floral / 2:Embestida / 3:Navahojazo"],
    ["Gotin", "agua","1:Ola / 2:Embestida / 3:Goteo"],
    ["Rockman", "piedra","1:Deslave / 2:Embestida / 3: Pedrada "],
    ["Kandle", "fuego","1:Rueda de fuego / 2:Embestida / 3:Abrazo fugaz"]
]

#Funcion para identificar el tipo de la criatura
def identificar_tipo(criatura):
    return criaturas_ataques[criatura - 1][1]  # El tipo está en el índice 1

#Funcion para mostrar ataques especificos
def asignar_ataque(criatura):
    return criaturas_ataques[criatura - 1][2] #Los ataques estan en el índice 2

#Funcion para asignar vida de cada criatura
def vida_inicial(tipo):
    vida_base = 100
    if tipo == "agua":
        return vida_base +10
    elif tipo == "planta":
        return vida_base
    elif tipo == "fuego":
        return vida_base + 30
    elif tipo == "piedra":
        return vida_base + 20
    elif tipo == "aereo":
        return vida_base - 10
    elif tipo == "electrico":
        return vida_base - 5

#Funcion de ataques efectivos
def es_efectivo(ataque,tipo1,tipo2):
   efectivo = "Este ataque es efectivo"
   no_efectivo = "Este ataque NO es efectivo"
   if ataque == 1 and tipo1 == "agua" and tipo2 == "piedra":
       return efectivo
   elif ataque == 1 and tipo1 == "agua" and tipo2 == "fuego":
       return efectivo
   elif ataque == 1 and tipo1 == "planta" and tipo2 == "agua":
       return efectivo
   elif ataque == 1 and tipo1 == "planta" and tipo2 == "piedra":
       return efectivo
   elif ataque == 1 and tipo1 == "fuego" and tipo2 == "planta":
       return efectivo
   elif ataque == 1 and tipo1 == "piedra" and tipo2 == "aereo":
       return efectivo
   elif ataque == 1 and tipo1 == "piedra" and tipo2 == "fuego":
       return efectivo
   elif ataque == 1 and tipo1 == "aereo" and tipo2 == "planta":
       return efectivo
   elif ataque == 1 and tipo1 == "electrico" and tipo2 == "agua":
       return efectivo
   elif ataque == 1 and tipo1 == "electrico" and tipo2 == "aereo":
       return efectivo
   elif ataque >= 4:
       return "Este ataque no existe"
   else:
       return no_efectivo

#Funcion para calcular daño
def danio(ataque,efectivo):
    if efectivo == "Este ataque es efectivo":
        valor_danio = 80
        return valor_danio
    elif efectivo == "Este ataque no existe":
        valor_danio = 0
        return valor_danio
    elif ataque == 2:
        valor_danio = 35
        return valor_danio
    elif ataque == 3:
        valor_danio = 30
        return valor_danio
    else: 
        valor_danio = 25
        return valor_danio
    

print ("BIENVENIDOS A ELEMENTAL BATTLE")
print ("¡¡¡EXITO A AMBOS!!!")
#Eleccion de criatura
seleccion_j1 = ["1-Volcano / 2-Flayer","3-Grasso / 4-Elektro", "5-Solbrick\
/ 6-Mr.Plane","7-Wettie / 8-Rhayman","9-Vaioleta / 10-Gotin", "11-Rockman\
/ 12-Kandle"]
for s1 in seleccion_j1:
    print(s1)

print("JUGADOR 1 - ELIGE UNA CRIATURA DE LAS ANTERIORES")
criatura_j1 = int(input())

seleccion_j2 = ["1-Volcano / 2-Flayer","3-Grasso / 4-Elektro", "5-Solbrick\
/ 6-Mr.Plane","7-Wettie / 8-Rhayman","9-Vaioleta / 10-Gotin", "11-Rockman\
/ 12-Kandle"]
for s2 in seleccion_j2:
    print(s2)

print("JUGADOR 1 - ELIGE UNA CRIATURA DE LAS ANTERIORES")
criatura_j2 = int(input())

#Identificar tipo y vida inicial
tipo_j1 = identificar_tipo(criatura_j1)
tipo_j2 = identificar_tipo(criatura_j2)


vidaj1 = vida_inicial(tipo_j1) 
vidaj2 = vida_inicial(tipo_j2)

print("La vida inicial del jugador 1 es: ", vidaj1)
print("La vida inicial del jugador 2 es: ", vidaj2)

# Ciclo para continuar la batalla
while vidaj1 >= 0 and vidaj2 >= 0:
    # Mostrar ataques disponibles y seleccionar
   
    #Aqui utilize la funcion f-string
    print(f"Jugador 1 - Selecciona un ataque: {asignar_ataque(criatura_j1)}")
    ataque1 = int(input()) 
    print(f"Jugador 2 - Selecciona un ataque: {asignar_ataque(criatura_j2)}")
    ataque2 = int(input()) 

    # Comprobar efectividad y calcular daño
    efectividad_t1 = es_efectivo(ataque1 , tipo_j1, tipo_j2)
    efectividad_t2 = es_efectivo(ataque2 , tipo_j2, tipo_j1)
    
    danioj1 = danio(ataque1 , efectividad_t2)
    danioj2 = danio(ataque2 , efectividad_t1)

    # Calcular vida restante
    vidaj1 -= danioj1
    vidaj2 -= danioj2

    # Mostrar vida actual
    print(f"La vida de Jugador 1 es: {vidaj1}")
    print(f"La vida de Jugador 2 es: {vidaj2}")

# Verificar ganador
if vidaj1 <= 0:
    print("Jugador 1 ha perdido") 
    print ("¡¡¡¡¡¡Jugador 2 gana!!!!!!")
elif vidaj2 <= 0:
    print("Jugador 2 ha perdido")
    print ("¡¡¡¡¡¡Jugador 1 gana!!!!!!")
