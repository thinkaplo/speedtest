import os
import time
import pandas as pd

load_results = []
transformation_results = []
writing_results = []

# --------------------------------------------------------- START EXPERIMENT 
for i in range (0,10):
# --------------------------------------------------------- LOADING 
    start_load = time.monotonic()
    
    file = pd.read_csv('input/SyntheticFinancial.csv')
    
    end_load = time.monotonic()
    
    load_result = end_load - start_load
    load_results.append(load_result)

# --------------------------------------------------------- TRANSFORMATION 
    start_transformation = time.monotonic()
    
    file['Text']=file.loc[:,'type'].apply(lambda x : x[::-1])
    file['Conditional']='More than a thousand'
    file.loc[file['amount'] <= 1000,'Conditional'] = 'Less than a thousand'
    file['Arithmetic']=file.loc[:,'newbalanceOrig']-file.loc[:,'oldbalanceOrg']

    end_transformation = time.monotonic()
    
    transformation_result = end_transformation - start_transformation 
    transformation_results.append(transformation_result)   

# --------------------------------------------------------- WRITING 
    start_writing = time.monotonic()

    file.to_csv('output/method_pandas.csv',index=False)
    
    end_writing = time.monotonic()

    writing_result = end_writing - start_writing
    writing_results.append(writing_result)

# --------------------------------------------------------- CLEAN FOR NEW CYCLE 
    os.remove('output/method_pandas.csv')
    file = []
# --------------------------------------------------------- WRITE RESULTS
f = open('results/pandas_result.txt','a')
f.write('Load results: \n')
f.write(str(load_results))
f.write('\n'*2)
f.write('Transformation results: \n')
f.write(str(transformation_results))
f.write('\n'*2)
f.write('Writing results: \n')
f.write(str(writing_results))
f.close()    
# --------------------------------------------------------- END EXPERIMENT 