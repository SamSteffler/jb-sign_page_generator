from PIL import Image, ImageDraw, ImageFont
import qrcode

def signGenerate(code, sciname, commonname):
  
  # criacao da placa com fundo, adaptar futuramente args para receber cor de fundo e cor de contorno
  sign = Image.new('RGB', (2350, 1500), color = (0, 99, 0)) # verde escuro
  draw = ImageDraw.Draw(sign)
  draw.rectangle([50, 50, 2300, 1450], fill=(0, 99, 0), outline=(255, 255, 255), width=50)

  # criacao do QR code


  # insercao dos icones do JB e UFSM


  # escrita do nome cientifico e nome comum


  # mostra placa no visualizador de fotos
  sign.show()
  # salva placa com o nome do codigo
  sign.save(f'{code}.png')
