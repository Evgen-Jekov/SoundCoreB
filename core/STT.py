import speech_recognition as sr

class STT:
    def listen_sound(self, lang, duration):
        recognizer = sr.Recognizer()
        try:
            with sr.Microphone() as sound:
                recognizer.adjust_for_ambient_noise(source=sound, duration=duration)
                audio = recognizer.listen(source=sound)

                result = recognizer.recognize_google(audio_data=audio, language=lang)

            return result

        except sr.UnknownValueError as e:
            return str(e)
        except sr.RequestError as e:
            return str(e)
        except sr.WaitTimeoutError as e:
            return str(e)
        except Exception as e:
            return str(e)