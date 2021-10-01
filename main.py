# 23.09.2021
# Решётка Кардано
# Работу выполнил: Грубов Михаил Дмитриевич


from CardanoLattice import CardanoLattice


def main():
    print('Enter text to encrypt: ', end=' ')
    message = input()
    myth = CardanoLattice(message)
    print('To encrypt Enter:\t\t\t\t\'enc\';\nTo decrypt Enter:\t\t\t\t\'dec\';\nTo print on display, '
          'Enter:\t\t\t\'print\';\nTo replace the message Enter:\t\t\t\'replace\';\nTo start cryptanalysis of the '
          'system, enter:\t\'analysis\'\nFor help information, '
          'Enter:\t\t\t\'help\'\nTo exit Enter:\t\t\t\t\t\'exit\';')
    check_out = True
    check_encrypt = False
    while check_out:
        print('>>>', end=' ')
        code = input()
        if code == 'enc':
            if not check_encrypt:
                myth.encrypt()
                check_encrypt = True
            else:
                print('The message is already encrypted!')
        elif code == 'dec':
            if check_encrypt:
                myth.decoder()
                check_encrypt = False
            else:
                print('The message is already decrypted!')
        elif code == 'print':
            print(myth.message)
        elif code == 'replace':
            print('Enter text to encrypt: ', end=' ')
            message = input()
            myth = CardanoLattice(message)
        elif code == 'exit':
            check_out = False
        elif code == 'analysis':
            if check_encrypt:
                myth.analysis()
                check_encrypt = False
            else:
                print('The message is already decrypted!')
        elif code == 'help':
            print('To encrypt Enter:\t\t\t\t\'enc\';\nTo decrypt Enter:\t\t\t\t\'dec\';\nTo print on display, '
                  'Enter:\t\t\t\'print\';\nTo replace the message Enter:\t\t\t\'replace\';\nTo start cryptanalysis of '
                  'the system, enter:\t\'analysis\'\nFor help information, '
                  'Enter:\t\t\t\'help\'\nTo exit Enter:\t\t\t\t\t\'exit\';')
        else:
            print('Enter the correct code!')


if __name__ == '__main__':
    main()
