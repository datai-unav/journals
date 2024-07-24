import pickle
import pandas as pd
from tqdm import tqdm



def map_pmid_to_journal(df, info_j):
    
    df_output = pd.DataFrame(columns=['PMID', 'Date', 'Title', 'Authors', 'Affiliation', 'Mail', 'Journal'])
    rows = list(df.iterrows())
    for index, row in tqdm(rows):
        data = row.to_dict()
        
        for jn in info_j:
            if str(data['PMID']) in jn['additional_info']:
                data['Journal'] = jn['name']
                temp_df = pd.DataFrame(data, index=[0])
                df_output = pd.concat([df_output, temp_df], ignore_index=True)                
                break 
    
    df_output.to_csv('data/journals_results_names.csv', index=False)    


def unique_mail(df: pd.DataFrame):

    # Get the unique mail
    print(df['Mail'].value_counts())


def detect_missing_journals():
    
    
        
    
    df = pd.read_csv('data/journals_completed.csv')
    
    
    with open('data/unique_names.csv', 'r') as file:
        names = file.readlines()
        
        names = [x.strip() for x in names]    
        
        names = set(names)
        
        to_delete = df[df['Finished'] == 1]
    
        to_delete = set(to_delete['Name'].values)

        diff = names.difference(to_delete)
        
        print(len(diff))
        
        with open('data/m_names.txt', 'w') as file:
            for x in diff:
                file.write(x + '\n')   
        
def split_txt(filename, parts=6):
    """Split a text file into a specified number of parts."""
    
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    # Calculate the number of lines per part
    lines_per_part = len(lines) // parts
    extra_lines = len(lines) % parts

    start = 0
    for i in range(parts):
        # Determine the end line index for this part
        # Add an extra line to the first 'extra_lines' parts to distribute any remainder
        end = start + lines_per_part + (1 if i < extra_lines else 0)
        
        # Write the current part to a new file
        with open(f'data/part_{i+1}.txt', 'w') as part_file:
            part_file.writelines(lines[start:end])
        
        # Update the start index for the next part
        start = end
    
    
    
            
if __name__ == '__main__':
    
    split_txt(filename='data/m_names.txt', parts=6)
    
    # Load the model
    # with open('data/info_ids.pkl', 'rb') as file:
    #     model = pickle.load(file)
    
    #print(model[0].keys())
     
     
    #print([x if "@" in x["Content"] else None for x in model[0:50]])   
    #print([ x.keys() if "Mail" in x.keys() else None for x in model] )
    
    # with open('data/info_journals.pkl', 'rb') as file:
    #     info_j = pickle.load(file)
        
    
    # # a =  [x["name"] for x in info_j]
    
    # # # Sort by ascending by letter
    # # a.sort()
    
    # # for x in a: 
    # #     print(x)
        
    # print([x if "Music" in x["name"] else None for x in info_j])
    
    # with open('data/unique_names.csv', 'r') as file:
    #     lines = file.readlines()
        
    
    # names = [x['name'] for x in info_j]
    
    # with open('data/missing_names.txt', 'w') as file:
    #     for line in lines:
    #         if line.strip() not in names:
    #             file.write(line)
    
    
    # Count the unique values in the Mail column, the Mail column is a list
  

    #df.to_csv('data/journals_results_filtered.csv', index=False)
    # # Remove the rows with [] value en Mail column
    # df = df[df['Mail'] != '[]']
    
    # print(df)
    
    # df.to_csv('data/journals_results_filtered.csv', index=False)
    
   