import requests


class Endereco:
    def __init__(self, cep, logradouro, complemento, bairro, localidade, uf):
        self.cep = cep
        self.logradouro = logradouro
        self.complemento = complemento
        self.bairro = bairro
        self.localidade = localidade
        self.uf = uf


class CEPAdapter:
    def __init__(self):
        self.base_url = "https://viacep.com.br/ws/"

    # Função para consultar o CEP
    def get_endereco(self, cep):
        # URL da API ViaCEP
        url = f"{self.base_url}{cep}/json/"

        # Fazendo a requisição GET
        response = requests.get(url)

        # Verificando se a requisição foi bem-sucedida (código de status 200)
        if response.status_code == 200:
            # Convertendo a resposta para JSON
            dados_endereco = response.json()

            # Verificando se o CEP foi encontrado
            if "erro" in dados_endereco and dados_endereco["erro"]:
                print(f"CEP {cep} não encontrado.")
            else:
                return Endereco(cep=dados_endereco["cep"], logradouro=dados_endereco["logradouro"],
                                complemento=dados_endereco["complemento"], bairro=dados_endereco["bairro"],
                                localidade=dados_endereco["localidade"], uf=dados_endereco["uf"])

        else:
            # Se a requisição não foi bem-sucedida, imprima o código de status para depuração
            print(f"Falha na requisição. Código de status: {response.status_code}")
            print(response.text)
