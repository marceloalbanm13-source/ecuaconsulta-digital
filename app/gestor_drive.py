from pathlib import Path


EMPRESA = "ECUACONSULTA DIGITAL"

CARPETAS = [
    "00. FUNDACIÓN",
    "01. MARCA",
    "02. SERVICIOS",
    "03. MÉTODO ECUACONSULTA",
    "04. OPERACIÓN",
    "05. SISTEMA COMERCIAL",
    "06. MARKETING",
    "07. PORTAFOLIO",
    "08. DOCUMENTOS COMERCIALES",
    "09. FINANZAS",
    "10. CLIENTES",
    "11. RECURSOS",
    "12. APRENDIZAJE",
    "13. PLAN ESTRATÉGICO",
    "14. REUNIONES",
    "99. ARCHIVO",
]


class GestorDrive:

    def __init__(self):
        self.raiz = Path("G:/Mi unidad") / EMPRESA

    def crear_estructura(self):

        print()
        print("=" * 60)
        print("ED-OS - Gestor de Google Drive")
        print("=" * 60)
        print()

        # Crear carpeta principal
        self.raiz.mkdir(parents=True, exist_ok=True)

        # Crear carpetas internas
        for carpeta in CARPETAS:

            ruta = self.raiz / carpeta
            ruta.mkdir(exist_ok=True)

            print(f"✓ {carpeta}")

        print()
        print("=" * 60)
        print("Estructura creada correctamente.")
        print(self.raiz)
        print("=" * 60)