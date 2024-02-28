from xml.etree import ElementTree as elem
from Data import ObjectXML

class XMLParser():
    def __init__(self):
    
        self.ObjectMass = []
        
    def Parsing(self, pathXML):
        self.tree = elem.parse(pathXML)
        self.root = self.tree.getroot()
        
        self.ObjectMass=[]
        
        for child in self.root.iter("base_data"):
            for chaild in child:
                if(chaild.tag == "land_records"):
                    land_records = chaild
                    for land_record in land_records:
                        x=[]
                        y=[]
                        errorRate=[]
                        ord_nmb = []
                        source = []
                        cadNumber=""
                        view=""
                        square_value = ""
                        
                        for common_dataChild in land_record.iter("common_data"):
                            cadNumber=common_dataChild[1].text
                            view = common_dataChild[0][1].text
                        for squareChild in land_record.iter("area"):
                            
                            square = squareChild.iter("value")
                            for value in square:
                                square_value = float(value.text)
                                
                            error_value = ""
                            area_error = squareChild.iter("inaccuracy")   
                            for error in area_error:
                                error_value = float(error.text)
                                
                        for ordinate in land_record.iter("ordinate"):
                            if ordinate.find("x") is not None:
                                x.append(float(ordinate.find("x").text))
                                
                            if ordinate.find("y") is not None:
                                y.append(float(ordinate.find("y").text))
                                
                            if ordinate.find("ord_nmb") is not None:
                                ord_nmb.append(ordinate.find("ord_nmb").text)
                            else:
                                ord_nmb.append("")
                                
                            source.append("КПТ")
                            
                            if ordinate.find("delta_geopoint") is not None:
                                errorRate.append(float(ordinate.find("delta_geopoint").text))
                            else:
                                errorRate.append("")
                        if x:
                            x.pop()
                            y.pop()
                        if errorRate:
                            errorRate.pop()
                        self.ObjectMass.append(
                                ObjectXML(
                                    area_error=error_value,
                                    view=view,
                                    cadNumber=cadNumber,
                                    errorRate=errorRate,
                                    x=x,
                                    y=y,
                                    square=square_value,
                                    source=source,
                                    ord_nmb=ord_nmb
                                )
                            )

                if(chaild.tag == "build_records"):
                    build_records=chaild
                    for build_record in build_records:
                        x=[]
                        y=[]
                        errorRate=[]
                        for common_dataChild in build_record.iter("common_data"):
                            cadNumber=common_dataChild[1].text
                            view = common_dataChild[0][1].text
                        for squareChild in build_record.iter("area"):
                             
                            square = squareChild.iter("value")
                            for value in square:
                                square_value = float(value.text)

                            error_value = ""
                            area_error = squareChild.iter("inaccuracy")   
                            for error in area_error:
                                error_value = float(error.text)
                                
                        for ordinate in build_record.iter("ordinate"):
                            if ordinate.find("x") is not None:
                                x.append(float(ordinate.find("x").text))
                                
                            if ordinate.find("y") is not None:
                                y.append(float(ordinate.find("y").text))
                                
                            if ordinate.find("ord_nmb") is not None:
                                ord_nmb.append(ordinate.find("ord_nmb").text)
                            else:
                                ord_nmb.append("")
                                
                            source.append("КПТ")
                            
                            if ordinate.find("delta_geopoint") is not None:
                                errorRate.append(float(ordinate.find("delta_geopoint").text))
                            else:
                                errorRate.append("")
                        if x:    
                            x.pop()
                            y.pop()
                        if errorRate:
                            errorRate.pop()
                        self.ObjectMass.append(ObjectXML(area_error=error_value, view=view, cadNumber=cadNumber, errorRate=errorRate, x=x, y=y, square=square_value, source=source, ord_nmb=ord_nmb))

                if(chaild.tag == "construction_records"):
                    construction_records=chaild
                    for construction_record in construction_records:
                        x=[]
                        y=[]
                        errorRate=[]
                        for common_dataChild in construction_record.iter("common_data"):
                            cadNumber=common_dataChild[1].text
                            view = common_dataChild[0][1].text
                        for squareChild in construction_record.iter("area"):
                             
                            square = squareChild.iter("value")
                            for value in square:
                                square_value = float(value.text)

                            error_value = ""
                            area_error = squareChild.iter("inaccuracy")   
                            for error in area_error:
                                error_value = float(error.text)
                                
                        for ordinate in construction_record.iter("ordinate"):
                            if ordinate.find("x") is not None:
                                x.append(float(ordinate.find("x").text))
                                
                            if ordinate.find("y") is not None:
                                y.append(float(ordinate.find("y").text))
                                
                            if ordinate.find("ord_nmb") is not None:
                                ord_nmb.append(ordinate.find("ord_nmb").text)
                            else:
                                ord_nmb.append("")
                                
                            source.append("КПТ")
                            
                            if ordinate.find("delta_geopoint") is not None:
                                errorRate.append(float(ordinate.find("delta_geopoint").text))
                            else:
                                errorRate.append("")
                        if x:
                            x.pop()
                            y.pop()
                        if errorRate:
                            errorRate.pop()
                        self.ObjectMass.append(ObjectXML(area_error=error_value, view=view, cadNumber=cadNumber, errorRate=errorRate, x=x, y=y, square=square_value, source=source, ord_nmb=ord_nmb))

                if(chaild.tag == "object_under_construction_records"):
                    object_under_construction_records=chaild
                    for object_under_construction_record in object_under_construction_records:
                        x=[]
                        y=[]
                        errorRate=[]
                        for common_dataChild in object_under_construction_record.iter("common_data"):
                            cadNumber=common_dataChild[1].text
                            view = common_dataChild[0][1].text
                        for squareChild in object_under_construction_record.iter("area"):
                             
                            square = squareChild.iter("value")
                            for value in square:
                                square_value = float(value.text)

                            error_value = ""
                            area_error = squareChild.iter("inaccuracy")   
                            for error in area_error:
                                error_value = float(error.text)
                            
                        for ordinate in object_under_construction_record.iter("ordinate"):
                            if ordinate.find("x") is not None:
                                x.append(float(ordinate.find("x").text))
                                
                            if ordinate.find("y") is not None:
                                y.append(float(ordinate.find("y").text))
                                
                            if ordinate.find("ord_nmb") is not None:
                                ord_nmb.append(ordinate.find("ord_nmb").text)
                            else:
                                ord_nmb.append("")
                                
                            source.append("КПТ")
                            
                            if ordinate.find("delta_geopoint") is not None:
                                errorRate.append(float(ordinate.find("delta_geopoint").text))
                            else:
                                errorRate.append("")
                        if x:
                            x.pop()
                            y.pop()
                        if errorRate:
                            errorRate.pop()
                        self.ObjectMass.append(ObjectXML(area_error=error_value, view=view, cadNumber=cadNumber, errorRate=errorRate, x=x, y=y, square=square_value, source=source, ord_nmb=ord_nmb)) 
        return True
    
xml_parser = XMLParser()