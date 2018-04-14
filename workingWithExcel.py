import openpyxl

workbook = openpyxl.load_workbook('cwd_file.xlxs')

# a sinle xlxs file might contain multiple tabs and 
# or maybe you can call that a sheet
# that little tab thingy in the left-bottom of your 
# excel file??? yeah, that's what it is... that's a sheet

# you can select a sheet by

sheet1 = workbook.get_sheet_by_name('sheet_name_i.e_sheet1')

# get names of all sheets, no paras

sheets = workbook.get_sheet_names()
# print (sheets) will result in sheet1

# let's suppose we get a sheet named sheet1, let's work with it
cellOrColumnName = sheet1['firstColumnName']
# [] bracket in sheet gets call objects
# cell objects have value member variable
# with all the contents of that cell. 

store = str(cellOrColumnName.value)
 
#  cell() method retusn a Cell object from a sheet