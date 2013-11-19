Ceiling Cavalcade: 2013 edition is a remake of a game I made when I was 15.  

There is just one .py file used in coding it, and that is named ceiling.py.

There are also a bunch of .png files used for graphics.


Gameplay is as follows: you control the character on the floor.  Bullets rain down from above, due to
Trrts, mysterious creatures that just so happen to be able to create these bullets.  A Trrt's color and
number of bullet holes are directly related, and although each Trrt fires bullets at the same rate, they
each fire a different number of bullets at once.  

Once you hit a bullet, you "die".  The game implements a "soft death" system where you can still play 
even once "dead".  The game records your deaths by printing out a timescore each time you are hit.  
The first timescore is how long you survived without dying, while each subsequent death is the number 
of time units from initial to that death.  Your first death is indicated by your character turning from 
white to dark grey, but after that deaths offer no visual cues aside from the timescore printed out.

Because of the soft death system, you can play for an indeterminately long amount of time.
