#Ejercicio 1#
nombre=""
cantidad_de_productos= ""
precio=""
tiene_descuento=""
descuento= 0.10
cantidad=""
total_sin_descuento = 0
total_con_descuento = 0

nombre = input("Ingrese su nombre: ")
while not nombre.isalpha():
    print("Solamente letras")
    nombre = input("Ingrese su nombre: ")
cantidad_de_productos = input("Escriba la cantidad de productos que va a llevar (Solo numeros): ")
while not cantidad_de_productos.isdigit() or cantidad_de_productos == "0":
    print("Error: Ingrese un numero mayor a 0.")
    cantidad_de_productos = input("Escriba la cantidad de productos que va a llevar (Solo numeros): ")
cantidad = int(cantidad_de_productos)
for i in range(cantidad):
    print(f"Producto {i+1}")
    precio = input("Ingrese el precio del producto: ")
    while not precio.isdigit():
        print("Error: Precio en Numeros")
        precio = input("Ingrese el precio del producto (Solo numeros): ")
    precio_flotante = float(precio)
    total_sin_descuento += precio_flotante 
    tiene_descuento = input("tiene descuento? Si= S o No= N: ").lower()
    while tiene_descuento not in ["s", "n"]:
        print('Porfavor solo ingrese S/N')
        tiene_descuento = input("Ingrese si tiene S/N: ").lower()
    if tiene_descuento == "s":
        descuento_aplicado = precio_flotante * 0.10
        precio_final = precio_flotante - descuento_aplicado
        print(f"con descuento quedaria en {precio_final}")
    else:
        precio_final = precio_flotante
        print("Este producto NO aplica al descuento")
    total_con_descuento += precio_final
ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad
print (f"Cliente: {nombre}")
print(f"total sin descuentos {total_sin_descuento}")
print(f"total con descuentos {total_con_descuento:.2f}")
print(f"Ahorro total {ahorro:.2f}")
print(f"Promedio por producto {promedio:.2f}")

#Ejercicio 2#
usuario=""
clave=""
usuario== "alumno"
clave == "pyhthon123"
salir = False
intentos = 0
intento=""
intento= 1
entro=""
nueva_clave1=""
nueva_clave2=""

while not salir and intentos < 3:
    print (f"intento numero {intento}/3")
    usuario = input("Ingrese su nombre de usuario: ")
    while not usuario.isalpha():
        print ("Usuario (Solo letras)")
        usuario= input ("Ingrese Nombre de usuario: ")
    clave = input("Ingrese su contraseña: ")
    intentos += 1
    intento +=1
    if usuario == "alumno" and clave == "python123":
        print("¡Acceso concedido!")
        while not salir:
            print ("Elija 1- Mostrar Estado de Inscripcion 2- Cambiar clave 3- Mostrar Mensaje Motivacional 4- Salir")
            entro= input ("Elija el Numero: ")
            while not entro.isdigit() or int(entro) < 1 or int(entro) > 4:
                print ("Opcion fuera de rango")
                entro= input ("Elija el numero: ")
            if entro == "1":
                print ("Usted está: Inscripto")
            elif entro == "2":
                nueva_clave1= (input("Ingrese su nueva clave: "))
                nueva_clave2= (input("Ingrese la confirmación: "))
                if len (nueva_clave2) <6:
                        print ("La clave no puede ser menor a 6 caracteres")
                elif nueva_clave1 == nueva_clave2: 
                        print ("Clave Cambiada correctamente")
                elif nueva_clave1 != nueva_clave2:
                        print ("Las claves no coinciden")
            elif entro == "3":
                print ("El éxito no es un evento repentino, sino el resultado acumulado de pequeños esfuerzos diarios que casi nadie ve, pero que lo cambian todo.")
            elif entro== "4":
                salir = True
                break
    else:
        print("Credenciales Invalidas")
        if intentos >= 3:
            print(" Cuenta bloqueada.")

