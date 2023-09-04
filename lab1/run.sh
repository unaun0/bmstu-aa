#!/bin/bash

libraries=("matplotlib" "tabulate" "art" "simple-term-menu")

pip install "${libraries[@]}"

python3 -O lab/main.py