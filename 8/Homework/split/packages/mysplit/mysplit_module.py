def mysplit(text):
    text += ' '
    redacted_text = []
    redacted_text = list(text)
    chars = ''
    res_list = []
    for item in redacted_text:
        if item != ' ':
            chars += item
        else:
            res_list.append(chars)
            chars = ''

    for blank in range(res_list.count('')):
        index_of_blank = res_list.index('')
        res_list.pop(index_of_blank)
    return res_list

