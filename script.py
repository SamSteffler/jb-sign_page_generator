import sys
import csv
from PIL import Image, ImageDraw, ImageFont

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

  sign = Image.new('RGB', (2350, 1500), color = (0, 99, 0))
  draw = ImageDraw.Draw(sign)
  draw.rectangle([50, 50, 2300, 1450], fill=(0, 99, 0), outline=(255, 255, 255), width=50)
  sign.show()
  sign.save('sign.png')

  file.close()

if __name__ == "__main__":
  main()