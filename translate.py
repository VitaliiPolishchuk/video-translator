from googleapiclient.discovery import build


def translate(text, src, trg):

  # Build a service object for interacting with the API. Visit
  # the Google APIs Console <http://code.google.com/apis/console>
  # to get an API key for your own application.
  service = build('translate', 'v2',
            developerKey='AIzaSyAjpIj2X-vjp4iWjqnPqW8QDXbPF1nDNlg')
  translated_text = service.translations().list(
      source=src,
      target=trg,
      q=[text]
    ).execute()

  return translated_text

def translate_transcript(transcript, src, trg):
  speech = []
  for result in transcript.results:
    alternative = result.alternatives[0]
    for i, word in enumerate(alternative.words):
        print(word)
        word_start = word.start_time.seconds + word.start_time.nanos * 1e-9
        word_end = word.end_time.seconds + word.end_time.nanos * 1e-9
        if word_end - word_start > 1:
           word_start = word_end - 1
        if i == 0:
            start = word_start
        if i == len(alternative.words) - 1:
            end = word_end
    translated_text = translate(alternative.transcript, src, trg)
    alt = {"alternative": translated_text['translations'][0]['translatedText'], "start":start, "end":end}
    speech.append(alt)
    # delta = 5
    # for i, word in enumerate(alternative.words):
    #     print(word)
    #     word_start = word.start_time.seconds + word.start_time.nanos * 1e-9
    #     word_end = word.end_time.seconds + word.end_time.nanos * 1e-9
    #     if word_end - word_start > 1:
    #        word_start = word_end - 1
    #     if i == 0 or i % delta == 1:
    #         start = word_start
    #     if i == len(alternative.words) - 1 or i % delta == 0:
    #         print(alternative.transcript)
    #         end = word_end
    #         if alternative.transcript != "":
    #             text = translate(alternative.transcript, src, trg)
    #             print(text)
    #             arrText = text['translations'][0]['translatedText'].split(" ")
    #             count_delta = (int)(i / delta)
    #             arrSubContent = arrText[(count_delta - 1) * delta:count_delta * delta]
    #             strText = ""
    #             for word in arrSubContent:
    #                 strText += word + ' '
    #             print(text)
    #             alt = {"alternative": strText, "start":float(start), "end":float(end)}
    #             speech.append(alt)
  return speech

def get_speech(transcript):
  speech = [] 
  for result in transcript.results:
    alternative = result.alternatives[0]
    delta = 9
    for i, word in enumerate(alternative.words):
        print(word)
        word_start = word.start_time.seconds + word.start_time.nanos * 1e-9
        word_end = word.end_time.seconds + word.end_time.nanos * 1e-9
        if word_end - word_start > 1:
           word_start = word_end - 1
        if i == 0 or i % delta == 1:
            start = word_start
        if i == len(alternative.words) - 1 or i % delta == 0:
            print(alternative.transcript)
            end = word_end
            text = alternative.transcript
            arrText = text.split(" ")
            count_delta = (int)(i / delta)
            arrSubContent = arrText[(count_delta - 1) * delta:count_delta * delta]
            strText = ""
            for word in arrSubContent:
                strText += word + ' '
            print(text)
            alt = {"alternative": strText, "start":float(start), "end":float(end)}
            speech.append(alt)

  return speech