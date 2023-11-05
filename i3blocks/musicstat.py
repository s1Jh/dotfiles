import subprocess, unicodedata

def get(arg):
    raw = subprocess.run(["playerctl", arg], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if len(raw.stdout) != 0:
        return raw.stdout.decode('utf-8')
    else:
        return raw.stderr.decode('utf-8')

stat = get("status").strip()

if (stat != "Playing"):
    print('{: >21}'.format(stat))
    quit()

meta = get("metadata").strip()

player = ""

attrs = {}

for line in meta.split('\n'):
    components = line.split()
    player = components[0]
    attribute = components[1]
    value = "".join(comp + ' ' for comp in components[2:]).strip()
    attrs[attribute] = value

artist = attrs.get('xesam:artist')
title = attrs.get('xesam:title')
album = attrs.get('xesam:album')

print('{: >21} '.format(f"{artist} - {title} {'(' + album + ')' if album != '' else '' }".strip()))

