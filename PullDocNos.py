
def extract_doc_no(mfol_file,doc_list_file):
    """
    This is a simple method to extarct doc no from the mfol file to a test file both in arguments.
    This is for identifying the docList from the MFOL File and
    then we'll pick the unique document no and put it in a DocListFile Test File
    which can further be used for their existence in Legacy Files.
    """
    # mfol_file = r"C:\Users\SG0701644\OneDrive - Sabre\Files\DailyMFOL\Sep\11-Sep\CREMCMC.CMP_20231011.txt"
    with open(mfol_file,'r',encoding="utf-8") as inp, open(doc_list_file,'w',encoding='utf-8') as out:
        line_buffer = inp.read()
        lines = line_buffer.split("\n")
        doc_list = []
        for line in lines:
            # the numbering starts from 0 for python while we have doc no starts from 11 pos in mfol
            #doc_list.append(line[10:23:])
            # for DG use this instead:
            #doc_list.append(line[52:65])
            
            if(mfol_file.__contains__("DG")):
                doc_list.append(line[52:65])
            else:
                doc_list.append(line[10:23:])

            # if(line.__contains__("20230912")):
            #     doc_list.append(line[10:23:])
                
        
        # use this if u want to verify the doc_list values
        # print(doc_list) 
        
        # inserting the list into a set to remove all the duplicate data 
        list_set = set(doc_list)
        
        # print("Doc Lis is ")
        print(doc_list)
        # print("List Set is:")
        print("Length of total unique Record :",(len(list_set)+1))

        #converting the unique set of doc no into list
        unique_doc_list = (list(list_set))
        newline=""
        for doc_no in unique_doc_list:
            if(doc_no != "" and len(doc_no) == 13 and doc_no.isnumeric() == True):
                out.write(newline+doc_no)
                newline="\n"


if __name__ == "__main__":
    mfol_file = r"C:\Users\SG0701644\OneDrive - Sabre\Files\DailyMFOL\Sep\29-Sep\CREMCTCN_20230927.txt"

    doc_list_file = r"C:\Users\SG0701644\OneDrive - Sabre\Files\codebase\Python\PulledDocList.txt"
    extract_doc_no(mfol_file,doc_list_file)