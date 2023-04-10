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

    def equalType(type1, type2):
        if type(type1) != type(type2):
            return False
        elif type(type1) is ArrayType and type(type2) is ArrayType:
            dimensions1 = type1.dimensions
            dimensions2 = type2.dimensions
            if type(type1.typ) != type(type2.typ):
                return False
            return dimensions1 == dimensions2
        else:
            return True


class FirstCheck(Visitor):
    def __init__(self):
        pass

    def visitProgram(self, ctx, o):
        self.checkEntryPoint = False
        o = []
        for decl in ctx.decls:
            o = self.visit(decl, o)
        return self.checkEntryPoint, o

    def visitVarDecl(self, ctx, o):
        for symbol in o:
            if ctx.name == symbol.name:
                raise Redeclared(Variable(), ctx.name)
        return o + [ctx]

    def visitFuncDecl(self, ctx, o):
        for symbol in o:
            if ctx.name == symbol.name:
                raise Redeclared(Function(), ctx.name)
        if ctx.name == 'main':
            self.checkEntryPoint = True
        return o + [ctx]


class Symbol:
    def __init__(self, name, typ, kind):
        self.name = name
        self.typ = typ
        self.kind = kind

    def __str__(self):
        return "{}({}, {})".format(self.kind, self.name, self.typ)


