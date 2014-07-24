import xlrd
import csv
import glob
import os
import sys

def csv_from_excel(file):

    wb = xlrd.open_workbook(file)
    sheets=wb.sheet_names()
    sh = wb.sheet_by_name(sheets[0])
              
    if sys.version_info >= (3,0,0):
        your_csv_file = open(file.split('.xlsx')[0] + '.csv', 'w', newline='')
    else:
        your_csv_file = open(file.split('.xlsx')[0] + '.csv', 'wb')
    wr = csv.writer(your_csv_file, delimiter='\t', quoting=csv.QUOTE_NONE)

    for rownum in range(sh.nrows):
        wr.writerow(sh.row_values(rownum))

    your_csv_file.close()
	

verbose=True    
if __name__ == '__main__':	
    import argparse

    whatitdoes="This program converts a series of xls[x] files into csv."
    myself="(c) JFB 2014"
    parser = argparse.ArgumentParser(description=whatitdoes, epilog=myself)

    parser.add_argument(
    help = 'List of files to convert (accepts regular expression)',
    dest = 'argfiles', default = '*.xls*', type = str,  nargs = '*')

    parser.add_argument('-v','--verbose', help = 'Prints information',
    dest = 'verbose', default = False,   #action='store_true'
    action='count')

    arguments = parser.parse_args()
    verbose=arguments.verbose
    if verbose==2: print("script arg: ", arguments.argfiles)
    xlsx_files = glob.glob(arguments.argfiles[0])
    if verbose==2: print("glog.glog expansion: ", xlsx_files, '\n')
    if len(xlsx_files) == 0:
        raise RuntimeError('No XLSX files to convert.')
    """    
    if len(sys.argv)>1:
        #print("Converting ",sys.argv[1])
        if verbose: print("script arg: ", sys.argv)
        xlsx_files = glob.glob(sys.argv[1])
        if verbose: print("glog.glog expansion: ", xlsx_files, '\n')
    else:
        xlsx_files = glob.glob('*.xls*')
        
    if len(xlsx_files) == 0:
        raise RuntimeError('No XLSX files to convert.')
    	
    """        
    for file in xlsx_files:
        if verbose:
            print("Converting {}".format(file))
        csv_from_excel(file)