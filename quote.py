from gtts import gTTS
import os
import time
import random
import codecs

def load_quotes(filename):	
	text_file = codecs.open(filename, encoding='utf-8')
	lines = text_file.readlines()
	lines = [line.strip() for line in lines]
	return lines

def check_exists(i, sound_path='./sounds/'): 
	filename = sound_path + str(i) + '.mp3'
	return os.path.isfile(filename)

def create_missing_sounds(quotes, sound_path='./sounds/'):
	for i in range(len(quotes)):		
		if not check_exists(i):
			text = quotes[i]	
			tts = gTTS(text=text, lang='en')
			tts.save(sound_path + str(i) + ".mp3")

def ring(quotes, duration, sound_path='./sounds/'):
	beep = sound_path + 'beep.mp3'
	while True:
		i = random.randint(0, len(quotes) - 1)
		print(quotes[i])		
		os.system('start ' + beep)		
		time.sleep(3)
		os.system('start ' + sound_path + str(i) + '.mp3')
		time.sleep(duration)

def main():
	quotes = load_quotes('data.txt')
	create_missing_sounds(quotes)
	ring(quotes, 60)	

if __name__== "__main__":
	main()