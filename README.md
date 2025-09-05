Pygame Translator

A simple desktop translator application built with Python and Pygame, using the Google Translate API via the googletrans library. It allows users to translate text between different languages with a graphical interface.

Features

Input source and destination language codes.

Enter text to translate.

Translate text using Google Translate.

Simple GUI with Pygame:

Input boxes

Output box

"Yes" / "No" buttons to continue or exit.

Supports multiple languages from a CSV file.

Installation

Clone the repository:
git clone https://github.com/yourusername/pygame-translator.git

Go into the project folder:
cd pygame-translator

Install dependencies:
pip install pygame googletrans==4.0.0-rc1

⚠️ Make sure you use googletrans version 4.0.0-rc1 for stability.

Prepare languages CSV:
Make sure languages.csv is in the project folder with this format:

code,language
en,English
fr,French
es,Spanish
...

Usage

Run the program:
python translator.py

Enter the source language code (or leave blank for auto-detect).

Enter the destination language code.

Type the text to translate.

Press Enter to translate.

Click Yes to translate more, No to exit.

Example

Source Language Code: en
Destination Language Code: fr
Text to Translate: Hello, how are you?
Translated Text: Bonjour, comment ça va ?
