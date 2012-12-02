#!/usr/bin/python

import os
import yaml


f = open("school_list")
conf = yaml.load(f)
f.close()

# print conf

f = open("Makefile", 'w')
f.write("all :")
for name in conf:
    f.write(" " + name)
f.write("\n")
f.write("\n")


for name in conf:
    f.write(name + " : " + "src/" + name + ".tex src/PhD.tex\n")
    f.write("\tcat src/PhD.tex src/" + name + ".tex > temp.tex\n")
    f.write("\techo \"" + name + "\" > schoolname.tex\n")
    f.write("\tpdflatex -jobname=\"" + name + "\" \"")
    for each_def in conf[name]:
        f.write("\\def\\" + each_def + "{" + str(conf[name][each_def]) + "} ")
    f.write("\\input{src/template.tex}\"\n")
    f.write("\tmv " + name + ".pdf build/\n")
    f.write("\trm schoolname.tex\n")
    f.write("\trm temp.tex\n")
    f.write("\n")

f.write(".PHONY: clean\n")
f.write("clean:\n")
f.write("\trm *.log *.out *.aux ./build/*.pdf")



