<h1 align="center">
	Challenge 2 - Catch them all
</h1>

### Instructions:
Something strange has happened. All your pokemons have escaped. Can you catch them all?

You've been given a map (shown with rows and columns) so you can find all the Pokémon. The Pokémon's name can only be found horizontally. But it can be written from left to right or right to left and it can be on more than one line. Once you catch a Pokémon make sure to remove it from the map. Because each Pokémon only appears once and some Pokémon can be hidden within other Pokémon.

### Input
The first line will have an Integer <b>N</b>, which is the number of cases for the problem. It is followed by a description of <b>T</b> cases.
Every case has an Integer <b>P</b>, which is the number of Pokémon to find, an Integer <b>R</b>, which is the number of rows, and an Integer <b>C</b>, which is the number of columns.
Then it has <b>P</b> lines with the names of each Pokémon <b>N</b>. And finally <b>R</b> lines with <b>C</b> characters split by an empty space.

### Output
<p>For each case, there should be a line starting with "Case #x: " followed by the result of the map without the Pokémon.</p>

<h3>Limits</h3>
<pre>
1 &le; T &le; 20
1 &le; P &le; 50
1 &le; C, R &le; 100
1 &le; N &le; 100
</pre>

<h3>Sample Input</h3>
<pre>
2
1 4 6
SNORLAX
T A K E C A
S N O R L A
X R E W I T
H V E N O M
2 3 10
PIKACHU
CHARIZARD
N O P O K E M U H C
A K I C H A R I Z A
R D P O N S H E R E
</pre>
<h3>Sample Output</h3>

<pre>
Case #1: TAKECAREWITHVENOM
Case #2: NOPOKEMONSHERE
</pre>
<h3>Explanation</h3>

<p>
    There is a map like the table below in the first scenario.
</p>

<table class="center-content">
    <tr>
        <td>T</td>
        <td>A</td>
        <td>K</td>
        <td>E</td>
        <td>C</td>
        <td>A</td>
    </tr>
    <tr>
        <td>S</td>
        <td>N</td>
        <td>O</td>
        <td>R</td>
        <td>L</td>
        <td>A</td>
    </tr>
    <tr>
        <td>X</td>
        <td>R</td>
        <td>E</td>
        <td>W</td>
        <td>I</td>
        <td>T</td>
    </tr>
    <tr>
        <td>H</td>
        <td>V</td>
        <td>E</td>
        <td>N</td>
        <td>O</td>
        <td>M</td>
    </tr>
</table>
<p> After you find SNORLAX you have the expected result. </p>
<table class="center-content">
    <tr>
        <td>T</td>
        <td>A</td>
        <td>K</td>
        <td>E</td>
        <td>C</td>
        <td>A</td>
    </tr>
    <tr>
        <td>R</td>
        <td>E</td>
        <td>W</td>
        <td>I</td>
        <td>T</td>
        <td>H</td>
    </tr>
    <tr>
        <td>V</td>
        <td>E</td>
        <td>N</td>
        <td>O</td>
        <td>M</td>
        <td> </td>
    </tr>
</table>
<p>
There is a map like the table below in the second scenario.
</p>
<table class="center-content">
    <tr>
        <td>N</td>
        <td>O</td>
        <td>P</td>
        <td>O</td>
        <td>K</td>
        <td>E</td>
        <td>M</td>
        <td>U</td>
        <td>H</td>
        <td>C</td>
    </tr>
    <tr>
        <td>A</td>
        <td>K</td>
        <td>I</td>
        <td>C</td>
        <td>H</td>
        <td>A</td>
        <td>R</td>
        <td>I</td>
        <td>Z</td>
        <td>A</td>
    </tr>
    <tr>
        <td>R</td>
        <td>D</td>
        <td>P</td>
        <td>O</td>
        <td>N</td>
        <td>S</td>
        <td>H</td>
        <td>E</td>
        <td>R</td>
        <td>E</td>
    </tr>
</table>
<p>
You can't find PIKACHU (UHCAKIP) until CHARIZARD has been caught.
</p>
<table class="center-content">
    <tr>
        <td>N</td>
        <td>O</td>
        <td>P</td>
        <td>O</td>
        <td>K</td>
        <td>E</td>
        <td>M</td>
        <td>U</td>
        <td>H</td>
        <td>C</td>
    </tr>
    <tr>
        <td>A</td>
        <td>K</td>
        <td>I</td>
        <td>P</td>
        <td>O</td>
        <td>N</td>
        <td>S</td>
        <td>H</td>
        <td>E</td>
        <td>R</td>
    </tr>
    <tr>
        <td>R</td>
        <td> </td>
        <td> </td>
        <td> </td>
        <td> </td>
        <td> </td>
        <td> </td>
        <td> </td>
        <td> </td>
        <td> </td>
    </tr>
</table>
<p>
All the Pokémon have been caught.
</p>

<table class="center-content">
    <tr>
        <td>N</td>
        <td>O</td>
        <td>P</td>
        <td>O</td>
        <td>K</td>
        <td>E</td>
        <td>M</td>
        <td>O</td>
        <td>N</td>
        <td>S</td>
    </tr>
    <tr>
        <td>H</td>
        <td>E</td>
        <td>R</td>
        <td>E</td>
        <td> </td>
        <td> </td>
        <td> </td>
        <td> </td>
        <td> </td>
        <td> </td>
    </tr>
</table>

## My notes: 

Python built-in string methods were a blessing for this one, since the bulk of the job was to try to find strings in the given map, looping until all of the given Pókemon were found. The given Pókemeon were always found and each of them appeared exactly once, so we didn't have to handle edge cases with missing or duplicate mons. 
