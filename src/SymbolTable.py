class SymbolTableEntry:
    def __init__(self, name, type):
        self.name = name
        self.type = type

class SymbolTableLiteralEntry(SymbolTableEntry):
    def __init__(self, name, value):
        SymbolTableEntry.__init__(self, name, "LiteralType")
        self.value = value

class SymbolTableVariableEntry(SymbolTableEntry):
    def __init__(self, name, type):
        SymbolTableEntry.__init__(self, name, "VariableType")

class SymbolTableFunctionEntry(SymbolTableEntry):
    def __init__(self, name, type):
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
        if self.parent != None:
            return self.parent.get(name)
        else:
            return None

    def getParent(self):
        return self.parent
