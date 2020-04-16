import requests

def client():
  token_h = "Token 7799c4df127d397049350c2f81c3c114c1e82979"
  # credentials = {"username": "testuser", "password": "Abcd@1234"}


  # response = requests.post("http://127.0.0.1:8000/api/rest-auth/login/",
  #                            data=credentials)   
  headers = {"Authorization": token_h}
  print(headers)
  response = requests.get("http://127.0.0.1:8000/api/profiles/", headers=headers)
  response_data = response.json()
  print(response_data)

if __name__ == "__main__":
  client()
