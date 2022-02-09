import pandas as pd
import xml.etree.ElementTree as et
import json

class ProjectDetails:
    
    def __init__(self,tags):
        self.tags = tags
        
    def Project(self):
        cols = []
        global temp1_dict
        temp1_dict ={}
        check = 1
        for elem in root.iter(self.tags):
            temp1_dict = elem.attrib
            if check == 1:
                for x in temp1_dict.keys():
                    cols.append(x)
                check = check + 1
            c = len(cols) 
            for x in range(c):
                temp1_dict[cols[x]] = elem.attrib[cols[x]]

class Parts:
    
    def __init__(self,tags):
        self.x = tags
    
    
    def Part(self):
        cols = []
        temp_dict={}
        dict = {}
        global dict1
        dict1 ={}
        check = 1
        count = 1
        global new_dict
        new_dict ={}
        for elem in root.iter(self.x):   
            
            temp_dict = elem.attrib
            if check == 1:
                for x in temp_dict.keys():
                    cols.append(x)
                check = check + 1
            c = len(cols) 
            for x in range(c):
                dict[cols[x]] = elem.attrib[cols[x]]
      
            root1 = et.Element
            root1 = elem
            
            dict1_user ={}
            dict_user ={}
            list_user=[]
            
            dict_gain ={}
            dict_refSide ={}
            for userAttributes in root1.iter('{http://www.design2machine.com}UserAttributes'):
                root2 = et.Element
                root2 = userAttributes
                temp_userAttribute = []
                cols_User =[]
                check_User = 1

                for userAttribute in root2.iter('{http://www.design2machine.com}UserAttribute'):
                    temp_userAttribute = userAttribute.attrib
                    if check_User == 1:
                        for x in temp_userAttribute.keys():
                            cols_User.append(x)
                        check_User = check_User + 1
                    c = len(cols_User) 
                    for x in range(c):
                        dict_user[cols_User[x]] = userAttribute.attrib[cols_User[x]]
                    dict1_user['userAttribute'] = dict_user
                    to_stringDict = str(dict1_user)
                    list_user.append(to_stringDict)
            dict ['UserAttribute'] = list_user
             
             
            temp_gainDir = []
            cols_gain =[]
            check_gain = 1
            for gainDir in root1.iter('{http://www.design2machine.com}GrainDirection'):
                    temp_gainDir = gainDir.attrib
                    if check_gain == 1:
                        for x in temp_gainDir.keys():
                            cols_gain.append(x)
                        check_gain = check_gain + 1
                    c = len(cols_gain) 
                    for x in range(c):
                        dict_gain[cols_gain[x]] = gainDir.attrib[cols_gain[x]]
            copy_dict_gain = dict_gain.copy()
            dict['Gain Direction'] = copy_dict_gain
            
            temp_ref = []
            cols_ref =[]
            check_ref = 1
            
            for Referenceside in root1.iter('{http://www.design2machine.com}ReferenceSide'):
                    temp_ref =Referenceside.attrib
                    if check_ref == 1:
                        for x in temp_ref.keys():
                            cols_ref.append(x)
                        check_ref = check_ref+ 1
                    c = len(cols_ref) 
                    for x in range(c):
                        dict_refSide[cols_ref[x]] = Referenceside.attrib[cols_ref[x]]
            copy_refSide = dict_refSide.copy()
            dict['Reference Sides'] = copy_refSide               
                
                
            new_dict = dict.copy()
            dict1['Part'+ str(count)] = new_dict
            count = count + 1
       
