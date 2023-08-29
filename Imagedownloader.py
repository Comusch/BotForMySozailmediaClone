import os
import requests
from PIL import Image
from io import BytesIO

PIXABAY_API_KEY = "38966630-c522f00ab1cb273715d900cee"

def load_previous_urls(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return file.read().splitlines()
    return []

def save_urls(filename, urls):
    with open(filename, 'w') as file:
        for url in urls:
            file.write(url + '\n')

def download_image(url, folder_path, name):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            image_data = BytesIO(response.content)
            img = Image.open(image_data)
            img_name = url.split('/')[-1]
            img_path = os.path.join(folder_path, f"{name}.jpg")
            img.save(img_path)
            print(f"Downloaded: {img_name} and saved as {name}.jpg in {folder_path}")
            return img
        else:
            print(f"Failed to download: {url} (Status Code: {response.status_code})")
    except Exception as e:
        print(f"An error occurred while downloading {url}: {e}")

def search_images(keyword, num_images, folder_path):
    url = f"https://pixabay.com/api/?key={PIXABAY_API_KEY}&q={keyword}&per_page={num_images}"
    images = []
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for item in data["hits"]:
                download_image(item["largeImageURL"], folder_path, name=keyword+"_"+str(item["id"]))
                images.append(folder_path+"/"+keyword+"_"+str(item["id"])+".jpg")
        else:
            print(response.status_code)
            print(f"Failed to fetch images for keyword '{keyword}'")
        return images
    except Exception as e:
        print(f"An error occurred while searching for '{keyword}': {e}")

def getImages(keyword, num_images, num_of_the_city, folder_path):
    num_images_per_keyword = num_images
    download_folder = folder_path
    os.makedirs(download_folder, exist_ok=True)

    images = search_images(keyword, num_images_per_keyword, download_folder)
    print(f"Found {len(images)} images")

    return images

if __name__ == "__main__":
    getImages("Munich", 3, 1, "images")
