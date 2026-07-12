from pathlib import Path


def crear_estructura(ruta, estructura):
    for nombre, contenido in estructura.items():

        carpeta = Path(ruta) / nombre

        carpeta.mkdir(parents=True, exist_ok=True)

        print(f"📁 {carpeta}")

        if isinstance(contenido, dict):
            crear_estructura(carpeta, contenido)