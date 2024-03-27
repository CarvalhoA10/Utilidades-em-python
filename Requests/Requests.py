import requests

# Metodo Get
r = requests.get('http://127.0.0.1:8000/user')

# Requisição com o metodo Post
data = {
    'username': 'joao',
    'email': 'joao@email.com'
}

r = requests.post("http://127.0.0.1:8000/user", data= data)

# Requisição com o metodo Post, header e token de autenticação
data = {
    'username': 'joao',
    'email': 'joao@email.com'
}

r = requests.post("http://127.0.0.1:8000/user", data= data, headers= {"Authorization": "Bearer token"})

