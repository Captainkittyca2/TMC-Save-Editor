# TMC (USA) Save File notes

## Offsets

* 0x34->0x37: The main checksum for file 1.
* 0x84: Brightness value (0 to 2)
* 0x85: Message Speed value (0 to 2)
* 0x86: value = 1: Link resume from the map he left from. value != 1: Link resumes from the house on the bed.
* 0x12D: Health remaining. [more info](###-Health-remaining-info)












## Health remaining info:
* value of 7 gives 3/4 of hearts remaining.
* value of 20 (14 in hex) gives 2 hearts and a half remaining.
