import pandas as pd
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define constants
CHROME_DRIVER_PATH = 'D:\Apps\chromedriver-win64\chromedriver.exe'
HOMEPAGE = "http://books.toscrape.com"
CATEGORIES = ["Humor", "Art"]

def init_browser(chrome_driver_path):
    """
    Initialize the Chrome WebDriver with headless option.
    
    Args:
    chrome_driver_path (str): Path to the ChromeDriver executable.
    
    Returns:
    WebDriver: Initialized Chrome WebDriver.
    """
    browser_options = ChromeOptions()
    browser_options.headless = True
    service = Service(chrome_driver_path)
    driver = Chrome(service=service, options=browser_options)
    return driver

def scrape_category(driver, url, category):
    """
    Scrape book data from a given category.
    
    Args:
    driver (WebDriver): The Chrome WebDriver instance.
    url (str): The base URL to navigate back to the homepage.
    category (str): The book category to scrape.
    
    Returns:
    list: A list of dictionaries containing book data.
    """
    data = []

    # Navigate to the category page
    category_link = driver.find_element(By.XPATH, f'//a[contains(text(), "{category}")]')
    category_link.click()

    try:
        # Wait for books to be loaded on the page
        books = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.product_pod'))
        )
    except Exception as e:
        raise e

    # Extract data for each book
    for book in books:
        title = book.find_element(By.CSS_SELECTOR, "h3 > a").get_attribute("title")
        price = book.find_element(By.CSS_SELECTOR, ".price_color").text
        stock = book.find_element(By.CSS_SELECTOR, ".instock.availability").text
        data.append({
            'title': title,
            'price': price,
            'stock': stock,
            'category': category
        })

    # Navigate back to the homepage
    driver.get(url)
    return data

def get_data(url, categories):
    """
    Gather data from multiple categories.
    
    Args:
    url (str): The base URL to navigate back to the homepage.
    categories (list): List of categories to scrape.
    
    Returns:
    list: A combined list of dictionaries containing book data from all categories.
    """
    driver = init_browser(CHROME_DRIVER_PATH)
    driver.get(url)
    driver.implicitly_wait(10)

    all_data = []
    for category in categories:
        category_data = scrape_category(driver, url, category)
        all_data.extend(category_data)

    driver.quit()
    return all_data

def export_to_csv(data, filename="books_exported.csv"):
    """
    Export the scraped data to a CSV file.
    
    Args:
    data (list): The data to be exported.
    filename (str): The name of the CSV file.
    """
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Data exported to {filename}")
    print(df)  # DEBUG

def main():
    """
    Main function to execute the scraping and exporting process.
    """
    data = get_data(url=HOMEPAGE, categories=CATEGORIES)
    export_to_csv(data)
    print('DONE')

if __name__ == '__main__':
    main()
