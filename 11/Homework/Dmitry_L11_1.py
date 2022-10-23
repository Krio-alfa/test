while True:
    inp = input('Input the name of file: ')

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

for result in res:
    print(result,'->',res[result])
