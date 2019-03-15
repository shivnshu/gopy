class SymbolTableEntry:
    def __init__(self, name, type):
        self.name = name
        self.type = type
    def prettyPrint(self):
        print(self.name, ", ", self.type, end=', ')

class SymbolTableVariableEntry(SymbolTableEntry):
    def __init__(self, name):
        SymbolTableEntry.__init__(self, name, "VarType")
        self.variableType = "Unknown"
        self.width = "Unknown"
        self.value = "Unknown"
    def setValue(self, value):
        self.value = value
    def getValue(self):
        return self.value
    def setType(self, type):
        self.variableType = type
    def getType(self):
        return self.variableType
    def prettyPrint(self):
        SymbolTableEntry.prettyPrint(self)
        print(self.variableType, ",")

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
        self.offset = 0
        self.currOffset = 0

    def put(self, symbol):
        if symbol.name in self.symbols:
            return False
        self.symbols[symbol.name] = symbol
        return True

    def get(self, name):
        if name in self.symbols:
            return self.symbols[name]
        else:
            return None

    def getParent(self):
        return self.parent

    def prettyPrint(self):
        print("\nName:", self.name)
        print("Parent:", self.parent)
        for sym in self.symbols:
            self.symbols[sym].prettyPrint()
            #print(sym + ":", self.symbols[sym].type)
        print()

    def toCSV(self):
        print("Name:", self.name, "\nParent:", self.parent, "\nSymbols:", self.symbols)
        print()
        print("Name, Type, variableType, Input Args")
        for sym in self.symbols:
            entry = self.symbols[sym]
            entry.prettyPrint()
