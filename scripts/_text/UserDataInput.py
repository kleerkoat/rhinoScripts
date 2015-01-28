import rhinoscriptsyntax as rs

def UserDataInput():
    obj = rs.GetObject("Select Object")

    Keylist = rs.GetUserText(obj,)

    UserDataList = []
    for n in Keylist:
        b = rs.GetUserText(obj,n)
        UserDataList.append(b)

    newlist=[]
    newlist = rs.PropertyListBox(Keylist,UserDataList,"User Data", "User Data Key List")

    if newlist:
        for c in range(len(Keylist)):
            rs.SetUserText(obj,Keylist[c],newlist[c])


UserDataInput()
