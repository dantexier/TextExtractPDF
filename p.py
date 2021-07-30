import PyPDF2

pdfFileObj = open('xyz.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pageCount = pdfReader.numPages
count = 0
text = ''

while count < pageCount:
    pageObj = pdfReader.getPage(count)
    count +=1
    text += pageObj.extractText()
    print ("line:"+str(count))
    print (text)

print (text)
