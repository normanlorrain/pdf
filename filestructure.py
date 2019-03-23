_HEADER="%PDF-1.7\n"

# See section 3.4 in spec.
class FileStructure():
    def __init__(self, documentStructure ):
        self.ds=documentStructure
        

    def __repr__(self):
        # generating cross reference requires the beginning of the offset
        bodyOffset = len(_HEADER)
        body, xref = self.ds.generateBody( bodyOffset )
        xrefOffset = bodyOffset + len(body)
        return _HEADER + body + xref + self.generateTrailer(xrefOffset)

    def generateTrailer(self, xrefOffset):
        return f"""trailer
<< /Size {len(self.ds.objects)+1}
   /Root {self.ds.catalog.objectNumber}
>>
startxref
{xrefOffset}
%%EOF"""

 
    

