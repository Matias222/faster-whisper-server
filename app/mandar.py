import requests
import time

def upload_audio(file_path):
    
    url = 'http://127.0.0.1:80/upload_audio'  # Replace with the actual server URL
    
    url = "https://pnvfyruuck.us-east-1.awsapprunner.com/upload_audio"

    st=time.time()

    files = {'audio': open(file_path, 'rb')}

    response = requests.post(url, files=files)
    
    if response.status_code == 200:
        print('Audio uploaded successfully.')
        print(response.json())
        print(time.time()-st)
    else:
        print(f'Failed to upload audio. Status code: {response.status_code}')
        print('Response:', response.text)

upload_audio("audio.mp3")