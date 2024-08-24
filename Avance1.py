print("Bienvenido a Elemental Batlle")

#Funcion de efectividad

def es_efectivo(tipo,ataque):
    efectivo = 1
    if tipo == "agua" and ataque == "lluvia floral":
        return efectivo
    if tipo == "fuego" and ataque == "ola":
        return efectivo
    if tipo == "piedra" and ataque == "ola":
        return efectivo
    if tipo == "planta" and ataque == "rueda de fuego":
        return efectivo
    if tipo == "aereo" and ataque == "pedrada":
        return efectivo
    if tipo == "planta" and ataque == "vendaval":
        return efectivo
    if tipo == "piedra" and ataque == "lluvia floral":
        return efectivo
    else:
        efectivo = 0
        return efectivo

#Funcion para calcular daño

def danio(efectivo):
    if efectivo == 1:
        valor_danio = 100 - (50*2)
        return valor_danio
    else: 
        valor_danio = 100 - 50
        return valor_danio
    
   
print("Jugador 1 - Escribe tu tipo (agua/fuego/piedra/planta/aereo): ")
tipo_j1 = input()
print("Jugador 2 - Escribe tu tipo (agua/fuego/piedra/planta/aereo): ")
tipo_j2 = input()
print("Jugador1 - Elige un ataque (ola/rueda de fuego/pedrada/lluvia floral/vendaval): ")
ataque1 = input()
print("Jugador2 - Elige un ataque (ola/rueda de fuego/pedrada/lluvia floral/vendaval): ")
ataque2 = input ()

#El ataque es efectivo contra t1
efectividad_t1= es_efectivo(tipo_j1,ataque2)
print(efectividad_t1)

#El ataque es efectivo contra t2
efectividad_t2= es_efectivo(tipo_j2,ataque1)
print(efectividad_t2)

#Danio contra tipo1
vidaj1= danio(efectividad_t1)
print("La vida de jugador 1 es: ", vidaj1)

#Danio contra tipo2
vidaj2= danio(efectividad_t2)
print("La vida de jugador 2 es: ", vidaj2)


