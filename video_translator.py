import os
import pipes
import wave
import contextlib
import shutil

from processing_file import *
from processing_audio import *
from translate import *
from transcript import *

video_file = 't22' + '.mp4'

# src = 'en'
# trg = 'uk'
# sup_voice =  'uk'
# sup_lang = 'en-US'

src = 'uk'
trg = 'en'
sup_voice =  'en'
sup_lang = 'uk-UA'

# src = 'ru'
# trg = 'uk'
# sup_voice =  'uk'
# sup_lang = 'ru'

audio_file_name = 'output.wav'

video_to_audio(video_file)
# # Instantiates a client
result = voice_to_text(audio_file_name, sup_lang)

speech_native = get_speech(result)

create_srt(speech_native, src + '.srt')

speech_translate = translate_transcript(result, src, trg)
print(speech_translate)

create_srt(speech_translate, trg + '.srt')

audio_format = '.mp3'

counter = 0
for _speech in speech_translate:
	synthesize_text(_speech['alternative'], sup_voice ,'output' + str(counter) + audio_format)
	update_speed('output' + str(counter) + audio_format, 'output_updated' + str(counter) + audio_format, float(_speech['end']) - float(_speech['start']))
	counter += 1
	# print(_speech)



create_audio(speech_translate, "input_audio", 'whole_audio.wav')

replace_audio(video_file, 'whole_audio.wav', "translated_video.mp4")

video_with_native_sub = "subtitles_native.mp4"

add_sub("translated_video.mp4", src + '.srt', trg + '.srt', video_with_native_sub)

video_with_translated_sub = "subtitles_translated.mp4"
# print(speech)