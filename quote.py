from gtts import gTTS
import os
import time
import random
import codecs
from flask import Flask

def load_quotes(filename):	
	text_file = codecs.open(filename, encoding='utf-8')
	lines = text_file.readlines()
	lines = [line.strip() for line in lines]
	return lines

def check_exists(i, sound_path='./static/'): 
	filename = sound_path + str(i) + '.mp3'
	return os.path.isfile(filename)

def create_missing_sounds(quotes, sound_path='./static/'):
	for i in range(len(quotes)):		
		if not check_exists(i):
			text = quotes[i]	
			tts = gTTS(text=text, lang='en')
			tts.save(sound_path + str(i) + ".mp3")

interval = 30
quotes = load_quotes('data.txt')
create_missing_sounds(quotes)
app = Flask(__name__)	

@app.route("/")
def home():

	quote_index = random.randint(0, len(quotes) - 1)
	quote = quotes[quote_index]	
	audio = "<audio controls autoplay><source src='/static/" + str(quote_index) + ".mp3' type='audio/mpeg'></audio>"
	text = (
		'<html>'
		+ '<head>'
		+ '<meta http-equiv="refresh" content="' + str(interval) + '">'
		+ '</head><body style="font-size: 3em; text-align: center; background-color: green; color: white">'
		+ quote + "<br/>"
		+ audio
		+ "</body></html>"
	)
	return text