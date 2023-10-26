import requests
import os

api_key = '303594tcni6524q2l2nt8h'  # Replace with your API key
url = f'https://doodapi.com/api/upload/server?key={api_key}'
response = requests.get(url)
upload_url = response.json().get('result')

# Specify your directory
directory_path = '/content/roop-unleashed/output/'  # Replace with the path of your directory

# Iterate over all files in the directory
for filename in os.listdir(directory_path):
    file_path = os.path.join(directory_path, filename)
  
    # Get the file extension
    file_extension = os.path.splitext(file_path)[1]

    # Check if the file is a .mp4 file
    if file_extension == '.mp4':
        with open(file_path, 'rb') as file:
            files = {'file': (f'file{file_extension}', file)}
            upload_response = requests.post(upload_url, files=files, data={'api_key': api_key})
        print(upload_response.json())
