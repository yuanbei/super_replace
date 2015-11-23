#!/usr/bin/env python
# coding: utf-8

from datetime import datetime
import argparse
import io
import os
import re
import string
import sys
import time

class PrintProgress():
    def __init__(self, taskName):
        self.taskName = taskName
        self.beginTime = datetime.now()

    def printSpendingTime(self):
        self.endTime = datetime.now()
        print '%s Begins at :%s' % (self.taskName, self.beginTime)
        print '%s Ends at   :%s' % (self.taskName, self.endTime)
        print 'Spend time: %s \n'%(self.endTime - self.beginTime)
        print 'Finish!'

class Replace():

    def __init__(self, parameters):
       self.input_files = parameters.input;
       self.searched_str = parameters.search;
       self.replace_str = parameters.replace;
       self.exclude_files = []

       with io.open(parameters.exclude, 'r') as handle:
           self.exclude_files = handle.readlines()

    def DoReplace(self):
        printProgress = PrintProgress('DoReplace')
        if os.path.isfile(self.input_files):
            if not self.is_excluded(self.input_files):
                self.replace_and_save(self.input_files)
        else:
            for root,dirs,files in os.walk(self.input_files):
                for file in files:
                    input_file = root + os.sep + file
                    if self.is_excluded(file):
                        continue
                    self.replace_and_save(input_file)
        printProgress.printSpendingTime()

    def replace_and_save(self, input_file):
        f = open(input_file,'r+')
        content=f.read()
        f.seek(0)
        f.truncate()
        f.write(content.replace(self.searched_str, self.replace_str))
        f.close()

    def is_excluded(self, file):
        for exclude_file in self.exclude_files:
            exclude_file_s = exclude_file.strip().strip('\n')
            if file.count(exclude_file_s) > 0:
                return True
        return False

def main():
    parser = argparse.ArgumentParser(description='Traverse a given dictionary or a given file , replace searched string with new string.')
    parser.add_argument(
      '-i', '--input', type=str,
      help='path to a dictionary or a file'
    )

    parser.add_argument(
      '-s', '--search', type=str,
      help='searched string'
    )

    parser.add_argument(
      '-r', '--replace', type=str,
      help='replace string'
    )

    parser.add_argument(
      '-e', '--exclude', type=str,
      help='excluded files list'
    )

    parameters = parser.parse_args()
    p = Replace(parameters)
    p.DoReplace()

if __name__ == '__main__':
    main()
