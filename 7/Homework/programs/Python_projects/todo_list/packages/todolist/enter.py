def enter(diction):
    '''
    Gives user enter form to write tasks.
    '''
    num = 1
    name = 'Default'
    while int(num) > 1 or int(num) < 15:
        num = input('Number of task: ')  # Asking number.
        if int(num) < 1 or int(num) > 15:
            print('Input again(only from 1 to 15)')
            num = 1
            continue
        else: 
            name = input('Name: ')  # Asking name.
            if len(name) < 7:
                print('Name have to be more than 7 sym')
                name = 'Default'
                continue
            else: 
                if num in diction:
                    diction[num] = name
                else:
                    diction.update({str(num):name})
                break

    


if __name__ == '__main__':
    print('I prefer to be a module')
else:
    print('I like to be a module')