cd $HOME

rm -r Wallpapers
mkdir -p Wallpapers

find .wp_raw/* | parallel --bar -P 24 convert {} -resize $1^ -gravity Center -extent $1 Wallpapers/{#}.png

 ln -s $HOME/Wallpapers/1.png $HOME/Wallpapers/current

