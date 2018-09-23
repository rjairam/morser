# Morser - a simple morse code command line utility
# Ria Jairam, N2RJ
# n2rj@arrl.net


import RPi.GPIO as GPIO
import time
import sys

#Speed per PARIS protocol
WPM = 20

#Base compensated speed
Base = WPM*1.9

#Calculate dits, dahs, words
ditLength = 2.4/Base
dahLength = ditLength*3
wordSpacing = ditLength*7

#Output pin. Layout is BOARD not BCM
spkrpin = 18

#Morse characters
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

#Some weird reason, need a delay after initializing GPIO.
time.sleep(1)

# Play a dit
def dit():
    t_end = time.time() + ditLength
    while time.time() < t_end:
       	GPIO.output(spkrpin,0)
       	time.sleep(.0005)
       	GPIO.output(spkrpin,1)
    	time.sleep(.0005)
    time.sleep(ditLength)

# Play a dah
def dah():
    t_end = time.time() + dahLength
    while time.time() < t_end:
       	GPIO.output(spkrpin,0)
       	time.sleep(.0005)
       	GPIO.output(spkrpin,1)
    	time.sleep(.0005)
    time.sleep(ditLength)
	

# Play a word in morse
def playword( str ):
    for letter in str:
    	        for symbol in CODE[letter.upper()]:
				if symbol == '-':
					dah()
				elif symbol == '.':
					dit()
				else:
					time.sleep(ditLength)
		time.sleep(ditLength)
	        
		sys.stdout.write(letter)	
		sys.stdout.flush()

# Main - take each parameter (word) then play back each word char by char. Write letter by letter to stdio
def main():
	try:
		args = len(sys.argv) - 1

		pos = 1  
		while (args >= pos):  
    			playword(sys.argv[pos])
    			pos = pos + 1
    			sys.stdout.write(' ')
    			sys.stdout.flush()
    			time.sleep (wordSpacing)
		print

	except KeyboardInterrupt:
		print
       		print ("Caught interrupt, exiting...")
	except:
		print
		print ("Fatal error, exiting...")
	finally:
		#Ensure GPIO is cleaned up when done
		GPIO.cleanup()
main()
