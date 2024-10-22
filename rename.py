import os

def rename_files(directory):
    for i in range(30000):
        old_png = os.path.join(directory, f'{i:06d}.png')
        old_json = os.path.join(directory, f'{i:06d}.json')
        new_png = os.path.join(directory, f'{i + 30001:06d}.png')
        new_json = os.path.join(directory, f'{i + 30001:06d}.json')
        
        if os.path.exists(old_png):
            os.rename(old_png, new_png)
            print(f'Renamed {old_png} to {new_png}')
        
        if os.path.exists(old_json):
            os.rename(old_json, new_json)
            print(f'Renamed {old_json} to {new_json}')

# Replace 'your_directory_path' with the path to your directory containing the images and labels
directory_path = '/home/rics/Desktop/f'
rename_files(directory_path)
