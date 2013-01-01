# encoding: utf-8
'''
configjson allows you to read configuration files in JSON that contain
comment lines, denoted by '#'. This module contains convenience methods that
return a python object of the JSON or a string.
'''
__author__ = "Wesley Hansen"
__date__ = "12/13/2012 11:17:02 AM"
__version__ = "0.1"
__status__ = "Prototype"


import json
import pprint

def load(fp):
	'''
	Load a commented json from file handler `fp` and return a python object.
	
	*fp* (``file``) is an object with an __iter__ method that returns strings. 
	
	Returns (``object``) a python built-in object (dict, list, string) that
		correctly represents the object defined in the cjson file.
	'''
	cjson_obj = ConfigJson()
	cjson_obj.parse(fp)
	return cjson_obj.to_object()

def to_string(fp):
	'''
	Load a commented json from file handler `fp` and return a string.
	
	*fp* (``file``) is an object with an __iter__ method that returns strings. 
	
	Returns (``str``) of the cjson file with all of the comment lines not
		returned in the string.
	'''
	cjson_obj = ConfigJson()
	cjson_obj.parse(fp)
	return str(cjson_obj)
	
class ConfigJson:
	'''
	Read a cjson (Commented JSON) file and provide methods for extracting the
	json in various formats.
	'''

	comment_delimiter = "#"

	def __init__(self):
		self.string = None

	def parse(self, fp):
		'''
		Parse the cjson file.
		
		*fp* (``file``) is an object with an __iter__ method that returns strings. 		
		'''
		parse_string = ""
		for line in fp:
			if line.strip().startswith(self.comment_delimiter):
				continue
			else:
				parse_string += line

		self.string = parse_string

	def __str__(self):
		'''
		Get the string representation of the commented json (without the comments)
		
		Returns (``str``) representation of the json string, comments excluded.
		'''
		assert self.string
		return self.string

	def to_object(self):
		'''
		Get the python built-in object representation of the commented json file.
		
		Returns (``builtin``) represenation of the commented json file.
		'''
		assert self.string
		return json.loads(self.string)


if __name__ == '__main__':
	print("** Testing cjson.load(): **")
	print(pprint.pformat(load(open("credentials.json", 'rb'))))
	print("** Testing cjson.loads(): **")
	print(to_string(open("credentials.json", 'rb')))
		
