
def printLine(line_num, entry_num):
    start = line_num+1
    end = line_num+entry_num
    while start<=end:
        if start == end:
            print("%3d" % start)
        else:
            print("%3d" % start, end='')
        start=start+1
            
entry = int(input())
i = 0
while i < entry:
    printLine(i, entry)
    i = i+1
