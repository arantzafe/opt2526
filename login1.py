import re

"""
Sistema de registro e inicio de sesión

Este programa permite registrar usuarios con contraseña segura y luego iniciar sesión.
Se almacena la información en un diccionario {email: contraseña}.
El programa valida la seguridad de las contraseñas y limita los intentos de inicio de sesión.
"""

# Diccionario para almacenar usuarios
usuarios = {}

# Función para validar contraseña segura
def validar_contraseña(contraseña):
    """
    Regresa True si la contraseña cumple con los requisitos:
    - Al menos 8 caracteres
    - Al menos una mayúscula
    - Al menos un número
    - Al menos un símbolo especial
    """
    if len(contraseña) < 8:
        print("❌ La contraseña debe tener al menos 8 caracteres.")
        return False
    if not re.search(r"[A-Z]", contraseña):
        print("❌ La contraseña debe contener al menos una letra mayúscula.")
        return False
    if not re.search(r"[0-9]", contraseña):
        print("❌ La contraseña debe contener al menos un número.")
        return False
    if not re.search(r"[!@#$%&*?]", contraseña):
        print("❌ La contraseña debe contener al menos un símbolo especial (!@#$%&*?).")
        return False
    return True

# Función para registrar un nuevo usuario
def registrarse():
    email = input("Introduce tu email: ").strip()
    if email in usuarios:
        print("⚠️ Este usuario ya existe.")
        return
    while True:
        contraseña = input("Crea una contraseña segura: ").strip()
        if validar_contraseña(contraseña):
            usuarios[email] = contraseña
            print("✅ Registro exitoso.\n")
            break

# Función para iniciar sesión
def iniciar_sesion():
    email = input("Introduce tu email: ").strip()
    if email not in usuarios:
        print("⛔ Usuario no encontrado.\n")
        return
    intentos = 0
    while intentos < 3:
        contraseña = input("Introduce tu contraseña: ").strip()
        if contraseña == usuarios[email]:
            print("✅ Acceso concedido.\n")
            return
        else:
            intentos += 1
            print(f"⛔ Contraseña incorrecta. Intento {intentos}/3")
    print("🚫 Demasiados intentos fallidos. Regresando al menú principal.\n")

# Programa principal
def menu_principal():
    while True:
        print("=== MENÚ PRINCIPAL ===")
        print("[1] Registrarse")
        print("[2] Iniciar sesión")
        print("[3] Salir")
        opcion = input("Elige una opción: ").strip()
        if opcion == "1":
            registrarse()
        elif opcion == "2":
            iniciar_sesion()
        elif opcion == "3":
            print("👋 Programa finalizado.")
            break
        else:
            print("⚠️ Opción no válida. Intenta de nuevo.\n")

# Ejecutar programa
menu_principal()
