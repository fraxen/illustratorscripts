# Convert old .doc metadata to XMP
import os

# First do this in c:\projection: attrib /s *.ai | cut -b14- > c:\home\hugo\work\allaifiles.txt
# Then we read that file into a list
"""
with open(r'c:\home\hugo\work\allaifiles.txt') as f:
    allAi = f.read()
allAi = allAi.split('\n')
"""

# Check where there are word files with the .ai files
"""
outFile = ''
for aifile in allAi:
    if os.path.exists(aifile[:-3] + '.doc'):
        outFile = outFile + aifile + '\n'

with open(r'c:\home\hugo\work\allaifiles2.txt','w') as f:
    f.write(outFile)
"""

# Convert doc to docx so that we can interpret the files

import win32com.client
wrd = win32com.client.Dispatch("Word.Application")
wrd.visible = 1
wb = wrd.Documents.Open(r"C:\project\1001 siwi west asia\graphics\02_jordangw\02_jordangw.doc")
wb.SaveAs2(r"c:\home\hugo\work\test.docx", FileFormat=16)
wb.Close()
wrd.Quit()
