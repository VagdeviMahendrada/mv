import argparse
from Lexer import CLexer
from Parser import CParser
parser = argparse.ArgumentParser()
parser.usage = "tinyCC [options] file"

parser.add_argument('-tokens',action='store_true',help="Show tokens in file.toks (or out.toks)")
parser.add_argument('-parse',action='store_true',help="Stop processing with parsing")
parser.add_argument('-ast', action='store_true',help="Show abstract syntax trees in file.ast (or out.ast)")
parser.add_argument('-symtab',action='store_true',help="Show symbol table in file.sym (or out.sym)")
parser.add_argument('-compile',action='store_true',help="Compile the program and generate spim code in file.spim (or out.spim)")
parser.add_argument('file',help="TinyC Program")
args = parser.parse_args()
lex=CLexer()
par=CParser()
f=open(args.file)
code=f.read()
tokens=lex.tokenize(code)
args.compile = True  #default value
if args.tokens:
    tokens_file_name = args.file +".toks"
    tokens_file = open(tokens_file_name,"w")
    for toks in tokens:
        tokens_file.write(f"type= {toks.type} , value= {toks.value} \n")
    # call tokenize and print tokens into tokens_file
if args.parse:
    res=par.parse(tokens)
    if res:
        print("code is valid,the code is accepted")
    else:
        print("errors in code!!!code not accepted")
	# call parser, which should not create Program data structure
    args.ast = False
    args.compile = False
if args.ast:
	ast_file_name = args.file +".ast"
	ast_file = open(ast_file_name,"w")
	# call parser, creates Program object
	# call program.print(), which should print ast
if args.compile:
	target_code_file_name = args.file +".spim"
	target_code_file = open(target_code_file_name,"w")
    # call parser, creates Program object
    # call program.compile(), which should 

