import requests
import json

url = "http://localhost:8081/users"

payload = json.dumps({
  "ime": "Milos",
  "prezime": "Vukadinovic",
  "smer": "IT",
  "predmeti": [
    {
      "ime": "RISO",
      "espb": 6
    },
    {
      "ime": "MTZPP",
      "espb": 8
    }
  ]
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)