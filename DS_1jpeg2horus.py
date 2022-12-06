from imageio import imread
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Input Agreement ============================================
sInputFileName='C:/VKHCG/05-DS/9999-Data/Angus.jpg'
InputData = imread(sInputFileName, as_gray=False, pilmode='RGBA')

print('Input Data Values ===================================')
print('X ',InputData.shape[0])
print('Y ',InputData.shape[1])
print('RGBA ', InputData.shape[2])
print('='*53)
# Processing Rules ===========================================
ProcessRawData=InputData.flatten()
y=InputData.shape[2] + 2
x=int(ProcessRawData.shape[0]/y)
ProcessData=pd.DataFrame(np.reshape(ProcessRawData, (x, y)))
sColumns= ['XAxis','YAxis','Red', 'Green', 'Blue','Alpha']
ProcessData.columns=sColumns
ProcessData.index.names =['ID']
print('Rows ',ProcessData.shape[0])
print('Columns ',ProcessData.shape[1])
print('='*53)
print('Process Data Values =================================')
print('='*53)
plt.imshow(InputData)
plt.show() 
print('='*53)
# Output Agreement ===========================================
OutputData=ProcessData
print('Storing File')
sOutputFileName='C:/VKHCG/05-DS/9999-Data/HORUS-Picture.csv'
OutputData.to_csv(sOutputFileName, index = False)
print('='*53)
print('Picture to HORUS - Done')
print('='*53)
