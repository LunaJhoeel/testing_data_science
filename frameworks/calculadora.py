import argparse

def suma(a, b):
    return a + b

def division(a, b):
    if b == 0:
        raise ValueError("no se puede dividir entre cero")
    return a / b

def main():
    parser = argparse.ArgumentParser(description="calculadora simple")
    parser.add_argument("operacion", choices=["suma", "division"], help="operación a realizar")
    parser.add_argument("numero1", type=float, help="primer número")
    parser.add_argument("numero2", type=float, help="segundo número")
    
    args = parser.parse_args()
    
    if args.operacion == "suma":
        resultado = suma(args.numero1, args.numero2)
    elif args.operacion == "division":
        resultado = division(args.numero1, args.numero2)
    
    print("resultado:", resultado)

if __name__ == "__main__":
    main()
