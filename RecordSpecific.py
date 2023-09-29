
input_file = r"C:\Users\SG0701644\OneDrive - Sabre\Files\DailyMFOL\Sep\29-Sep\ORINFix\CREMCTCN_20230925.txt"

out_file = r"C:\Users\SG0701644\OneDrive - Sabre\Files\DailyMFOL\Sep\29-Sep\ORINFix\Record3Only.txt"

search_record = "03"
with open(input_file,'r',encoding="utf-8") as inp , open(out_file,'w',encoding="utf-8") as out:
    lines_buffer = inp.read()
    all_lines = lines_buffer.split("\n")
    for line in all_lines:
        if line.startswith(search_record):
            out.write(line+"\n")
            
        # # for Deggusa File use this 
        # if (line.startswith("96") and line[42:44]== search_record):
        #     out.write(line+"\n")

