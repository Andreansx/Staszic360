import re
import os

index_path = 'index.html'
media_folder = 'media/lowscaled_images'

with open(index_path, 'r', encoding='utf-8') as f:
    content = f.read()

used_paths = re.findall(r'"panorama"\s*:\s*"([^"]+)"', content)
used_paths = list(set(used_paths)) 

print("🔍 Znaleziono ścieżki do obrazów w index.html:")
for path in used_paths:
    print(" -", path)

print("\n📌 Podaj ścieżki, które mają być traktowane jako *wyjątki* (np. plik nie istnieje, ale ma tak być).")
print("Wpisz je po jednej linii, zakończ wpisywanie pustym enterem:")

exceptions = set()
while True:
    line = input()
    if line.strip() == "":
        break
    exceptions.add(line.strip())

missing = []
for path in used_paths:
    if path in exceptions:
        continue
    if not os.path.exists(path):
        missing.append(path)

all_files = []
for root, dirs, files in os.walk(media_folder):
    for file in files:
        full_path = os.path.join(root, file).replace("\\", "/")
        all_files.append(full_path)

unused = [file for file in all_files if file not in used_paths]

print("\n=== 📋 PODSUMOWANIE ===")

if not missing:
    print("✅ Wszystkie używane pliki istnieją (po uwzględnieniu wyjątków).")
else:
    print(f"❌ Brakuje {len(missing)} plików:")
    for p in missing:
        print(" -", p)

if not unused:
    print("✅ Wszystkie pliki w folderze są używane.")
else:
    print(f"📁 Znaleziono {len(unused)} plików w folderze, które nie są używane:")
    for u in unused:
        print(" -", u)
