<h1 align="center">
	Challenge 10 - Packets delivery
</h1>
	
### Instructions:

<p>
We've discovered a security hole in the enemy communication system and we need your
help to move forward.
</p>

<p>
Thanks to our secret agent, we found out the enemy was using a quite exotic
physical transport layer described in the experimental <a href="https://datatracker.ietf.org/doc/html/rfc1149">RFC 1149</a>.
However, you don't need to be an expert in that RFC, since we've already
been able to do a MITM attack on the communication system (with a shotgun) and extract
the packets.
</p>

<p>
What do we need from you? Because we've heard you're a forensics expert, we need
you to extract the information from the intercepted packets. You can
download them from this URL: <a href="10%20Packets/icmps.pcap">ICMPs pcap</a>.
</p>

<p>The test and submission passwords are the same. </p>

<h3>Input</h3>
No input needed

<h3>Output</h3>
<p>
The password hidden on the pcap file
</p>

## My notes:

I had no idea how to get started here, but thankfully found some command that let me view the contents of a pcap file. I stored that in a file and used that as the input for the program. Before doing anything else, I saw a hidden message in the file that said something like "What a mess, you need to reorder this" So I started ordering the packets using different parameters until I found one that had "PNG" and "IHDR" inside. A quick search revealed that those are chunks of a PNG file so I wrote those bytes to a .png after converting from hexadecimal and it revealed a QR code with the answer. 
