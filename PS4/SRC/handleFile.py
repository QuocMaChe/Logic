from helper import standardize
#
def readFile(inputPath):
    # Mo file input
    file = open(inputPath, 'r')
    # Tra ve tat ca dong cho allLine
    allLine = file.readlines()
    
    del allLine[1]
    List = []
    # Tach chuoi, bo cac ki tu OR
    for line in allLine:
        List.append(list(filter(standardize, line.strip().split())))
        
    # Doi dau chuoi dau tien. Vi du A or -B se thanh 2 menh de la -A va B
    for i in List[0]:
        if i[0] == '-':
            List.append([i[1]])
        else:
            tempNeg = '-' + i
            List.append([tempNeg])
    
    del List[0]
    return List