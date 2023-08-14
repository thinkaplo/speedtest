import os
import time
import pandas as pd
from functions import *

results = []
# --------------------------------------------------------- START EXPERIMENT 
for i in range (0,2):
# --------------------------------------------------------- LOADING 
    row = {}
    start_load = time.monotonic()
    
    file = pd.read_csv('input/SyntheticFinancial1%.csv')
    
    end_load = time.monotonic()
    
    load_result = end_load - start_load
    row['Load'] = load_result

# --------------------------------------------------------- TRANSFORMATION 
    start_transformation = time.monotonic()
    
    file['Text']=file.loc[:,'type'].apply(lambda x : x[::-1])
    file['Conditional']='More than a thousand'
    file.loc[file['amount'] <= 1000,'Conditional'] = 'Less than a thousand'
    file['Arithmetic']=file.loc[:,'newbalanceOrig']-file.loc[:,'oldbalanceOrg']

    end_transformation = time.monotonic()
    
    transformation_result = end_transformation - start_transformation 
    row['Transformation'] = transformation_result   

# --------------------------------------------------------- WRITING 
    start_writing = time.monotonic()

    file.to_csv('output/method_pandas.csv',index=False)
    
    end_writing = time.monotonic()

    writing_result = end_writing - start_writing
    row['Writing']=writing_result

# --------------------------------------------------------- CLEAN FOR NEW CYCLE 
    os.remove('output/method_pandas.csv')
    file = []
    results.append(row)
# --------------------------------------------------------- WRITE RESULTS
write_csv('results/results_pandas.csv',results)
# --------------------------------------------------------- END EXPERIMENT 
