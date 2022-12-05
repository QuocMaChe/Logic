from helper import check
#
def merge(List1, List2):
    Remove=[]
    # Them vao mang Remove
    for i_item in List1:
        for j_item in List2:
            if i_item[-1] == j_item[-1] and i_item[0] != j_item[0]:
                if Remove == []:
                    Remove.append(i_item)
                    Remove.append(j_item)
                else:
                    return None
    return check(List1,List2,Remove)
#
def plResolution(List, filePath):
    Remove=[]
    with open(filePath, 'w') as f:
        temp = []
        check = False
        while check == False:
            # Merge 2 List
            for i in range(len(List)-1):
                for j in range(i+1, len(List)):
                    tempList = merge(List[i], List[j])
                    if (tempList != None) and tempList not in temp:
                        temp.append(tempList)
                        
            temp = [item for item in temp if item not in List]
            # In ra so luong phan tu ben trong
            print(len(temp), file=f)
            if (temp == []):
                break
            for i in temp:
                if i == ["{}"]:
                    check = True
                print(' OR '.join(i),  file=f)
            #Cho vao list
            List += temp
        #Ket thuc vong lap in ra ket luan 
        if check==True:
            print("YES",  file=f)
        else:
            print("NO",  file=f)       