import requests
import flet as ft
mdsvlr = []
rot = 0
def obter_cotacoes(moedas):
    global rot
    # URL base da AwesomeAPI
    url = f"https://economia.awesomeapi.com.br/json/last/{moedas}"

    try:
        # Fazer a requisição
        response = requests.get(url)
        response.raise_for_status()  # Levanta um erro para status HTTP 4xx/5xx

        # Obter os dados em JSON
        dados = response.json()

        # Lista para armazenar os valores processados

        # Processar os pares de moedas
        for par, info in dados.items():
            moeda_base = info['code']
            moeda_destino = info['codein']
            valor = float(info['bid'])  # Garantir que é um número (float)

            # Adicionar as informações à lista
            if rot == 0:
                mdsvlr.append({
                    'nome': moeda_base,
                    'nomec': moeda_destino,
                    'valor': valor  # Garantir que 'valor' seja um número
                })
                print(f"{moeda_base}/{moeda_destino}: {valor}")
            else:
                for mdsvl in mdsvlr:
                    if mdsvl["nome"] == moeda_base:
                        mdsvl["valor"] = valor

    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a API: {e}")
    rot = 1

def main(page:ft.Page):
    page.clean()
    obter_cotacoes("USD-BRL,EUR-BRL,ARS-BRL")
    for moedas in mdsvlr:
        nome = ft.Text(moedas["nome"],size=22, weight="bold", text_align="center")
        valor = ft.Text(moedas["valor"],size=22,weight="bold", text_align="center")
        quantidade = ft.TextField(label="QUANTIDADE", width=100, text_size=22)
        resultado = ft.Text("", size=20, weight="bold", text_align="center", color="green")
        btn = ft.ElevatedButton("=", bgcolor="white", on_click= lambda e, resultado = resultado, valor=valor, quantidade=quantidade: convertertela(resultado,valor, quantidade))
        
        page.add(
            ft.Container(
                ft.Row(
                    [
                        nome,
                        valor,
                        quantidade,
                        btn,
                        resultado
                    ],
                    alignment="center",
                    vertical_alignment="center",
                ),
                bgcolor="blue",
            )
        )

    def convertertela(resultado,valor, quantidade):
        quant = int(quantidade.value)
        vlr = float(valor.value)
        conversao = quant/vlr
        resultado.value = conversao
        page.update()
        #page.add(ft.Text(conversao, size=27, weight="bold", color="green"))
    page.add(ft.ElevatedButton("ATUALIZAR", on_click=lambda e: main(page)))
    

ft.app(main)
