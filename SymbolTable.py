from enum import Enum
DataType = Enum('DataType',['INT','DOUBLE'])

class SymbolTableEntry:
	def __init__(self,name,datatype):
		self.name=name
		self.datatype=datatype
	def getSymbolName(self):
		return self.name
	def getDataType(self):
		return self.datatype
	def print(self):
		pass


class SymbolTable:
	def __init__(self):
		self.table = []
	def addSymbol(self,symbol):
		self.table.append(symbol)
	def nameInSymbolTable(self,name):
		for ste in self.table:
			if ste.getSymbolName()==name:
				return ste
		return None
	def printSymbolTable(self):
		pass
