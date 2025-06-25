import os

# Path to your directory
directory = '/Users/karandeepbajajbajaj/PycharmProjects/pythonProject/LeetCode'

# Loop through all files in the directory
for filename in os.listdir(directory):
    old_path = os.path.join(directory, filename)

    # Check if it is a file (not a folder)
    if os.path.isfile(old_path):
        new_filename = '00' + filename
        new_path = os.path.join(directory, new_filename)

        # Rename the file
        os.rename(old_path, new_path)
        print(f'Renamed: {filename} -> {new_filename}')
