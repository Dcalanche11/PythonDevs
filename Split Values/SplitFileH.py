global headerlog
global headerError
headerError = "[ERROR] : "
headerlog = "[LOG] : "

class ProcessTextFile:

    def __init__(self, Namefileread) -> None:
        self.Namefileread = Namefileread

    def replaceHeaders (self, x):
        local = x.replace(" ", "").replace(";", "")
        local = local.replace("staticDimVar", "").replace("dcwCOMVAR,","")
        return local   
    
    def getParameterCode (self, fileResult):
        file = open(self.Namefileread, "r")
        with open(fileResult, "wb") as binary_file:
            for line in file:
                local = self.replaceHeaders(line)
                local = local[:local.find("(")] + "\n"
                binary_file.write(local.encode('utf-8', 'ignore'))
        binary_file.close()
        file.close()        

    def getParameterName (self, fileResult):
        file = open(self.Namefileread, "r")
        with open(fileResult, "wb") as binary_file:
            for line in file:
                local = self.replaceHeaders(line)
                local = local[local.find("//"):] + "\n"
                local = local.replace("/", "")     
        binary_file.close()
        file.close()               
    
    def getParameterLegth (self, fileResult):
        file = open(self.Namefileread, "r")
        with open(fileResult, "wb") as binary_file:
            for line in file:
                local = self.replaceHeaders(line)
                local = local[local.find("UI"):local.find(")")]                        
                local = local[local.find("L"):].replace("\"", "").replace("L", "") + "\n"  
        binary_file.close()
        file.close() 

    def getParameterType (self, fileResult):
        file = open(self.Namefileread, "r")
        with open(fileResult, "wb") as binary_file:
            for line in file:
                local = self.replaceHeaders(line)
                local = local[local.find("UI"):local.find("\")")]
                local = local[local.find("I"):local.find("l")].replace("I","") + "\n"    
        binary_file.close()
        file.close()      

    def getjsonfile (self, fileResult):
        file = open(self.Namefileread, "rb")
        with open (fileResult, "wb") as binary:
            for line in file:
                local = str(line).replace(",","")
                local = local[local.find(":"):].replace(":", "").replace("\"", "")
                local = local[:local.find("\\")] +  "\n"
                binary.write(local.encode('utf-8', 'ignore'))
        binary.close()
        file.close()


