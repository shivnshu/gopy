#!/usr/bin/env bash

$GoPyPATH/src/codegen/codegen.py $1 $2 > /dev/null 2>&1

if [[ "$2" == "" ]]; then
	out="tmp";
else
	out="$2";
fi

$GoPyPATH/src/codegen/link-run.sh $out
