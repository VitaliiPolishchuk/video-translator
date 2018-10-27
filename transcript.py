
import io
import os

from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
# Instantiates a client
def voice_to_text(file_audio, sup_lang):
	client = speech.SpeechClient()

	# Loads the audio into memory
	with io.open(file_audio, 'rb') as audio_file:
	    content = audio_file.read()
	    audio = types.RecognitionAudio(content=content)

	config = types.RecognitionConfig(
			encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
	        sample_rate_hertz=44100,
	        language_code=sup_lang,
	        enable_word_time_offsets=True)

	operation = client.long_running_recognize(config, audio)

	result = operation.result(timeout=90)
	print(result)
	return result
