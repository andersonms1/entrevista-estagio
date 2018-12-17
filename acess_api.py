import requests
from util import Utils

class AcessAPI:
 
    def simple_request(self, endpoint):

        launch = requests.get(endpoint)

        if launch.status_code == 200 :

            for item in launch.json():
                print(item, end=':\t')
                print(launch.json()[item])
                # print(type(launch.json()[item]))
                Utils().clear_screen(1)
        
        else:
            print('Behaviour not expected happend')
            print('Error Code: ', end=' ')
            print(launch.status_code)


    def tree_request(self, endpoint):
        
        launch = requests.get(endpoint)

        if launch.status_code == 200 :
        
            tree_launches = launch.json()

            for root in tree_launches:
                Utils().clear_screen(3)
                for item in root:
                    print(item, end=':\t')
                    print(root[item])
                    Utils().clear_screen(1)

        else:
            print('Behaviour not expected happend')
            print('Error Code: ', end=' ')
            print(launch.status_code)