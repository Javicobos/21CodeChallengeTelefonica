<h1 align="center">
	Challenge 3 - The night of the hunter
</h1>
	
### Instructions:
Love or Hate? True or False? Create or Destroy? Which word would win in a hypothetical fight between antonyms? It depends on the values of the letters, of course.

<h3>Input</h3>
<p>
The first line has an integer <b>N</b>, which is the number of cases for the problem. Each case is a fight
between two antonyms. Each line has:

<ol class="list">
  <li>Two opposite words separated by '-'</li>
  <li>The character '|'</li>
  <li>The value of each letter, which can be an integer or a fraction. The list of letters with its values can be in many formats:
    <ul class="list">
      <li>As a dictionary: <br><pre>{'a': 2/3, 'e': 4, 'h': 3, 'l': 5, 'o': 1, 't': 6, 'v': 0}</pre></li>
      <li>As a list of tuples: <br><pre>[('a', 2/3), ('e', 4), ('h', 3), ('l', 5), ('o', 1), ('t', 6), ('v', 0)]</pre></li>
      <li>As a list of assignments: <br><pre>a=2/3,e=4,h=3,l=5,o=1,t=6,v=0</pre></li>
    </ul>
  </li>
</ol>
</p>

<h3>Output</h3>
<p>For each case, there should be a line starting with "Case #x: " followed by the winning word or '-' when the result is a draw. </p>

<h3>Sample Input</h3>
<pre>10
love-hate|a=2,e=4,h=3,l=5,o=1,t=6,v=0
low-high|[('g', 1/3), ('h', 2), ('i', 1/9), ('l', 4), ('o', 0), ('w', 1/8)]
clever-stupid|c=6/9,d=5/6,e=8/9,i=1/7,l=0,p=8/10,r=5/10,s=6/9,t=5/6,u=4/10,v=3/8
lose-find|{'d': 3, 'e': 0, 'f': 5, 'i': 2, 'l': 1, 'n': 4, 'o': 7, 's': 6}
win-lose|e=1,i=4,l=2,n=0,o=6,s=3,w=5
blame-praise|[('a', 5), ('b', 8), ('e', 4), ('i', 2), ('l', 0), ('m', 1), ('p', 3), ('r', 6), ('s', 7)]
false-true|{'a': 7/9, 'e': 2/5, 'f': 3, 'l': 0, 'r': 7, 's': 2, 't': 5, 'u': 1/5}
soft-hard|a=0,d=1,f=4,h=7,o=2,r=5,s=6,t=3
rough-smooth|g=7/10,h=7/9,m=3,o=4,r=6,s=1,t=4/5,u=3/10
tame-wild|{'a': 1, 'd': 5, 'e': 3, 'i': 0, 'l': 2, 'm': 4, 't': 7, 'w': 6}
</pre>

<h3>Sample Output</h3>
<pre>Case #1: hate
Case #2: high
Case #3: stupid
Case #4: -
Case #5: lose
Case #6: praise
Case #7: true
Case #8: soft
Case #9: smooth
Case #10: tame
</pre>

## My notes: 

This problem took a lot of work, as I had to manually parse each type of input and turn it into a dictionary so it could be understood by the code. I'm 95% sure it could have been done in a faster way but I didn't know how to so that's what I did. After the information was parsed, I removed all denominators by multiplying all fractions (and numbers) by each denominator. It's not a fantastic method as it does use the GCD and it will do the same thing twice for a duplicate denominator, but it works well enough for the given data even if the numbers are a bit larger than they have to be. Importing math would've saved some time. 
Once the values for each letter were calculated as a whole number, getting the solution just meant adding all letters of each word and comparing. 
