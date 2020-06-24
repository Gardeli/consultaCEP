import requests

def main():
    print("##########################")
    print("### - Consulta CEPs - ###")
    print("##########################")

    print()

    cep_input = input('Digite o CEP desejado para a busca:')
    if len(cep_input) != 8:
        print('Quantidade de digitos inválida!')
        exit()

    req = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))
    address_data = req.json()

    if 'erro' not in address_data:
        print('==>> CEP encontrado!! <<==')
        print('CEP: {}'.format(address_data['cep']))
        print('Logradouro: {}'.format(address_data['logradouro']))
        print('Complemento: {}'.format(address_data['complemento']))
        print('Bairro: {}'.format(address_data['bairro']))
        print('Cidade: {}'.format(address_data['localidade']))
        print('Estado: {}'.format(address_data['uf']))
    else:
        print('{}: CEP inválido!'.format(cep_input))

    print('---------------------------------')
    option = int(input('Deseja realizar uma nova consulta?\n 1. Sim\n 2. Sair\n'))
    if option == 1:
        main()
    else:
        print('Saindo...')

if __name__ == '__main__':
    main()
