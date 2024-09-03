headerlog = "[LOG] : "
headerError = "[ERROR] : "
def splittext (fileName, action):
    try:
        fileName = "ParameterdataType.txt"
        f = open("ListVariables.txt", "r")
        with open(fileName, "wb") as binary_file:
            for x in f:
                local = x.replace(" ", "").replace(";", "")
                local = local.replace("staticDimVar", "").replace("dcwCOMVAR,","")
                match action:
                    case 1:
                        local = local[:local.find("(")] + "\n"
                        binary_file.write(local.encode('utf-8', 'ignore'))
                        print (fileName + action)
                        print(local)
                    case 2:
                        local = local[local.find("//"):] + "\n"
                        local = local.replace("/", "")
                        binary_file.write(local.encode('utf-8', 'ignore'))
                        print(local)
                    case 3:
                        local = local[local.find("UI"):local.find(")")]
                        print(local)
                        local = local[local.find("L"):].replace("\"", "").replace("L", "") + "\n"
                        print(local)
                        binary_file.write(local.encode('utf-8', 'ignore'))
                        print(local)
                    case 4:
                        local = local[local.find("UI"):local.find("\")")]
                        local = local[local.find("I"):local.find("l")].replace("I","") + "\n"
                        binary_file.write(local.encode('utf-8', 'ignore'))
                        print(local)
                    case _:
                        print("Vacio")
                
        binary_file.close()
        f.close()
    except:
        print("Vacio")



def readjsonfile ():
    f = open("Lecturajson.txt", "rb")
    with open ("result.txt", "wb") as binary:
        for x in f:
            local = str(x).replace(",","")
            local = local[local.find(":"):].replace(":", "").replace("\"", "")
            local = local[:local.find("\\")] +  "\n"
            binary.write(local.encode('utf-8', 'ignore'))
            print(local)

    binary.close()
    f.close()


def main():
    path = ""
    while True:
        try:
            print('****************************\n' +  
                'SPLIT TEXT DOCUMENTS\n' + 
                '****************************\n')
            print('Número de Maquinas\n' +
                '1.ParameterCode\n'+
                '2.ParameterName\n'+
                '3.ParameterLegth\n'+
                '4.ParameterdataType\n'+
                '5.Exit')
            numeroAction = input("Seleccione la option que desea: ")
            if numeroAction == "1":
                splittext("ParameterCode1.txt", 1)
            if numeroAction == "2":
                splittext("ParameterName.txt", 2)
            if numeroAction == "3":
                splittext("Parameterlength.txt", 3)                
            if numeroAction == "4":
                splittext("ParameterdataType.txt", 4)                
            if numeroAction == "5":
                print(headerlog + "ADIOS")
                break
            if numeroAction == "6":
                readjsonfile()
                break
        except:
            print(headerError + "Error")
            break;

#main()
readjsonfile()

