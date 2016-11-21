'''
Created on Nov 20, 2016

@author: cfsu
'''

from Rename.Uitl import get_files_list, get_dirs_list, parse_file_name,\
    rename_file_list
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Rename files")
    parser.add_argument('-dir', action='store', dest='dir')
    parser.add_argument('-update', action='store_true', default=False, dest='update')
    args = parser.parse_args()
    print "running script on {} with update flag {}".format(args.dir, args.update)
    
    result = get_files_list(args.dir, True)
    rename_file_list(result, args.update)
