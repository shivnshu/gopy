type_to_size = {}
type_to_size["int"] = 4
type_to_size["long"] = 8
type_to_size["char"] = 1
type_to_size["float"] = 4
type_to_size["double"] = 8

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
        self.ret_types = []
        self.memoryLocation = ""
    def setInputArgs(self, l):
        self.input_args = l
    def getInputArgs(self):
        return self.input_args
    def setReturnTypes(self, l):
        self.ret_types = l
    def getReturnTypes(self):
        return self.ret_types
    def prettyPrint(self):
        SymbolTableEntry.prettyPrint(self)
        print(",", self.input_args, ",", self.ret_types)

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


class ActivationRecord:
    def __init__(self, func_entry):
        self.ret_values = []
        self.input_args = []
        self.old_st_ptrs = {"%ebp": (0, 8)}
        self.saved_regs = {}
        self.local_vars = {}
        self.offset = 0
        self.setRetValues(func_entry)
        self.setInputArgs(func_entry)
        self.offset = -8

    def setRetValues(self, func_entry):
        global type_to_size
        ret_list = func_entry.getReturnTypes()
        for typ in ret_list:
            size = type_to_size(typ)
            self.offset += size
            self.ret_values += [(self.offset, size)]

    def setInputArgs(self, func_entry):
        global type_to_size
        args_list = func_entry.getInputArgs()
        for arg in args_list:
            size = type_to_size(arg)
            self.offset += size
            self.input_args += [(self.offset, size)]

    def setLocalVar(self, sym_table, name):
        global type_to_size
        var_entry = sym_table.symbols[name]
        size = max(1, var_entry.getDim()) * type_to_size(var_entry.getType())
        self.offset -= size
        self.local_vars[name] = (self.offset, size)

    def prettyPrint(self):
        print("Ret value:", self.ret_values, "Params:", self.input_args, "OldStPtrs:", self.old_st_ptrs, "SavedRegs:", self.saved_regs, "LocalVars:", self.local_vars)
