import RPi.GPIO as GPIO
import time
import sys

speed=0.25
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
GPIO.setup(18,GPIO.OUT)

def dit():
    t_end = time.time() + speed*0.25
    while time.time() < t_end:
       	GPIO.output(18,0)
       	time.sleep(.0004)
       	GPIO.output(18,1)
    	time.sleep(.0004)
    time.sleep(0.25)


def dah():
    t_end = time.time() + speed
    while time.time() < t_end:
       	GPIO.output(18,0)
       	time.sleep(.0004)
       	GPIO.output(18,1)
    	time.sleep(.0004)
    time.sleep(0.25)
	


def playword( str ):
	for letter in "10.25.234.254":
			for symbol in CODE[letter.upper()]:
				print symbol
				if symbol == '-':
					dah()
				elif symbol == '.':
					dit()
				else:
					time.sleep(0.25)
			time.sleep(0.25)


args = len(sys.argv) - 1

pos = 1  
while (args >= pos):  
    playword(args)
    pos = pos + 1
    time.sleep (0.1)
