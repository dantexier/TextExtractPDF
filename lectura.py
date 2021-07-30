import os
from os.path import isfile, join
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTFigure, LTText,LTTextBoxHorizontal
#LTTextBox
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage, PDFTextExtractionNotAllowed
from pdfminer.pdfparser import PDFParser
from cleantext import clean

pdf_dir = "./FILES"
count = 1
corpus = (f for f in os.listdir(pdf_dir) if not f.startswith('.') and isfile(join(pdf_dir, f)))
for filename in corpus:
    print (str(count) + " "+ filename)
    count+=count
    text = ""
    with open(pdf_dir+"/"+filename, 'rb') as f:
        parser = PDFParser(f)
        doc = PDFDocument(parser)
        page = list(PDFPage.create_pages(doc))[0]
        rsrcmgr = PDFResourceManager()
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        interpreter.process_page(page)
        layout = device.get_result()
        numLayout = 0
        p = ""
        for obj in layout:
            if isinstance(obj, LTTextBoxHorizontal):
                values = obj.get_text()
                v =str(values).replace('\n', ' ')
        print("LLLL"+p)
#            if isinstance(obj, LTTextBox):
#                text += obj.get_text()
#                if isinstance(text, LTText):
#                    for text_line in element:
#                        print (text_line)
#            elif isinstance(obj, LTFigure):
#                stack += list(obj)

        #print(text.encode("utf-8"))
        #print (text+"\t \t \t")

        
        
