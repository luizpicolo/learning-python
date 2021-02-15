import requests
import json

class ReadAPI:
    def __init__(self, user):
        self.user = user

    def request_api(self, data_api = ''):
        response = requests.get(
            f'https://api.github.com/users/{self.user}{self.__format_uri(data_api)}'
        )

        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code

    def repositories(self):
        repos = []
        
        data_api = self.request_api('repos')
        if type(data_api) is not int:
            for i in range(len(data_api)):
                repos.append({data_api[i]['name'], data_api[i]['language']})
        else:
            return data_api

        return repos
    
    def info_user(self):
        data_api = self.request_api()
        return data_api

    def __format_uri(self, param = ''):
        return f'/{param}' if param != '' else param

# Instance class
data_api = ReadAPI('luizpicolo')
print(data_api.repositories()) 