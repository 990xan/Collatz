import time
import os

def TestForExit(text):
    imp = (input(text))
    if imp.upper() == "EXIT":
        raise SystemExit
    else:
        imp = int(imp)

    return imp


mode = 0
while mode == 0:
    os.system('cls')
    dat = input("Select a mode [Single, Up To, Infinite]: ")
    if (dat.upper() == "SINGLE"):
        mode = 1
    elif (dat.upper() == "UP TO"):
        mode = 2
    elif (dat.upper() == "INFINITE"):
        mode = 3
    else:
        print("Invalid mode! Please try again.")
        continue

_workingnum = 1 #stores current number
_counter = 1 #stores number of steps
_megacounter = 1 #stores number of numbers iterated through for upto and infinite modes
cntrecord = 0 # highest number of steps reached
numrecord = 1 # number with the cntrec
countval = 0 # number needed to be counted to for up to

while mode == 1:
    _workingnum = TestForExit("Please enter a positive integer [or 'exit' to exit]: ")

    print(str(_workingnum) + " | 0")

    while _workingnum != 1:
        if (_workingnum % 2) == 0:
            _workingnum = _workingnum / 2
            print(str(_workingnum) + " | DIV 2 | " + str(_counter))
        else:
            _workingnum = _workingnum * 3
            _workingnum += 1
            print(str(_workingnum) + " | MUL 3 ADD 1 | " + str(_counter))
        _counter += 1
    _counter = 0

while mode == 2:
    countval = TestForExit("Please enter a positive integer to go up to [or 'exit' to exit]: ")

    while _megacounter <= countval:
        print("------------------")
        print(_megacounter)
        print("Rec: " + str(cntrecord) + "  Num Rec: " + str(numrecord))

        while _workingnum != 1:
            if (_workingnum % 2) == 0:
                _workingnum = _workingnum / 2
                print(str(_workingnum) + " | DIV 2 | " + str(_counter))
            else:
                _workingnum = _workingnum * 3
                _workingnum += 1
                print(str(_workingnum) + " | MUL 3 ADD 1 | " + str(_counter))
            _counter += 1

        # records
        if _counter >= cntrecord:
            cntrecord = _counter
            numrecord = _megacounter

        _counter = 0
        _megacounter += 1
        _workingnum = _megacounter

# infinite mode, no while needed
while True:

    print("------------------")
    print(_megacounter)
    print("Rec: " + str(cntrecord) + "  Num Rec: " + str(numrecord))

    while _workingnum != 1:
        if (_workingnum % 2) == 0:
            _workingnum = _workingnum / 2
            print(str(_workingnum) + " | DIV 2 | " + str(_counter))
        else:
            _workingnum = _workingnum * 3
            _workingnum += 1
            print(str(_workingnum) + " | MUL 3 ADD 1 | " + str(_counter))
        _counter += 1

    if _counter >= cntrecord:
        cntrecord = _counter
        numrecord = _megacounter
    _counter = 0
    _megacounter += 1
    _workingnum = _megacounter

