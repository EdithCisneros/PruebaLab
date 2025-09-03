import yaml

def generar_preguntas():
    return [
        {
            "title": "Función pura suma",
            "prompt": "Escribe una función pura `suma(a, b)` que devuelva a + b.",
            "hints": ["No uses variables globales", "Devuelve el resultado directamente"],
            "tags": ["funciones", "aritmética"]
        },
        {
            "title": "Filtrar pares",
            "prompt": "Crea una función que reciba una lista y devuelva solo los números pares.",
            "hints": ["Usa filter()", "Comprueba con % 2 == 0"],
            "tags": ["funciones", "listas"]
        },
        {
            "title": "Elevar al cuadrado",
            "prompt": "Implementa una función que use map() para elevar al cuadrado cada número en una lista.",
            "hints": ["Usa map()", "Lambda puede ser útil"],
            "tags": ["funciones", "map"]
        },
        {
            "title": "Filtrar impares",
            "prompt": "Usa filter() para obtener los números impares de una lista.",
            "hints": ["Usa % 2 != 0", "Devuelve el resultado como lista"],
            "tags": ["funciones", "filter"]
        },
        {
            "title": "Reduce producto",
            "prompt": "Crea una función que use reduce() para calcular el producto de una lista de números.",
            "hints": ["Importa reduce de functools", "Multiplica en cada paso"],
            "tags": ["funciones", "reduce"]
        },
        {
            "title": "Factorial recursivo",
            "prompt": "Implementa una función recursiva que calcule el factorial de un número.",
            "hints": ["Caso base: factorial(0) = 1", "Llamada recursiva"],
            "tags": ["funciones", "recursividad"]
        },
        {
            "title": "Strings a mayúsculas",
            "prompt": "Escribe una función que convierta todos los strings de una lista a mayúsculas usando map().",
            "hints": ["Usa str.upper()", "Devuelve lista"],
            "tags": ["funciones", "strings"]
        },
        {
            "title": "Ordenar tuplas",
            "prompt": "Usa lambda para ordenar una lista de tuplas por el segundo elemento.",
            "hints": ["Usa sorted()", "Lambda con índice 1"],
            "tags": ["funciones", "lambda"]
        },
        {
            "title": "Elementos únicos",
            "prompt": "Crea una función que cuente cuántos elementos únicos hay en una lista.",
            "hints": ["Convierte a set", "Usa len()"],
            "tags": ["funciones", "sets"]
        },
        {
            "title": "Combinar listas",
            "prompt": "Implementa una función que combine dos listas en un diccionario usando zip().",
            "hints": ["Usa dict(zip(lista1, lista2))", "Devuelve el diccionario"],
            "tags": ["funciones", "diccionarios"]
        },
    ]

def cargar_preguntas(archivo="problems.yaml"):
    preguntas = generar_preguntas()

    try:
        with open(archivo, "r") as f:
            data = yaml.safe_load(f)
            if data is None:
                data = []
    except FileNotFoundError:
        data = []

    data.extend(preguntas)

    with open(archivo, "w") as f:
        yaml.dump(data, f, allow_unicode=True)

    print(f"✅ Se cargaron {len(preguntas)} preguntas en {archivo}")

if __name__ == "__main__":
    cargar_preguntas()
