from acess_api import AcessAPI
from util import Utils


class Main:

    utils = Utils()
    api = AcessAPI()
    
    while(True):
        
        utils.print_menu()
        
        try:
            
            option = int(input('Insira a opção: '))
            utils.clear_screen(3)

            if option == 1: api.simple_request('https://api.spacexdata.com/v3/launches/next')
        
            elif option == 2: api.simple_request('https://api.spacexdata.com/v3/launches/latest')
                
            elif option == 3: api.tree_request('https://api.spacexdata.com/v3/launches/upcoming')

            elif option == 4: api.tree_request('https://api.spacexdata.com/v3/launches/past')

            else:
                print('Opção invalida. Por favor digite um numero válido(1, 2, 3, 4)')
                utils.clear_screen(10)

        except ValueError:
            print('Erro! Digite apenas o numero da sua opção')








    

    
