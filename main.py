import os
import requests

def get_extention(image_url: str) -> str | None:
    extentions: list[str] = ['.png', '.jpeg', '.jpg', '.gif', '.svg']
    for ext in extentions:
        if ext in image_url:
            return ext
    return None
        
def download_image(image_url: str, name: str, folder: str = None):
    if ext := get_extention(image_url):
        if folder:
            image_name: str = f'{folder}/{name}{ext}'
        else:
            image_name: str = f'{name}{ext}'
    else:
        raise Exception('Image extension cannot be located...')
    
    # Check if name already exists
    if os.path.isfile(image_name):
        raise Exception('File name already exists...')
    
    # Download the image
    try:
        image_content: bytes = requests.get(image_url).content 
        with open(image_name, 'wb') as handler:
            handler.write(image_content)
            print(f'Downloaded: "{image_name}" successfully')
    except Exception as e:
        print(f'Error: {e}')
        
if __name__ == '__main__':
    input_url: str = input('Enter a URL: ')
    input_name: str = input('Enter a name please: ')
    
    # Ensure the folder exists
    folder = 'images'
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    print('Downloading...')
    download_image(input_url, name=input_name, folder=folder)
