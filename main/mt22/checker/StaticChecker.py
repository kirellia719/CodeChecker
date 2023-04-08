from Visitor import Visitor
from StaticError import *
from AST import *


class Util:
    def print(o):
        print('----------------------------')
        print('[')
        for env in o:
            print('   [{}]'.format(
                ' ** '.join([str(symbol) for symbol in env])))
        print(']')


class Symbol:
    def __init__(self, name, typ, kind):
        self.name = name
        self.typ = typ
        self.kind = kind

    def __str__(self):
        temp = "Func"
        if type(self.kind) is Variable:
            temp = "Var"
        if type(self.kind) is Parameter:
            temp = "Param"
        return "{}({}, {})".format(temp, self.name, self.typ)


class StaticChecker(Visitor):
    def __init__(self, ctx):
        self.ctx = ctx

    def check(self):
        self.visit(self.ctx, None)
        return ''

    def visitIntegerType(self, ctx, o): return IntegerType()
    def visitFloatType(self, ctx, o): return FloatType()
    def visitBooleanType(self, ctx, o): return BooleanType()
    def visitStringType(self, ctx, o): return StringType()
    def visitArrayType(self, ctx, o): return ArrayType()
    def visitAutoType(self, ctx, o): return AutoType()
    def visitVoidType(self, ctx, o): return VoidType()

    def visitIntegerLit(self, ctx, o): return IntegerType()
    def visitFloatLit(self, ctx, o): return FloatType()
    def visitStringLit(self, ctx, o): return StringType()
    def visitBooleanLit(self, ctx, o): return BooleanType()
    def visitArrayLit(self, ctx, o): return ArrayType()

    def visitBinExpr(self, ctx, o): pass
    def visitUnExpr(self, ctx, o): pass

    def visitId(self, ctx, o):
        for env in o:
            for symbol in env:
                if (ctx.name == symbol.name):
                    return symbol.typ
        raise Undeclared(Variable(), ctx.name)

    def visitArrayCell(self, ctx, o): pass
    def visitFuncCall(self, ctx, o): pass

    def visitAssignStmt(self, ctx, o):
        right = self.visit(ctx.rhs, o)
        left = self.visit(ctx.lhs, o)
        if type(left) != type(right):
            raise TypeMismatchInStatement(ctx)

    def visitBlockStmt(self, ctx, o):
        for stmt in ctx.body:
            if type(stmt) is BlockStmt:
                self.visit(stmt, [[]] + o)
            else:
                self.visit(stmt, o)

    def visitIfStmt(self, ctx, o):
        cond = self.visit(ctx.cond, o)
        if type(ctx.tstmt) is BlockStmt:
            self.visit(ctx.tstmt, [[]] + o)
        else:
            self.visit(ctx.tstmt, o)
        if ctx.fstmt:
            if type(ctx.fstmt) is BlockStmt:
                self.visit(ctx.fstmt, [[]] + o)
            else:
                self.visit(ctx.stmt, o)
        if type(cond) is not BooleanType:
            raise TypeMismatchInExpression(ctx.cond)

    def visitForStmt(self, ctx, o): pass
    def visitWhileStmt(self, ctx, o): pass
    def visitDoWhileStmt(self, ctx, o): pass
    def visitBreakStmt(self, ctx, o): pass
    def visitContinueStmt(self, ctx, o): pass
    def visitReturnStmt(self, ctx, o): pass
    def visitCallStmt(self, ctx, o): pass

    def visitVarDecl(self, ctx, o):
        for symbol in o[0]:
            if ctx.name == symbol.name:
                raise Redeclared(Variable(), ctx.name)
        typ = self.visit(ctx.typ, o)
        if ctx.init is None:
            if type(typ) is AutoType:
                raise Invalid(Variable(), ctx.name)
            else:
                o[0] += [Symbol(ctx.name, typ, Variable())]
        else:
            init = self.visit(ctx.init, o)
            if type(typ) is AutoType:
                typ = init
            if type(typ) is FloatType and type(init) is IntegerType:
                init = typ
            if type(typ) == type(init):
                o[0] += [Symbol(ctx.name, typ, Variable())]
            else:
                raise TypeMismatchInVarDecl(ctx)
        return o

    def visitParamDecl(self, ctx, o):
        for symbol in o[0]:
            if ctx.name == symbol.name:
                raise Redeclared(Parameter(), ctx.name)
        typ = self.visit(ctx.typ, o)
        o[0] += [Symbol(ctx.name, typ, Parameter())]
        return o

    def visitFuncDecl(self, ctx, o):
        for symbol in o[0]:
            if ctx.name == symbol.name:
                raise Redeclared(Function(), ctx.name)
        typ = self.visit(ctx.return_type, o)
        o[0] += [Symbol(ctx.name, typ, Function())]

        newo = [[]] + o
        for param in ctx.params:
            newo = self.visit(param, newo)
        self.visit(ctx.body, newo)
        return o

    def visitProgram(self, ctx, o):
        o = [[]]
        for decl in ctx.decls:
            o = self.visit(decl, o)