class Transformations:  
    
    def __init__(self,tags):
        self.tags = tags
        
    def transformation(self):
        cols =[]
        check =1
        dict ={}
        count =1
        
        temp_GUIDdict ={}
        for elem in root.iter(self.tags):  
           
            root1 = et.Element
            root1 = elem
            temp_GUID =[]
            temp_ref =[]
            temp_xvector =[]
            temp_yvector = []
            for innerElem in root1.iter('{http://www.design2machine.com}Transformation'):
                temp_dict = innerElem.attrib
                if check == 1:
                    for x in temp_dict.keys():
                        cols.append(x)
                    check = check + 1
                c = len(cols) 
                for x in range(c):
                    dict[cols[x]] = innerElem.attrib[cols[x]]

                root2 = et.Element
                root2 = innerElem
                
                temp_position_dict ={}
                for innerInner in root2.iter('{http://www.design2machine.com}Position'):
                    root3 = et.Element
                    root3 = innerInner
                    
                    check_ref =1
                    cols_ref=[]
                    dict_ref={}
                    
                    check_xvector =1
                    cols_xvector=[]
                    dict_xvector={}
                    
                    check_yvector =1
                    cols_yvector=[]
                    dict_yvector={}     
                                   
                    for position in root3.iter('{http://www.design2machine.com}ReferencePoint'):
                        temp_dict_ref = position.attrib
                        if check_ref == 1:
                            for x in temp_dict_ref.keys():
                                cols_ref.append(x)
                            check_ref = check_ref + 1
                        c = len(cols_ref) 
                        for x in range(c):
                            dict_ref[cols_ref[x]] = position.attrib[cols_ref[x]]
          
                    for position in root3.iter('{http://www.design2machine.com}XVector'):
                        temp_dict_xvector = position.attrib
                        if check_xvector == 1:
                            for x in temp_dict_xvector.keys():
                                cols_xvector.append(x)
                            check_xvector = check_xvector + 1
                        c = len(cols_xvector) 
                        for x in range(c):
                            dict_xvector[cols_xvector[x]] = position.attrib[cols_xvector[x]]
                     
                    for position in root3.iter('{http://www.design2machine.com}YVector'):
                        temp_dict_yvector = position.attrib
                        if check_yvector == 1:
                            for x in temp_dict_yvector.keys():
                                cols_yvector.append(x)
                            check_yvector = check_yvector + 1
                        c = len(cols_yvector) 
                        for x in range(c):
                            dict_yvector[cols_yvector[x]] = position.attrib[cols_yvector[x]]                        
                        
                copy_ref = dict_ref.copy()
                temp_ref.append(copy_ref)
                temp_position_dict['Reference Points'] = copy_ref
                
                copy_xvector = dict_xvector.copy()
                temp_xvector.append(copy_xvector)
                temp_position_dict['XVector'] = copy_xvector
                
                copy_yvector = dict_yvector.copy()
                temp_yvector.append(copy_yvector)
                temp_position_dict['YVector'] = copy_yvector
                        
                dict['Position']=temp_position_dict  
                copy_temp_GUID = dict.copy()
                temp_GUID.append(copy_temp_GUID) 
                
            temp_GUIDdict['Transformation']=temp_GUID
            temp1 = dict1['Part'+ str(count)]
            copy_temp_GUIDdict = temp_GUIDdict.copy()
            temp1['Transformations'] = copy_temp_GUIDdict
            count = count + 1    

