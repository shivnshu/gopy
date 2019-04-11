#!/usr/bin/env python3

def symTableToCSV(symTableDict):
    for key in symTableDict:
        symTableDict[key].toCSV()
        print("\n\n")
