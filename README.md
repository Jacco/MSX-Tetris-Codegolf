# MSX-Tetris-Codegolf

My 1994 MSX "Kort maar Krachtig" (short but powerfull) implementation of Tetris

It is three lines of BASIC code. Only 760 bytes.

To see how it works you can load the disk into http://webmsx.org/

Steps:
  1. download the [dsk](https://github.com/Jacco/MSX-Tetris-Codegolf/blob/master/tetris.dsk?raw=true) file of this repository
  2. goto http://webmsx.org/
  3. enter todays date (M-D-Y format)
  4. press F6 load the [dsk](https://github.com/Jacco/MSX-Tetris-Codegolf/blob/master/tetris.dsk?raw=true) file
  5. type: load "tetris.bas"
  6. type "run"

Keys to play the game:
,            rotate left
.            rotate right
arrow down   faster down
arrow left   move left
arrow right  move right

Note: the steering is delays one cycle for smaller code size. Makes it harder to play :-)
