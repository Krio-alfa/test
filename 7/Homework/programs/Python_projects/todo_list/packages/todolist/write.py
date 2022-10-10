
def op():
    try:
        with open('D:\\source.txt', 'r') as f:
            dic = f.read()
        f.close()
    except:
        with open("D:\\source.txt", "w") as f:
            f.write(str({1:'new'}))
            f.close()
        with open('D:\\source.txt', 'r') as f:
            dic = f.read()
            f.close()
            print(dic)
    return dic

def wr(dic):
    with open('D:\\source.txt', 'w') as f:
        f.write(str(dic))
    f.close()

if __name__ == '__main__':
    print('I prefer to be a module')
else:
    print('I like to be a module')