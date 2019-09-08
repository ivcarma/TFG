import xlrd 
import os
import pandas as pd
import difflib
from operator import itemgetter

def GetConferenceRating(venue):
  
  #gets your current directory
  dirname = os.path.dirname(__file__)
  loc = os.path.join(dirname, r'GII-GRIN-SCIE-Conference-Rating-30-mag-2018-11.54.45-Output.xlsx')
  
  workbook = xlrd.open_workbook(loc) 
  sheet = workbook.sheet_by_index(0) 
  art = {} 

  enc = False
  for box in range(sheet.nrows):


    if venue == sheet.cell_value(box,1) or venue == sheet.cell_value(box,2):
        enc = True
        art['classRate'] = sheet.cell_value(box,3)
        art['rating'] = sheet.cell_value(box,4)
        art['classes'] = sheet.cell_value(box,5)
       

  if enc ==  False:
    art['classRate'] = 'Not Found'
    art['rating'] = 'Not Found'
    art['classes'] = 'Not Found'
    

  return art

  

def GetAcronymSlice(venue):
  
  splits = venue.split(' ')
  aux = ''
  acronym = ''
  
  for i in splits:
	  acronym = acronym + '' + aux
	  aux = ''
	  if i[0].isupper():
		  aux = i[0]

  return acronym


def DiffLibSearch(revista):
    
  #Get path file
  dirname = os.path.dirname(__file__)
  loc = os.path.join(dirname, r'JCR2018.xlsx')

  #Initialize reader
  workbook = xlrd.open_workbook(loc) 
  sheet = workbook.sheet_by_index(0) 

  tuplas = []


  for i in range(sheet.nrows):
      valor = (sheet.cell_value(i,1), difflib.SequenceMatcher(None, revista, sheet.cell_value(i,1)).ratio())
      tuplas.append(valor)

  result = max(tuplas,key=itemgetter(1))[0]
  
  return result


def GetJournalRating(venue): 

  dirname = os.path.dirname(__file__)
  loc = os.path.join(dirname, r'JCR2018.xlsx')
  
  
  
  workbook = xlrd.open_workbook(loc) 
  sheet = workbook.sheet_by_index(0) 
  art = {}

  venue = DiffLibSearch(venue)

  for box in range(sheet.nrows):

    if venue == sheet.cell_value(box,1):
      art['2015_CiteScore'] = sheet.cell_value(box,7)
      art['2015_SJR'] = sheet.cell_value(box,8)
      art['2015_SNIP'] = sheet.cell_value(box,9)
      art['2016_CiteScore'] = sheet.cell_value(box,10)
      art['2016_SJR'] = sheet.cell_value(box,11)
      art['2016_SNIP'] = sheet.cell_value(box,12)
      art['2017_CiteScore'] = sheet.cell_value(box,13)
      art['2017_SJR'] = sheet.cell_value(box,14)
      art['2017_SNIP'] = sheet.cell_value(box,15)

      

  return art





  

  
    
    
     






  




