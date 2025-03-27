import re
import os

index_path = 'index.html'
media_folder = 'media/lowscaled_images'

with open(index_path, 'r', encoding='utf-8') as f:
    content = f.read()

paths = re.findall(r'"panorama"\s*:\s*"([^"]+)"', content)

paths = list(set(paths))
print(f"\nSprawdzam {len(paths)} ścieżek...")

missing = []
for path in paths:
    if not os.path.exists(path):
        missing.append(path)

if not missing:
    print("✅ Wszystkie pliki istnieją.")
else:
    print(f"\n❌ Brakuje {len(missing)} plików:")
    for p in missing:
        print(" -", p)
