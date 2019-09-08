import xlrd 
import os
import pandas as pd
import difflib
from distance import levenshtein
from distance  import sorensen
from  distance import jaccard
from time import time



def RatingLevenshtein(revista):
    
    #Get path file
    dirname = os.path.dirname(__file__)
    loc = os.path.join(dirname, r'JCR2018.xlsx')

    #Initialize reader
    workbook = xlrd.open_workbook(loc) 
    sheet = workbook.sheet_by_index(0) 

    tuplas = []

    start_time = time()

    for i in range(sheet.nrows):
        valor = (sheet.cell_value(i,1), levenshtein(revista, sheet.cell_value(i,1)))
        tuplas.append(valor)
        

    final_time = time()  
    execution_time = round(final_time - start_time, 2) 

    tuplas.sort(key=lambda revista: revista[1])

    top_5 = tuplas[:10]

    result = (top_5, execution_time)
    
    return result


def RatingSorensen(revista):
    
    #Get path file
    dirname = os.path.dirname(__file__)
    loc = os.path.join(dirname, r'JCR2018.xlsx')

    #Initialize reader
    workbook = xlrd.open_workbook(loc) 
    sheet = workbook.sheet_by_index(0) 

    tuplas = []

    start_time = time()

    for i in range(sheet.nrows):
        valor = (sheet.cell_value(i,1), sorensen(revista, sheet.cell_value(i,1)))
        tuplas.append(valor)
        

    final_time = time()  
    execution_time = round(final_time - start_time, 2)

    tuplas.sort(key=lambda revista: revista[1])

    top_5 = tuplas[:10]

    result = (top_5, execution_time)
    
    return result


def RatingJaccard(revista):
    
    #Get path file
    dirname = os.path.dirname(__file__)
    loc = os.path.join(dirname, r'JCR2018.xlsx')

    #Initialize reader
    workbook = xlrd.open_workbook(loc) 
    sheet = workbook.sheet_by_index(0) 

    tuplas = []

    start_time = time()

    for i in range(sheet.nrows):
        valor = (sheet.cell_value(i,1), jaccard(revista, sheet.cell_value(i,1)))
        tuplas.append(valor)
        

    final_time = time()  
    execution_time = round(final_time - start_time, 2)

    tuplas.sort(key=lambda revista: revista[1])

    top_5 = tuplas[:10]

    result = (top_5, execution_time)
    
    return result


def RatingDiffLib(revista):
    
    #Get path file
    dirname = os.path.dirname(__file__)
    loc = os.path.join(dirname, r'JCR2018.xlsx')

    #Initialize reader
    workbook = xlrd.open_workbook(loc) 
    sheet = workbook.sheet_by_index(0) 

    tuplas = []

    start_time = time()

    for i in range(sheet.nrows):
        valor = (sheet.cell_value(i,1), difflib.SequenceMatcher(None, revista, sheet.cell_value(i,1)).ratio())
        tuplas.append(valor)


    final_time = time()  
    execution_time = round(final_time - start_time, 2)

    tuplas.sort(key=lambda revista: revista[1], reverse = True)

    top_5 = tuplas[:10]

    result = (top_5, execution_time)
    
    return result

