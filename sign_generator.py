from PIL import Image, ImageDraw, ImageFont
import qrcode

def signGenerate(code, sciname, commonname):

  # criacao da placa com fundo, adaptar futuramente args para receber cor de fundo e cor de contorno
  sign = Image.new('RGB', (2350, 1500), color = (0, 99, 0)) # verde escuro
  draw = ImageDraw.Draw(sign)
  draw.rectangle([50, 50, 2300, 1450], fill=(0, 99, 0), outline=(255, 255, 255), width=50)

  # criacao do QR code
  qrstring = f'http://www.jardimbotanico.ufsm.br/plantas/{code}'
  qr = qrcode.QRCode(
      version=1,
      error_correction=qrcode.constants.ERROR_CORRECT_L,
      box_size=10,
      border=0,
  )
  qr.add_data(qrstring)
  qr.make(fit=True)
  qr_img = qr.make_image(fill_color=(255, 255, 255), back_color=(0, 99, 0)).convert("RGBA")
  qr_img = qr_img.resize((800, 800), Image.Resampling.LANCZOS) # redimensiona o QR code para 800x800 pixels
  # insercao dos icones do JB e UFSM
  icon_jb = Image.open('src/jb_icon.png')
  icon_ufsm = Image.open('src/ufsm_icon.png')
  icon_jb = icon_jb.resize((500, 500), Image.Resampling.LANCZOS) # redimensiona o icone do JB para 500x500 pixels
  icon_ufsm = icon_ufsm.resize((500, 500), Image.Resampling.LANCZOS) # redimensiona o icone do UFSM para 500x500 pixels
  sign.paste(icon_jb, (200, 750), icon_jb)
  sign.paste(icon_ufsm, (750, 750), icon_ufsm)
  sign.paste(qr_img, (1350, 500), qr_img)

  # escrita do nome cientifico e nome comum
  title_font = ImageFont.truetype('src/GOTHICB.ttf', min(192, 192 * (17 / len(commonname)))) # fonte para o nome comum
  subtitle_font = ImageFont.truetype('src/GOTHICI.ttf', min(96, 96 * (27 / len(sciname)))) # fonte para o nome cientifico
  code_font = ImageFont.truetype('src/GOTHIC.ttf', 56) # fonte para o codigo

  draw.text((150, 175), commonname, font=title_font, fill=(255, 255, 255), anchor="lt") # nome comum
  draw.text((150, 400), sciname, font=subtitle_font, fill=(255, 255, 255), anchor="lt") # nome cientifico
  draw.text((150, 550), code, font=code_font, fill=(255, 255, 255), anchor="lt") # codigo
  # mostra placa no visualizador de fotos
  sign.show()
  # salva placa com o nome do codigo
  sign.save(f'output/{code}.png')
