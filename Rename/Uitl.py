'''
Created on Nov 14, 2016

@author: cfsu
'''

from os import walk
import os
import re

def get_files_list(path, recursive = False):
    total_filenames = []
    for (dirpath, dirnames, filenames) in walk(unicode(path, 'utf-8')):
        #print filenames
        full_dirpaths = []
        full_filenames = []
        full_dirpaths.extend(os.path.join(dirpath, dir) for dir in dirnames) 
        full_filenames.extend(os.path.join(dirpath, f) for f in filenames)         
        total_filenames.extend(full_filenames)
        if recursive == False :
            break

    return total_filenames
        
def rename_file_list(filenames, update=False):
    old_name_2_new_name_ts = {}
    new_name_2_old_name_ts = {}
    for file in filenames :
        (new_name, ts) = parse_file_name(file)
        #print "parse {} to ({}, {})".format(file, new_name,ts)
        old_name_2_new_name_ts[file] = (new_name, ts)
        #check if the new_name already exits
        if new_name in new_name_2_old_name_ts:
            (old_name, last_ts) = new_name_2_old_name_ts[new_name]
            if last_ts > ts:
                #older copy exists, this becomes a delete candidate
                old_name_2_new_name_ts[file] = (None, None)
            else:
                #this is an older copy. Keep it and delete the earlier one
                old_name_2_new_name_ts[old_name] = (None, None)
                new_name_2_old_name_ts[new_name] = (file, ts)                
        else:
            new_name_2_old_name_ts[new_name] = (file, ts)
        
    for file in old_name_2_new_name_ts:
        (new_name, ts) = old_name_2_new_name_ts[file]
        if not update:
            if new_name:
                if file != new_name:
                    print "Dry run: rename {} to {}".format(file.encode("UTF-8"), new_name.encode("UTF-8"))
            else:
                print "Dry run: delete {}".format(file.encode("UTF-8"))
        else:  
            if new_name:
                if file != new_name:
                    try:
                        print "rename {} to {}".format(file.encode("UTF-8"), new_name.encode("UTF-8"))
                        os.rename(file, new_name)
                    except OSError:
                        print "rename failed"
            else:
                try:
                    print "delete {}".format(file.encode("UTF-8"))
                    os.remove(file)
                except OSError:
                    print "delete fialed"
            
def parse_file_name(file):
    ts_search = re.search('\((20.*)UTC\)', file)
    if ts_search:
        ts = ts_search.group(1).strip()
        new_name = re.sub(' \(' + ts + ' UTC\)', '', file)
        return (new_name, ts)
    else:
        return (file, '9999')

def get_dirs_list(path):
    return True

if __name__ == '__main__':
    pass