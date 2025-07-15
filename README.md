# Automated-Book-Publication-Workflow

# AI Content Scraper, Rewriter, Reviewer, and Voice Reader

This Python script performs automated **content scraping**, **AI rewriting**, **human-in-the-loop review**, and **text-to-speech reading** for any provided webpage.

---

## 🚀 **Features**

✅ Scrape web page content and save it locally  
✅ Generate rewritten content using Google Gemini AI  
✅ Review rewritten content with an AI reviewer  
✅ Human approval system with Accept, Reject, Edit, and Voice options  
✅ Reward logging for accepted, rejected, or edited outputs  
✅ Text-to-Speech reading using pyttsx3  
✅ Screenshot saving for visual verification  
✅ Uses **Playwright**, **Google GenAI**, **ChromaDB**, and **pyttsx3**

---

## 📂 **File Structure**

- `pro.py` : Main program script
- `chapter.txt` : Stores scraped text content
- `screenshot.png` : Screenshot of the scraped web page

---

## 🔧 **Requirements**

Install dependencies via pip:

```bash
pip install playwright
pip install google-generativeai
pip install pyttsx3
pip install chromadb

Additionally, install Playwright browsers:

playwright install


💻 How to Run
Run the program using:
python pro.py

📝 Usage Flow
Scraping: Fetches content from the hardcoded URL.

Rewriting: Uses Gemini AI to rewrite the scraped content.

Reviewing: AI reviews the rewritten content.

Human-in-the-loop:

Accept to approve and log reward +10

Reject to discard and log reward 0

Edit to manually edit and log reward +8

Voice to hear the text before final approval

Reward Logging: Logs user actions with rewards.


⚠️ Notes
The current URL is hardcoded to The Gates of Morning Wikisource page.

Ensure your API key has sufficient quota for requests.

ChromaDB initialization is included but vector operations are not used in this prototype. Extend as needed.

