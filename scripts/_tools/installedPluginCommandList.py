################################################
import Rhino
plugins = Rhino.PlugIns.PlugIn.GetInstalledPlugIns()

for item in plugins:
   id = item.Key
   name = item.Value
   print name
   commands = Rhino.PlugIns.PlugIn.GetEnglishCommandNames(id)
   for command in commands:
       print "  - ", command
################################################ 