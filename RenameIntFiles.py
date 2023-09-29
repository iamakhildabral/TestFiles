import os

def rename_int_file(folder):
    """This method renames the INT files present in the folder in the DEV_CRE format.

    Args:
        folder (folder) : this is the folder path where all the files are kept
    """
    # folder = r"C:\Users\SG0701644\OneDrive - Sabre\Files\INTEncryptedFiles\Sep\7-Sep"
    all_files = os.listdir(folder)

    for file in all_files:
        # print(file)
        file_name = file[16::] # for removing prefix as this version of python doesnt support prefix method
        # use this for INT Files
        if(file.__contains__("INT")):
            file_name = "DEV_" + file_name

        #use this for CERT Files
        if(file.__contains__("CERT")):
            file_name = "DEV" + file_name

        # if(file_name.count("TKTT") > 1):
        #     file_name = file_name.replace("_TKTT","",1)

        old_file_path = os.path.join(folder,file)
        new_file_path = os.path.join(folder,file_name)
        os.rename(old_file_path,new_file_path)
        print(f"The {file} has been renamed to \n {file_name}\n\n")
        

if __name__ == "__main__":
    folder = r"C:\Users\SG0701644\OneDrive - Sabre\Files\INTEncryptedFiles\Sep\26-Sep"
    rename_int_file(folder)