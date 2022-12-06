import sys
import os
import pandas as pd

sInputFileName='Good-or-Bad.csv'
sOutputFileName='Good-or-Bad-03.csv'
Company='01-Vermeulen'
Base='E:/VKHCG'

print('='*32)
print('Working Base: ',Base,' using Windows')
sFileDir=Base+'/'+Company+'/'+'02-Assess/01-EDS/02-Python'
if not os.path.exists(sFileDir):
    os.makedirs(sFileDir())
sFileName=Base+'/'+Company+'/'+'00-RawData/'+sInputFileName
print('Loading: ',sFileName)

RawData=pd.read_csv(sFileName,header=0)
print('='*32)
print('Raw Data Values')
print('='*32)
print(RawData)
print('='*32)
print('Data Profile')
print('Rows: ',RawData.shape[0])
print('Columns: ',RawData.shape[1])
print('='*32)

sFileName=sFileDir+'/'+sInputFileName
RawData.to_csv(sFileName,index=False)

TestData=RawData.dropna(thresh=2)
print('='*32)
print('Test Data Values')
print('='*32)
print(TestData)
print('='*32)
print('Data Profile')
print('='*32)
print('Rows: ',TestData.shape[0])
print('Columns: ',TestData.shape[0])
print('='*32)
sFileName=sFileDir+'/'+sOutputFileName
TestData.to_csv(sFileName,index=False)
print('='*13,'Done','='*13)