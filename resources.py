class Resources():
    def __init__(self, parent):
        self.objectNumber = parent.ds.nextObjectNumber()

        self.resourceString = "[/PDF]"
            #    /Contents {self.contentsObjectNumber} 0 R
        parent.ds.objects.append(self)


    def __repr__(self):
        return f"""{self.objectNumber} 0 obj
    {self.resourceString}
endobj

"""    