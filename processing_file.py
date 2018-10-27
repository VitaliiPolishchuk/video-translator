import urllib.request
import urllib.error
import re
import sys
import time
import os
import pipes
import wave
import contextlib
import shutil
from mutagen.mp3 import MP3
from datetime import timedelta
from srt import *

def video_to_audio(fileName):
	try:
		file, file_extension = os.path.splitext(fileName)
		file = pipes.quote(file)
		# video_to_wav = 'ffmpeg -i ' + file + file_extension + ' ' + file + '.mp3'	
		video_to_wav = 'ffmpeg -i ' + fileName +' -vn -acodec pcm_s16le -ar 44100 -ac 1 output.wav'
		# final_audio = 'lame '+ file + '.wav' + ' ' + file + '.wav'
		os.system(video_to_wav)
		# os.system(final_audio)
		#file=pipes.quote(file)
		#os.remove(file + '.wav')
		print("sucessfully converted ", fileName, " into audio!")
	except OSError as err:
		print(err.reason)
		exit(1)

def replace_audio(video_file, audio_file, video_output):
	video_to_wav = 'ffmpeg -i ' + video_file + ' -i ' + audio_file + ' -c:v copy -map 0:v:0 -map 1:a:0 ' + video_output
	os.system(video_to_wav)

def update_speed(file, output_file_update, duration_update):
	audio = MP3(file)
	duration_primitive = audio.info.length
	atempo = '"atempo=' +str(round(float(duration_primitive) / float(duration_update) , 2)) + '" '
	command_to_update = 'ffmpeg -i ' + file + ' -filter:a ' + atempo + str(output_file_update)
	print(command_to_update)
	os.system(command_to_update)	
	path = 'C:/Users/Champion/Documents/Sublime project/Python project/Google Translator video/'
	shutil.move(path + output_file_update, path + "input_audio/" + output_file_update)

def create_srt(speech, srt_file):
	subs = []
	for i, val in enumerate(speech):
      		sub = Subtitle(index=i, start=timedelta(seconds = val['start']), end=timedelta(seconds = val['end']), content=val['alternative'])
      		subs.append(sub)
	sbt = compose(subs)
	print(sbt)
	file = open(srt_file, 'w', encoding='utf-8')
	file.write(sbt)
	file.close()

def add_sub(video_file, srt_file_native, srt_file_translated, video_output):
	command_add_sub = 'ffmpeg -i ' + video_file + ' -i ' + srt_file_native + ' -i ' + srt_file_translated + ' -c:s mov_text -c:v copy -c:a copy -map 0:v -map 0:a -map 1 -map 2 -metadata:s:s:0 language=spa -metadata:s:s:1 language=eng ' + video_output
	os.system(command_add_sub)

# update_speed('output1.wav', 'output_update1.wav', float(3))