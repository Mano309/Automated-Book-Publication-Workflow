#Automated Book Publication Workflow
This is a simple Python program that scrapes content from a webpage, rewrites it using AI, lets you review it, and reads it out loud if you want.

#What it does
Scrapes text from a webpage
Rewrites it using Google Gemini AI
Reviews the rewritten text using AI
Lets you accept, reject, edit, or listen to the text
Logs your actions as rewards
Saves a screenshot of the page

#Files
pro.py – main program file
chapter.txt – stores the scraped text
screenshot.png – screenshot of the webpage

How to set up
First, install the required Python packages:
pip install playwright google-generativeai pyttsx3 chromadb

Then install Playwright browsers:
playwright install

How to run
Run this command in your terminal:
python pro.py


#Notes
Right now, the URL is hardcoded to The Gates of Morning Wikisource page

Make sure you replace the API key in the code with your own

ChromaDB is initialized, but it’s not storing anything yet – you can extend it later if needed


