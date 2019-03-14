class SymbolTableEntry:
    def __init__(self, name, type):
        self.name = name
        self.type = type

class SymbolTableLiteralEntry(SymbolTableEntry):
    def __init__(self, name, value):
        SymbolTableEntry.__init__(self, name, "LiteralType")
        self.value = value

class SymbolTableVariableEntry(SymbolTableEntry):
    def __init__(self, name):
        SymbolTableEntry.__init__(self, name, "VariableType")

class SymbolTablePackageEntry(SymbolTableEntry):
    def __init__(self, name):
        SymbolTableEntry.__init__(self, name, "PackageType")

class SymbolTableInterfaceEntry(SymbolTableEntry):
    def __init__(self, name):
        SymbolTableEntry.__init__(self, name, "InterfaceType")

class SymbolTableStructEntry(SymbolTableEntry):
    def __init__(self, name):
        SymbolTableEntry.__init__(self, name, "StructType")

class SymbolTableFunctionEntry(SymbolTableEntry):
    def __init__(self, name):
        SymbolTableEntry.__init__(self, name, "FuncType")

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
        print("Name:", self.name)
        print("Parent:", self.parent)
        for sym in self.symbols:
            print(sym + ":", self.symbols[sym].type)
        print("\n")
