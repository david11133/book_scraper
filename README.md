# book_scraper

BookScrapePro is a Python-based web scraping project that extracts book data from the [Books to Scrape](http://books.toscrape.com) website. Using Selenium, the project navigates through specified book categories, collects relevant data such as titles, prices, and stock availability, and exports the information to a CSV file. This project aims to provide a comprehensive dataset for book enthusiasts, data analysts, and developers.

## Features

- **Automated Web Scraping**: Utilizes Selenium for seamless navigation and data extraction.
- **Headless Browser**: Operates in headless mode to improve performance and efficiency.
- **Category-Based Scraping**: Extracts data from specified book categories.
- **Data Export**: Saves the scraped data into a CSV file for easy access and analysis.

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/BookScrapePro.git
    cd BookScrapePro
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Download ChromeDriver**:
    Download the ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/) and place it in a known directory. Update the `CHROME_DRIVER_PATH` in the script accordingly.

## Usage

1. **Update the Configuration**:
    Ensure the `CHROME_DRIVER_PATH` and `CATEGORIES` in the script are set to your preferences.

2. **Run the Script**:
    ```bash
    python bookscrapepro.py
    ```

3. **View the Output**:
    The scraped data will be saved in `books_exported.csv`. Open this file to view the collected book data.

## Project Structure

- `bookscrapepro.py`: The main script that contains the scraping and data export logic.
- `requirements.txt`: Lists the dependencies required to run the project.
- `README.md`: Project description and instructions.

## How It Works

1. **Initialization**:
    - The script initializes the Chrome WebDriver in headless mode for efficient scraping.
    
2. **Category Navigation**:
    - For each specified category, the script navigates to the category page, waits for the page to load, and then extracts the book data.

3. **Data Extraction**:
    - The script collects the book title, price, and stock availability for each book in the category.

4. **Data Export**:
    - After collecting the data, it is exported to a CSV file for further analysis or use.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Books to Scrape](http://books.toscrape.com) for providing the data.
- [Selenium](https://www.selenium.dev/) for the web scraping capabilities.

## Contact

For any inquiries, please contact [yourname](mailto:youremail@example.com).

---

**BookScrapePro** - Efficiently scrape and collect book data for your needs.
