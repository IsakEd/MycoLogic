import json
import requests

f = open("secrets.json", "r")
secrets = json.load(f)


class CopernicusInstance:

  def __init__(self) -> None:
    self.access_token = self.get_access_token(secrets["copernicus_authentication"]["username"], secrets["copernicus_authentication"]["password"])

  def get_access_token(self, username: str, password: str) -> str:
    data = {
    "client_id": "cdse-public",
    "username": username,
    "password": password,
    "grant_type": "password",
    }
    try:
      r = requests.post("https://identity.dataspace.copernicus.eu/auth/realms/CDSE/protocol/openid-connect/token",
      data=data,
    )
      r.raise_for_status()
    except Exception as e:
      raise Exception(
        f"Access token creation failed. Reponse from the server was: {r.json()}"
      )
    return r.json()["access_token"]

  def screenshot(latitude, longitude, date, bands) -> None:
    pass

instance = CopernicusInstance()
print(instance.access_token)