type_to_size = {}
type_to_size["int"] = 4
type_to_size["long"] = 8
type_to_size["char"] = 1
type_to_size["float"] = 4
type_to_size["double"] = 8
type_to_size["string"] = 4 # Since storing address

class SymbolTableEntry:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.parent = None
    def setTable(self, table):
        self.table = table
    def getName(self):
        return self.name
    def getSymbolType(self):
        return self.type
    def prettyPrint(self):
        print("Name:" + self.name + " ," + "Type:" + self.type + " ," + "TableName:" + self.table.getName(), end=', ')

class SymbolTableVariableEntry(SymbolTableEntry):
    def __init__(self, name):
        SymbolTableEntry.__init__(self, name, "VarType")
        self.variableType = ""
        self.dimension = 0
        self.dim_ranges = []
        self.is_local = True
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
    def isNotLocal(self):
        self.is_local = False
    def getIsLocal(self):
        return self.is_local
    def prettyPrint(self):
        SymbolTableEntry.prettyPrint(self)
        print("VariableType:" + self.variableType + ", ", "Dimensions:", self.dimension, ", " +"DimRanges:", self.dim_ranges, ", ", "Local:", self.is_local, ", ")

class SymbolTableLitEntry(SymbolTableEntry):
    def __init__(self, name, typ):
        SymbolTableEntry.__init__(self, name, "LitEntry")
        self.variableType = typ
    def getType(self):
        return self.variableType
    def prettyPrint(self):
        SymbolTableEntry.prettyPrint(self)
        print("VariableType:", self.variableType, ",")

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

    def getSymbols(self):
        return self.symbols

    def getVarSymbols(self):
        res = {}
        for symbol in self.symbols:
            if (self.symbols[symbol].getSymbolType() == "VarType"):
                res[symbol] = self.symbols[symbol]
        return res

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

    def prettyPrint(self):
        print("\nName:", self.name)
        if (self.parent != None):
            print("Parent:", self.parent.getName())
        else:
            print("Parent:", None)
        for sym in self.symbols:
            self.symbols[sym].prettyPrint()
        print()

    # def toCSV(self):
    #     print("Name:", self.name, "\nParent:", self.parent, "\nSymbols:", self.symbols)
    #     print()
    #     print("Name, Type, variableType, Input Args")
    #     for sym in self.symbols:
    #         entry = self.symbols[sym]
    #         entry.prettyPrint()


class ActivationRecord:
    def __init__(self, name):
        self.name = name
        self.ret_values = []
        self.input_args = {}
        self.old_st_ptrs = {}
        self.saved_regs = {}
        self.local_vars = {}
        self.global_vars = {}
        self.const_vars = []
        self.access_links = {}
        self.pos_offset = 8 # 4 for saved ebp and 4 for return address
        self.offset = 0

    def getName(self):
        return self.name

    # def storeOldStPtr(self, name):
    #     self.old_st_ptrs[name] = (self.pos_offset, 4)
    #     self.pos_offset += 4

    def setRetValues(self, func_entry):
        global type_to_size
        ret_list = func_entry.getReturnTypes()
        for typ in ret_list:
            size = type_to_size[typ]
            self.ret_values += [(self.pos_offset, size)]
            self.pos_offset += size

    def getRetValues(self):
        return self.ret_values

    def setLocalVarsInputArgs(self, sym_table):
        global type_to_size
        varSymbols = sym_table.getVarSymbols()
        for symbol in varSymbols:
            var_entry = varSymbols[symbol]
            var_type = var_entry.getType()
            if (var_entry.getIsLocal() == True):
                size = max(1, var_entry.getDim()) * type_to_size[var_type]
                self.offset -= size
                self.local_vars[var_entry.getName()] = (self.offset, size)
            else:
                size = type_to_size[var_type]
                self.input_args[var_entry.getName()] = (self.pos_offset, size)
                self.pos_offset += size

    def getLocalVars(self):
        return self.local_vars

    def setGlobalVars(self, global_vars):
        self.global_vars = global_vars

    def getGlobalVars(self):
        return self.global_vars

    def putConstVar(self, var):
        self.const_vars += [var]

    def setConstVars(self, const_vars):
        self.const_vars = const_vars

    def getConstVars(self):
        return self.const_vars

    def getVarTuple(self,var_name):
        if var_name in self.local_vars:
            return self.local_vars[var_name], ""
        if var_name in self.input_args:
            return self.input_args[var_name], ""
        if var_name in self.global_vars:
            return self.global_vars[var_name], "global"
        if var_name in self.const_vars:
            return (None, None), "const"
        return (None, None), ""

    def prettyPrint(self):
        print("Name:", self.name, "Ret value:", self.ret_values, "Params:", self.input_args, "OldStPtrs:", self.old_st_ptrs, "SavedRegs:", self.saved_regs, "LocalVars:", self.local_vars, "GlobalVars:", self.global_vars, "ConstVars:", self.const_vars, "\n")
