import requests
import xmltodict
from xml.dom.minidom import parseString
import json

class TestXMLParsing:

    #Basic XML element validation
    def test_xml_response_1(self):
        """
        validates:
        - HTTP STATUS CODE
        - CONTENT-TYPE
        - SPECIFIC XML ELEMENT VALUES
        """
        url = "https://mocktarget.apigee.net/xml"
        res = requests.get(url)
        assert res.status_code == 200, "Wrong status code"
        assert res.headers["Content-Type"] == "application/xml; charset=utf-8", "Wrong header content"
        #pretty print of xml
        print(parseString(res.text).toprettyxml())
        #conversion of xml to json
        json_data = xmltodict.parse(res.text)
        #pretty print of json
        print(json.dumps(json_data, indent=4))

        root = json_data["root"]
        assert root["city"] == "San Jose", "Wrong city"

    #Basic XML attribute Validations
    def test_xml_response_2(self):
        """
        validates:
        - HTTP STATUS CODE
        - CONTENT-TYPE
        - XML Attribute using @ notation
        """

        url = "https://httpbin.org/xml"
        res = requests.get(url)
        assert res.status_code == 200, "Wrong status code"

        assert res.headers["Content-Type"] == "application/xml", "Wrong header content"

        print(parseString(res.text).toprettyxml())
        # conversion of xml to json
        json_data = xmltodict.parse(res.text)
        # pretty print of json
        print(json.dumps(json_data, indent=4))

        #Extract and validate attributes
        slideshow = json_data["slideshow"]
        assert slideshow["@title"] == "Sample Slide Show", "Wrong slideshow title"
        assert slideshow["@date"] == "Date of publication", "Wrong slideshow date"
        assert slideshow["@author"] == "Yours Truly", "Wrong author"


    #Parse and avalidate slide content
    def test_xml_response_3(self):
        """
            validates:
             - Number of slides
             - slides title
             - Number and content of items
             - Dynamic presence check
        """

        url = "https://httpbin.org/xml"
        res = requests.get(url)
        assert res.status_code == 200, "Wrong status code"

        assert res.headers["Content-Type"] == "application/xml", "Wrong header content"

        print(parseString(res.text).toprettyxml())
        # conversion of xml to json
        json_data = xmltodict.parse(res.text)
        # pretty print of json
        print(json.dumps(json_data, indent=4))

        slides = json_data["slideshow"]["slide"]

        #Validations
        assert len(slides) == 2, "Wrong number of slides"
        title = [slide['title'] for slide in slides]
        print("titles", title)
        assert len(title) == 2, "Wrong slides title"
        assert title[0] == "Wake up to WonderWidgets!"
        assert title[1] == "Overview"

        items = []
        for slide in slides:
            item = slide.get('item', [])
            if isinstance(items, str):
                items.append(item)
            else:
                items.extend(item)

        print("items", items)
        assert len(items) ==3, "Wrong number of items"

