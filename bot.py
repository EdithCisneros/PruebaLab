import json
import os
import random
from datetime import datetime
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

# Importar las funciones de los módulos
try:
    from POO import cargar_preguntas_poo
    from Funcional import cargar_preguntas_func
except ImportError:
    print("Los módulos POO y Funcional no están disponibles")
    cargar_preguntas_poo = None
    cargar_preguntas_func = None

def cargar_preguntas():
    """Función principal que carga preguntas de ambos enfoques"""
    if cargar_preguntas_poo:
        cargar_preguntas_poo()
    else:
        print("Función POO no disponible")
    
    if cargar_preguntas_func:
        cargar_preguntas_func()
    else:
        print("Función Funcional no disponible")

def main():
    """Función principal del bot"""
    print("Bot de retos de programación")
    print("Cargando preguntas...")
    
    cargar_preguntas()
    print("Proceso completado")

if  __name__== "__main__":
    main()

