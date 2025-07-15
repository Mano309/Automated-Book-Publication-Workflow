from playwright.sync_api import sync_playwright
from google import genai 
import pyttsx3
import chromadb 

Ai = genai.Client(api_key="YOUR_API_KEY")
voice = pyttsx3.init()
chroma = chromadb.Client()
collection = chroma.create_collection("content")
reward_log = []

def content(url,content):
    with sync_playwright() as playwright:
        chrome = playwright.chromium.launch(headless=False,slow_mo=500)
        page = chrome.new_page()
        page.goto(url) 
        page_text = page.inner_text("body")
        page.screenshot(path="screenshot.png", full_page=True) 
        print("Screenshot saved")
        chrome.close()
        with open(content, "w", encoding="utf-8") as file:
                file.write(page_text)
                print("Scraped content")
    return page_text


def rewrite(text):
    retext = f"Please rewrite the following text in a:\n{text}"
    message = Ai.models.generate_content(model="gemini-2.5-flash", contents=retext)
    return message.text

def reviewer(text):
    message = Ai.models.generate_content(model="gemini-2.5-flash", contents=text)
    return message.text

def read(text):
    voice.say(text)
    voice.runAndWait()

def reward(action, reward):
    reward_log.append({
        "action": action,
        "reward": reward})

def human_review(text):
    print(text)  
    print("\nChoose an option:")
    print(" A for Accept \n R for Reject \n E for Edit \n V for Voice" )
    button = input("Your choice:")
    button.lower()
    
    if button == 'a':
        print("You accepted it.")
        reward("accept", 10)
        return text, True

    elif button == 'r':
        print("You rejected it.")
        reward("reject", 0)
        return None, False

    elif button == 'e':
        print("Type your edits below (or) Press Enter on an empty line to finish.")
        edited_lines = []
        while True:
            line = input()
            if line == '':
                break
            edited_lines.append(line)
        edited_text = "\n".join(edited_lines)
        reward("edit", 8)
        return edited_text, True

    elif button == 'v': 
        read(text)
        return human_review(text) 

    else:
        print("Sorry, that's not a key.")

def main():
    url = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"
    content(url, "chapter.txt")

    with open("chapter.txt", "r", encoding="utf-8") as file:
        original_text = file.read()

    writer = rewrite(original_text)
    review = reviewer(writer)
    current_text = review
    while True:
        result = human_review(current_text)
        if result:
            print("\nFinal version approved after review.")
            print("\nReward Log:", reward_log)
            break

if __name__ == "__main__":
    main()