#Ejercicio 3#
Nombre= input ("Ingrese su nombre: ")
menu=""
salir= False
dias=""
reserva=""
lunes_1=""
lunes_2=""
lunes_3=""
lunes_4=""
martes_1=""
martes_2=""
martes_3=""
print (f"Hola {Nombre}, elija una de las 5 opciones")
while not salir:
    menu= input ("1-Reservar turno 2- Cancelar turno 3- Ver agenda del día 4- Ver resumen general 5- Cerrar sistema")
    while not menu.isdigit() or int (menu)<1 or int (menu)>5:
            print ("Opcion fuera de Rango")
            menu= int (input ("Elija un numero: "))
    if menu=="1":
            print ("Los dias disponibles son: Lunes y martes. Presione 1 o 2 dependiendo el dia que quiera!")
            dias=""
            while not dias.isdigit() or int (dias)<1 or int (dias)>2:
                dias= input("Ingrese el dia, 1(Lunes) o 2(Martes): ")
            if dias=="1":
                if lunes_1=="":
                    lunes_1= (input ("Ingrese su nombre para ser registrado: "))
                    print ("Turno Agendado con exito!")
                elif lunes_2=="":
                    lunes_2= (input ("Ingrese su nombre para ser registrado: "))
                    print ("Turno Agendado con exito!")
                elif lunes_3=="":
                    lunes_3= (input ("Ingrese su nombre para ser registrado: "))
                    print ("Turno Agendado con exito!")
                elif lunes_4=="":
                    lunes_4= (input ("Ingrese su nombre para ser registrado: "))
                    print ("Turno Agendado con exito!")
                else:
                    print ("No hay mas turnos, lo sentimos!")
            elif dias=="2":
                if martes_1=="":
                    martes_1 =(input ("Ingrese su nombre para ser registrado: "))
                    print ("Turno Agendado con exito!")
                elif martes_2=="":
                    martes_2= (input ("Ingrese su nombre para ser registrado: "))
                    print ("Turno Agendado con exito!")
                elif martes_3=="":
                    martes_3= (input ("Ingrese su nombre para ser registrado: "))
                    print ("Turno Agendado con exito!")
                else:
                    print ("No hay mas turnos, lo sentimos!")
    elif menu== "2":
        nombre=""
        while nombre=="":
            nombre= input("Si usted quiere cancelar su turno, escriba su nombre y este se le cancelara: ")
        if nombre== lunes_1:
                lunes_1=""
                print ("Su cancelacion fue exitosa")
        elif nombre==lunes_2:
                lunes_2=""
                print ("Su cancelacion fue exitosa")
        elif nombre==lunes_3:
                lunes_3=""
                print ("Su cancelacion fue exitosa")
        elif nombre==lunes_4:
                lunes_4=""
                print ("Su cancelacion fue exitosa")
        elif nombre==martes_1:
                martes_1=""
                print ("Su cancelacion fue exitosa")
        elif nombre==martes_2:
                martes_2=""
                print ("Su cancelacion fue exitosa")
        elif nombre==martes_3:
                martes_3=""
                print ("Su cancelacion fue exitosa")
        else:
            print("No se encontró ninguna reserva a nombre de:", nombre)

    elif menu == "3":
        print ("Si quiere ver la agenda, elija su dia 1- Lunes y 2- Martes")
        que_dia=""
        while not que_dia.isdigit() or int (que_dia)<1 or int (que_dia)>2:
            que_dia= input("Ingrese el dia, 1(Lunes) o 2(Martes): ")
        if que_dia=="1":
            print ("Lunes")
            if lunes_1 =="":
                print ("Libre") 
            else:
                print  ("Ocupado por", lunes_1)
            if lunes_2 =="":
                print ("Libre")
            else: 
                print  ("Ocupado por", lunes_2)
            if lunes_3 =="":
                print ("Libre")
            else: lunes_3 !=""
            print  ("Ocupado por", lunes_3)
            if lunes_4 =="":
                print ("Libre")
            else: lunes_4 !=""
            print  ("Ocupado por", lunes_4)
        elif que_dia==2:
            print ("Martes")
            if martes_1 =="":
                print ("Libre") 
            else:
                print  ("Ocupado por", martes_1)
            if martes_2 =="":
                print ("Libre")
            else:
                print  ("Ocupado por", martes_2)
            if martes_3 =="":
                print ("Libre")
            else: martes_3 !=""
            print  ("Ocupado por", martes_3)
    elif menu=="4":
        total_lunes=0
        total_martes=0
    if lunes_1 != "": total_lunes += 1
    if lunes_2 != "": total_lunes += 1
    if lunes_3 != "": total_lunes += 1
    if lunes_4 != "": total_lunes += 1

    if martes_1 != "": total_martes += 1
    if martes_2 != "": total_martes += 1
    if martes_3 != "": total_martes += 1
    print(f"Lunes: {total_lunes} ocupados / {4 - total_lunes} disponibles.")
    print(f"Martes: {total_martes} ocupados / {3 - total_martes} disponibles.")
    print("-" * 30)
    if total_lunes > total_martes:
        print("El día con más demanda es el LUNES.")
    elif total_martes > total_lunes:
        print("El día con más demanda es el MARTES.")
    else:
        if total_lunes == 0:
            print("Todavía no hay turnos agendados en ningún día.")
        else:
            print("Hay un EMPATE en la cantidad de turnos entre ambos días.")
    if menu=="5":
        salir= True

#Ejercicio 4#
energia = 100 
tiempo = 12 
cerraduras_abiertas = 0 
alarma = False 
codigo_parcial = ""
numero=""
forzar_seguidas=0
elige_numeero=""
nro=""

nombre= input ("Ingrese su nombre: ")
while not nombre.isalpha():
    nombre= input("Ingrese su nombre: ")
