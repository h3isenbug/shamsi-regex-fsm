import state_matchine
T = ""
"""
for i in range(10, 99):
    for j in range(1, 12):
        for k in range(1, 31):
            date = "13"+str(i) + ' ' + str(j) + ' ' + str(k)
            T = T + "asdqwepopi " + date"""
T = "asd 1377-03-18 shit"
import state_matchine, fileinput

for line in fileinput.input():
    i = 0
    while i < len(line) - 1:
        a = state_matchine.Context()
        j = 0
        while (not a._state.__class__ == state_matchine.DEAD) and i+j < len(line):
            a.handle(line[i+j])
            j+=1
        while not a._state == None:
            if a.is_accept():
                break
            a.back()
        if not a._state == None:
            if a.is_accept():
                path = a.get_path()
                print(path)
                i += len(path) - 1
        i+=1