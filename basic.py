from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LTTextBoxHorizontal

def extraer():
    # Press Ctrl+F8 to toggle the breakpoint.
    document = open('5.pdf', 'rb')
    # Create resource manager
    rsrcmgr = PDFResourceManager()
    # Set parameters for analysis.
    laparams = LAParams()
    # Create a PDF page aggregator object.
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    numpage = 0
    for page in PDFPage.get_pages(document):
        interpreter.process_page(page)
        # receive the LTPage object for the page.
        layout = device.get_result()
        numpage += 1
        print("PAGE " + str(numpage))
        v = ""
        lines = []
        for element in layout:
            if isinstance(element, LTTextBoxHorizontal):
                # lines.extend(element.get_text().splitlines())
                values = element.get_text()
            v = str(values).replace('\n', ' ')
            print(v)
        # print(lines)
        # for lll in lines:
        #    print(lll)
    document.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    extraer()

