import subprocess
import datetime
import random
ic = input("Pick an option (cancel by inputting any non-options):\n1) Remove all bloat\n2) Remove all bloat excluding Google\n3) Undo all\n")
o = ["1","2","3"]
d = "files/"
dto = str(datetime.date.today())
rng = random.randrange(1,255)
otf = "logs/removed-packages-" + str(rng) + "-" + dto + ".txt"
rt = 0
if ic == "1":
    fi = "ev.txt"
if ic == "2":
    fi = "abg.txt"
if ic == "3":
    fi = "ue.txt"
    rt = 1
if ic not in o:
    print("Cancelled!")
    exit()
with open(d + fi) as f:
    c = f.readlines()
g = [x.strip("\n") for x in c]
sr = []
while g:
    for x in g:
        u = x.split()
        t = u[-1]
        try:
            if rt == 1: et = "cmd package install-existing "
            if rt != 1: et = "pm uninstall -k --user 0 "
            y = subprocess.check_output("adb shell " + et + x, shell=True)
            z = ''.join(filter(str.isalnum, y.decode("utf-8")))
            print("Successfully Removed " + t)
            g.remove(x)
            sr.append(t)
        except:
            print(t + " is not installed so not removed")
            g.remove(x)
with open(otf, 'w') as f:
    for x in sr:
        f.write("%s\n" % x)
