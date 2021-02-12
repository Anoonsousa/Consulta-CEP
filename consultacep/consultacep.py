import requests as rq

def main():
    print('#################################')
    print('#####CONSULTA CEP BY ANTONIO#####')
    print('#################################')
    print()


    cep = input('Digite o cep para a consulta:')



    if len(cep) != 8:
        print('Quantidade de digitos inválida!')
        exit()

    request = rq.get('https://viacep.com.br/ws/{}/json/'.format(cep))

    address_data = request.json()

    if 'erro' not in address_data:
        print('+++ CEP VÁLIDO +++')
        print('CEP: {}'.format(address_data['cep']))
        print('LOGRADOURO: {}'.format(address_data['logradouro']))
        print('COMPLEMENTO: {}'.format(address_data['complemento']))
        print('BAIRRO: {}'.format(address_data['bairro']))
        print('CIDADE: {}'.format(address_data['localidade']))
        print('ESTADO: {}'.format(address_data['uf']))
        print('DDD: {}'.format(address_data['ddd']))

    else:
        print('CEP {} inválido!'.format(cep))

    print('----------------------------------')

    option = int(input('Deseja realizar uma nova consulta?\n1. SIM \n2. SAIR \n'))
    if option == 1:
        main()
    else:
        print('Saindo...')



if __name__ == '__main__':
    main()







