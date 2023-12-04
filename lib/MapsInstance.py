import json
import requests
api_key = json.load(open("secrets.json", "r"))["google_maps_key"]

class MapsInstance:

  maptype = "satellite"
  zoom = 20
  size = "640x640"
  scale = 1
  format = "png"
  key = api_key



  def snapshot(self, latitude: float, longitude: float, class_name: str):
      url = f"https://maps.googleapis.com/maps/api/staticmap?center={latitude},{longitude}&zoom={self.zoom}&size={self.size}&scale={self.scale}&maptype={self.maptype}&format={self.format}&key={self.key}"
      res = requests.get(url)

      if res.status_code == 200:
          self.write_image(res, latitude, longitude, class_name)
      else:
          return f"Error: {res.status_code} - {res.text}"
      
  def write_image(self, res, latitude: float, longitude: float, class_name: str):
      lat, lon = str(latitude).replace(".", "_"), str(longitude).replace(".", "_")
      fname = f"lat{lat}_lon{lon}.png"
      with open(f"images/{class_name}/{fname}", "wb") as f:
          f.write(res.content)
      return "Image saved successfully"
    

""" if __name__ == "__main__":
  instance = MapsInstance()
  destination = "images"
  fig = instance.snapshot(58.26016, 12.54354, "semilanceata")
 """