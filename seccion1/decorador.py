# Escriba un decorador en Python llamado tiempo_ejecucion 
# que calcule el tiempo que tarda en ejecutarse una función.
# Aplique este decorador a una función de ejemplo.
import time

def tiempo_ejecucion(funcion):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = funcion(*args, **kwargs)
        end = time.time()-t1
        return result, end
    return wrapper


@tiempo_ejecucion
def ejemplo():
    time.sleep(3)
