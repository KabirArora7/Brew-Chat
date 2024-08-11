
import assemblyai as aai

# Replace with your API key
aai.settings.api_key = "898fe3a1ae274f9b9d220dc63006d5e2"

def transcribe(FILE_URL):
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(FILE_URL)

    if transcript.status == aai.TranscriptStatus.error:
        return ""
    else:
        return (transcript.text)
