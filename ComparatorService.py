

## decalring the legacy file directory path
legacy_file = r"C:\Users\SG0701644\OneDrive - Sabre\Files\LegacyFiles\Sep\28-Sep\CREMCTCN_20230928.txt"

mfol_file = r"C:\Users\SG0701644\OneDrive - Sabre\Files\DailyMFOL\Sep\29-Sep\CREMCTCN_20230927.txt"

comparator_file = r"TestComparator.txt"


with open(comparator_file,'w',encoding='utf-8') as result:
    line_number = 0

    with open(legacy_file,'r',encoding='utf-8') as legacy_reader,open(mfol_file,'r',encoding='utf-8') as mfol_reader:
        legacy_line_buffer = legacy_reader.read()
        legacy_lines = legacy_line_buffer.split("\n")
        
        mfol_line_buffer = mfol_reader.read()
        mfol_lines = mfol_line_buffer.split("\n")

        # since having the record in the MC file is mandatory, we are using the MFOL first
        
        for legacy_line in legacy_lines:
            
            for mfol_line in mfol_lines:
                # for Record 1
                if legacy_line[10:23:] == mfol_line[10:23:] and legacy_line.startswith("01") and mfol_line.startswith("01"):
                    result.write("                  ####################  MAIN Document Number  :"+legacy_line[10:23:]+"       ##################"+"\n")
                    result.write("Legacy RECORD\n")
                    result.write(legacy_line+"\n")
                    result.write(mfol_line+"\n")
                    result.write("MFOL Record"+"\n\n")
                    # differences = list(diff.compare(legacy_line,mfol_file))
                    # if len(differences) >0:
                    #     result.write("Differences are :"+"".join(differences))
                    #     result.write("\n\n\n")
                        
                    # for reporting difference 
                    # Find and report the differing portion
                    for j in range(42,len(legacy_line)):
                        if legacy_line[j] != mfol_line[j]:
                            starting_mismatch_point = j
                            while(j<len(legacy_line)):
                                j+=1
                                if(legacy_line[j] == mfol_line[j]):
                                    break
                            legacy_differing_portion = legacy_line[starting_mismatch_point:j]
                            mfol_differing_portion = mfol_line[starting_mismatch_point:j]
                            result.write(f"Differing portion starts at column : {starting_mismatch_point+1} ########Legacy Value : {legacy_differing_portion} |  MFOL Value : {mfol_differing_portion}\n\n\n\n\n")
                            break
                    
                    
                # for Record 3
                if legacy_line[10:23:] == mfol_line[10:23:] and legacy_line.startswith("03") and mfol_line.startswith("03"):
                    result.write("Legacy_Record Document Number  :"+legacy_line[10:23:]+"\n")
                    result.write(legacy_line+"\n")
                    result.write(mfol_line+"\n")
                    result.write("MFOL RECORD"+"\n\n\n")
                    # differences = list(diff.compare(legacy_line,mfol_file))
                    # if len(differences) >0:
                    #     result.write("Differences are :"+"".join(differences))
                    #     result.write("\n\n\n")
                    
                    # Find and report the differing portion
                    for j in range(42,len(legacy_line)):
                        if legacy_line[j] != mfol_line[j]:
                            starting_mismatch_point = j
                            while(j<len(legacy_line)):
                                j+=1
                                if(legacy_line[j] == mfol_line[j]):
                                    break
                            legacy_differing_portion = legacy_line[starting_mismatch_point:j]
                            mfol_differing_portion = mfol_line[starting_mismatch_point:j]
                            result.write(f"Differing portion starts at column : {starting_mismatch_point+1} ######Legacy Value : {legacy_differing_portion} |  MFOL Value : {mfol_differing_portion}\n\n\n\n\n")
                            break
                
                # for Record 4
                if legacy_line[10:23:] == mfol_line[10:23:] and legacy_line.startswith("04") and mfol_line.startswith("04"):
                    result.write("Legacy_Record Document Number  :"+legacy_line[10:23:]+"\n")
                    result.write(legacy_line+"\n")
                    result.write(mfol_line+"\n")
                    result.write("MFOL RECORD"+"\n\n\n")
                    # differences = list(diff.compare(legacy_line,mfol_file))
                    # if len(differences) >0:
                    #     result.write("Differences are :"+"".join(differences))
                    #     result.write("\n\n\n")
                    
                    # Find and report the differing portion
                    for j in range(42,len(legacy_line)):
                        if legacy_line[j] != mfol_line[j]:
                            starting_mismatch_point = j
                            endpoint = j
                            while j < len(legacy_line):
                                j += 1
                                if j < len(legacy_line) and legacy_line[j] == mfol_line[j]:
                                    endpoint = j
                                    break
                            legacy_differing_portion = legacy_line[starting_mismatch_point:endpoint]
                            mfol_differing_portion = mfol_line[starting_mismatch_point:endpoint]
                            result.write(f"Differing portion starts at column : {starting_mismatch_point+1} ######## Legacy Value : {legacy_differing_portion} |  MFOL Value : {mfol_differing_portion}\n\n\n\n\n")
                                    
                                        
                # for Record 5
                if legacy_line[10:23:] == mfol_line[10:23:] and legacy_line.startswith("05") and mfol_line.startswith("05"):
                    result.write("Legacy_Record Document Number  :"+legacy_line[10:23:]+"\n")
                    result.write(legacy_line+"\n")
                    result.write(mfol_line+"\n")
                    result.write("MFOL RECORD"+"\n\n\n")
                    
                    # if len(differences) >0:
                    #     result.write("Differences are :")
                    #     for difference in differences:
                    #         result.write(difference+"      ")
                    #     result.write("\n\n\n")
                    
                    # Find and report the differing portion
                    for j in range(42,len(legacy_line)):
                        if legacy_line[j] != mfol_line[j]:
                            
                            while(j<len(legacy_line)):
                                starting_mismatch_point = j
                                j+=1
                                if(legacy_line[j] == mfol_line[j]):
                                    break
                            legacy_differing_portion = legacy_line[starting_mismatch_point:j]
                            mfol_differing_portion = mfol_line[starting_mismatch_point:j]
                            result.write(f"Differing portion starts at column : {starting_mismatch_point+1} #########Legacy Value : {legacy_differing_portion} |  MFOL Value : {mfol_differing_portion}\n\n\n\n\n")
                            #break
                    
                # for Record 7
                if legacy_line[10:23:] == mfol_line[10:23:] and legacy_line.startswith("07") and mfol_line.startswith("07"):
                    result.write("Legacy_Record Document Number  :"+legacy_line[10:23:]+"\n")
                    result.write(legacy_line+"\n")
                    result.write(mfol_line+"\n")
                    result.write("MFOL RECORD"+"\n\n\n")
                    # differences = list(diff.compare(legacy_line,mfol_file))
                    # if len(differences) >0:
                    #     result.write("Differences are :")
                    #     result.write("\n\n\n")
                    
                    # Find and report the differing portion
                    for j in range(42,len(legacy_line)):
                        if legacy_line[j] != mfol_line[j]:
                            starting_mismatch_point = j
                            while(j<len(legacy_line)):
                                j+=1
                                if(legacy_line[j] == mfol_line[j]):
                                    break
                            legacy_differing_portion = legacy_line[starting_mismatch_point:j]
                            mfol_differing_portion = mfol_line[starting_mismatch_point:j]
                            result.write(f"Differing portion starts at column : {starting_mismatch_point+1} #### Legacy Value : {legacy_differing_portion} |  MFOL Value : {mfol_differing_portion}\n\n\n\n\n")
                            break
                
                # for Record 8
                if legacy_line[10:23:] == mfol_line[10:23:] and legacy_line.startswith("08") and mfol_line.startswith("08"):
                    result.write("Legacy_Record Document Number  :"+legacy_line[10:23:]+"\n")
                    result.write(legacy_line+"\n")
                    result.write(mfol_line+"\n")
                    result.write("MFOL RECORD"+"\n\n\n")
                    # differences = list(diff.compare(legacy_line,mfol_file))
                    # if len(differences) >0:
                    #     result.write("Differences are :"+"".join(differences))
                    #     result.write("\n\n\n")
                    
                    # Find and report the differing portion
                    for j in range(42,len(legacy_line)):
                        if legacy_line[j] != mfol_line[j]:
                            starting_mismatch_point = j
                            while(j<len(legacy_line_buffer)):
                                j+=1
                                if(legacy_line[j] == mfol_line[j]):
                                    break
                            legacy_differing_portion = legacy_line[starting_mismatch_point:j]
                            mfol_differing_portion = mfol_line[starting_mismatch_point:j]
                            result.write(f"Differing portion starts at column : {starting_mismatch_point+1} ###### Legacy Value : {legacy_differing_portion} |  MFOL Value : {mfol_differing_portion}\n\n\n\n\n")
                            break