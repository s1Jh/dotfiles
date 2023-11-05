#!/bin/bash

setxkbmap -query | grep 'cz' && setxkbmap us || setxkbmap cz qwerty > /dev/null

