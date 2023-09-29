"""
This Program will search for a list of document no present in the DocList File 
and then search them in the exisiting legacy file with a particular record.
"""
import os

## decalring the legacy file directory path
legacy_folder = r"C:\Users\SG0701644\OneDrive - Sabre\Files\LegacyFiles\Test"

files = os.listdir(legacy_folder)

doc_file = r"C:\Users\SG0701644\OneDrive - Sabre\Files\codebase\Python\PulledDocList.txt"

with open(doc_file,'r',encoding='utf-8') as doc_file_reader:
    doc_line_buffer = doc_file_reader.read()
    doc_lines = doc_line_buffer.split("\n")

findings = r"LegacyFindings.txt"

search_record = "01"

with open(findings,'w',encoding='utf-8') as findwriter:
    line_number = 0
    for currentfile in files:
        fullpath = os.path.join(legacy_folder,currentfile)
        with open(fullpath,'r',encoding='utf-8') as reader:
            line_buffer = reader.read()
            lines = line_buffer.split("\n")

            for line in lines:
                line_number += 1
                for doc_line in doc_lines:
                    if(not (line.__contains__(doc_line) and line.startswith(search_record) and line.__contains__("20230912"))):
                        value = f"The document no {doc_line} is present in file {currentfile} at line no {line_number}"
                        findwriter.write(value+"\n")
                        print(value)
