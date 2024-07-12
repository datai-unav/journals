import argparse
import pickle
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def load_progress(file_name):
    """
    Load progress data from a pickle file.

    Args:
    - file_name (str): Name of the file to load progress from.

    Returns:
    - dict or None: Loaded progress data or None if file not found.
    """
    try:
        with open(file_name, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return None

def save_progress(progress, file_name):
    """
    Save progress data to a pickle file.

    Args:
    - progress (dict): Progress data to be saved.
    - file_name (str): Name of the file to save progress to.

    Returns:
    - None
    """
    with open(file_name, 'wb') as f:
        pickle.dump(progress, f)

def save_errors(error_list, file_name):
    """
    Save error list to a pickle file.

    Args:
    - error_list (list): List of errors to be saved.
    - file_name (str): Name of the file to save errors to.

    Returns:
    - None
    """
    with open(file_name, 'wb') as f:
        pickle.dump(error_list, f)

def load_data(file_name):
    """
    Load data from a pickle file.

    Args:
    - file_name (str): Name of the file to load data from.

    Returns:
    - list: Loaded data or an empty list if file not found.
    """
    try:
        with open(file_name, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return []

def save_data(data, file_name):
    """
    Save data to a pickle file.

    Args:
    - data (object): Data to be saved.
    - file_name (str): Name of the file to save data to.

    Returns:
    - None
    """
    current_data = load_data(file_name)
    current_data.append(data)
    with open(file_name, 'wb') as f:
        pickle.dump(current_data, f)

def process_journal_by_name(journals, journal_name, processed_file, errors_file, data_file, id_num):
    """
    Process IDs of a journal by name independently and save them.

    Args:
    - journals (list): List of journal information dictionaries.
    - journal_name (str): Name of the journal to process.
    - processed_file (str): File name to save processed IDs.
    - errors_file (str): File name to save IDs with errors.
    - data_file (str): File name to save article data.
    - id_num (int): Single ID number to process.

    Returns:
    - None
    """
    error_list = []  # List to store IDs with errors
    e = 0 # Counter for progress tracking
    driver = webdriver.Chrome()
    start_time = time.time()
    progress = load_progress(processed_file) # Load progress from file

    # Initialize progress if it's None (file not found)
    if progress is None:
        progress = {"processed_nums": []}
    else:
        e = len(progress["processed_nums"]) # Get count of processed IDs

    # Find the journal by name in the list of journals
    journal = next((j for j in journals if j.get('name') == journal_name), None)
    if journal is None:
        print(f"Journal '{journal_name}' not found.")
        return

    num = int(id_num)
    # Check if ID is already processed
    if num in progress["processed_nums"]:
        print(f"Article {num} already processed.")
        return
    
    url = 'https://pubmed.ncbi.nlm.nih.gov/' + str(num) + '/?format=pubmed'
    print(f'{e}: {url}')
    driver.get(url)
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "article-details")))
        search_results = driver.find_element(By.CLASS_NAME, "article-details").text
        data = {"Journal": journal_name, "Num": num, "Content": search_results}
        
        # Save the data immediately
        save_data(data, data_file)
        
        e += 1
        progress["processed_nums"].append(num)
        save_progress(progress, processed_file)
    except Exception as ex:
        print(f"Failed to extract content for article {num} - Journal: {journal_name}: {str(ex)}")
        error_list.append(num)  # Add ID to the error list

    # Save errors to file
    save_errors(error_list, errors_file)

    end_time = time.time()
    total_time = end_time - start_time
    print(f"Total time: {total_time} seconds")
    driver.quit()
    print('Processing completed.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('journal_name', type=str, help='Journal name')
    parser.add_argument('--processed_file', type=str, default='num_processed.pkl', help='File name to save processed IDs')
    parser.add_argument('--errors_file', type=str, default='errors_ids.pkl', help='File name to save IDs with errors')
    parser.add_argument('--data_file', type=str, default='info_ids.pkl', help='File name to save article data')
    args = parser.parse_args()
    
    # Load the list of journals from the file
    with open('info_journals.pkl', 'rb') as f:
        journals = pickle.load(f)
    
    # Check if the specified journal name exists in the loaded journal data
    if args.journal_name not in [journal['name'] for journal in journals]:
        print(f"The journal '{args.journal_name}' doesn't exist.")
    else:
        # Obtain the list of IDs for the specified journal
        journal_info = next(journal for journal in journals if journal['name'] == args.journal_name)
        id_list = journal_info.get('additional_info', [])
        
        # Process each ID individually
        for id_num in id_list:
            # Call process_journal_by_name() for each ID
            process_journal_by_name(journals, args.journal_name, args.processed_file, args.errors_file, args.data_file, id_num)
            
            # Verify the content of the info_ids.pkl after each save
            saved_data = load_data(args.data_file)

# cd 'Directorio_donde_se_encuentre_el_archivo'
# python get_ids_info.py "Aphasiology"