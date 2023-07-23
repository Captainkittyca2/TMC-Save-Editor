# TMC (USA) Save File notes

## Offsets

* 0x34->0x37: The main checksum for file 1.
* 0x81: Triforce flag in file select (0 = off, 1 = on)
* 0x84: Brightness value (0 to 2).
* 0x85: Message Speed value (0 to 2).
* 0x86: value = 1: Link resume from the map he left from. value != 1: Link resumes from the house on the bed.
* 0x108->0x10C: Spawn point. [more info](#spawn-point-info)
* 0x10C: Spawn point animation.
* 0x10E->0x10F: room ID and area ID respectively.
* 0x12D: Health remaining. [more info](#health-remaining-info)
* 0x2D9: hatless Link (0x08) or hat Link (0x38).

## Spawn point info:

* 0x108 = big y position.
* 0x109 = small y position.
* 0x10A = big x position.
* 0x10B = small x position.

## Health remaining info:

* Formula: (user's input value) * 8.
* Values 1, 2, and 3 are all 1/4 hearts visually in-game, however, a value of 3 allows you to touch octorock 2 times before dying while values of 1 and 2 only allow octorock touch once.
* Starting from value 4 (2/4 health), every 2 values increase the health amount by 1/4.
* Starting from value 3 (1 octorock touch), every 2 values increase octorock touch amount by 1.
* [Some documentation.](https://docs.google.com/spreadsheets/d/1yzXh2QSfBaXGAapngyejzW3H_ALxxMkaxuRX4HG2dis/edit?usp=sharing) (F to I)
