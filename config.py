import json
from typing import List


class Config(object):


	def __init__(self, arg):

		with open("config.jsons",'r',encoding = 'utf-8') as f:
			self.configJsonUrls = json.loads(f.read())["urls"]
	
	def __getProxy():
		pass

	def getProxy():
		pass
		
	def getUrls(self) -> List:
		return self.configJsonUrls

				
