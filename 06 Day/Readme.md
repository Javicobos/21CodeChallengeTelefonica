
<h1 align="center">
	Challenge 6 - What day is it?
</h1>
	
### Instructions:

Have you ever wondered what day of the week a date is? I'm sure you have. In this challenge, you have to code a program to figure out how to tell anybody the day of the week (from a list of languages) for a given date.

<h3>Input</h3>
<p>
The first line has an integer N, which is the number of cases for the problem. Each case has a date, the character ':' and a two-letter language code.
<ol class="list">
  <li>The date format can be: YYYY-MM-DD or DD-MM-YYYY </li>
  <li>All dates are after 1970-01-01 </li>
  <li>Input cases may have invalid dates, like an invalid month (MM>13) or an invalid day of a month </li>
  <li>The weekday of a date can be given in any of these twenty languages:
  </li>
</ol>
<table>
  <tr>
    <td>CA: catalan</td>
    <td>CZ: czech</td>
    <td>DE: german</td>
    <td>DK: danish</td>
    <td>EN: english</td>
  </tr>
  <tr>
    <td>ES: spanish</td>
    <td>FI: finnish</td>
    <td>FR: french</td>
    <td>IS: icelandic</td>
    <td>GR: greek</td>
  </tr>
  <tr>
    <td>HU: hungarian</td>
    <td>IT: italian</td>
    <td>NL: dutch</td>
    <td>VI: vietnamese</td>
    <td>PL: polish</td>
  </tr>
  <tr>
    <td>RO: romanian</td>
    <td>RU: russian</td>
    <td>SE: swedish</td>
    <td>SI: slovenian</td>
    <td>SK: slovak</td>
  </tr>
</table>

</p>

<h3>Output</h3>
<p>For each case, there should be a line starting with "Case #x: " followed by the weekday IN LOWERCASE of the day in the indicated language, or 'INVALID_DATE' if given date is invalid, or 'INVALID_LANGUAGE' for an unknown language code.
</p>

<h3>Sample Input</h3>
<pre>12
2021-04-01:ES
2021-04-07:ES
01-02-2021:GR
2021-02-07:VI
2021-02-01:DE
01-02-2021:EN
01-02-2021:XX
29-02-2021:FR
15-20-2020:EN
2020-02-29:RU
01-02-2021:CA
2021-02-01:CZ
</pre>

<h3>Sample Output</h3>
<pre>Case #1: jueves
Case #2: miércoles
Case #3: δευτέρα
Case #4: chủ nhật
Case #5: montag
Case #6: monday
Case #7: INVALID_LANGUAGE
Case #8: INVALID_DATE
Case #9: INVALID_DATE
Case #10: суббота
Case #11: dilluns
Case #12: pondělí
</pre>

## My notes:
This challenge was painful. First, I had to find the days of the week in all those languages and paste them into a matrix. This seemed hard enough but turned out to be even harder when, upon checking the answers, I found that many used characters that weren't exactly right. I had to copy and paste from many different sources (the best ones being Wikipedia and Google translate) until all of the days seemed to be correct.


As for the actual code to know what day it is, I basically counted back years until 1970-01-01, a Thursday. To do this, we count a day forward for each year and two days for each leap year (with a special rule for Century leap years). Then we count the days for each month that has fully passed in the given year, and then finally the days in that month until we find the desired day. We work mod 7 so that we roll over to Monday after a week is completed, and that tells us the result. 
