from subprocess import *
import os

p = Popen(['rofi', '-dmenu', '-p', '', '-i'], stdout=PIPE, stdin=PIPE)

home = os.path.expanduser('~')

cmds = {
    " CHANGE WALLPAPER": f"ln -sf ~/$(find Wallpapers -type f | shuf -n 1) Wallpapers/current && wal -l -i $(realpath ~/Wallpapers/current)",
    " NETWORK INFO": "ip a | xargs -0 rofi -e",
    " NEOFETCH": "neofetch --stdout | head -n-1 | xargs -0 rofi -e",
    " HTOP": "urxvt -e htop &",
    "-----------------------------------------------------------------------------": "",
    " SHUTDOWN": "systemctl poweroff",
    " HIBERNATE": "systemctl hibernate",
    " RESTART": "systemctl reboot",
    " EXIT": "i3-msg exit"
}

opts = "\n".join(cmds.keys())

raw = p.communicate(input=opts.encode())[0]

choice = raw.decode('utf-8').strip()
cmd = cmds.get(choice, '')
os.system(cmd)

