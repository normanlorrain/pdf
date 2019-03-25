import documentstructure as ds
import content_stream
import resources

class Page():
    def __init__(self, parent):
        self.parent = parent
        self.ds = parent.ds
        self.objectNumber = self.ds.nextObjectNumber()
        self.contentsObjectNumber = 0
        self.resourceObjectNumber = 0
        self.ds.objects.append(self)

    def __repr__(self):
        return f"""{self.objectNumber} 0 obj
    << /Type /Page
       /Parent {self.parent} 0 R
       /MediaBox [0 0 612 792]
       /Contents {self.contentsObjectNumber} 0 R
       /Resources << /ProcSet {self.resourceObjectNumber} 0 R >>
    >>
endobj

"""        
    def addContents(self):
        cont = content_stream.ContentStream(self)
        self.contentsObjectNumber = cont.objectNumber
        res = resources.Resources(self)
        self.resourceObjectNumber = res.objectNumber


