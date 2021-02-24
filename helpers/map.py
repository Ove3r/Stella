import requests
from helpers.player import Player
from PIL import Image, ImageDraw
from constants import constants_map
from helpers.errors import LocationError

def get_player_status_image(user, location):
    options = constants_map.LOCATIONS
    if location in options and options[location]["type"] == "standard":
        request_image = requests.get(f"https://visage.surgeplay.com/face/80/{user.uuid}.png")

        with open(f"data/head/{user.name}.png","wb") as file:
            file.write(request_image.content)

        #Opens supporting images
        head = Image.open(f"data/head/{user.name}.png")
        circle = Image.open("data/head/circle.png")
        marker = Image.open("data/maps/marker.png")

        circle_resize = circle.resize((80,80)) #Resizes bounding circle to fit the head

        #Masks the circle onto the head
        mask_im = Image.new("L", head.size, 0)
        draw = ImageDraw.Draw(mask_im)
        draw.ellipse((0, 0, 80, 80), fill=255)

        #Opens the map
        skyblock_map = Image.open("data/maps/map.png")
        background = skyblock_map.copy()

        #Fetches from location
        options = constants_map.LOCATIONS
        player_cord = options[location]["icon_cordinates"]
        marker_cord = options[location]["marker_cordinates"]


        #Flattens all map objects
        background.paste(head,player_cord,mask_im)
        background.paste(circle_resize,player_cord,circle_resize)
        background.paste(marker,marker_cord,marker)
        background = background.resize((750,750))
        background.save(f"data/maps/{user.name}.png")
        return f"data/maps/{user.name}.png"
    else:
        raise LocationError
