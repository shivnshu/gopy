class SymbolTableEntry:
    def __init__(self, name, type):
        self.name = name
        self.type = type
    def prettyPrint(self):
        print("Name:", self.name, "Type:", self.type)

class SymbolTableLiteralEntry(SymbolTableEntry):
    def __init__(self, name, value):
        SymbolTableEntry.__init__(self, name, "LiteralType")
        self.value = value
    def prettyPrint(self):
        SymbolTableEntry.prettyPrint(self)
        print("Value:", self.value)

class SymbolTableVariableEntry(SymbolTableEntry):
    def __init__(self, name):
        SymbolTableEntry.__init__(self, name, "VarType")
        self.varType = "Unknown"
        self.width = "Unknown"
    def prettyPrint(self):
        SymbolTableEntry.prettyPrint(self)
        print("varType:", self.varType, "width:", self.width)
        print()

class SymbolTablePackageEntry(SymbolTableEntry):
    def __init__(self, name):
        SymbolTableEntry.__init__(self, name, "PackageType")
    def prettyPrint(self):
        SymbolTableEntry.prettyPrint(self)
        print()

class SymbolTableInterfaceEntry(SymbolTableEntry):
    def __init__(self, name):
        SymbolTableEntry.__init__(self, name, "InterfaceType")
    def prettyPrint(self):
        SymbolTableEntry.prettyPrint(self)
        print()

class SymbolTableStructEntry(SymbolTableEntry):
    def __init__(self, name):
        SymbolTableEntry.__init__(self, name, "StructType")
    def prettyPrint(self):
        SymbolTableEntry.prettyPrint(self)
        print()

class SymbolTableFunctionEntry(SymbolTableEntry):
    def __init__(self, name):
        SymbolTableEntry.__init__(self, name, "FuncType")
    def prettyPrint(self):
        SymbolTableEntry.prettyPrint(self)
        print()

class SymbolTable(object):
    def __init__(self, parent, name):
        self.name = name
        self.parent = parent
        self.symbols = {}

    def put(self, symbol):
        if symbol.name in self.symbols:
            return False
        self.symbols[symbol.name] = symbol
        return True

    def get(self, name):
        if symbol.name in self.symbols:
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
