import os

directory = "."
for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)
    if os.path.isfile(filepath):
        new_filename = filename[:-5]
        new_filepath = os.path.join(directory, new_filename)
        os.rename(filepath, new_filepath)

        print(f"Le fichier '{filename}' a été renommé en '{new_filename}'")
print("Terminé.")
