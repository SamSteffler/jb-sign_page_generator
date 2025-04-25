import sys
import csv

def main():
  if len(sys.argv) != 2:
    print("Uso: python script.py <arquivo.csv>")
    sys.exit(1)

  input_file = sys.argv[1]

  try:
    file = open(input_file, mode='r', encoding='utf-8')
    if file:
      print("Arquivo aberto com sucesso.")
  except FileNotFoundError:
    print(f"Erro: Arquivo '{input_file}' nao encontrado.")
  except Exception as e:
    print(f"Um erro ocorreu: {e}")

if __name__ == "__main__":
  main()