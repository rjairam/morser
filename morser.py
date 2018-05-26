import RPi.GPIO as GPIO
import time
import sys

#Speed per PARIS protocol
WPM = 60

#Base compensated speed
Base = WPM*1.9

#Calculate dits, dahs, words
ditSpeed = 2.4/Base
dahSpeed = ditSpeed*3
wordSpeed = ditSpeed*7

#Output pin
spkrpin = 18

#Store Morse in an array
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

#GPIO setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(spkrpin,GPIO.OUT)

#dits
def dit():
    t_end = time.time() + ditSpeed
    while time.time() < t_end:
       	GPIO.output(spkrpin,0)
       	time.sleep(.0004)
       	GPIO.output(spkrpin,1)
    	time.sleep(.0004)
    time.sleep(ditSpeed)

#dahs
def dah():
    t_end = time.time() + dahSpeed
    while time.time() < t_end:
       	GPIO.output(spkrpin,0)
       	time.sleep(.0004)
       	GPIO.output(spkrpin,1)
    	time.sleep(.0004)
    time.sleep(ditSpeed)
	

#Play the word in morse
def playword( str ):
    for letter in str:
    	        for symbol in CODE[letter.upper()]:
				if symbol == '-':
					dah()
				elif symbol == '.':
					dit()
				else:
					time.sleep(ditSpeed)
		time.sleep(ditSpeed)
	        
		sys.stdout.write(letter)	
		sys.stdout.flush()


args = len(sys.argv) - 1

#Loop through command line args and play each word
pos = 1  
while (args >= pos):  
    playword(sys.argv[pos])
    pos = pos + 1
    sys.stdout.write(' ')
    sys.stdout.flush()
    time.sleep (wordSpeed)
