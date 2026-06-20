# Gestión de Vacaciones Automatizada - Asistente Virtual
### Trabajo Práctico Integrador | Organización Empresarial
**Tecnicatura Universitaria en Programación - UTN**

---

## Integrantes y Cátedra
* **Estudiante:** Matías Rosas Castaño
* **Profesora Titular:** Prof. Gabriela Martínez
* **Profesores Adjuntos:** Prof. Carolina Bruno, Prof. Mario Raúl López, Prof. Andrea Ramos

---

## Descripción del Proyecto
Este proyecto resuelve la automatización del proceso de solicitud de vacaciones de una organización mediante la implementación de un bot por consola en Python. El diseño unifica el modelado del negocio (BPMN 2.0) con software dinámico que simula la interacción real del área de Recursos Humanos.

### Aspectos Técnicos Destacados
1. **Máquina de Estados Finitos:** El flujo del bot avanza de manera controlada según el contexto de la conversación (Estado 0: Identificación, Estado 1: Solicitud de días, Estado 2: Validación de fecha, Estado 3: Procesamiento y fin).
2. **Persistencia Simulada:** Los saldos de días se consultan y modifican en tiempo real sobre un diccionario que actúa como base de datos en memoria.
3. **Manejo del Camino Infeliz (Unhappy Path):** Se validan de forma estricta todos los ingresos erróneos del usuario (letras en campos numéricos, días insuficientes o formatos de fecha incorrectos).
4. **Lógica Condicional Pura:** En cumplimiento con las pautas de diseño fijadas, **no se utilizan bloques try/except** en el script; la totalidad de las excepciones y el control de errores se resuelven mediante condicionales estructurados nativos.

---

## Guía de Uso
1. Ejecutar el archivo `TPI-Oe-Rosas.py`.
2. Ingresar un legajo válido de prueba (ej. `1001`, `1002`, `1003`).
3. Declarar la cantidad de días deseados.
4. Definir la fecha de inicio en formato `DD/MM/AAAA`.
*Nota: Tipeando la palabra `salir` en cualquier momento se interrumpe la sesión de forma segura sin guardar cambios.*