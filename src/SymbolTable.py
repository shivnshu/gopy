class SymbolTableEntry:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.parent = None
    def setTable(self, table):
        self.table = table
    def prettyPrint(self):
        print("Name:" + self.name + " ," + "Type:" + self.type + " ," + "TableName:" + self.table.getName(), end=', ')

class SymbolTableVariableEntry(SymbolTableEntry):
    def __init__(self, name):
        SymbolTableEntry.__init__(self, name, "VarType")
        self.variableType = "Unknown"
        self.dimension = 0
        self.dim_ranges = []
        self.width = "Unknown"
        self.value = "Unknown"
        self.memoryLocation = 0
    def setValue(self, value):
        self.value = value
    def getValue(self):
        return self.value
    def setType(self, type):
        self.variableType = type
    def getType(self):
        return self.variableType
    def getDim(self):
        return self.dimension
    def setDim(self, dimension):
        self.dimension = dimension
    def getDimRanges(self):
        return self.dim_ranges
    def setDimRanges(self, dim_ranges):
        self.dim_ranges = dim_ranges
    def setMemoryLocation(self, size):
        self.memoryLocation = self.table.getCurrOffset()
        self.size = size
        self.table.decCurrOffset(size)
    def prettyPrint(self):
        SymbolTableEntry.prettyPrint(self)
        print("VariableType:" + self.variableType + ", ", "Dimensions:", self.dimension, ", " +"DimRanges:", self.dim_ranges, ", ")

class SymbolTablePackageEntry(SymbolTableEntry):
    def __init__(self, name):
        SymbolTableEntry.__init__(self, name, "PackageType")
    def prettyPrint(self):
        SymbolTableEntry.prettyPrint(self)
        print(",")

class SymbolTableInterfaceEntry(SymbolTableEntry):
    def __init__(self, name):
        SymbolTableEntry.__init__(self, name, "InterfaceType")
    def prettyPrint(self):
        SymbolTableEntry.prettyPrint(self)
        print(",")

class SymbolTableStructEntry(SymbolTableEntry):
    def __init__(self, name):
        SymbolTableEntry.__init__(self, name, "StructType")
    def prettyPrint(self):
        SymbolTableEntry.prettyPrint(self)
        print(",")

class SymbolTableFunctionEntry(SymbolTableEntry):
    def __init__(self, name):
        SymbolTableEntry.__init__(self, name, "FuncType")
        self.input_args = []
        self.return_type = ""
        self.memoryLocation = ""
    def setInputArgs(self, l):
        self.input_args = l
    def getInputArgs(self):
        return self.input_args
    def prettyPrint(self):
        SymbolTableEntry.prettyPrint(self)
        print(",", self.input_args)

class SymbolTableImportEntry(SymbolTableEntry):
    def __init__(self, name):
        SymbolTableEntry.__init__(self, name, "ImportType")
    def prettyPrint(self):
        SymbolTableEntry.prettyPrint(self)
        print(",")



class SymbolTable(object):
    def __init__(self, parent, name):
        self.name = name
        self.parent = parent
        self.symbols = {}
        if (parent != None):
            self.offset = parent.getOffset() + parent.getCurrOffset()
        else:
            self.offset = 0
        self.currOffset = 0

    def put(self, symbol):
        if symbol.name in self.symbols:
            return False
        symbol.setTable(self)
        self.symbols[symbol.name] = symbol
        return True

    def get(self, name):
        if name in self.symbols:
            return self.symbols[name]
        else:
            return None

    def getParent(self):
        return self.parent

    def getName(self):
        return self.name

    def getOffset(self):
        return self.offset

    def getCurrOffset(self):
        return self.currOffset

    def decCurrOffset(self, size):
        self.currOffset -= size

    def prettyPrint(self):
        print("\nName:", self.name)
        if (self.parent != None):
            print("Parent:", self.parent.getName())
        else:
            print("Parent:", None)
        print("Offset:", self.offset)
        for sym in self.symbols:
            self.symbols[sym].prettyPrint()
            #print(sym + ":", self.symbols[sym].type)
        print()

    # def toCSV(self):
    #     print("Name:", self.name, "\nParent:", self.parent, "\nSymbols:", self.symbols)
    #     print()
    #     print("Name, Type, variableType, Input Args")
    #     for sym in self.symbols:
    #         entry = self.symbols[sym]
    #         entry.prettyPrint()
