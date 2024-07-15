import pickle
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


if __name__ == '__main__':
    

    #data = pickle.load(open(r'data\journals\eLife\elif\info_ids.pkl', 'rb'))
    with open(r'data/unique_names.csv', 'r') as file:
        unique_names = file.readlines()
        
    # Split the lines into a 3 .txt files
    file1 = open(r'data/unique_names1.txt', 'w')
    file2 = open(r'data/unique_names2.txt', 'w')
    file3 = open(r'data/unique_names3.txt', 'w')
    count  = len(unique_names)
    for i in range(count):
        if i < count/3:
            file1.write(unique_names[i])
        elif i < 2*count/3:
            file2.write(unique_names[i])
        else:
            file3.write(unique_names[i])
    file1.close()
    file2.close()
    file3.close()
    
    # Load the model
    # with open('info_ids.pkl', 'rb') as file:
    #     model = pickle.load(file)
    
    # with open(r'data\journals\num_processed.pkl', 'rb') as file:
    #     num_processed = pickle.load(file)

    #print(num_processed)

    # with open('errors_ids.pkl', 'rb') as file:
    #     errors = pickle.load(file)
    
    # with open(r'data\info_journals.pkl', 'rb') as file:
    #     info_j = pickle.load(file)
    
    #Export Unique names from info_journals
    # unique_names = set()
    # for journal in info_j:
    #     unique_names.add(journal['name'])
    
    # with open(r'data\unique_names.csv', 'w') as file:
    #     for name in unique_names:
    #         file.write(name + '\n')

    #  # Set Chrome to run headlessly
    # chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Ensure GUI is off
    # chrome_options.add_argument("--disable-gpu")  # Recommended as per documentation
    # chrome_options.add_argument("--no-sandbox")  # Bypass OS security model, REQUIRED for Docker. Comment this line if not using Docker
    # chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
    # chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36")


    # driver = webdriver.Chrome(options=chrome_options)  # Initialize Chrome driver
    
    # url = 'https://pubmed.ncbi.nlm.nih.gov/' + str(30242045) + '/?format=pubmed'
    # driver.get(url)

    
    # # WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "article-details")))
    # # search_results = driver.find_element(By.CLASS_NAME, "article-details").text
    # # data = {"Journal": 'eLife', "Num": 30242045, "Content": search_results}
    # # Print the entire HTML content of the page
    # html_content = driver.page_source
    # print(html_content)

    # # Close the driver after inspection
    # driver.quit()
    # #print(data)