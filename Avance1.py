print("Bienvenido a Elemental Batlle")


#Funcion para identificar tipo
def identificar_tipo (criatura):
    if criatura == "wettie" or criatura == "gotin":
        return "agua"
    elif criatura == "kandle" or criatura == "volcano":
        return "fuego"
    elif criatura == "vaioleta" or criatura == "grasso":
        return "planta"
    elif criatura == "mrplane" or criatura == "flayer":
        return "aereo"
    elif criatura == "rockman" or criatura == "solbrick":
        return "piedra"
    elif criatura == "elektro" or criatura == "rhayman":
        return "electrico"
    
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


#Funcion para mostrar ataque especifico
def asignar_ataque(tipo):
    if tipo == "agua":
        return "1:Ola / 2: Polvareda / 3:Oxidacion"
    elif tipo == "fuego":
        return "1:Rueda de fuego / 2: Polvareda / 3:Oxidacion"
    elif tipo == "piedra":
        return "1:Pedrada / 2: Polvareda / 3:Oxidacion"
    elif tipo == "planta":
        return "1:Lluvia floral / 2: Polvareda / 3:Oxidacion"
    elif tipo == "aereo":
        return "1:Vendaval / 2: Polvareda / 3:Oxidacion"
    elif tipo == "electrico":
        return "1:Rayo / 2: Polvareda / 3:Oxidacion"


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
def danio(efectivo):
    if efectivo == "Este ataque es efectivo":
        valor_danio = 80
        return valor_danio
    else: 
        valor_danio = 40
        return valor_danio
    
#Eleccion de criatura
print("Jugador 1 - Escoje una criatura y escribela: (volcano, flayer, grasso, elektro, solbrick,\
 mrplane, wettie, rhayman, vaioleta, gotin, rockman, kandle): ")
criatura_j1 = input()
print("Jugador 2 - Escoje una criatura y escribela: (volcano, flayer, grasso, elektro, solbrick,\
 mrplane, wettie, rhayman, vaioleta, gotin, rockman, kandle): ")
criatura_j2 = input()


#Identificar tipo y vida inicial
tipo_j1 = identificar_tipo(criatura_j1)
tipo_j2 = identificar_tipo(criatura_j2)

vidaj1 = vida_inicial(tipo_j1) 
vidaj2 = vida_inicial(tipo_j2)


#Ciclo para continuar batalla
while vidaj1 > 0 and vidaj2 > 0:

#Identificar ataques
    print ("Jugador 1 - Selecciona un ataque:", asignar_ataque(tipo_j1))
    ataque1 = int (input())
    print ("Jugador 2 - Selecciona un ataque:", asignar_ataque(tipo_j2))
    ataque2 = int (input())

#El ataque es efectivo contra t1
    efectividad_t1= es_efectivo(ataque1,tipo_j1,tipo_j2)
    print(efectividad_t1)

#El ataque es efectivo contra t2
    efectividad_t2= es_efectivo(ataque2,tipo_j2,tipo_j1)
    print(efectividad_t2)

#Danio contra tipo1
    danioj1= danio(efectividad_t2)
#Danio contra tipo2
    danioj2= danio(efectividad_t1)

#Calcular vida final de cada jugador
    vidaj1 = vidaj1 - danioj1
    vidaj2 = vidaj2 - danioj2
    print("La vida de jugador 1 es: ", vidaj1)
    print("La vida de jugador 2 es: ", vidaj2)

if vidaj1 <= 0:
    print("Jugador 1 ha perdido. ¡Jugador 2 gana!")
elif vidaj2 <= 0:
    print("Jugador 2 ha perdido. ¡Jugador 1 gana!")
