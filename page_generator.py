import html

def pageGenerate(argslist):
    code = argslist[0]
    sciname = argslist[1]
    commonname = argslist[2]
    latitude = argslist[3]
    longitude = argslist[4]
    origin = argslist[5]
    type = argslist[6]
    description = argslist[7]
    image = argslist[8]
    
    # criar html modelo da pagina
    html_template = """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Placa de Identificação</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 20px;
                background-color: #f4f4f4;
            }}
            .container {{
                max-width: 800px;
                margin: auto;
                background: white;
                padding: 20px;
                border-radius: 5px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }}
            h1 {{
                text-align: center;
            }}
            img {{
                max-width: 100%;
                height: auto;
                margin-bottom: 10px;
            }}
            .info {{
                margin-top: 20px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Informações da planta</h1>
            {images}
            <div class="info">
                <h2>{sciname}</h2>
                <p><strong>Nome Comum:</strong> {commonname}</p>
                <p><strong>Código:</strong> {code}</p>
                <p><strong>Latitude:</strong> {latitude}</p>
                <p><strong>Longitude:</strong> {longitude}</p>
                <p><strong>Origem:</strong> {origin}</p>
                <p><strong>Tipo:</strong> {type}</p>
                <p><strong>Descrição:</strong></p>
                <p>{description}</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    # Generate multiple <img> tags if needed
    image_list = image.split(';')  # Assuming images are separated by semicolons
    images = ''.join(f'<img src="images/{code}-{i+1}.png" alt="{html.escape(commonname)}" style="height: 400px; width: auto;">' for i in range(len(image_list)))
    # criar html com os dados
    html_content = html_template.format(
        code=html.escape(code),
        sciname=html.escape(sciname),
        commonname=html.escape(commonname),
        latitude=html.escape(latitude),
        longitude=html.escape(longitude),
        origin=html.escape(origin),
        type=html.escape(type),
        description=html.escape(description),
        images=images  # ← do NOT escape this
    )
    # salvar html em arquivo
    with open(f'output/{code}.html', 'w', encoding='utf-8') as file:
        file.write(html_content)
    print(f"Arquivo HTML '{code}.html' gerado com sucesso.")
    # abrir html no navegador
    import webbrowser
    webbrowser.open(f'file://{code}.html')


def CSVtoJSON(csv_file):
    import csv
    import json
    data = []
    args = ["code", "sciname", "commonname", "latitude", "longitude", "origin", "type", "description", "image"]
    # Lê o arquivo CSV e converte para JSON
    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            # Cria um dicionário para cada linha do CSV
            entry = {args[i]: row[i] for i in range(len(args))}
            # Adiciona o dicionário à lista de dados
            data.append(entry)
    json_file = f'output/{csv_file.split(".")[0]}.json'
    json_vue = f'vue_jb_static_pages/public/data/{csv_file.split(".")[0]}.json'
    # Salva o JSON em um arquivo
    with open(json_file, mode='w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    with open(json_vue, mode='w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    print(f"Arquivos JSON '{json_file}' e '{json_vue}' gerados com sucesso.")