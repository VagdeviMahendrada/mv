from sly import Parser
from Lexer1 import CLexer
from SymbolTable1 import SymbolTableEntry,SymbolTable
from Ast1 import NameAst,NumberAst,AssignAst,PrintAst
gst=SymbolTable()
class CParser(Parser):
    tokens=CLexer.tokens
    literals=CLexer.literals
    @_('program')
    def s(self,p):
        return p[0]
    @_('return_type identifier "(" ")" "{" statements "}" ')
    def program(self,p):
        pr=Program()
        pr.addFunctionDetails(p.identifier,p.statements)
        return pr
    @_('INT')
    def return_type(self,p):
        return p[0]
    @_('statement ";" statements')
    def statements(self,p):
        return [p[0]]+p[2]
    @_('statement ";"')
    def statements(self,p):
        return [p[0]]
    @_('declaration_stmt')
    def statement(self,p):
        return p[0]
    @_('assignment_stmt')
    def statement(self,p):
        return p[0]
    @_('print_stmt')
    def statement(self,p):
        return p[0]
    @_('type list_of_variables')
    def declaration_stmt(self,p):
        # se=SymbolTableEntry(,p[0])
        # gst.addSymbol()
        for i in p[1]:
            se=SymbolTableEntry(i,p[0])
            gst.addSymbol(se)
    @_('identifier "," list_of_variables')
    def list_of_variables(self,p):
        return [p[0]]+p[2]
    @_('identifier')
    def list_of_variables(self,p):
        return [p[0]]
    @_('identifier "=" identifier')
    def assignment_stmt(self,p):
        la=NameAst(gst.nameInSymbolTable(p.identifier))
        ra=NameAst(gst.nameInSymbolTable(p.identifier))
        aa=AssignAst(la,ra)
        return aa
    @_('identifier "=" constant')
    def assignment_stmt(self,p):
        la=NameAst(gst.nameInSymbolTable(p.identifier))
        ra=NumberAst(p.constant)
        aa=AssignAst(la,ra)
        return aa
    @_('PRINT identifier')
    def print_stmt(self,p):
        pa=PrintAst(gst.nameInSymbolTable(p.identifier))
        return pa
    @_('INT')
    def type(self,p):
        return p[0]
    @_('ID')
    def identifier(self,p):
        return p[0]
    @_('NUMBER')
    def constant(self,p):
        return p[0]
lexer=CLexer()
parser=CParser()
code='''int main(){
int a;
a=30;
print a;
}'''
res=(parser.parse(lexer.tokenize(code)))
if res:
    print("valid code")
else:
    print("invalid code")