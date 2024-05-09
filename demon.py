from PIL import Image

# Replace "path/to/your/spritesheet.png" with the actual path
image = Image.open("assets/images/boss_demon_slime_FREE_v1.0/spritesheets/")
width, height = image.size

print(f"Image width: {width} pixels")
print(f"Image height: {height} pixels")
