"""
This Program will search for a list of document no present in the DocList File 
and then search them in the exisiting legacy file with a particular record.
"""
import os

## decalring the legacy file directory path
legacy_file = r"C:\Users\SG0701644\OneDrive - Sabre\Files\LegacyFiles\Sep\28-Sep\CREMCTCN_20230928.txt"


doc_file = r"C:\Users\SG0701644\OneDrive - Sabre\Files\codebase\Python\PulledDocList.txt"

with open(doc_file,'r',encoding='utf-8') as doc_file_reader:
    doc_line_buffer = doc_file_reader.read()
    doc_lines = doc_line_buffer.split("\n")

findings = r"Findings.txt"

# search record should always be 01 or 03 as they will be present even in the CNJ records
search_record = "03"
dg_search_record = "96                                        03000000"

matched_no = []
with open(findings,'w',encoding='utf-8') as findwriter:
    line_number = 0

    with open(legacy_file,'r',encoding='utf-8') as reader:
        line_buffer = reader.read()
        lines = line_buffer.split("\n")

        for line in lines:
            line_number += 1
            for doc_line in doc_lines:
                if(line.__contains__(doc_line) and line.startswith(search_record)):
                    value = f"The document no {doc_line} is present in file {legacy_file} at line no {line_number}"
                    matched_no.append(doc_line)
                    findwriter.write(value+"\n")
                    print(value)

all_nos = set(doc_lines)
matched_set = set(matched_no)

unmatched_set = list(all_nos-matched_set)
print(unmatched_set)