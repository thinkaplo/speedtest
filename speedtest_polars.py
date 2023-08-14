import os
import time
import polars as pl
from functions import *

results = []
# --------------------------------------------------------- START EXPERIMENT 
for i in range (0,100):
# --------------------------------------------------------- LOADING 
    row = {}
    start_load = time.monotonic()
    
    file = pl.read_csv('input/SyntheticFinancial1%.csv')
    
    end_load = time.monotonic()
    
    load_result = end_load - start_load
    row['Load'] = load_result

# --------------------------------------------------------- TRANSFORMATION 
    start_transformation = time.monotonic()
    
    file = file.with_columns(pl.col('type').apply(lambda x : x[::-1]).alias('Text'))
    file = file.with_columns(pl.when(pl.col('amount')>1000).then(pl.lit('More than a thousand')).otherwise(pl.lit('Less than a thousand')).alias('Conditional'))    
    file = file.with_columns((pl.col('newbalanceOrig') - pl.col('oldbalanceOrg')).alias('Arithmetic'))

    end_transformation = time.monotonic()
    
    transformation_result = end_transformation - start_transformation 
    row['Transformation'] = transformation_result   

# --------------------------------------------------------- WRITING 
    start_writing = time.monotonic()

    file.write_csv('output/method_polars.csv')
    
    end_writing = time.monotonic()

    writing_result = end_writing - start_writing
    row['Writing']=writing_result

# --------------------------------------------------------- CLEAN FOR NEW CYCLE 
    os.remove('output/method_polars.csv')
    file = []
    results.append(row)
# --------------------------------------------------------- WRITE RESULTS
write_csv('results/results_polars.csv',results) 
# --------------------------------------------------------- END EXPERIMENT 
