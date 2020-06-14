import textract

text = textract.process(r"C:\Users\212437054\Documents\projects\confluence-api\data\WHB\1 01 2013 PER_Kodex chování skupiny WW_4.pdf", method='pdfminer')

print(text)