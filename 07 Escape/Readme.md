
<h1 align="center">
	Challenge 7 - Escape or Die
</h1>
	
### Instructions:

Hello, dear friend. Do you feel like you're in some kind of jail? Did you wake up this morning with the feeling that everything was dark?
Well, it isn't a dream. You're really here, in a long dark dungeon.
What do you have to do? It's simple. Try to escape from the dungeon. But, hurry up or something bad will happen to you.
You have to find the shortest path to the exit to escape the maze.
Good luck, my friend. Your dungeon is waiting for you at <strong>codechallenge-daemons.0x14.net:4321</strong>

<h3>Input</h3>
<p>No input needed</p>

<h3>Output</h3>
<p>A list of coordinates with the shortest path to the exit. The list must have the following syntax:</p>
<p>
<pre>
(x0, y0), (x1, y1), (x2, y2), (x3, y3)... (xn, yn)
</pre>
</p>

<p>Where (x0, y0) is the starting position in the maze and (xn, yn) is the final position (the exit).</p>
<p>For example, if your initial position is (3, 4) and the exit is at (5, 6), the following could be a good solution:</p>
<p>
<pre>
(3, 4), (3, 5), (3,6), (4, 6), (5, 6)
</pre>
</p>
<p>Assuming the path is clear, of course.</p>

## My notes:

When I first read the instructions here, I was completely lost and thought I'd skip the challenge. Thankfully someone had asked on Twitter about the url and they'd told him to use netcat, so I looked into it. I was able to connect to the "maze", and then had to learn how to work there within Python and also think about how to solve a maze. It took some intense googling but eventually my program was able to communicate with the maze and send commands and movement to it. 

As for the maze-solving algorithm, it's very simple: write in how many ways we can move from each position, and set one to '0' after we do it (so we know not to go that way again if we do come back to that position). We also make a list of the positions we've been two, and if we go back to one that was already on the list we delete everything after it, since that was not the way. Finally all solutions are listed and the shortest one is printed (though the given mazes only had one solution, so that part of the code is untested)
