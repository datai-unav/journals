import pickle
import pandas as pd
#from tqdm import tqdm



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

if __name__ == '__main__':
    # Load the model
    # with open('data/info_ids.pkl', 'rb') as file:
    #     model = pickle.load(file)
    
    #print(model[0].keys())
     
     
    #print([x if "@" in x["Content"] else None for x in model[0:50]])   
    #print([ x.keys() if "Mail" in x.keys() else None for x in model] )
    
    with open('data/info_journals.pkl', 'rb') as file:
        info_j = pickle.load(file)
     
     
    print(info_j[0].keys())   
    
    # # a =  [x["name"] for x in info_j]
    
    # # # Sort by ascending by letter
    # # a.sort()
    
    # # for x in a: 
    # #     print(x)
        
    # print([x if "Music" in x["name"] else None for x in info_j])
    
    
    # Load a dataframe in csv file with headers
    # df = pd.read_csv('data/journals_results_filtered.csv')


    # mails = pd.read_csv('data\mails.csv')
                
    # print(len(mails['mails'].unique()))
    
    
    # Count the unique values in the Mail column, the Mail column is a list
  

    #df.to_csv('data/journals_results_filtered.csv', index=False)
    # # Remove the rows with [] value en Mail column
    # df = df[df['Mail'] != '[]']
    
    # print(df)
    
    # df.to_csv('data/journals_results_filtered.csv', index=False)
    
    