<h1 align="center">
	Challenge 8 - Awesome Sales Inc.!
</h1>
	
### Instructions:
<p>
You've been contacted by a company called Awesome Sales Inc. They recently bought some new ultra-modern
AI based software for creating travel plans for their sales force. But, it seems to have a huge problem
and the developers have gone MIA. So they need you to figure out how to fix it.
</p>

<p>
The <i>"awesome"</i> software works with two modules. The first module (<samp>AICityPicker</samp>) picks
the best cities to be visited by each employee based on a number of the employee’s records and traits.
It also takes another important factor into account, which is that employees can move between cities
on an <b>ASCB</b> (<i>Awesome Sales Connection Bus</i>).
</p>

<p>
Once the cities have been picked by the AI, a plan is generated in the form of bus tickets that can
be used multiple times to move between cities. For example, <samp>t1: [A, B]</samp> is a ticket that
can be used to go from city A to city B and vice versa. In the plans, employees can always reach one
city from another using their tickets. For example, if an employee has to visit cities A, B and C,
there will always be a way to go from A to C, even if they have to go from A to B and then from B to C.
</p>

<p>
The other module (<samp>AICityRemover</samp>) is the one with the problems. Once a plan is generated,
this module evaluates budgets, costs and other things and picks cities from the initial plan to remove.
It cancels the bus tickets for them and everything else – all automatically.
</p>

<p>
The biggest problem is that this module doesn't take the <b>ASCB</b> into account. Cities are removed
and employees can no longer reach all their destinations. For example, if an employee has to visit
A, B and C, the module may remove B, even if none of the <b>ASCB</b> can go from A to C directly. So, when an employee finds themselves in that situation they have to find a way to reach their destination. Sometimes they pay for a regular bus ticket or taxi out of their own pocket or they might even ask a stranger for a ride. Not good.
</p>

<p>
Of course, you don't have access to the source code. But, you manage to reverse engineer the
<samp>AICityRemover</samp> module and find the root cause of the problem. A function called
<samp>currentPlan.getCriticalCitiesThatCannotBeRemoved()</samp> wasn't implemented and always
returns an empty list! Luckily, the documentation has some examples so you can work out your own implementation.
</p>

<p>
You need to write the <samp>getCriticalCitiesThatCannotBeRemoved()</samp> function so that for each
plan it returns a list of cities that can't be removed. In other words, the list of cities where if
any city is removed the initial plan breaks and the employee can't reach the rest of the cities
using their <b>ASCB</b> tickets.
</p>

<p>
Cities are removed one by one, so when a city is removed from the initial plan, other cities might
become critical now but that would be a whole new case. You need to provide the list of cities that
are critical from the initial plan.
<p>

<h3>Input</h3>
<p>
The first line will have an integer <b>C</b>, which is the number of cases for the problem. The
description of the <b>C</b> cases follows. For each case, the first line is an integer <b>T</b>
showing the number of tickets. Then <b>T</b> lines follow, each describing a ticket. Each ticket
is described in the form <samp>"City A,City B"</samp>, which means the ticket can be used to go
from <samp>City A</samp> to <samp>City B</samp> and vice versa.
</p>

<h3>Output</h3>
<p>
For each case, there should be a line starting with "<samp>Case #x: y</samp>", where x is the test case number
(starting from 1) and y is the list of the critical cities, in the form
<samp>"City A,City B"</samp>. The list should be ordered alphabetically. If none of the cities are
critical a dash (<samp>-</samp>) should be printed instead.
</p>

<h3>Limits</h3>
<ul class="list">
<li>1 &le; <b>C</b> &le; 100</li>
<li>1 &le; <b>T</b> &le; 1500</li>
</ul>

<h3>Sample Input</h3>

<pre>
3
2
Chicago,Houston
Houston,Dallas
4
Madrid,Barcelona
Barcelona,Zaragoza
Zaragoza,Valencia
Valencia,Madrid
6
París,Lyon
Lyon,Toulouse
Toulouse,Lille
Toulouse,Niza
Nantes,Niza
Niza,Lille
</pre>

<h3>Sample Output</h3>

<pre>
Case #1: Houston
Case #2: -
Case #3: Lyon,Niza,Toulouse
</pre>

## My notes: 

This challenge took a lot of effort, and my original solution was... really bad. It worked, but it was extremely inefficient because I basically made a full list for each point, saving all other points it could visit, and repeated a process several times until no new connections could be found. It worked for the test cases with reasonably-sized list of cities, but not for the one thousand or two thousand trips in the submission case. In my defense, people don't usually plan trips with seven hundred cities in them. 

The "good" solution had some steps: first making a list of all cities and their connections, then removing a city and checking if the graph was still connected. To do that, it would start from the first city and go to each new city it could find, writing their indexes. If it got done and they were all visited, the graph was connected. If there was any zero along the way, then it wasn't. The it'd make a list with these critical cities that can't be removed and print it. 

When the whole thing worked, I was very happy about it.

<img src="https://user-images.githubusercontent.com/27980285/147273152-c30c432c-185c-4146-b9eb-b71110b842a8.png" width="436" height="22">
