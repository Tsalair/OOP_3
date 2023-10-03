import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {'Authorization': 'OAuth '+token}
        params = {'path': file_path}
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        if 200 <= response.status_code < 300:
            file_url = data['href']
            with open('Task_2.py', 'rb') as f:\
                response = requests.post(file_url, files={'file': f})
            print(response.status_code)

if __name__ == '__main__':
    
    path_to_file = input('Введите путь к файлу на вашем компьютере: ')
    token = input('Введите token': )
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)