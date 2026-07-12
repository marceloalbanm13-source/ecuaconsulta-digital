from app.gestor_drive import GestorDrive


def main():

    print()
    print("=" * 60)
    print("ECUACONSULTA DIGITAL")
    print("Sistema Operativo ED-OS")
    print("=" * 60)

    drive = GestorDrive()
    drive.crear_estructura()


if __name__ == "__main__":
    main()