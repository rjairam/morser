# morser

A really simple utility to take text from the command line and play it through a speaker attached to your GPIO.

v 0.2 Alpha known issues
- Has a fixed speed. Plan to make that variable in the future
- Cadence of morse characters needs to be adjusted
- Morse beep is slightly higher pitched when starting.

How to use:
- Attach an ordinary speaker or passive piezo buzzer to pin 18 and ground.
- python morser.py <whatever text you want to hear in morse code>

For example, play back your IP address of eth0 in morse:

python morser.py `ifconfig eth0 2>/dev/null|awk '/inet addr:/ {print $2}'|sed 's/addr://'`

LICENSE:

Freeware, with attribution. Please do let me know when/where you use it. I'm good in QRZ. (n2rj@arrl.net)

Have fun!
73, Ria, N2RJ
