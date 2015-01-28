import rhinoscriptsyntax as rs
import System.Drawing as SD
 
def PictureframeOnScale():
    filter = "PNG (*.png)|*.png|JPG (*.jpg)|*.jpg|BMP (*.bmp)|*.bmp|All (*.*)|*.*||"
    #filter = "PNG (*.png)|*.png"
    filename = rs.OpenFileName("Select existing image file", filter)
    if not filename: return
    # use the System.Drawing.Bitmap class described at
    # [url]http://msdn.microsoft.com/en-us/library/system.drawing.bitmap.aspx[/url]
    img = SD.Bitmap(filename)
    img.Dispose
    # define scale from inch to file unitsystem
    dblScale = rs.UnitScale(rs.UnitSystem(),8)
    
    #calculate width based on image pixel dimension and image HorizontalResolution
    w=str((img.Width/img.HorizontalResolution)*dblScale)
    
    #release the image (not sure if this is correct but seems to work)
    
    
    # scripted rhino command pictureframe with width and height as calculated above
    rs.Command("!_-PictureFrame \""+filename+"\" _Pause "+w+" ")
 
 
if __name__=="__main__":
    PictureframeOnScale() 