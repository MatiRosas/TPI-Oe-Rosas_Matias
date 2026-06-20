# Trabajo Práctico Integrador
# Alumno: Rosas Castaño, Matias
# Comision 15

# Base de datos simulada 
base_datos_empleados = {
    "1001": {"nombre": "Matías", "dias_disponibles": 14},
    "1002": {"nombre": "Gabriela", "dias_disponibles": 21},
    "1003": {"nombre": "Carlos", "dias_disponibles": 7}
}

solicitudes_registro = []

# Estados del BOT
# 0: Inicio / Esperando Legajo
# 1: Legajo válido / Esperando cantidad de días
# 2: Días Válidos / Esperando Fecha
# 3: Solicitud Procesada / Fin

def simular_chatbot():
    estado = 0
    legajo_actual = ""
    dias_solicitados = 0

    print("=== BOT DE GESTIÓN DE VACACIONES EN LÍNEA ===")
    print("Escriba 'salir' en cualquier momento para cancelar. \n")

    while estado != 3:
        # --- Estado 0: IDENTIFICACIÓN ---
        if estado == 0:
            entrada = input("Bot: Bienvenido. Por favor, ingrese su legajo (ej: 1001): ").strip()

            if entrada.lower() == 'salir':
                print("Bot: Sesión finalizada.")
                break

            # Camino Infeliz: Validar que sea número y exista
            if not entrada.isdigit():
                print("Bot: [ERROR] El legajo debe contener solo números. Intente de nuevo.\n")
            elif entrada not in base_datos_empleados:
                print("Bot: [ERROR] El legajo no se encuentra registrado. Intente de nuevo.\n")
            else:
                legajo_actual = entrada
                empleado = base_datos_empleados[legajo_actual]
                print(f"Bot: Hola {empleado['nombre']}. Disponés de {empleado['dias_disponibles']} días de vacaciones.")
                estado = 1 # Avanza de estado
                print("-" * 40)

        # --- Estado 1: SOLICITUD DE DIAS ---
        elif estado == 1:
            entrada = input("Bot: ¿Cuántos días deseas solicitar?: ").strip()

            if entrada.lower() == 'salir':
                print("Bot: Sesión finalizada.")
                break

            # Camino Infeliz: Validar que sea entero
            if not entrada.isdigit() or int(entrada) <= 0:
                print("Bot: [ERROR] Ingrese una cantidad válida de días (número entero mayor a 0).\n")
            else:
                dias_solicitados = int(entrada)
                saldo_actual = base_datos_empleados [legajo_actual]["dias_disponibles"]

                # Compuerta Logica 1: Tiene saldo?
                if dias_solicitados > saldo_actual:
                    print(f"Bot: [RECHAZADO] No tenés saldo suficiente. Solicitaste {dias_solicitados} pero te quedan {saldo_actual}.")
                    print("Bot: Volviendo al inicio del proceso de días.\n")
                    # Mantiene el estado 1 para que vuelva a intentar o cambie de opinion
                else:
                    estado = 2 # Avanza a la fecha
                    print("-" * 40)

        # --- Estado 2: FECHA E INTEGRACIÓN ---
        elif estado == 2:
            fecha_inicio = input("Bot: Ingrese la fecha de inicio (DD/MM/AAAA): ").strip()

            if fecha_inicio.lower() == 'salir': 
                print("Bot: Solicitud cancelada.")
                break

            # Validacion simple de formato de fecha (Camino Infeliz)
            if len(fecha_inicio) != 10 or fecha_inicio[2] != '/' or fecha_inicio[5] != '/':
                print("Bot: [ERROR] Formato de fecha inválido. Use el formato DD/MM/AAAA.\n")
            else:
                # Compuerta Logica 2: Simulacion de aprobacion de RRHH
                # Para el TPI simula una aprobacion automatica o negocio directo
                print("\nBot: Procesando con el departamento de Organización Empresarial / RRHH....")

                # Actualizo la persistencia (Base de Datos)
                base_datos_empleados[legajo_actual]["dias_disponibles"] -= dias_solicitados

                nueva_solicitud = {
                    "legajo": legajo_actual,
                    "dias": dias_solicitados,
                    "fecha": fecha_inicio,
                    "estado": "Aprobado"
                }

                solicitudes_registro.append(nueva_solicitud)

                print("Bot: ¡Solicitud APROBADA exitosamente!")
                print(f"Bot: Se han descontado {dias_solicitados} días. Tu nuevo saldo es de {base_datos_empleados[legajo_actual]['dias_disponibles']} días.")
                print(f"Bot: Comprobante de registro Nro: VAC-{100 + len(solicitudes_registro)}")

                estado = 3 # Finaliza la maquina de estados
                print("\n=== Fin del Proceso Simulado ===")

# Ejecucion del bot
simular_chatbot()