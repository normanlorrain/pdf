import documentstructure as ds
import content_stream
import resources


class Page():
    def __init__(self, parent):
        self.height = 792 # points, letter size
        self.width = 612 # points, letter size 
        self.parent = parent
        self.ds = parent.ds
        self.objectNumber = self.ds.nextObjectNumber()
        #self.contentsObjectNumber = 0
        #self.resourceObjectNumber = 0
        self.ds.objects.append(self)

    def __repr__(self):
        return f"""{self.objectNumber} 0 obj
    << /Type /Page
       /Parent {self.parent.objectNumber} 0 R
       /MediaBox [0 0 {self.width} {self.height}]
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


