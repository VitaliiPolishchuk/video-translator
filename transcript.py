
import io
import os

from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
# Instantiates a client
def voice_to_text(file_audio, sup_lang):
	client = speech.SpeechClient()

	# The name of the audio file to transcribe
	file_name = 'OSR_us_000_0010_8k.wav'

	# Loads the audio into memory
	with io.open(file_name, 'rb') as audio_file:
	    content = audio_file.read()
	    audio = types.RecognitionAudio(content=content)

	config = types.RecognitionConfig(
			encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
	        sample_rate_hertz=8000,
	        language_code=sup_lang,
	        enable_word_time_offsets=True)

	operation = client.long_running_recognize(config, audio)

	result = operation.result(timeout=90)
	print(result)
	return result
