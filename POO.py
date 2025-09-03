import yaml

class Pregunta:
    def __init__(self, title, prompt, hints, tags):
        self.title = title
        self.prompt = prompt
        self.hints = hints
        self.tags = tags

    def to_dict(self):
        return {
            "title": self.title,
            "prompt": self.prompt,
            "hints": self.hints,
            "tags": self.tags
        }

def cargar_preguntas_poo(archivo="problems.yaml"):
    preguntas_iniciales = [
        Pregunta("Imprimir Hola Mundo", "Escribe un programa que imprima 'Hola, mundo'.", ["Usa print()", "Solo imprime el texto"], ["salida", "básico"]),
        Pregunta("Saludo con nombre", "Escribe un programa que pida tu nombre y lo muestre en un saludo.", ["Usa input()", "Concatena con print()"], ["entrada", "strings"]),
        Pregunta("Suma de dos números", "Escribe un programa que sume dos números ingresados por el usuario.", ["Usa input()", "Convierte a int()", "Usa +"], ["aritmética", "entrada"]),
        Pregunta("Área de un triángulo", "Escribe un programa que calcule el área de un triángulo (base * altura / 2).", ["Solicita base y altura", "Haz la operación matemática"], ["aritmética", "fórmulas"]),
        Pregunta("Número par o impar", "Escribe un programa que determine si un número es par o impar.", ["Usa el operador %", "Compara con == 0"], ["condicionales", "aritmética"]),
        Pregunta("Tabla de multiplicar", "Escribe un programa que muestre la tabla de multiplicar de un número.", ["Usa un bucle for", "Multiplica en cada iteración"], ["bucles", "aritmética"]),
        Pregunta("Mayor de tres números", "Escribe un programa que encuentre el mayor de tres números.", ["Usa if/else", "Compara entre ellos"], ["condicionales", "comparaciones"]),
        Pregunta("Invertir cadena", "Escribe un programa que invierta una cadena de texto.", ["Usa slicing con ::-1", "También puedes usar reversed()"], ["strings", "funciones"]),
        Pregunta("Contar vocales", "Escribe un programa que cuente cuántas vocales tiene una palabra.", ["Recorre la cadena", "Compara con a,e,i,o,u"], ["strings", "bucles"]),
        Pregunta("Serie Fibonacci", "Escribe un programa que genere los primeros 10 números de la serie Fibonacci.", ["Comienza con 0 y 1", "Usa un bucle para generar el resto"], ["bucles", "aritmética"]),
    ]

    try:
        with open(archivo, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
            if data is None:
                data = []
    except FileNotFoundError:
        data = []

    for p in preguntas_iniciales:
        data.append(p.to_dict())

    with open(archivo, "w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True)

    print(f"✅ Se cargaron {len(preguntas_iniciales)} preguntas en {archivo}")

if __name__ == "__main__":
    cargar_preguntas_poo()
