class ContentStream():
    def __init__(self, parent):
        self.objectNumber = parent.ds.nextObjectNumber()
        self.streamString = "BT\n/F1 24 Tf\n100 100 Td\n(Hellow World) Tj\nET" 
        parent.ds.objects.append(self)
    def __repr__(self):
        return f"""{self.objectNumber} 0 obj
<< /Length {len(self.streamString)} >>
stream
{self.streamString}
endstream
endobj

"""        
