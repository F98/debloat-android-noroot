import subprocess
import datetime
import random
ic = input("Pick an option (cancel by inputting any non-options):\n1) Remove all bloat\n2) Remove all bloat excluding Google\n3) Undo all\n")
o = ["1","2","3"]
d = "files/"
dto = str(datetime.date.today())
rng = random.randrange(1,255)
otf = "logs/removed-packages-" + str(rng) + "-" + dto + ".txt"
if ic == "1":
    fi = d + "ev.txt"
if ic == "2":
    fi = d + "abg.txt"
if ic == "3":
    fi = d + "ue.txt"
if ic not in o:
    print("Cancelled!")
    exit()
with open(fi) as f:
    c = f.readlines()
g = [x.strip("\n") for x in c]
sr = []
while g:
    for x in g:
        u = x.split()
        t = u[-1]
        try:
            y = subprocess.check_output("adb shell " + x, shell=True)
            z = ''.join(filter(str.isalnum, y.decode("utf-8")))
            print("Successfully Removed " + t)
            g.remove(x)
            sr.append(t)
        except Exception:
            print(t + " is not installed so not removed")
            g.remove(x)
with open(otf, 'w') as f:
    for x in sr:
        f.write("%s\n" % x)
