import re
import os

def update_image_paths(html_content):
    pattern = r'media/(?!lowscaled_images/)([^"\s]+?)(\.[a-zA-Z0-9]+)'
    replacement = r'media/lowscaled_images/\1-lowscaled\2'
    new_content = re.sub(pattern, replacement, html_content)
    return new_content

def main():
    file_path = input("Podaj pełną ścieżkę do pliku index.html: ").strip()
    
    if not os.path.isfile(file_path):
        print("Plik nie został znaleziony. Upewnij się, że ścieżka jest poprawna.")
        return

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    updated_content = update_image_paths(content)
    dir_name = os.path.dirname(file_path)
    new_file_path = os.path.join(dir_name, "index_modified.html")
    
    with open(new_file_path, "w", encoding="utf-8") as file:
        file.write(updated_content)
    
    print(f"Zaktualizowany plik zapisano jako: {new_file_path}")

if __name__ == '__main__':
    main()
