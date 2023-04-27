""" 
    
    Written as a little "test drive" of the two cool Python features, 
       Requests, for dealing with APIs
       Pillow, for displaying images on the laptop screen
    
    Author: KEN
    Date:   2023.04.27

 """

import requests
from PIL import Image
from io import BytesIO

url = 'https://dog.ceo/api/breeds/image/random'
response = requests.get(url)
data = response.json()

image_url = data['message']
image_response = requests.get(image_url)

if image_response.status_code == 200:
    image = Image.open(BytesIO(image_response.content))
    image.show()
else:
    print(f"Error: Unable to fetch the dog image. Status code: {image_response.status_code}")
