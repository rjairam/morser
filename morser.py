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

#Output pin
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

time.sleep(1)

#dits
def dit():
    t_end = time.time() + ditLength
    while time.time() < t_end:
       	GPIO.output(spkrpin,0)
       	time.sleep(.0005)
       	GPIO.output(spkrpin,1)
    	time.sleep(.0005)
    time.sleep(ditLength)

#dahs
def dah():
    t_end = time.time() + dahLength
    while time.time() < t_end:
       	GPIO.output(spkrpin,0)
       	time.sleep(.0005)
       	GPIO.output(spkrpin,1)
    	time.sleep(.0005)
    time.sleep(ditLength)
	

#Play the word in morse
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

#Main loop
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
		GPIO.cleanup()
main()
