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
            }}
            .info {{
                margin-top: 20px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Informações da planta</h1>
            <img src="{image}" alt="{commonname}">
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
        image=html.escape(image)
     )
    # salvar html em arquivo
    with open(f'output/{code}.html', 'w', encoding='utf-8') as file:
        file.write(html_content)
    print(f"Arquivo HTML '{code}.html' gerado com sucesso.")
    # abrir html no navegador
    import webbrowser
    webbrowser.open(f'file://{code}.html')
