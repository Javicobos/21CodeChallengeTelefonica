<h1 align="center">
	Challenge 9 - Collisions!
</h1>
	
### Instructions:
We’re building the collision detection module for our 2D game engine. We want to be able to process a lot of sprites at the same time and detect all the collisions. We'll provide the bitmask for each sprite, where 0 indicates transparency and 1 indicates a solid part of the sprite. If two solid parts of different sprites share the same location then it's counted as a collision. If two sprites collide at different points a single collision is counted. A sprite can collide with multiple other sprites.

Given a set of sprites, return how many collisions are detected.

<h3>Limits</h3>
<ul class="list">
  <li>T &le; 10</li>
  <li>D &le; 10</li>
  <li>W, H &le; 512</li>
  <li>P &le; 50000</li>
  <li>X, Y &le; 100000</li>
</ul>

<h3>Input</h3>
<p>The first line will have an integer <b>T</b>, which is the number of cases for the problem. The next
line has an integer <b>D</b>, which is the number of sprite definitions. <b>D</b> sprite bitmask
definitions follow. Each sprite bitmask definition starts with a line with two integers
<b>W</b>, <b>H</b>, which are the width and height of the sprite followed by <b>H</b> lines of length <b>W</b> of 0's or
1's. <b>T</b> test cases follow. Each case starts with an integer <b>P</b>, which is the number of sprite
positions in the test. <b>P</b> lines follow and each line has 3 integers: <b>I</b>, <b>X</b>, <b>Y</b>, where
<b>I</b> is the sprite identifier (from 0 to <b>D</b>-1), and <b>X</b>, <b>Y</b> are the coordinates of the sprite.</p>

<p>The (0,0) coordinate is the top-left corner of the display and sprites. </p>

<h3>Output</h3>
<p>For each case, there should be a line starting with "Case #x: " followed by the number of collisions for that test case.</p>

<h3>Sample Input</h3>
<pre>
3
2
16 8
0000100000100000
0000010001000000
0000111111100000
0001101110110000
0011111111111000
0010111111101000
0010100000101000
0000011011000000
4 4
0110
1111
1111
0110
2
0 0 0
1 2 2
5
0 0 2
1 0 2
1 5 0
1 11 2
1 12 8
6
0 0 2
1 7 0
1 1 2
1 10 2
1 12 5
1 2 2
</pre>

<h3>Sample Output</h3>
<pre>
Case #1: 1
Case #2: 0
Case #3: 6
</pre>

## My notes: 

I wasn't sure how to approach this challenge in a way that wouldn't take 6 million years, so after some thinking with a friend (thanks Fen!) we had some ideas about how this could work. First, check if two sprites overlap at all or not. If there is some overlap, we'd then get the offset needed to compare the corresponding points in the overlapping region, seeing if we find a 1 that matches a 1. If we do, we add a collision to our total and go to the next sprite. For each sprite, we work with all sprites after it so the process takes less and less time as it gets closer to the end. 

Accessing the right element in a given list of matrices was fun, and it let me write terrifying lines such as:
<img src="https://user-images.githubusercontent.com/27980285/147273543-84a7d0e2-43df-416a-82a4-c7cb3ce8cf08.png" width="1163" height="19">

The final version of the program took about 10 minutes to finish the submission output, but considering that the final case had 50 thousand 300x300 sprites with a total of more than 120 thousand collisions, I thought it was good enough. (Though it can probably be done way faster)
