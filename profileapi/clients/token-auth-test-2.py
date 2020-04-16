import requests

def client():
  # token_h = "Token 702c9b194973bb9e313703d8c14f3256e914059d"
  
  data = {
    "username": "testuser4",
    "email": "test@rest.com",
    "password1": "Abcd@1234",
    "password2": "Abcd@1234",
    }


  response = requests.post("http://127.0.0.1:8000/api/rest-auth/registration/",
                             data=data)   
  # headers = {"Authorization": token_h}
  # print(headers)
  # response = requests.get("http://127.0.0.1:8000/api/profiles/", headers=headers)
  response_data = response.json()
  print(response_data)

if __name__ == "__main__":
  client()