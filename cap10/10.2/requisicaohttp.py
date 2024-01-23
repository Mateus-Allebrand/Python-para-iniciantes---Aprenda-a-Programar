

import requests

# URL da API JSONPlaceholder para obter posts de usuários
url = "https://jsonplaceholder.typicode.com/posts"

try:
    # Faz uma requisição GET à API
    response = requests.get(url)

    # Verifica se a requisição foi bem-sucedida (código de status 200)
    if response.status_code == 200:
        # Converte a resposta JSON para um formato Python (lista de dicionários)
        posts = response.json()

        # Exibe os títulos dos primeiros 5 posts
        for post in posts[:5]:
            print(f"ID: {post['id']}, Título: {post['title']}")
    else:
        # Se a requisição não foi bem-sucedida, exibe o código de status
        print(f"Erro na requisição. Código de status: {response.status_code}")

except requests.RequestException as e:
    # Captura exceções relacionadas a requisições
    print(f"Erro na requisição: {e}")

