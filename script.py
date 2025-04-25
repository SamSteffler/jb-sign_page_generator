import sys
import csv
import page_generator as page_gen
import sign_generator as sign_gen

def main():
  if len(sys.argv) != 2:
    print("Uso: python script.py <arquivo.csv>")
    sys.exit(0)

  input_file = sys.argv[1]

  try:
    file = open(input_file, mode='r', encoding='utf-8')
    if file:
      print("Arquivo aberto com sucesso.")
  except FileNotFoundError:
    print(f"Erro: Arquivo '{input_file}' nao encontrado.")
  except Exception as e:
    print(f"Um erro ocorreu: {e}")

  reader = csv.reader(file, delimiter=',')
  for row in reader:
    print(row)
    code = row[0]
    sciname = row[1]
    commonname = row[2]

    sign_gen.signGenerate(code, sciname, commonname)

  file.close()

if __name__ == "__main__":
  main()