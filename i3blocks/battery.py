from subprocess import *
from datetime import *
import os

output = run(['acpi'], stdout=PIPE).stdout.decode('utf-8')

lines = output.split('\n')

def extract(line):
    return [word.strip() for word in ":".join(line.split(':')[1:]).split(',')]

def fmt(data):
    tcontrib = 0
    if len(data) > 2:
        try:
            t = data[2]
            comps = t.split(' ')[0].split(':')
            tcontrib = int(comps[0]) * 3600 + int(comps[1]) * 60 + int(comps[2])
        except:
            pass
    
    states = {
        'Discharging': "-",
        'Full': "",
        'Charging': "+",
        'Not charging': '!'
    }

    return (states[data[0]], data[1], tcontrib)

tleft = 0
status = ""

def process(battery):
    global tleft, status
    tleft += battery[2]
    
    if not len(status) == 0:
        status += ':'

    status += battery[0] + battery[1]

for line in lines:
    if len(line) == 0:
        continue
    data = extract(line)
    formatted = fmt(data)
    process(formatted)

t = datetime.fromtimestamp(tleft)

discharging = '-' in status 

print(f"{status}{' ' + t.strftime('%H:%M:%S') if discharging else ''}")

# 30 minutes
if tleft < 30*60 and discharging:
#    os.system('notify-send -t 300000 "Low battery!"')
    quit(33)

quit(0)

