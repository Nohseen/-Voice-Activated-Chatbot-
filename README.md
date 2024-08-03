# Voice-Activated Chatbot

## Description

This project is a voice-activated chatbot built using Python. It leverages several libraries to recognize voice commands, convert text to speech, play YouTube videos, tell the current time, and fetch information from Wikipedia. The bot listens for commands and responds accordingly, making it a versatile and interactive tool.

## Features

- **Voice Command Recognition**: Uses `speech_recognition` to listen and interpret voice commands.
- **Text-to-Speech**: Employs `pyttsx3` for converting text to speech.
- **YouTube Playback**: Utilizes `pywhatkit` to search and play YouTube videos.
- **Current Time Announcement**: Tells the current time using the `datetime` library.
- **Wikipedia Information Fetching**: Provides summaries of topics using `wikipedia`.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/Voice-Activated-Chatbot.git

2. Navigate to the project directory:
    %cd Voice-Activated-Chatbot

3. Install the required libraries:
    pip install speechrecognition pyttsx3 pywhatkit wikipedia


## Usage
1. Run the chatbot.py script:

    python chatbot.py
2. Speak your commands, starting with "Alexa" to activate the bot.