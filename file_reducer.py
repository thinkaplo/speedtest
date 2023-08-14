from functions import *
import random 

### files/Sportsbook.txt -> files_xs/Sportsbook.csv
sportsbook = read_csv('input/SyntheticFinancial.csv')
sportsbook_xs = []
sportsbook_len = len(sportsbook)
for i in range(0,round(sportsbook_len*0.01)):
    sportsbook_xs.append(sportsbook[i])
write_csv('input/SyntheticFinancial1%.csv',sportsbook_xs)