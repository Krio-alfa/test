class StudentsDataException(Exception):
    pass

class BadLine(StudentsDataException):
    print('Bad Line error accuried', '\n\n', 'Check the following format in file >>> ', '\n', 'The elements are separated with white spaces. Each student may appear more than once inside Prof. Stefan`s file', '\n', 'Andrew Ivanov     1.5')
    pass

class FileEmpty(StudentsDataException):
    print('File is empty, please check file name or data inside it.')

while True:
    inp = input('Input the name of file: ')

    try:
        stream = open(inp, 'rt')
        break
    except:
        print('File with this name doesn`t exists...' + '\n\n' + 'Try again >>>')

data = {}
end = 'entering'

while end != '':
    try:
        end = stream.readline()
    except:
        raise FileEmpty

    try:
        name, surname, num = end.split()
        data[name+'_'+surname] = num
    except:
        raise BadLine

for result in data:
    name, surname = str(result.split('_'))
    print(name.capitalize(),surname.capitalize(), '->', data[result])
