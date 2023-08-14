import os
import time
import polars as pl

load_results = []
transformation_results = []
writing_results = []

# --------------------------------------------------------- START EXPERIMENT 
for i in range (0,10):
# --------------------------------------------------------- LOADING 
    start_load = time.monotonic()
    
    file = pl.read_csv('input/SyntheticFinancial.csv')
    
    end_load = time.monotonic()
    
    load_result = end_load - start_load
    load_results.append(load_result)

# --------------------------------------------------------- TRANSFORMATION 
    start_transformation = time.monotonic()
    
    file = file.with_columns(pl.col('type').apply(lambda x : x[::-1]).alias('Text'))
    file = file.with_columns(pl.when(pl.col('amount')>1000).then(pl.lit('More than a thousand')).otherwise(pl.lit('Less than a thousand')).alias('Conditional'))    
    file = file.with_columns((pl.col('newbalanceOrig') - pl.col('oldbalanceOrg')).alias('Arithmetic'))

    end_transformation = time.monotonic()
    
    transformation_result = end_transformation - start_transformation 
    transformation_results.append(transformation_result)   

# --------------------------------------------------------- WRITING 
    start_writing = time.monotonic()

    file.write_csv('output/method_polars.csv')
    
    end_writing = time.monotonic()

    writing_result = end_writing - start_writing
    writing_results.append(writing_result)

# --------------------------------------------------------- CLEAN FOR NEW CYCLE 
    os.remove('output/method_polars.csv')
    file = []
# --------------------------------------------------------- WRITE RESULTS
f = open('results/polars_result.txt','a')
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