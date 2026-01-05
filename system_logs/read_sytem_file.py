file_path="system_logs\\system.txt"
info_path="system_logs\\info.txt"
warning_path="system_logs\\warning.txt"
eror_path="system_logs\\eror.txt"

fr_filepath=open(file_path,"r")

fw_info=open(info_path,"w")
fw_warning=open(warning_path,"w")
fw_eror=open(eror_path,"w")

for line in fr_filepath:

    line=line.rstrip("\n")

    log_type=line.split(" ")[2].casefold()

    if log_type=="error":

        fw_eror.write(log_type+"\n")
    elif log_type=="warning":

        fw_warning.write(log_type+"\n")

    elif log_type=="info":

        fw_info.write(log_type+"\n")

print("program end")


    

    
