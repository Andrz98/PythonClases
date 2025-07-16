class MiExcepcion(Exception):
    def __init__(self, err):
        print(f"Impresionante, cometiste el siguiente error: {err}")


try:
    raise MiExcepcion("Vaya error")
except ValueError:
    print("Como vas a cometer ese error...")
