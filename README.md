# Entrevista de Estágio Zapay

Esse código faz parte da entrevista de estágio da startup Zapay.

## Funcionamento do código

### Executando a aplicação

Para executar o programa, digite: 

```shell
    python3.7 main.py
```
OBS: Foi utilizado a versão 3.7 do python, porém versões superiores a versão 3.4 devem funcionar corretamente.

### Passo a passo

```python
    from acess_api import AcessAPI
    from util import Utils
```

Primeiro importação de classes utilizadas, nesse caso  temos apenas classes criadas por mim mesmo que serão explicadas abaixo.
O motivo para tal separação é de seguir boas práticas e filosofias. A primeira alcançada que podemos citar é da orientação a objetos referente a criação de classes e objetos, temos estruturas bem separadas e com atribuição responsabildade unica, alta coesão e baixo acoplamento. Dos principios do SOLID podemos citar o 'Single atribuition Principle' em que classes, métodos, arquivos possuem responsabilidade unica. 


```python

while(True):
        
        utils.print_menu()
        
        try:
            
            option = int(input('Insira a opção: '))
            utils.clear_screen(3)

            ...
        
         except ValueError:
            print('Erro! Digite apenas o numero da sua opção')


```

Criei um loop para poder oferecer ao usuário a possibilidade de receber mais que uma informação desejada sem a necessidade de reiniciar a aplicação.
Utilizo o tratamento de exceções, pois o usuário pode entrar no teclado algo diferente de numeros e quebrar a aplicação, tratando esse erro esse caso necessário.


```python
if option == 1: api.simple_request('https://api.spacexdata.com/v3/launches/next')
        
elif option == 2: api.simple_request('https://api.spacexdata.com/v3/launches/latest')
    
elif option == 3: api.tree_request('https://api.spacexdata.com/v3/launches/upcoming')

elif option == 4: api.tree_request('https://api.spacexdata.com/v3/launches/past')

else:
    print('Opção invalida. Por favor digite um numero válido(1, 2, 3, 4)')
    utils.clear_screen(10)
```

Com base na opção do usuário é disparado o método atribuído no endpoint específico, separando em métodos é promovido aproveitamento de código e maior legibilidade.
E foi tratado caso o usuário não entre uma opção válida.

```python

    def simple_request(self, endpoint):

        launch = requests.get(endpoint)

        if launch.status_code == 200 :

            for item in launch.json():
                print(item, end=':\t')
                print(launch.json()[item])
                Utils().clear_screen(1)
        
        else:
            print('Behaviour not expected happend')
            print('Error Code: ', end=' ')
            print(launch.status_code)

```

Para requests em que existe apenas um resultado esse metodo é chamado, é recebido o endpoint e então é iterado os seu itens. 
E caso o seu status não seja sucesso, é informado uma mensagem de erro e o status do erro ocorrido.

```python

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


```

Método similar ao anterior, porém utilizado para requests em que existe mais que um valor.



