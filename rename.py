


import os

# Path to your directory
directory = '/Users/karandeepbajajbajaj/PycharmProjects/pythonProject/LeetCode'

# Loop through all files in the directory
for filename in os.listdir(directory):
    old_path = os.path.join(directory, filename)

    # Check if it is a file
    if os.path.isfile(old_path):
        # Only modify files that start with "00"
        if filename.startswith("A"):
            # Remove "00" and add "A"
            new_filename =filename[1:]
            new_path = os.path.join(directory, new_filename)

            # Rename the file
            os.rename(old_path, new_path)
            print(f'Renamed: {filename} -> {new_filename}')
