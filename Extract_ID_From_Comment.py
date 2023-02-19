

# =============================================================================
# =============================================================================
# # # pyinstaller id_extractor_from_google_meet_cmnt.py -F
# =============================================================================
# =============================================================================

import re,pyperclip
from csv import DictWriter
nm,dt,mnth=input("Enter course Name Date Month\n\n").split()
s=pyperclip.paste()
IDNo=re.compile(r'\d\d\d\d\d\d\d\d')
ids=IDNo.findall(s)

with open(f'{nm}_attendance_{dt}_{mnth}.csv','a',newline ='') as wf: 
       csv_writer = DictWriter(wf,fieldnames = ['Student ID'])
       csv_writer.writeheader()
       for i in ids:
              csv_writer.writerow({'Student ID':i})