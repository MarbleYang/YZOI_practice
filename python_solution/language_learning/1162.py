def getNext(input_string, str_len):
    result = []
    result.append(-1)
    j = 0
    k = -1
    while j < str_len :
        if k == -1:
            k = k+1
            j = j+1
            result.append(k)
        elif input_string[j] == input_string[k]:
            k = k+1
            j = j+1
            result.append(k)
        else:
            k = result[k]
    return result


def trace_next(next, len):
    repeat_len = next[len]
    if repeat_len != 0:
        len = repeat_len
        trace_next(next, len)
        print(repeat_len, end=' ')
    else:
        return
    


while 1:

    input_line = input()
    input_len = len(input_line)

    next = getNext(input_line, input_len)
    trace_next(next, input_len)
    print(input_len)
    