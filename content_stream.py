class ContentStream():
    def __init__(self, parent):
        self.objectNumber = parent.ds.nextObjectNumber()
        self.streamString =  ""
        parent.ds.objects.append(self)
    def __repr__(self):
        return f"""{self.objectNumber} 0 obj
<< /Length {len(self.streamString)} >>
stream
{self.streamString}
endstream
endobj

"""        
