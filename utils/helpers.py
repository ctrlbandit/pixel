import re
import validators

VALID_IMAGE_EXTENSIONS = ('.png', '.jpg', '.jpeg')

def is_valid_hex_color(color_code: str) -> bool:
    return bool(re.fullmatch(r'^#(?:[0-9a-fA-F]{3}){1,2}$', color_code))

def is_valid_url(url: str) -> bool:
    return validators.url(url) and url.startswith("https://")

def is_valid_image_file(file_name: str) -> bool:
    return file_name.lower().endswith(VALID_IMAGE_EXTENSIONS)
