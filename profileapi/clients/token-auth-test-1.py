import requests

def client():
  credentials = {"username": "testuser", "password": "Abcd@1234"}

  response = requests.post("http://127.0.0.1:8000/api/rest-auth/login/",
                             data=credentials)    
  response_data = response.json()

if __name__ == "__main__":
  client()
