import os
import semver
import subprocess

# Odczytaj bieżącą wersję z pliku version.txt
with open('version.txt', 'r') as version_file:
    current_version = version_file.read().strip()

# Zwiększ minor version o 1
parsed_version = semver.VersionInfo.parse(current_version)
new_version = f"{parsed_version.major}.{parsed_version.minor + 1}.{parsed_version.patch}"

# Aktualizuj plik version.txt z nową wersją
with open('version.txt', 'w') as version_file:
    version_file.write(new_version)

# Tworzenie i zapisywanie taga w repozytorium Git
tag_name = f"v{new_version}"
subprocess.run(["git", "tag", "-a", tag_name, "-m", f"Release {tag_name}"])
subprocess.run(["git", "push", "origin", tag_name])

# Teraz możesz użyć nowej wersji do innych działań w swoim skrypcie
print(f'Created Git tag: {tag_name}')

