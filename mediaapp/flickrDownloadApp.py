from downloaderApp import downloaderApp
from dataType import aplicationType
import requests
from requests_oauthlib import OAuth1
#from requests_oauthlib import oauth1_auth
import json
from cityName import getCityCordinates
from lxml import etree
import re
import flickrapi

class flickrDownloadApp(downloaderApp):
    __requestID = None
    __payload = None
    __city = None
    __xml = """<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
xmlns:fo="http://www.w3.org/1999/XSL/Format" >
    <xsl:output method="text" omit-xml-declaration="yes" indent="no"/>
    <xsl:template match="//photos[@page='1']">
		<xsl:for-each select="//photo">
        <xsl:value-of select="concat('https://farm'
                    ,@farm
                    ,'.staticflickr.com/'
                    ,@server
                    ,'/'
                    ,@id
                    ,'_'
                    ,@secret
                    ,'_t.jpg'
                    ,'&#xA;')"/>
		</xsl:for-each>
    </xsl:template>
</xsl:stylesheet>"""

    def __init__(self, requestID, city):
        self.__requestID = requestID
        self.__city = city
        return

    def get_requestID(self):
        return self.__requestID
    
    def set_payload(self, data):
        self.__payload = data
        
    def get_payload(self):
        return self.__payload

    def get_city(self):
        return self.__city

    def get_ID(self):
        return aplicationType.flickr
 
    def get_clean_payload(self):
	xslt_root = etree.fromstring(self.__xml)
	transform = etree.XSLT(xslt_root)
	links = str(transform(self.__payload))
	linkstable = links.split('\n')

	#usuwa puste linie z tabeli
	linkstable = [item for item in linkstable if  re.search('(http*)',item)]
	dict = {'FlickrApp' : {'status': '1', 'requestID': self.__requestID, 'fields': linkstable} };	
	return json.dumps(dict)

    def do(self):
	api_key = '41949c4634dba6daa92644a4a6aad65e'
	api_secret = '6e80f255ff2f383b'

        cordinates = getCityCordinates(self.__city)
	flickr = flickrapi.FlickrAPI(api_key,secret=api_secret)
	self.__payload = flickr.photos_search(lat=cordinates['lat'], lon=cordinates['lng'], per_page='30')
	return
	