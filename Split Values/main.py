from SplitFileH import *

def main():
    file = ProcessTextFile("ListVariables.txt")
    while True:
        try:
            print('****************************\n' + 'SPLIT TEXT DOCUMENTS\n' + '****************************\n')
            print('Número de Maquinas\n' +
                '1.ParameterCode\n'+
                '2.ParameterName\n'+
                '3.ParameterLegth\n'+
                '4.ParameterdataType\n'+
                '5.Jsonfile\n' +
                '6.Exit')
            vtOption = input("Seleccione la option que desea: ")
            match vtOption:
                case "1":
                    file.getParameterCode("ParameterCode.txt")
                case "2":
                    file.getParameterName("ParameterName.txt")
                case "3":
                    file.getParameterLegth("Parameterlength.txt")
                case "4":
                    file.getParameterType("ParameterdataType.txt")
                case "5":                    
                    file.getjsonfile("result.txt")                    
                case _:
                    print(headerlog + "ADIOS")
                    break
        except IOError:
            print(headerError + " " +  "Unable to open or read the data in the file.")
        except:
            print(headerError + "Error")
            break;
        else:
            print(headerlog + " " + "The file was written successfully.")


main()