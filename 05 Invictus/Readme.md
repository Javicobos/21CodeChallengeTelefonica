
<h1 align="center">
	Challenge 5 - Invictus
</h1>
	
### Instructions:

<pre>
INVICTUS

Out of the night that covers me,
      Black as the pit from pole to pole,
I thank whatever gods may be
      For my unconquerable soul.

In the fell clutch of circumstance
      I have not winced nor cried aloud.
Under the bludgeonings of chance
      My head is bloody, but unbowed.

Beyond this place of wrath and tears
      Looms but the Horror of the shade,
And yet the menace of the years
      Finds and shall find me unafraid.

It matters not how strait the gate,
      How charged with punishments the scroll,
I am the master of my fate,
      I am the captain of my soul.

William Ernest Henley
</pre>

<h3>Input</h3>
Find the PASSWORD hidden in the following file: <a href="/05%20Invictus/Invictus.txt" download>Invictus.txt</a>

<h3>Output</h3>
Find the PASSWORD. It contains the SURNAME in UPPERCASE of the famous person in the picture.

## My notes:

When I got to this challenge, I could see why a lot of people had skipped it. I had no idea where to start, but saw that there were some weird non-ascii characters in the given txt. I tried subtracting many different values but couldn't really see anything after many tries, so I decided to list them and saw that there seemed to be a pattern. The characters were in blocks of four and the first two in each block were always the same, so I got rid of them. I knew that I had to find "MANDELA" so I looked at the differences in ascii between those letters and then tried to find those same differences between characters in the file. It took a while to realize that I had to compare the fourth character in each block with the next one but eventually I saw that MANDELA was there and that gave me the required number to subtract to those characters, which  was 110. These characters all had a 129 before them but others had a 130, however with this method we had NEL_ON somewhere else in the password which gave the key to turn that missing character into an S, which was 46.
