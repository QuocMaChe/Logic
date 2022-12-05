def standardize(variable):
    # Bo cac ki tu 'OR', A OR B => 'A', 'B'
    if variable.upper() != 'OR':
        return True
    return False
#
def check(List1, List2, Remove):
    # Neu mang Remove rong
    if (Remove == []):
        return None
    # Gop 2 list voi nhau
    Result = List1+List2
    # Xoa cac item bi trung lap, ben trong Remove[]
    Result = [item for item in Result if item not in Remove]
    # Neu Result rong thi tra ve ["{}"]
    if (Result == []):
        return ["{}"]
    # Sap xep theo alphabet, loai bo cac item trung lap
    Result = sorted(list(set(Result)), key=lambda x: x[-1])
    return Result