while cerraduras_abiertas < 3 and tiempo > 0 and energia > 0 and not (alarma == True and tiempo <= 3):
        print (f"LLevas una energia de {energia}, un tiempo de {tiempo}, y llevas abiertas {cerraduras_abiertas} cerraduras.") 
        print ("Elija una accion a segun cual eliga presione 1, 2 o 3")
        numero=""
        while not numero.isdigit() or int (numero)<0 or int (numero) > 3:
            numero= input ("Ingrese el numero:")
        if numero=="1": 
            print ("Usted eligio forzar cerradura")
            tiempo-=2
            energia-=20
            forzar_seguidas += 1
            

            if forzar_seguidas == 3:
                alarma=True
                energia-=20
                tiempo-=2
                print ("Se trabo la cerradura")
            else:
                if energia<40:
                    nro=""
                    while not nro.isdigit() or int(nro) < 1 or int(nro) > 3:
                        nro = input ("Ingrese un numero del 1 al 3: ")
                    if nro =="3":
                        alarma=True
                        print ("La alarma se activo")
                    elif nro =="2" or nro=="1":
                        cerraduras_abiertas+=1
                        print ("Felicidades +1 cerradura")
                else:
                    cerraduras_abiertas+=1
                    print ("Felicidad +1 cerradura")

        elif numero=="2":
            energia -=10
            tiempo -=3
            paso=0
            forzar_seguidas=0

            for paso in range (4):
                codigo_parcial += "A"
                print (codigo_parcial)

            if len (codigo_parcial) >= 8:
                cerraduras_abiertas+=1
                codigo_parcial=""
                print ("Felicidades +1 cerradura")

        elif numero =="3":
            energia+= 15
            if energia>100:
                print ("No puedes tener mas de 100 puntos")
                energia=100
            tiempo-=1
            forzar_seguidas=0
            if alarma==True:
                energia-=10
if cerraduras_abiertas==3:
    print ("Felicitaciones abriste las 3 cerraduras")
elif alarma==True and tiempo<=3:
    print ("Derrota, usted perdio debido a que el sistema se bloqueo por alarma")
elif energia<=0:
    print ("Derrota, se quedo sin energia")
else:
    print ("Derrota, Se terminó el tiempo.")

#Ejercicio 5#
print ("----Bienvenido a la Arena----")
while True:
    nombre = input("Ingrese el nombre de su gladiador: ")
    if nombre.isalpha():
        print(f"{nombre} Su nombre es Valido")
        break
    else:
        print("¡Error, solo Letras! Por favor, ingrese un nombre válido.")
vida=int (100)
pociones=int (3)
vida_enemigo=int (100)
daño_base=int (15)
daño_base_enemigo=int (12)
turno_gladiador= True
Rafaga_veloz= int (5)
print (f"Tu salud actual es {vida} y la del duende es de {vida_enemigo} y tenes una cantidad de 2 ataques optandote por Ataque Pesado, y Rafaga Veloz, tambien contando con un total de {pociones} pociones")
while vida > 0 and vida_enemigo > 0:
    while True:
        opciones = input("Cual eliges 1, 2 o 3: ")
        if opciones.isdigit():
            ataque = int(opciones)
            if 1 <= ataque <= 3:
                break
            else:
                print("Debe ser un numero del 1 al 3")
        else:
            print("Solamente se aceptan numeros")
    if ataque==1:
        vida_enemigo=vida_enemigo - daño_base
        print (f"Usas Ataque Pesado, le quitas 15 de vida al duende, esto lo deja con {vida_enemigo}")
    elif ataque==2:
        for ataque in range (1,4):
            vida_enemigo=vida_enemigo - Rafaga_veloz
        print(f"Usas Rafaga veloz, le quitas 15 puntos de daño al duende, esto lo deja con {vida_enemigo}")
    elif ataque==3:
        if pociones>0:
            pociones-=1
            vida+= 35
            print (f"Usas 1 de tus, esto te deja con {pociones} pociones curandote asi un 30hp dejandote un total de {vida}hp")
        else:
            print ("Te haz quedado sin pociones")
    turno_gladiador= not turno_gladiador
    vida= vida-daño_base_enemigo
    print (f"El duende te ataca, dejandote en un total de {vida}")
    turno_gladiador= turno_gladiador
    if ataque==1:
        if vida_enemigo<=20: 
            daño_base=15 + 1*3
            vida_enemigo-=daño_base
            print (f"Haz Realizado un golpe critico, provocando que el duende quede con {vida_enemigo} de hp, a este lo atacaste por la cantidad de {daño_base} puntos de daño")
    if vida_enemigo<=0:
        print (f"Felicitaciones {nombre} Haz Ganado")
        break
    if vida<=0:
        print ("Haz sido derrotado, suerte para la proxima")
        break