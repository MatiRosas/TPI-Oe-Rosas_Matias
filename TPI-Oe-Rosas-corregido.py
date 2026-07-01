"""
UNIVERSIDAD TECNOLÓGICA NACIONAL - Facultad Regional Rosario
Tecnicatura Universitaria en Programación
Cátedra: Organización Empresarial
Trabajo Práctico Integrador: Creación de un ChatBot
Alumno: Rosas Castaño, Matías
"""

# Persistencia simulada de datos (Estado del sistema Abierto)
base_datos_empleados = {
    "1001": {"nombre": "Matías Rosas", "saldo_vacaciones": 14},
    "1002": {"nombre": "Juan Pérez", "saldo_vacaciones": 0},  
    "1003": {"nombre": "Ana Gómez", "saldo_vacaciones": 21}
}

solicitudes_registro = []

def iniciar_chatbot():
    estado = 0
    legajo_actual = ""
    dias_solicitados = 0
    fecha_inicio = ""
    
    print("=== BOT DE GESTIÓN DE VACACIONES EN LÍNEA ===")
    print("Escriba 'salir' en cualquier momento para cancelar.\n")
    
    while estado != 3:
        # ==========================================
        # ESTADO 0: IDENTIFICACIÓN Y VALIDACIÓN DE LEGAJO
        # ==========================================
        if estado == 0:
            entrada = input("Bot: Bienvenido. Por favor, ingrese su legajo (ej: 1001): ").strip()
            
            if entrada.lower() == 'salir':
                print("Bot: Sesión cancelada por el usuario. Fin del proceso.")
                return
            
            if not entrada.isdigit():
                print("[ERROR] El legajo debe contener únicamente caracteres numéricos. Intente nuevamente.")
                continue
                
            if entrada not in base_datos_empleados:
                print(f"[ERROR] El legajo {entrada} no se encuentra registrado en el sistema.")
                continue
            
            # Legajo válido encontrado
            legajo_actual = entrada
            empleado = base_datos_empleados[legajo_actual]
            saldo_disponible = empleado["saldo_vacaciones"]
            
            print(f"Bot: Hola {empleado['nombre']}. Disponés de {saldo_disponible} días de vacaciones.")
            
            # --- NUEVA RESTRICCIÓN SOLICITADA ---
            if saldo_disponible <= 0:
                print("Bot: Al no poseer días disponibles de vacaciones, el sistema no puede procesar solicitudes.")
                print("Fin del Proceso Simulado (Cierre por saldo cero).")
                return
            
            estado = 1  # Transición al siguiente estado
            
        # ==========================================
        # ESTADO 1: SOLICITUD Y COMPROBACIÓN DE DÍAS
        # ==========================================
        elif estado == 1:
            entrada = input("Bot: ¿Cuántos días deseas solicitar?: ").strip()
            
            if entrada.lower() == 'salir':
                print("Bot: Sesión cancelada de forma segura. No se alteraron los registros.")
                return
                
            if not entrada.isdigit() or int(entrada) <= 0:
                print("[ERROR] Cantidad inválida. Debe ingresar un número entero positivo superior a 0.")
                continue
                
            dias_solicitados = int(entrada)
            saldo_real = base_datos_empleados[legajo_actual]["saldo_vacaciones"]
            
            if dias_solicitados > saldo_real:
                print(f"[ERROR] Denegación automática por saldo insuficiente (Solicitado: {dias_solicitados} | Disponible: {saldo_real}).")
                print("Bot: Retornando al paso de especificación de días.")
                continue
                
            estado = 2  # Transición aprobada por compuerta de negocio
            
        # ==========================================
        # ESTADO 2: INGRESO Y VALIDACIÓN DE FECHA (RANGOS LOGICOS)
        # ==========================================
        elif estado == 2:
            entrada = input("Bot: Ingrese la fecha de inicio (DD/MM/AAAA): ").strip()
            
            if entrada.lower() == 'salir':
                print("Bot: Sesión cancelada de forma segura. No se alteraron los registros.")
                return
                
            # Validación estricta de estructura y longitud sin librerías externas
            if len(entrada) != 10 or entrada[2] != '/' or entrada[5] != '/':
                print("[ERROR] Formato incorrecto. Asegúrese de usar barras separadoras y el formato DD/MM/AAAA.")
                continue
                
            partes = entrada.split('/')
            dia_str, mes_str, anio_str = partes[0], partes[1], partes[2]
            
            if not (dia_str.isdigit() and mes_str.isdigit() and anio_str.isdigit()):
                print("[ERROR] La fecha debe estar compuesta únicamente por números separados por barras.")
                continue
                
            dia = int(dia_str)
            mes = int(mes_str)
            anio = int(anio_str)
            
            # Validación estricta de rangos lógicos
            if mes < 1 or mes > 12:
                print("[ERROR] Mes fuera de rango lógico (Debe ser un valor entre 01 y 12).")
                continue
                
            # Determinación de días máximos del mes de forma condicional manual
            dias_maximos = 31
            if mes in [4, 6, 9, 11]:
                dias_maximos = 30
            elif mes == 2:
                # Verificación simple de año bisiesto
                if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
                    dias_maximos = 29
                else:
                    dias_maximos = 28
                    
            if dia < 1 or dia > dias_maximos:
                print(f"[ERROR] Día fuera de rango lógico para el mes seleccionado (Debe ser entre 01 y {dias_maximos}).")
                continue
                
            if anio < 2026:
                print("[ERROR] El año ingresado no puede ser anterior al período corriente operativo (2026).")
                continue
                
            # Fecha completamente validada
            fecha_inicio = entrada
            estado = 3  # Tránsito al estado de finalización
            
    # ==========================================
    # ESTADO 3: PERSISTENCIA, EMISIÓN Y CIERRE
    # ==========================================
    # Aplicación de cambios sobre la base de datos simulada
    base_datos_empleados[legajo_actual]["saldo_vacaciones"] -= dias_solicitados
    nuevo_saldo = base_datos_empleados[legajo_actual]["saldo_vacaciones"]
    
    # Consolidación histórica
    id_comprobante = f"VAC-10{len(solicitudes_registro) + 1}"
    registro_exitoso = {
        "comprobante": id_comprobante,
        "legajo": legajo_actual,
        "nombre": base_datos_empleados[legajo_actual]["nombre"],
        "dias": dias_solicitados,
        "fecha": fecha_inicio
    }
    solicitudes_registro.append(registro_exitoso)
    
    print("\nBot: Procesando con el departamento de Organización Empresarial / RRHH....")
    print("Bot: ¡Solicitud APROBADA exitosamente!")
    print(f"Bot: Se han descontado {dias_solicitados} días. Tu nuevo saldo es de {nuevo_saldo} días.")
    print(f"Bot: Comprobante de registro Nro: {id_comprobante}")
    print("\n=== Fin del Proceso Simulado ===")

if __name__ == "__main__":
    iniciar_chatbot()