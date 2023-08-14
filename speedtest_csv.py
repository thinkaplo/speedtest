import os
import time
from functions import *

load_results = []
transformation_results = []
writing_results = []

# --------------------------------------------------------- START EXPERIMENT 
for i in range (0,2):
# --------------------------------------------------------- LOADING 
    start_load = time.monotonic()
    
    file = read_csv('input/SyntheticFinancial1%.csv')
    
    end_load = time.monotonic()
    
    load_result = end_load - start_load
    load_results.append(load_result)

# --------------------------------------------------------- TRANSFORMATION 
    start_transformation = time.monotonic()
    
    add_col(file,'Text')
    add_col(file,'Conditional')
    add_col(file,'Arithmetic')
    for i in file:
        i['Text'] = i['type'][::-1]
        i['Arithmetic'] = float(i['newbalanceOrig'])-float(i['oldbalanceOrg'])
        if float(i['amount']) > 1000:
            i['Conditional'] = 'More than a thousand'
        else:
            i['Conditional'] = 'Less than a thousand'

    end_transformation = time.monotonic()
    
    transformation_result = end_transformation - start_transformation 
    transformation_results.append(transformation_result)   

# --------------------------------------------------------- WRITING 
    start_writing = time.monotonic()

    write_csv('output/method_csv.csv',file)
    
    end_writing = time.monotonic()

    writing_result = end_writing - start_writing
    writing_results.append(writing_result)

# --------------------------------------------------------- CLEAN FOR NEW CYCLE 
    os.remove('output/method_csv.csv')
    file = []
# --------------------------------------------------------- WRITE RESULTS
f = open('results/csv_result.txt','a')
f.write('''{'Load':'''+str(load_results)+''','Transformation':'''+str(transformation_results)+''','Writing':'''+str(writing_results)+'}')
f.close()    
# --------------------------------------------------------- END EXPERIMENT 