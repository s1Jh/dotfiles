import subprocess

def get(arg):
    raw = subprocess.run(['pactl', arg, '@DEFAULT_SINK@'], stdout=subprocess.PIPE)
    return raw.stdout.decode('utf-8').strip()

muted = get('get-sink-mute').split()[1]

if muted == "yes":
    print('MUTED')
    quit(33)

stat = get('get-sink-volume').split()[4].strip()
print('🔊{: >4}'.format(stat))

quit(0)

