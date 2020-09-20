#!/usr/bin/env python3

import random

from glob import glob
from os.path import basename, splitext

from sh import magick

WIDTH = 640
HEIGHT = 1920

magick(
    'convert',
    '-size', f'{WIDTH}x{HEIGHT}',
    '-define', 'png:color-type=2',
    'canvas:#7C7C7C',
    'canvas.png')

black = glob('black/*')
white = glob('white/*')

times = 0

while times < 100:
    files = [random.choice(black), random.choice(white)]

    file_1 = files.pop(random.randint(0, 1))
    file_2 = files.pop()

    output = f'output/{splitext(basename(file_1))[0]}-{splitext(basename(file_2))[0]}.png'

    magick(
        'composite',
        '-gravity',
        'North',
        '-geometry', WIDTH,
        file_1,
        'canvas.png',
        'canvas-out-1.png')

    magick(
        'composite',
        '-gravity', 'South',
        '-geometry', WIDTH,
        file_2,
        'canvas-out-1.png',
        output)

    print(f'wrote {output}')

    times += 1
