import trailer

class FileStructure():
    def __init__(self, documentStructure ):
        self.header="%PDF-1.7\n"
        self.ds=documentStructure
        self.xref=""
        self.trailer=trailer.Trailer()
        pass

    def __repr__(self):
        return self.header + str(self.ds) + self.xref + str(self.trailer)
    

