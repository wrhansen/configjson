==========
configjson
==========

Description
-----------

	configjson is a json decoder that can read json files that were created as
	config files into a string or python object. This means that it can accept 
	json files that contain comment lines and also has more relaxed formatting
	constraints (ignores extra commas in data structures and in-line comments).

The config file
---------------
	
	The config file can be any json object represented in a text file but may
	also include comment lines (lines that start with `#`) as well as any in-line
	comments (in-line comment starts at `#`). Here's an example:
	
		::
			
			{
				# This is a commented line in a config file read by configjson
				'some-key': "Some String",
				'another-key': "Yet another string", # This is an in-line comment
			}

How to use configjson
---------------------

	There are two ways to read in the file: as a string, or as a python object.
	
	Let's say the above example was created in a file *example.json*. To read this
	config file to a string:
	
		::
			
			
			import configjson
			print configjson.to_string(open('example.json', 'rb'))

			{
				"some-key": "Some String",
				"another-key": "Yet another string"
			}
	
	
	To read this config file to a python object:
	
		::
		
		
			import configjson
			print configjson.load(open('example.json', 'rb'))
			
			{
				"some-key": "Some String",
				"another-key": "Yet another string"
			}

NOTE: Parsing the file for inline comments is not implemented yet, but will be
soon enough			
