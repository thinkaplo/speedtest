import os
import time
from functions import *

results = []
# --------------------------------------------------------- START EXPERIMENT 
for i in range (0,2):
# --------------------------------------------------------- LOADING 
    row = {}
    start_load = time.monotonic()
    
    file = read_csv('input/SyntheticFinancial1%.csv')
    
    end_load = time.monotonic()
    
    load_result = end_load - start_load
    row['Load'] = load_result

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
    row['Transformation'] = transformation_result   

# --------------------------------------------------------- WRITING 
    start_writing = time.monotonic()

    write_csv('output/method_csv.csv',file)
    
    end_writing = time.monotonic()

    writing_result = end_writing - start_writing
    row['Writing']=writing_result

# --------------------------------------------------------- CLEAN FOR NEW CYCLE 
    os.remove('output/method_csv.csv')
    file = []
    results.append(row)
# --------------------------------------------------------- WRITE RESULTS
write_csv('results/results_csv.csv',results)
# --------------------------------------------------------- END EXPERIMENT 
