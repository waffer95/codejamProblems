
f_in = open('input.dat', 'r')
f_out = open('out.dat', 'w')

N = int(f_in.readline())

i = 1
for test in range(N):
    line = ((f_in.readline()).strip('\n')).split(' ')
    line.reverse()

    newline = ""
    
    for word in line:
        newline += word + ' '

    print("Case #{0}: {1}".format(i, newline), file = f_out)
    newline = ""
    i += 1
