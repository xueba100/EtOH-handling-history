# Data-Extract#
##Scripts in this directory are used for data extraction from txt files.##

##Here are steps to use these scripts to get csv file.##
###Step 1. Download data from websites like http://kdd.ics.uci.edu/databases/eeg/eeg.html###
###Step 2. Manally get txt files from gz packages.(This is an exhausting job. If you know how to do this with little pain, please let me know.)###
###Step 3. Use get_txt_format_in_a_given_directory.py in folder "encoding-format" to check endoding format###
###Step 4. If not all usf-8-sig(or the format you want),use format_converting.py in folder "encoding-format" to convert it to utf-8-sig. If you like other formats, please modify the script on your own.###
###Step 5. Convert the txt file to a csv file. Use from_txt_to_csv_massive.py to convert all txt files in a given directory from you to csv file.###