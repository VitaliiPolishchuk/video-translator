

from processing_file import *
from processing_audio import *
from translate import *
from transcript import *

video_file = 'We'

src = 'en'
trg = 'fr'
sup_voice = 'fr-FR'
sup_lang = 'en-US'
audio_file_name = 'OSR_us_000_0010_8k.wav'

# video_to_audio(video_file + '.mp4')
# Instantiates a client
# result = voice_to_text(audio_file_name, sup_lang)
# print(result)
# speech = translate_transcript(result, src, trg)

# counter = 0
# for _speech in speech:
# 	synthesize_text(_speech['alternative'], sup_voice ,'output' + str(counter) + '.mp3')
# 	counter = counter + 1

# create_audio(speech, "input", 'whole_audio.wav')

replace_audio("video_test.mp4", "out_sine.wav", "translated_video.mp4")


# print(speech)