{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "c7cf3ffe",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please say something...\n",
      "You said: hello\n",
      "Enter the target language (e.g., 'en' for English, 'fr' for French): ta\n",
      "Translated text: வணக்கம்\n"
     ]
    }
   ],
   "source": [
    "import speech_recognition as sr\n",
    "from googletrans import Translator\n",
    "\n",
    "recognizer = sr.Recognizer()\n",
    "\n",
    "with sr.Microphone() as source:\n",
    "    print(\"Please say something...\")\n",
    "    recognizer.adjust_for_ambient_noise(source)\n",
    "    \n",
    "    audio = recognizer.listen(source)\n",
    "\n",
    "    try:\n",
    "        text_to_translate = recognizer.recognize_google(audio)\n",
    "        print(f\"You said: {text_to_translate}\")\n",
    "    except sr.UnknownValueError:\n",
    "        print(\"Sorry, I could not understand the audio.\")\n",
    "        text_to_translate = None\n",
    "    except sr.RequestError:\n",
    "        print(\"Sorry, there was an error with the speech recognition service.\")\n",
    "        text_to_translate = None\n",
    "\n",
    "if text_to_translate:\n",
    "    translator = Translator()\n",
    "    target_language = input(\"Enter the target language (e.g., 'en' for English, 'fr' for French): \")\n",
    "    translation = translator.translate(text_to_translate, dest=target_language)\n",
    "    print(f\"Translated text: {translation.text}\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
