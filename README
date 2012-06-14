Stathammer (c) 2012
Author   Kevin Fronczak
Email    kfronczak@gmail.com
Source   http://github.com/fronzbot/Stathammer

== LEGAL ==

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

Stathammer is in no way afiliated with Games Workshop.  This
tool uses basic statistical principles to calculate probabilities
based on stats input by the user.  These stats are availaible by
purchasing the approriate rulebooks and codices from http://games-workshop.com
This program does not contain, nor distribute, any information that
could undermine the value of Games Workshop products.  The end-user
must physically own all information in order to use this tool.


== OPERATION ==

To use the Stathammer tool, simply enter the stats of your units in the
appropriate boxes.  You can save your units to a file in order to keep
your settings (so you don't have to re-enter them every time!)
By clicking File>New Weapon you can create weapon profiles that your
units can use.  Each weapon can have a maximum of four attributes
such as Re-Roll to Hit and Rending.  This allows for you to have a
good amount of flexibility in simulation units.

Once you have all of your stats entered, just hit the "Calculate" button
and you can view your Results on the Results page!  If you would like 
a quicker simulation, you can click on Options>Iterations.  As a warning
though, the fewer iterations there are, the less accurate the results
will be (and likewise, the more iterations, the more accurate).  See the
SIMULATION header for more information on why this is.

You can click on any of the colored circles on the resulting graph to view
what that specific probability is.  You can also click on Options>Export CSV
to export the data to a CSV file for later viewing.


== SIMULATION ==

Stathammer uses a monte_carlo method to simulate unit statistics and outcomes.
On a very basic level what happens is that the program "rolls the dice" using
Python's random() method and the result is the roll of the die (1-6).  This
is repeated for however many iterations are selection in the Options menu.
This gives a very good approximation as to what the realistic scenarios would
be and is also far less overhead than calculating probabilities based on
binomials.


== BUG REPORTING ==

If you find any bugs, the first preferred method of contact would be to submit
an issue on the Stathammer page on github 
<http://github.com/fronzbot/Stathammer/issues>
This will allow me to keep all the bugs organized and prioritize them.
If you do not want to create an account to submit the bug, please email me
at kfronczak@gmail.com with the subject [Stathammer].


== UPDATES ==

All new distributions will be posted to
<http://github.com/fronzbot/Stathammer/downloads>


== CONTRIBUTING ==

Anyone is free to fork the Stathammer repo at <http://github.com/fronzbot/Stathammer>
or, if you'd like to be a collaborator, just send me an email at
kfronczak@gmail.com with the subject [Stathammer]