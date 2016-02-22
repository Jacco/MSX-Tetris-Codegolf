Short & Powerfull (Kort & Krachtig)
Miniature Tetris

In the past Jacco Kulman already proved to be a gifted programmer for the K&K section. Now as a writer he tries to explain the workings of his really super-short version of Tetris.

In the previous MCCM Frank promised a column by me. Every now and then I write an article for the magazine of the MSX Computer Club Enschede so I already had some stuff laying around for publication.

Tetris
Tetris is, as everyone will probably know, a puzzle game. It so extremely popular, that game publishers created all sorts of variantions and extras and that for literally every aparatus, with the slightest resemblance to a computer, there is likely to be tetris a version for it. It seems therefore a bit superfluous, to post a listing in magazine of a game everybody already owns. Indeed, everyone has got it, but hardly anyone has ever programmed it themselves and because the title of this article reads Short and Powerfull, this is therefore a very special version.

The idea
On one of the cozy club evenings of the MCCE the group of programmers - which I also hang around with every now and then - was as always bragging heavily about the Flight Simulators, Graphic Adventures and Super Applications, that we all had written. And as always finishing describing the explosions, short circuits and other disasters, leading to the desctruction of the disk containing the sourcecode of these truely amazing programs. Until Albert Huitsing gave a demonstration of a Tetris-version in seven lines. Everyone was impressed and congratulated Albert. The others left it at that, but I - stuborn as I am - wanted to write an even shorter version.

The principle
It is - in the context of this column - not possible to cover all the tricks that are used in this little program. Nevertheless I will explain the principles for the user who - just as I thought - thinks he make make it even shorter.

To get the program short a number of things have to be striked out from the Tetris script: in the described version there are no separate levels nor  colors. Also missing are score-keeping and a high score list. In this version even the detection for the end of the game is missing.

These shortcomings make it possible to execute Tetris on SCREEN 1, which makes that this version should also be runable on a MSX 1. Furthermore the operation is based on the fact that the playingfield (without colors) is build from an array of binary numbers. These binary numbers will be printed to the screen using the BASIC-function BIN$. But of course a screen with only changing zeros and ones is not very illustrating. For that matter I added a few VPOKEs in the right spots in the video memory, e voila, the zero-and-ones screen is transformed into a real MSX blue-white Tetris field. With this, however, I was not ready; all known Tetris figures had yet to be defined, they have to fall, rotate and fill the field.

So to carry on
I defined the Tetris blocks hexadecimaly in a string: this takes 4 characters per block; there are 7 blocks in 4 different turning directions, so this already takes up 4x4x7=112 characters. A BASIC-line is maximised at 255 characters, so a oneliner was out of the question. If you can now display the pieces on the screen and remove them without messing up the rest of the screen, the moving and rotating solved. Falling is moving so that is solved too. The displaying is realised by saving the active piece in a separate array, separate from an array in which the 'fixed' play field is stored. Because all graphical elements are stored in binary format displaying a piece over a fixed pattern is a simple matter of boolean algebra: the application of logical operations.

Multiplying by 2 and divisions by 2 move the bit-pattern to the right and left respectively. Using this principle the pieces can always be printed on their initial position while able to move horizontally. After implementing this enough problems remain to be solved.

More problems yet
The pieces now fall down, move to the left and right and turn. But they - although leaving it as is - also move right trhough the side walls. And if that was all, it wouldn't be so bad, but imagine a piece is against the left wall of the Tetris field and you want to turn it, but once turned an extremity goes right through the wall. Right... so more problems. This problem, together with that of the colliding of falling or rotating pieces is solved with logical operations. With all these options incorporated the program still was quit long, so what to do about it?

Delayed control
A rewarding method to make programs shorter is combining of pieces of code with the same structure. I had three FOR-NEXT-loops that all would iterate four times: one for the check if a piece can be moved in a certain direction, one for changing of the pieces, and one for the displaying of it. I combined those three loops to one loop. When I got this working it appeared I had lost some speed, but if shortness is the name of the game...  The control of the pieces now runs with a one step delay: the new movement desire is evaluated while the previous movement is simultaniously created and displayed. These are the kind of things you sacrifice when achieving compactness.

Removing lines
The last problem to be tackled is the removal of complete lines from the playing field. Until now the blocks fall down, moven or not, but full lines waited patiently until a CTRL+STOP finally removed them. By application of one small FOR-NEXT-loop with some logical operations the lines are now cleared on the screen as well as in the array.

Wrapping up
After optimising: use variables with one character, replacing calculations that appear more than once by one and replacing manu if statements by boolean algebra there remained space left for a DEFINT A-Z which makes this type of program a lot faster.

End result
After a week of measuring and fitting the moment had arrrived. Tetris was finished! In three lines! The little program is printed in the artcile. The extra colon indicate the amount of space left on each line. In total 22 characters left, but hack, what can you do ion 22 characters, when they are divided over two lines that each already have a function? I don't rule out anything, give it a try to expand the program.

Manual
A first requirment is that you key in the program character by character or load it from the disk from your subscription. After that a simple RUN is enough to start the game. The controls are given in the table below. Abort if the field is full with CTRL+STOP.

Levels after all
When I wrote this article, which is a time consuming activity all the same, I adapted the program for KUN-BASIC. In this BASIC-version you can use no dynamic arrays and so a fourth line was needed, although nothing much needed to be in it.

I would not be worthy the Short and Powerfull column if I would not stuff this line full of code as well. For this faster BASIC-version a delay already had to be added, so I also built in 10 levels: Every 40 seconds, at 3.5 MHz, the bricks will fall faster downwards. The first version had no ending and that proved very uncomfortable with KUN-BASIC because you have to reset the machine to exit. And because I was tinkering anyhow I added keeping the score will be shown at the end of the game. Press x when the game is over and it will neatly show the score and achieved level on the screen. 

If this version is not hard enough for you, try playing it 7 MHz ;-)

Jacco Kulman
