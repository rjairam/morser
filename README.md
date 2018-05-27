# morser

A really simple utility to take text from the command line and play it through a speaker attached to your GPIO.

v 0.3 Alpha known issues
- Speed is variable. Change "WPM" variable.
- Morse beep is slightly higher pitched when starting. Could be due to GPIO timing and/or loading.
- GPIO access requires elevated privilege. Run it using sudo or run as root.

How to use:
- Attach a passive piezo buzzer to pin 18 and ground. (you can change the output pin in the code) Moving coil speakers may work, but you may need a driver circuit. I have used one with a 220uF cap in series. 

Ideas here:
https://raspberrypi.stackexchange.com/questions/47324/hooking-up-a-speaker-to-the-gpio?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa

To send morse, type:
```python morser.py <whatever text you want to hear in morse code>```

For example, play back your IP address of eth0 in morse:

```sudo python morser.py `ifconfig eth0 2>/dev/null|awk '/inet addr:/ {print $2}'|sed 's/addr://'` ```

LICENSE:

Freeware, with attribution. Please do let me know when/where you use it. I'm good in QRZ. (n2rj@arrl.net)

Have fun!

73, Ria, N2RJ
