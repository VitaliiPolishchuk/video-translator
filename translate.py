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
        if i == 0:
            start = word.start_time.seconds + word.start_time.nanos * 1e-9
        elif i == len(alternative.words) - 1:
            end = word.end_time.seconds + word.end_time.nanos * 1e-9
    translated_text = translate(alternative.transcript, src, trg)
    alt = {"alternative": translated_text['translations'][0]['translatedText'], "start":start, "end":end}
    speech.append(alt)
  return speech
