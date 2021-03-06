# -*- coding: utf-8 -*-

'''
Created on Nov 14, 2016

@author: cfsu
'''

import unittest
import os
from Rename.Uitl import get_files_list, get_dirs_list, parse_file_name,\
    rename_file_list

class Test(unittest.TestCase):

    def setUp(self):

        create_test_dir_in('.', 'datadir')
        create_test_dir_in('datadir', 'testdir1')
        
        create_test_files_in('datadir')

        create_test_dir_in('datadir', 'testdir2')
        create_test_dir_in('datadir', 'testdir3')
        create_test_dir_in('datadir', 'testdir4')

        create_test_files_in(os.path.join('datadir', 'testdir3'))
        

    def tearDown(self):
        #shutil.rmtree('testdir1')
        pass

    def test_get_files_list(self):
        result = get_files_list('datadir', False)
        print result
        self.assertTrue(len(result), 'get correct lists of files')
        
    def test_get_dirs_list(self):
        result = get_dirs_list('.')
        self.assertTrue(result, 'get correct lists of dirs')

    def test_parse_file_nmae(self):
        old_name = "Thumbs (2014_08_25 20_02_34 UTC).pdf"
        new_name = "Thumbs.pdf"
        ts = "2014_08_25 20_02_34"
        found_name, found_ts = parse_file_name(old_name)
        self.assertEqual(found_name, new_name, "new name is wrong")
        self.assertEqual(found_ts, ts, "time stamp is wrong")

        old_name = "Thumbs (2014_08_25).pdf"
        new_name = "Thumbs (2014_08_25).pdf"
        ts = '9999'
        found_name, found_ts = parse_file_name(old_name)
        self.assertEqual(found_name, new_name, "new name is wrong")
        self.assertEqual(found_ts, ts, "time stamp is wrong")

        old_name = "abc/xyz/Thumbs (2014_08_25 20_02_34 UTC).pdf"
        new_name = "abc/xyz/Thumbs.pdf"
        ts = "2014_08_25 20_02_34"
        found_name, found_ts = parse_file_name(old_name)
        self.assertEqual(found_name, new_name, "new name is wrong")
        self.assertEqual(found_ts, ts, "time stamp is wrong")

        old_name = "abc/xyz/Thumbs (2) (2014_08_25 20_02_34 UTC).pdf"
        new_name = "abc/xyz/Thumbs (2).pdf"
        ts = "2014_08_25 20_02_34"
        found_name, found_ts = parse_file_name(old_name)
        self.assertEqual(found_name, new_name, "new name is wrong")
        self.assertEqual(found_ts, ts, "time stamp is wrong")


        old_name = '各班代表名單 (2014_06_09 02_52_33 UTC).xls'
        new_name = '各班代表名單.xls'
        ts = "2014_06_09 02_52_33"
        found_name, found_ts = parse_file_name(old_name)
        self.assertEqual(found_name, new_name, "new name is wrong")
        self.assertEqual(found_ts, ts, "time stamp is wrong")

        old_name = u'2016新春祈福流程_V6_021017 (2016_02_12 12_32_32 UTC).doc'
        new_name = u'2016新春祈福流程_V6_021017.doc'
        ts = "2016_02_12 12_32_32"
        found_name, found_ts = parse_file_name(old_name)
        self.assertEqual(found_name, new_name, "new name is wrong")
        self.assertEqual(found_ts, ts, "time stamp is wrong")


    def test_rename_files(self):
        result = get_files_list('datadir', True)
        rename_file_list(result, True)
        result = get_files_list('datadir/testdir3/', False)
        self.assertEqual(['datadir/testdir3/test1.txt', 'datadir/testdir3/test2.txt', 'datadir/testdir3/test3.txt'], result, "time stamp is wrong")
        
    def test_handel_chinese_character(self):
        file_name = u'2016新春祈福流程_V6_021017 (2016_02_12 12_32_32 UTC).doc'
        with open(os.path.join('datadir','testdir4', file_name), "w") as f:
            f.write(file_name.encode("UTF-8"))

        result = get_files_list('datadir/testdir4', True)
        rename_file_list(result, True)
        result = get_files_list('datadir/testdir4/', False)
        self.assertEqual([u'datadir/testdir4/2016新春祈福流程_V6_021017.doc'], result, "time stamp is wrong")
        

def create_test_files_in(path):
    file_names = ('test1 (2014_08_25 20_02_34 UTC).txt', 'test1 (2014_12_25 20_02_34 UTC).txt', 'test2.txt', 'test3 (2014_08_25 20_02_34 UTC).txt', 'test3 (2014_12_25 20_02_34 UTC).txt')
    for file_name in file_names:
        with open(os.path.join(path, file_name), "w") as f:
            f.write(file_name)

def create_test_dir_in(current, dir_name):
    dirpath = os.path.join(current,dir_name)
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)
    pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()