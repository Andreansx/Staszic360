import os
from PIL import Image

def main():
    folder_path = input("Podaj ścieżkę folderu ze zdjęciami: ").strip()
    
    if not os.path.isdir(folder_path):
        print("Podana ścieżka nie jest folderem.")
        return

    try:
        height = int(input("podaj wysokość: "))
        width = int(input("podaj szerokość: "))
    except ValueError:
        print("Wysokość i szerokość muszą być liczbami całkowitymi.")
        return

    output_folder = os.path.join(folder_path, "lowscaled_images")
    os.makedirs(output_folder, exist_ok=True)
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path) and file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            try:
                with Image.open(file_path) as img:
                    resized_img = img.resize((width, height))
                    file_name, ext = os.path.splitext(file)
                    output_path = os.path.join(output_folder, f"{file_name}-lowscaled{ext}")
                    resized_img.save(output_path)
                    print(f"Przeskalowano i zapisano: {output_path}")
            except Exception as e:
                print(f"Błąd przetwarzania pliku {file}: {e}")
    print("Gotowe.")
if __name__ == '__main__':
    main()
