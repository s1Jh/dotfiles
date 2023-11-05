import os, subprocess, time

raw = subprocess.run(["xkb-switch"], stdout=subprocess.PIPE)

layout = raw.stdout.decode('utf-8')[0:2]

flags = {
    "us": "🇺🇸", 
    "cz": "🇨🇿"
}

raw = subprocess.run(["xset", "-q"], stdout=subprocess.PIPE)
state = raw.stdout.decode('utf-8').split('\n')[3].split()

icons_caps = {
    'off': '',
    'on': 'C',
        }

icons_num = {
    'off': '',
    'on': 'N'
        }

caps = icons_caps.get(state[3], '?')
num = icons_num.get(state[7], '?')

print(f'{flags[layout]} {num} {caps}'.strip())

