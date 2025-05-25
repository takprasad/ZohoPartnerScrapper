# 🌍 Zoho Partner Scraper

This project is a **web scraper** built using Python and Selenium that extracts information about Zoho partners from different countries listed on [Zoho's Find a Partner](https://www.zoho.com/partners/find-partner.html) page.

## 🚀 Features

- Automatically searches for Zoho partners by country
- Extracts key partner details such as:
  - Company name
  - Partner name
  - Email address
  - Phone number
  - Website
  - LinkedIn profile
  - Head office address
- Saves the collected data into a CSV file (`lexyl.csv`)

## 🛠️ Technologies Used

- Python 3.x
- Selenium WebDriver
- Chrome (headless mode)
- pandas

## 📦 Requirements

Make sure the following Python packages are installed:

```bash
pip install selenium pandas
```
## 🧠 How It Works

1. The script opens the [Zoho Find a Partner](https://www.zoho.com/partners/find-partner.html) page using Selenium in headless Chrome mode.
2. It iterates through a predefined list of countries.
3. For each country:
   - Enters the country name in the search box.
   - Clicks the search results tab.
   - Waits for the partner list to load.
   - Iterates over each listed partner.
   - For each partner:
     - Clicks to open the profile.
     - Scrapes:
       - Company name
       - Partner name
       - Email
       - Phone number
       - Website
       - LinkedIn profile (if available)
       - Head office address
     - Appends the scraped data to a list.
     - Clicks "Back" to return to the list.
4. After all countries are processed, the list is converted to a pandas DataFrame.
5. Finally, the data is saved as a CSV file named `lexyl.csv`.

---

## 📌 Notes

- The scraper runs in **headless mode**, meaning Chrome operates without a GUI for faster performance.
- All elements are accessed using **XPath**, so if Zoho updates the webpage structure, you'll need to revise the XPath selectors.
- Includes `try-except` blocks to skip missing data and ensure the script doesn't crash.
- Make sure:
  - Your version of ChromeDriver matches your Chrome browser.
  - ChromeDriver is added to your system path.
  - Internet connection is active, as this scraper loads live web content.
- This scraper is built for educational and personal use. Respect Zoho’s [terms of use](https://www.zoho.com/terms.html) when scraping their site.