class Processings:
    
    def __init__(self,tags):
        self.tags = tags
            
    def Processing(self):
        count =1
        for elem in root.iter(self.tags):
            root1 = et.Element
            root1 = elem
            
            for processing in root1.iter('{http://www.design2machine.com}Processings'):
                root2 = et.Element
                root2 = processing
                
                check_freecontour =1
                cols_freecontour =[]
                dict_freecontour ={}
                temp_freecontour_list=[]
                temp_freecontour_dict ={}
                
                for freecontour in root2.iter('{http://www.design2machine.com}FreeContour'):
                    temp_freecontour = freecontour.attrib
                    if check_freecontour == 1:
                        for x in temp_freecontour.keys():
                            cols_freecontour.append(x)
                        check_freecontour = check_freecontour + 1
                    c = len(cols_freecontour) 
                    for x in range(c):
                        dict_freecontour[cols_freecontour[x]] = freecontour.attrib[cols_freecontour[x]]
                    
                    root3 = et.Element
                    root3 = freecontour
    
                    for contour in root3.iter('{http://www.design2machine.com}Contour'):
                        root4 = et.Element
                        root4 = contour  
                        
                        check_startpoint =1
                        cols_startpoint =[]
                        dict_startpoint ={}
                        temp_startpoint_list=[]
                        temp_startpoint_dict ={}  
                        
                        check_inclination =1
                        cols_inclination =[]
                        dict_inclination ={}
                        temp_inclination_list=[]
                        temp_inclination_dict ={}
                        
                        check_endpoint =1
                        cols_endpoint =[]
                        dict_endpoint ={}
                        temp_line=[]
                        temp_endpoint_dict ={}
                         
                        temp=[]
                        for startPoint in root4.iter('{http://www.design2machine.com}StartPoint'):
                            temp_startpoint = startPoint.attrib
                            if check_startpoint == 1:
                                for x in temp_startpoint.keys():
                                    cols_startpoint.append(x)
                                check_startpoint = check_startpoint + 1
                            c = len(cols_startpoint) 
                            for x in range(c):
                                dict_startpoint[cols_startpoint[x]] = startPoint.attrib[cols_startpoint[x]]
                            copy_startpoint = dict_startpoint.copy()
                            temp_startpoint_list.append(copy_startpoint) 
                        temp_startpoint_dict['Start Points'] = temp_startpoint_list
                    
                            
                        for Line in root4.iter('{http://www.design2machine.com}Line'):
                            temp_inclination = Line.attrib
                            if check_inclination == 1:
                                for x in temp_inclination.keys():
                                    cols_inclination.append(x)
                                check_inclination = check_inclination + 1
                            c = len(cols_inclination) 
                            for x in range(c):
                                dict_inclination[cols_inclination[x]] = Line.attrib[cols_inclination[x]]
                            copy_inclination = dict_inclination.copy()
                            temp_inclination_list.append(copy_inclination) 
                        
                            root5 = et.Element
                            root5 = Line
                            
                            for EndPoint in root5.iter('{http://www.design2machine.com}EndPoint'):
                                temp_endpoint = EndPoint.attrib
                                if check_endpoint == 1:
                                    for x in temp_endpoint.keys():
                                        cols_endpoint.append(x)
                                    check_endpoint = check_endpoint + 1
                                c = len(cols_endpoint) 
                                for x in range(c):
                                    dict_endpoint[cols_endpoint[x]] = EndPoint.attrib[cols_endpoint[x]]
                                copy_endpoint = dict_endpoint.copy()
                                temp_endpoint_dict['End Points'] = copy_endpoint
                                copy_temp_endpoint = temp_endpoint_dict.copy()
                            temp_inclination_list.append(copy_temp_endpoint) 
                        temp_inclination_dict['Line'] = temp_inclination_list
                    
                        temp.append(temp_startpoint_dict)
                        temp.append(temp_inclination_dict)
                        
                    copy_freecontour = dict_freecontour.copy()   
                    copy_freecontour['Contour']=temp
                    temp_freecontour_list.append(copy_freecontour)
      
                temp_freecontour_dict['Free Contour']=temp_freecontour_list 
                temp1 = dict1['Part'+ str(count)]
                copy_temp_dict = temp_freecontour_dict.copy()
                temp1['Processings'] = copy_temp_dict
                count = count + 1
            
        temp1_dict['Parts'] = dict1
        Dict_convert['Project'] = temp1_dict  
        out_file = open(path+fileName, "w")
        json.dump(Dict_convert, out_file, indent = 5)
        out_file.close()        

XmlFile = input(r'''Enter File Directory(Eg: C:\Users\Karan\Desktop\New folder\00002.BTLX) :  ''') #Example input as complete Directory of XmlFIle C:\Users\Karan\Desktop\New folder\00002.BTLX
tree = et.parse(XmlFile)
root = tree.getroot()
newFile = XmlFile.split('\\')
CsvFile = newFile[-1].split('.')
fileName = ('_').join(CsvFile)+'Sample_Dict.txt'
del newFile[-1]
path = '\\'.join(newFile) + '\\' #Path where converted files are saved

Dict_convert ={}

ProjectDetail = ProjectDetails(r'{http://www.design2machine.com}Project')  
Parts = Parts(r'{http://www.design2machine.com}Part')   
Transformations = Transformations(r'{http://www.design2machine.com}Transformations')  
Processign = Processings(r'{http://www.design2machine.com}Parts')  

ProjectDetail.Project()
Parts.Part()
Transformations.transformation()  
Processign.Processing()



