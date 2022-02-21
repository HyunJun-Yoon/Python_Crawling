from google_images_download import google_images_download  

response = google_images_download.googleimagesdownload()  

arguments = {"keywords":"블랙핑크 제니, 블랙핑크 지수, 블랙핑크 로제, 블랙핑크 리사, 레드벨벳 조이, 레드벨벳 슬기, 레드벨벳 예리, 레드벨벳 웬디, 레드벨벳 아이린", "limit":50,"print_urls":True, "format": "jpg"}   

paths = response.download(arguments) 

print(paths)   