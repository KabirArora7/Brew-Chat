import pyaudio
import wave
from audio import transcribe
from summarize import summarize


flag = True


def recorder():

    global flag
    flag = True

    filename = "hello"
    actual_file = "recordings/" + filename + ".mp3"
    audio = pyaudio.PyAudio()
    stream = audio.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=44100,
        input=True,
        frames_per_buffer=1024,
    )

    frames = []

    while flag:
        data = stream.read(1024)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    audio.terminate()

    sound_file = wave.open(actual_file, "wb")

    sound_file.setnchannels(1)
    sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    sound_file.setframerate(44100)
    sound_file.writeframes(b"".join(frames))

    sound_file.close()

    transcription = transcribe(actual_file)
    if len(transcription) >= 50:
        summary = summarize(transcription)
        return summary

    print("no")
    return ""


def stopRecording():
    global flag
    flag = False
