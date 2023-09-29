"""
This file will only show specific transactions("RFND") of a particular record 07 in a file
"""

input_file = r"C:\Users\SG0701644\OneDrive - Sabre\Files\DailyMFOL\Sep\6-Sep\Kamal\CREMCMC.CMP_20230904.txt"

out_file = r"C:\Users\SG0701644\OneDrive - Sabre\Files\DailyMFOL\Sep\6-Sep\Kamal\Record7RFNDOnly.txt"
out = open(out_file,'w',encoding='utf-8')
docNo = "0"
with open(input_file,'r',encoding='utf-8') as file:
    line_buffer = file.read()
    lines = line_buffer.split("\n")

    for line in lines:
        """
        from this condition i am picking the doc no as
        RFND and RECORD7 data will not in the same line
        """
        if( "RFND  " in line):
            docNo = line[11:25]
        
        """
            Once I got the docno which contains RFND after checking for the record7 I am 
            writing those one to the files
        """
        if(docNo is not "0"):
            if(line.startswith("07") and (docNo in line)):
                out.write(line+"\n")
                print(line)