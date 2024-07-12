import pickle
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


if __name__ == '__main__':
    
    # Load the model
    # with open('info_ids.pkl', 'rb') as file:
    #     model = pickle.load(file)
    
    with open(r'data\journals\num_processed.pkl', 'rb') as file:
        num_processed = pickle.load(file)

    #print(num_processed)

    # with open('errors_ids.pkl', 'rb') as file:
    #     errors = pickle.load(file)
    
    with open('data\info_journals.pkl', 'rb') as file:
        info_j = pickle.load(file)
    
     # Set Chrome to run headlessly
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Ensure GUI is off
    chrome_options.add_argument("--disable-gpu")  # Recommended as per documentation
    chrome_options.add_argument("--no-sandbox")  # Bypass OS security model, REQUIRED for Docker. Comment this line if not using Docker
    chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36")


    driver = webdriver.Chrome(options=chrome_options)  # Initialize Chrome driver
    
    url = 'https://pubmed.ncbi.nlm.nih.gov/' + str(30242045) + '/?format=pubmed'
    driver.get(url)

    
    # WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "article-details")))
    # search_results = driver.find_element(By.CLASS_NAME, "article-details").text
    # data = {"Journal": 'eLife', "Num": 30242045, "Content": search_results}
    # Print the entire HTML content of the page
    html_content = driver.page_source
    print(html_content)

    # Close the driver after inspection
    driver.quit()
    #print(data)