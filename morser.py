import RPi.GPIO as GPIO
import time
import sys

#Speed per PARIS protocol
WPM = 20
ditSpeed = 2.4/WPM
dahSpeed = ditSpeed*3
wordSpeed = ditSpeed*7
spkrpin = 18

CODE = {' ': ' ', 
        "'": '.----.', 
        '(': '-.--.-', 
        ')': '-.--.-', 
        ',': '--..--', 
        '-': '-....-', 
        '.': '.-.-.-', 
        '/': '-..-.', 
        '0': '-----', 
        '1': '.----', 
        '2': '..---', 
        '3': '...--', 
        '4': '....-', 
        '5': '.....', 
        '6': '-....', 
        '7': '--...', 
        '8': '---..', 
        '9': '----.', 
        ':': '---...', 
        ';': '-.-.-.', 
        '?': '..--..', 
        'A': '.-', 
        'B': '-...', 
        'C': '-.-.', 
        'D': '-..', 
        'E': '.', 
        'F': '..-.', 
        'G': '--.', 
        'H': '....', 
        'I': '..', 
        'J': '.---', 
        'K': '-.-', 
        'L': '.-..', 
        'M': '--', 
        'N': '-.', 
        'O': '---', 
        'P': '.--.', 
        'Q': '--.-', 
        'R': '.-.', 
        'S': '...', 
        'T': '-', 
        'U': '..-', 
        'V': '...-', 
        'W': '.--', 
        'X': '-..-', 
        'Y': '-.--', 
        'Z': '--..', 
        '_': '..--.-'}


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(spkrpin,GPIO.OUT)

def dit():
    ditSpeed=2.4/WPM
    t_end = time.time() + ditSpeed
    while time.time() < t_end:
       	GPIO.output(spkrpin,0)
       	time.sleep(.0004)
       	GPIO.output(spkrpin,1)
    	time.sleep(.0004)
    time.sleep(ditSpeed)


def dah():
    t_end = time.time() + dahSpeed
    while time.time() < t_end:
       	GPIO.output(spkrpin,0)
       	time.sleep(.0004)
       	GPIO.output(spkrpin,1)
    	time.sleep(.0004)
    time.sleep(ditSpeed)
	


def playword( str ):
	print str
	for letter in str:
			for symbol in CODE[letter.upper()]:
				print symbol
				if symbol == '-':
					dah()
				elif symbol == '.':
					dit()
				else:
					time.sleep(ditSpeed)
			time.sleep(ditSpeed)


args = len(sys.argv) - 1

pos = 1  
while (args >= pos):  
    playword(sys.argv[pos])
    pos = pos + 1
    time.sleep (wordSpeed)
