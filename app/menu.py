from pathlib import Path

from estructuras.hogar import HOGAR
from core.crear_estructura import crear_estructura


ANCHO = 60


def linea():
    print("=" * ANCHO)


def titulo():
    print()
    linea()
    print("                 ORDEN Y CONTROL")
    print("            Sistema Inteligente")
    linea()


def instalar_hogar():

    print("\n🏠 Instalando Sistema Hogar...\n")

    # Ruta donde se creará el sistema
    destino = Path(r"G:\Mi unidad\ORDEN Y CONTROL")

    crear_estructura(destino, HOGAR)

    print("\n✅ Instalación finalizada correctamente.")


def iniciar():

    while True:

        titulo()

        print("1. 🏠 Sistema Hogar")
        print("2. 🏢 Sistema Empresa")
        print("3. 🎵 Biblioteca Musical")
        print("4. 📷 Fotografías")
        print("5. ☁ Google Drive")
        print("6. ⚙ Configuración")
        print("0. ❌ Salir")

        linea()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":

            instalar_hogar()

        elif opcion == "2":

            print("\n🚧 Módulo en desarrollo.")

        elif opcion == "3":

            print("\n🚧 Módulo en desarrollo.")

        elif opcion == "4":

            print("\n🚧 Módulo en desarrollo.")

        elif opcion == "5":

            print("\n🚧 Módulo en desarrollo.")

        elif opcion == "6":

            print("\n🚧 Módulo en desarrollo.")

        elif opcion == "0":

            print("\n👋 Gracias por usar Orden y Control.")
            break

        else:

            print("\n❌ Opción no válida.")