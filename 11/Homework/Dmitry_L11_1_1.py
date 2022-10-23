while True:
    inp = input('Input the name of file: ')
    name, format = inp.split('.')
    try:
        stream = open(inp, 'rt')
        break
    except:
        print('Cannot open the file...' + '\n\n' + 'Try again >>>')

count_alf = {chr(ch): 0 for ch in range( ord('a'), ord('z') + 1 ) }

chars = list(stream.read().lower())
res = {}

for i in chars:
    if i in count_alf:
        count_alf[i] += 1

for unused in count_alf:
    if count_alf[unused] != 0:
        res[unused] = count_alf[unused]

sorted_dict = {k: v for k, v in sorted(res.items(), key=lambda item: item[1], reverse=True)}\

x = ''
try:
    post = open(name + '.hist', 'x')
except:
    post= open(name + '.hist', 'w')

for result in sorted_dict:
    print(result,'->',sorted_dict[result])
    post.write(str(result)+' -> '+str(sorted_dict[result])+'\n')
    

stream.close()



post.close()