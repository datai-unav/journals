import pickle
import pandas as pd
from tqdm import tqdm


if __name__ == '__main__':
    # Load the model
    with open('data/info_ids.pkl', 'rb') as file:
        model = pickle.load(file)
    
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
    df = pd.read_csv('data/journals_results.csv')
    
    # # Remove the rows with [] value en Mail column
    # df = df[df['Mail'] != '[]']
    
    # print(df)
    
    # df.to_csv('data/journals_results_filtered.csv', index=False)
    
    df_output = pd.DataFrame(columns=['PMID', 'Date', 'Title', 'Authors', 'Affiliation', 'Mail', 'Journal'])
    rows = list(df.iterrows())
    for index, row in tqdm(rows[0:10]):
        data = row.to_dict()
        
        for jn in info_j:
            if data['PMID'] in jn['additional_info']:
                data['Journal'] = jn['name']
                temp_df = pd.DataFrame(data, index=[0])
                df_output = df.concat(df_output, temp_df)                
                break 
    
    df_output.to_csv('data/journals_results_names.csv', index=False)    
    