class StaticChecker(Visitor):
    def __init__(self, ctx):
        self.ctx = ctx
        self.firstCheck = None

    def check(self):
        self.visit(self.ctx, None)
        return []

    def visitIntegerType(self, ctx, o): return ctx
    def visitFloatType(self, ctx, o): return ctx
    def visitBooleanType(self, ctx, o): return ctx
    def visitStringType(self, ctx, o): return ctx
    def visitArrayType(self, ctx, o): return ctx
    def visitAutoType(self, ctx, o): return ctx
    def visitVoidType(self, ctx, o): return ctx

    def visitIntegerLit(self, ctx, o): return IntegerType()
    def visitFloatLit(self, ctx, o): return FloatType()
    def visitStringLit(self, ctx, o): return StringType()
    def visitBooleanLit(self, ctx, o): return BooleanType()

    def visitArrayLit(self, ctx, o):
        arrayType = None
        for expr in ctx.explist:
            typ = self.visit(expr, o)
            if arrayType:
                if not Util.equalType(arrayType, typ):
                    raise IllegalArrayLiteral(ctx)
            else:
                arrayType = typ
        if type(arrayType) is not ArrayType:
            return ArrayType([len(ctx.explist)], arrayType)
        else:
            dimensions = [len(ctx.explist)] + arrayType.dimensions
            arrayType = arrayType.typ
            return ArrayType(dimensions, arrayType)

    def visitBinExpr(self, ctx, o):
        left = self.visit(ctx.left, o)
        right = self.visit(ctx.right, o)

        if ctx.op in ['+', '-', '*', '/']:
            if (type(left) is not IntegerType and type(left) is not FloatType) or (type(right) is not IntegerType and type(right) is not FloatType):
                raise TypeMismatchInExpression(ctx)
            elif type(left) is FloatType or type(right) is FloatType:
                return FloatType()
            else:
                return IntegerType()

        if ctx.op in ['%']:
            if type(left) is IntegerType and type(right) is IntegerType:
                return IntegerType()
            else:
                raise TypeMismatchInExpression(ctx)

        if ctx.op in ['&&', '||']:
            if type(left) is BooleanType and type(right) is BooleanType:
                return BooleanType()
            else:
                raise TypeMismatchInExpression(ctx)

        if ctx.op in ['::']:
            if type(left) is StringType and type(right) is StringType:
                return StringType()
            else:
                raise TypeMismatchInExpression(ctx)

        if ctx.op in ['==', '!=']:
            if (type(left) is not IntegerType and type(left) is not BooleanType):
                raise TypeMismatchInExpression(ctx)
            elif (type(right) is not IntegerType and type(right) is not BooleanType):
                raise TypeMismatchInExpression(ctx)
            elif type(left) != type(right):
                raise TypeMismatchInExpression(ctx)
            else:
                return BooleanType()

        if ctx.op in ['>', '<', '>=', '<=']:
            if (type(left) is not IntegerType and type(left) is not FloatType) or (type(right) is not IntegerType and type(right) is not FloatType):
                raise TypeMismatchInExpression(ctx)
            else:
                return BooleanType()

    def visitUnExpr(self, ctx, o):
        val = self.visit(ctx.val, o)
        if ctx.op == '!':
            if type(val) is not BooleanType:
                raise TypeMismatchInExpression(ctx)
            else:
                return BooleanType()
        if ctx.op == '-':
            if type(val) is not IntegerType and type(val) is not FloatType:
                raise TypeMismatchInExpression(ctx)
            else:
                return val

    def visitId(self, ctx, o):
        for env in o:
            for symbol in env:
                if (ctx.name == symbol.name):
                    return symbol.typ
        raise Undeclared(Variable(), ctx.name)

    def visitArrayCell(self, ctx, o):
        for env in o:
            for symbol in env:
                if (ctx.name == symbol.name):
                    if type(symbol.typ) is not ArrayType:
                        raise TypeMismatchInExpression(ctx)
                    if len(ctx.cell) > len(symbol.typ.dimensions):
                        raise TypeMismatchInExpression(ctx)
                    for cell in ctx.cell:
                        typ = self.visit(cell, o)
                        if type(typ) is not IntegerType:
                            raise TypeMismatchInExpression(cell)
                    return symbol.typ.typ
        raise Undeclared(Variable(), ctx.name)

    def visitFuncCall(self, ctx, o):
        for decl in self.firstCheck:
            if decl.name == ctx.name and type(decl) is FuncDecl:
                for i in range(len(decl.params)):
                    param = self.visit(decl.params[i].typ, o)
                    arg = self.visit(ctx.args[i], o)
                    if type(param) is AutoType or type(arg) is AutoType:
                        continue
                    elif not Util.equalType(param, arg):
                        raise TypeMismatchInExpression(ctx.args[i])
                return decl.return_type
        raise Undeclared(Function(), ctx.name)

    def visitAssignStmt(self, ctx, o):
        o = o[0]
        right = self.visit(ctx.rhs, o)
        left = self.visit(ctx.lhs, o)
        if not Util.equalType(left, right):
            raise TypeMismatchInStatement(ctx)
        return right

    def visitBlockStmt(self, ctx, o):
        loop = o[1]
        o = o[0]
        newo = [[]] + o
        for stmt in ctx.body:
            self.visit(stmt, (newo, loop))

    def visitIfStmt(self, ctx, o):
        loop = o[1]
        o = o[0]
        cond = self.visit(ctx.cond, o)
        if type(cond) is not BooleanType:
            raise TypeMismatchInExpression(ctx.cond)
        self.visit(ctx.tstmt, (o, loop))
        if ctx.fstmt:
            self.visit(ctx.fstmt, (o, loop))

    def visitForStmt(self, ctx, o):
        o = o[0]
        init = self.visit(ctx.init, (o, True))
        if type(init) is not IntegerType:
            raise TypeMismatchInExpression(ctx.init)
        cond = self.visit(ctx.cond, o)
        if type(cond) is not BooleanType:
            raise TypeMismatchInExpression(ctx.cond)
        upd = self.visit(ctx.upd, o)
        if type(upd) is not IntegerType:
            raise TypeMismatchInExpression(ctx.upd)
        self.visit(ctx.stmt, (o, True))

    def visitWhileStmt(self, ctx, o):
        o = o[0]
        cond = self.visit(ctx.cond, o)
        if type(cond) is not BooleanType:
            raise TypeMismatchInExpression(ctx.cond)
        self.visit(ctx.stmt, (o, True))

    def visitDoWhileStmt(self, ctx, o):
        o = o[0]
        cond = self.visit(ctx.cond, o)
        if type(cond) is not BooleanType:
            raise TypeMismatchInExpression(ctx.cond)
        self.visit(ctx.stmt, (o, True))

    def visitBreakStmt(self, ctx, o):
        if not o[1]:
            raise MustInLoop(ctx)

    def visitContinueStmt(self, ctx, o):
        if not o[1]:
            raise MustInLoop(ctx)

    def visitReturnStmt(self, ctx, o):
        o = o[0]
        if ctx.expr:
            self.visit(ctx.expr, o)

    def visitCallStmt(self, ctx, o):
        if ctx.name == 'super' or ctx.name == 'preventDefault':
            raise InvalidStatementInFunction(o[2])
        o = o[0]
        for decl in self.firstCheck:
            if decl.name == ctx.name and type(decl) is FuncDecl:
                for i in range(len(decl.params)):
                    param = self.visit(decl.params[i].typ, o)
                    arg = self.visit(ctx.args[i], o)
                    if type(param) is AutoType or type(arg) is AutoType:
                        continue
                    elif not Util.equalType(param, arg):
                        raise TypeMismatchInExpression(ctx.args[i])
                return
        raise Undeclared(Function(), ctx.name)

    def visitVarDecl(self, ctx, o):
        o = o[0]
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
            if Util.equalType(typ, init):
                o[0] += [Symbol(ctx.name, typ, 'Variable')]
            else:
                raise TypeMismatchInVarDecl(ctx)

    def visitParamDecl(self, ctx, o):
        tag = o[1]
        o = o[0]
        for symbol in o[0]:
            if ctx.name == symbol.name:
                if (symbol.kind == 'Parameter'):
                    raise Redeclared(Parameter(), ctx.name)
                elif (symbol.kind == 'Inherit'):
                    raise Invalid(Parameter(), ctx.name)

        typ = self.visit(ctx.typ, o)
        o[0] += [Symbol(ctx.name, typ, tag)]

    def visitFuncDecl(self, ctx, o):
        o = o[0]
        for symbol in o[0]:
            if ctx.name == symbol.name:
                raise Redeclared(Function(), ctx.name)
        typ = self.visit(ctx.return_type, o)
        o[0] += [Symbol(ctx.name, typ, 'Function')]

        # Nếu có kế thừa
        if ctx.inherit:
            parent = None
            for decl in self.firstCheck:
                if (ctx.inherit == decl.name) and type(decl) is FuncDecl:
                    parent = decl
                    break
            if parent:  # Tìm thấy cha
                inheritParams = []
                for parentParam in parent.params:
                    if (parentParam.inherit):
                        inheritParams += [parentParam]
                newo = [[]] + o
                for iParam in inheritParams:
                    self.visit(iParam, (newo, 'Inherit'))
                for param in ctx.params:
                    self.visit(param, (newo, 'Parameter'))
                if len(parent.params) > 0:
                    if (len(ctx.body.body) > 0):
                        if type(ctx.body.body[0]) is CallStmt and (ctx.body.body[0].name == 'super' or ctx.body.body[0].name == 'preventDefault'):
                            if ctx.body.body[0].name == 'preventDefault':
                                pass
                            else:
                                self.visit(
                                    CallStmt(
                                        parent.name, ctx.body.body[0].args),
                                    (newo, False)
                                )
                            ctx.body.body = ctx.body.body[1:]
                        else:
                            raise InvalidStatementInFunction(ctx.name)
                    else:
                        raise InvalidStatementInFunction(ctx.name)
                else:
                    if (len(ctx.body.body) > 0):
                        if type(ctx.body.body[0]) is CallStmt and ctx.body.body[0].name == 'preventDefault':
                            ctx.body.body = ctx.body.body[1:]
                for stmt in ctx.body.body:
                    self.visit(stmt, (newo, False, ctx.name))
            else:   # Không tìm thấy cha
                raise Undeclared(Function(), ctx.inherit)
        else:
            newo = [[]] + o
            for param in ctx.params:
                self.visit(param, (newo, 'Parameter'))
            for stmt in ctx.body.body:
                self.visit(stmt, (newo, False, ctx.name))

    def visitProgram(self, ctx, o):
        checkEntryPoint, self.firstCheck = FirstCheck().visit(ctx, [])
        o = [[]]
        for decl in ctx.decls:
            self.visit(decl, (o, False))
        if (not checkEntryPoint):
            raise NoEntryPoint()
