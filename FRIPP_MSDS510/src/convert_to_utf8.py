# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 21:14:56 2018

@author: jfrip
"""
# Create script to convert avengers.csv file to utf-8 encoding

import sys, csv

def utf8_encode(input_file_path, output_file_path):
    '''
    This will open a file in format ISO-8859 to prepare it for conversion to
    prepare it for another format during decoding/encoding
    Mode is Read Binary (Windows)
    '''
    with open(input_file,mode='rb') as a:
        txt_file = a.read()

    #write the new file as (Entered File Name) to the working directory
    with open(output_file,encoding='UTF8' ,mode='w') as a:
        #This works, but it writes it to the current working directory when I run it in the
        #console if I'm using an IDE like Spyder
        #Perhaps someone could help with how/if running via command line works and I'm just doing something wrong?
        a.write('txt_file')
        



