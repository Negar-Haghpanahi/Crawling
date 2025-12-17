
---

# 🕸️ WebToMarkdown Extractor

A Python-based automation tool that crawls specific web pages using **Selenium**, extracts structural content (Headers and Body) with **BeautifulSoup**, and converts the HTML elements into clean, readable **Markdown** files.

## 🚀 Features

* **Dynamic Crawling:** Uses Selenium (Firefox/Chrome support) to handle dynamic content and sub-links.
* **Intelligent Extraction:** Specifically targets judicial/legal document structures (based on the `ara.jri.ac.ir` sample).
* **HTML to Markdown:** Automatically converts `<h1>`, `<b>`, and `<br>` tags into proper Markdown syntax (`#`, `##`, and newlines).
* **Automated Workflow:** Extracts links from a landing page and automatically processes the sub-pages.

## 🛠️ Tech Stack

* **Python 3.x**
* **Selenium:** For web browser automation.
* **BeautifulSoup4:** For parsing and cleaning HTML.
* **WebDriver:** Supports Firefox (GeckoDriver) and Chrome (ChromeDriver).

---

## 📂 Project Structure

| File | Description |
| --- | --- |
| `main.py` | The entry point. Coordinates the crawling and conversion process. |
| `ExtractingText.py` | Handles the logic for finding specific `div` classes and IDs. |
| `MarkDown.py` | The engine that transforms HTML strings into Markdown format. |
| `Crawling.py` | Configures the Selenium WebDriver (Headless mode supported). |
| `InputClass.py` | Contains the data models for URL and Driver management. |

---

## ⚙️ Installation & Setup

1. **Clone the Repository:**
```bash
git clone https://github.com/yourusername/WebToMarkdown-Extractor.git
cd WebToMarkdown-Extractor

```


2. **Install Dependencies:**
```bash
pip install selenium beautifulsoup4

```


3. **WebDriver Setup:**
* Ensure you have **GeckoDriver** (for Firefox) or **ChromeDriver** (for Chrome) installed and added to your System PATH.
* In `test.py` or `main.py`, update the executable path if necessary:
```python
driver = webdriver.Chrome(executable_path="path/to/chromedriver.exe")

```





---

## 📑 Usage

To run the full extraction pipeline:

1. Open `main.py`.
2. Set your target `URL`, `inner_class_name`, and `Xpath`.
3. Run the script:
```bash
python main.py

```


4. The output will be generated as `output.md` in the root directory.

---

## 🔍 Example Transformation

**Input (HTML):**

```html
<div class="col-md-11">
    <h1>رأی شعبه دیوان عالی کشور</h1>
</div>

```

**Output (Markdown):**

```markdown
# رأی شعبه دیوان عالی کشور

```

---
