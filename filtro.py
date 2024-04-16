
import sys

def filtrar_productos(precios, umbral, operacion="mayor"):
    productos_filtrados = {}
    for productos, precio in precios.items():
        if (operacion == "mayor" and precio > umbral) or (operacion == "menor" and precio < umbral):
            productos_filtrados [productos] = precio
    return productos_filtrados

def main():
    precios = {
        'Notebook': 700000,
        'Teclado': 25000,
        'Mouse': 12000,
        'Monitor': 250000,
        'Escritorio': 135000,
        'Tarjeta de Video': 1500000
    }

    if len(sys.argv) < 2:
        print("Usar: python filtro.py <umbral> [mayor/menor]")
        sys.exit(1)

    umbral = float(sys.argv[1])
    operacion = sys.argv[2] if len(sys.argv) > 2 else "mayor"

    if operacion not in ["mayor", "menor"]:
        print("Lo sentimos, no es una operación válida")
        sys.exit(1)

    productos_filtrados = filtrar_productos(precios, umbral, operacion)

    print(f"Los productos {operacion} al umbral son: {', '.join(productos_filtrados.keys())}")

if __name__ == "__main__":
    main()
