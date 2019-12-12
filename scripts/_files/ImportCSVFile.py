#Script by Sylvain Kieffer 27/08/2019
# translated french to english - rg 2019-12-12
import Rhino
import rhinoscriptsyntax as rs
from operator import itemgetter

def ImportCSVFile():
    filter = "*.csv|*.csv|All Files (*.*)|*.*||"
    filename = rs.OpenFileName("Select the file to import.",filter)
    if not filename: return
    plane=Rhino.Geometry.Plane.WorldXY
    ListTailles = []
    rs.EnableRedraw(True)
    tableau = rs.GetPoint("Choose location of the table.")
    #width calc
    with open(filename, 'r') as listA:
        rs.EnableRedraw(False)
        ListLargeur = []
        ListLen = []
        a=0
        for row  in listA:
            row = row.split(";")
            rowA = []
            for str in row:
                str = str.replace("\n","")
                rowA.append(str)
            rowB = []
            for aa in rowA:
                rowB=aa.split(',')
            if len(rowB)<= len(rowA):rowB=rowA
            list=[]
            A=len(rowB)
            ListLen.append(A)
            for txt in rowB:
                if txt :
                   test = rs.AddText(txt, plane, height=1.5, font='Arial', font_style=0, justification=None)
                   bb = rs.BoundingBox(test, plane, in_world_coords=True)
                   if bb :
                       largeur =round(( bb[1].DistanceTo(bb[0])),1)
                       if largeur < 0: largeur=largeur*(-1)
                       list.append(largeur)
                       rs.DeleteObject(test)
                   else :
                       largeur=0.0
                       list.append(largeur)
                else :
                       largeur=0.0
                       list.append(largeur)
            ListLargeur.append(list)
        N = max(ListLen)
        d_max = {i: max(map(itemgetter(i), ListLargeur)) for i in range(N)}
        #column width
        ListMax = d_max.values()
        #placement of layers
        rs.AddLayer("Nomenclature")
        rs.AddLayer("Frame",parent="Nomenclature")
        rs.AddLayer("Value",parent="Nomenclature")
    #placement of table
    with open(filename, 'r') as listB:
        ListLargeur = []
        Group=rs.AddGroup()
        ListGroup = []
        H=1.5
        font='Arial'
        count=1
        for row  in listB:
            V=0
            Y=0
            row = row.split(";")
            rowA = []
            for str in row:
                str = str.replace("\n","")
                rowA.append(str)
            rowB = []
            for aa in rowA:
                rowB=aa.split(',')
            if len(rowB)<= len(rowA):rowB=rowA
            for valeur in rowB:
                #displacement value
                placeA= ((-3.0) - (float(count)*3))
                placeB= ((-1.50) - (float(count)*3))
                #rectangle
                LX = (ListMax[Y])+2
                recA=rs.AddRectangle(plane,LX,3)
                VV=V+(LX/2)
                recA=rs.MoveObject(recA,[V,placeA,0.0])
                rs.ObjectLayer(recA,"Frame")
                ListGroup.append(recA)
                #text
                txt=valeur
                if txt :
                    txtA=rs.AddText (txt,plane,H,font,0,2 + 131072)
                    txtA=rs.MoveObject(txtA,[VV,placeB,0.0])
                    rs.ObjectLayer(txtA,"Value")
                    ListGroup.append(txtA)
                #new displacement value
                Y=Y+1
                V=V+LX
            #new line
            count=count+1
        ListGroup=rs.MoveObjects(ListGroup,tableau)
        rs.EnableRedraw(True)
    rs.AddObjectsToGroup(ListGroup,Group)

if( __name__ == "__main__" ):
    ImportCSVFile()
