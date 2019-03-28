import documentstructure as ds
import content_stream
import resources

import font.core14

class Page():
    def __init__(self, parent):
        self.pageHeight = 792 # points, letter size
        self.pageWidth = 612 # points, letter size 
        self.topMargin = 72
        self.leftMargin = 72
        self.rightMargin = 72
        self.bottomMargin = 72

        self.parent = parent
        self.ds = parent.ds
        self.objectNumber = self.ds.nextObjectNumber()
        #self.contentsObjectNumber = 0
        #self.resourceObjectNumber = 0
        self.ds.objects.append(self)

        self.textPositionX = self.leftMargin
        self.textPositionY = self.pageHeight - self.topMargin


    def __repr__(self):
        return f"""{self.objectNumber} 0 obj
    << /Type /Page
       /Parent {self.parent.objectNumber} 0 R
       /MediaBox [0 0 {self.pageWidth} {self.pageHeight}]
       /Contents {self.contentsObjectNumber} 0 R
       /Resources << /ProcSet {self.resourceObjectNumber} 0 R >>
    >>
endobj

"""        
    def addContents(self, streamString):
        cont = content_stream.ContentStream(self)
        cont.streamString = streamString
        self.contentsObjectNumber = cont.objectNumber
        res = resources.Resources(self)
        self.resourceObjectNumber = res.objectNumber


    def addText(self, textString ):
        self.textPositionY -= font.core14.stringHeight(textString,font.core14.HELVETICA, 12)
        self.addContents(f"BT\n/F1 12 Tf\n{self.textPositionX} {self.textPositionY} Td\n0 Tr\n({textString}) Tj\nET")
