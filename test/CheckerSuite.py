import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *


class CheckerSuite(unittest.TestCase):
    # # #------------------ Check

    def test_400(self):
        input = Program([VarDecl("a", IntegerType()),
                        VarDecl("c", FloatType())])
        expected = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input, expected, 400))

    # def test_401(self):
    #     input = Program([
    #         VarDecl('x', IntegerType()),
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([]))
    #     ])
    #     expected = str([])
    #     self.assertTrue(TestChecker.test(input, expected, 401))

    # def test_402(self):
    #     input = Program([
    #         VarDecl('x', IntegerType()),
    #         VarDecl('y', IntegerType()),
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([]))
    #     ])
    #     expected = str([])
    #     self.assertTrue(TestChecker.test(input, expected, 402))

    # def test_403(self):
    #     input = Program([VarDecl('a', IntegerType()),
    #                     VarDecl('a', IntegerType())])
    #     expected = str(Redeclared(Variable(), 'a'))
    #     self.assertTrue(TestChecker.test(input, expected, 403))

    # def test_404(self):
    #     input = Program([VarDecl('a', IntegerType()), VarDecl(
    #         'a', FloatType()), VarDecl('a', BooleanType())])
    #     expected = str(Redeclared(Variable(), 'a'))
    #     self.assertTrue(TestChecker.test(input, expected, 404))

    # def test_405(self):
    #     input = Program([FuncDecl('main', VoidType(), [], None, BlockStmt([
    #         VarDecl('a', IntegerType(), IntegerLit(1))
    #     ]))])
    #     expected = str([])
    #     self.assertTrue(TestChecker.test(input, expected, 405))

    # def test_406(self):
    #     input = Program([FuncDecl('main', VoidType(), [], None, BlockStmt([
    #         VarDecl('a', IntegerType(), IntegerLit(1)),
    #         VarDecl('b', FloatType(), FloatLit(1.2))
    #     ]))])
    #     expected = str([])
    #     self.assertTrue(TestChecker.test(input, expected, 406))

    # def test_407(self):
    #     input = Program([VarDecl('x', IntegerType(), IntegerLit(
    #         1)), VarDecl('x', FloatType(), FloatLit(3.4))])
    #     expected = str(Redeclared(Variable(), 'x'))
    #     self.assertTrue(TestChecker.test(input, expected, 407))

    # # # # --------------------------IntegerLit thay FloatLit-------------------------

    # def test_408(self):
    #     input = Program([
    #         VarDecl('x', FloatType(), IntegerLit(1)),
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([]))
    #     ])
    #     expected = str([])
    #     self.assertTrue(TestChecker.test(input, expected, 408))

    # def test_409(self):
    #     input = Program([VarDecl('x', IntegerType(), FloatLit(2.123))])
    #     expected = str(TypeMismatchInVarDecl(
    #         VarDecl('x', IntegerType(), FloatLit(2.123))))
    #     self.assertTrue(TestChecker.test(input, expected, 409))

    # # # ---------------------- Check Auto Invalid ---------------------
    # def test_410(self):
    #     input = Program([VarDecl('x', AutoType())])
    #     expected = str(Invalid(Variable(), 'x'))
    #     self.assertTrue(TestChecker.test(input, expected, 410))

    # def test_411(self):
    #     input = Program([
    #         VarDecl('x', AutoType(), FloatLit(2.123)),
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([]))
    #     ])
    #     expected = str([])
    #     self.assertTrue(TestChecker.test(input, expected, 411))

    # def test_412(self):
    #     input = Program([FuncDecl('main', VoidType(), [], None, BlockStmt([
    #         VarDecl('x', AutoType(), IntegerLit(0)),
    #         VarDecl('y', AutoType(), FloatLit(2.123))
    #     ]))])
    #     expected = str([])
    #     self.assertTrue(TestChecker.test(input, expected, 412))

    # def test_413(self):
    #     input = Program([VarDecl('a', AutoType(), IntegerLit(2)),
    #                     VarDecl('a', AutoType(), FloatLit(1.9))])
    #     expected = str(Redeclared(Variable(), 'a'))
    #     self.assertTrue(TestChecker.test(input, expected, 413))

    # # # ------------------ Function Check - --------------------

    # def test_414(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([]))
    #     ])
    #     expected = str([])
    #     self.assertTrue(TestChecker.test(input, expected, 414))

    # def test_415(self):
    #     input = Program([
    #         VarDecl('a', IntegerType()),
    #         FuncDecl('b', VoidType(), [], None, BlockStmt([])),
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([]))
    #     ])
    #     expected = str([])
    #     self.assertTrue(TestChecker.test(input, expected, 415))

    # def test_416(self):
    #     input = Program([VarDecl('same', IntegerType()), FuncDecl(
    #         'same', VoidType(), [], None, BlockStmt([]))])
    #     expected = str(Redeclared(Function(), 'same'))
    #     self.assertTrue(TestChecker.test(input, expected, 416))

    # def test_416(self):
    #     input = Program([
    #         FuncDecl('a', VoidType(), [], None, BlockStmt([])),
    #         FuncDecl('a', VoidType(), [], None, BlockStmt([])),
    #         FuncDecl('a', VoidType(), [], None, BlockStmt([]))
    #     ])
    #     expected = str(Redeclared(Function(), 'a'))
    #     self.assertTrue(TestChecker.test(input, expected, 416))

    # # # -------------------- Check Redeclared Param Scope ---------------------
    # def test_417(self):
    #     input = Program([
    #         FuncDecl(
    #             'a',
    #             VoidType(),
    #             [ParamDecl('a', IntegerType())],
    #             None,
    #             BlockStmt([])
    #         ),
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([]))
    #     ])
    #     expected = str([])
    #     self.assertTrue(TestChecker.test(input, expected, 417))

    # def test_418(self):
    #     input = Program([
    #         FuncDecl(
    #             'a',
    #             VoidType(),
    #             [ParamDecl('x', IntegerType()), ParamDecl('x', IntegerType())],
    #             None,
    #             BlockStmt([])
    #         )
    #     ])
    #     expected = str(Redeclared(Parameter(), 'x'))
    #     self.assertTrue(TestChecker.test(input, expected, 418))

    # def test_419(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([])),
    #         FuncDecl('a', VoidType(),
    #                  [ParamDecl('x', IntegerType())],
    #                  None, BlockStmt([])
    #                  ),
    #         FuncDecl('b', VoidType(),
    #                  [ParamDecl('x', IntegerType())],
    #                  None, BlockStmt([])
    #                  )
    #     ])
    #     expected = str([])
    #     self.assertTrue(TestChecker.test(input, expected, 419))

    # # # --------------- Check Redclare In Block - -------------------

    # def test_420(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('a', IntegerType())
    #         ]))
    #     ])
    #     expected = str([])
    #     self.assertTrue(TestChecker.test(input, expected, 420))

    # def test_421(self):
    #     input = Program([
    #         FuncDecl('a', VoidType(), [], None, BlockStmt([
    #             VarDecl('a', IntegerType()),
    #             VarDecl('a', IntegerType()),
    #         ]))
    #     ])
    #     expected = str(Redeclared(Variable(), 'a'))
    #     self.assertTrue(TestChecker.test(input, expected, 421))

    # def test_422(self):
    #     input = Program([
    #         VarDecl('a', IntegerType()),
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('a', IntegerType()),
    #         ]))
    #     ])
    #     expected = str([])
    #     self.assertTrue(TestChecker.test(input, expected, 422))

    # def test_423(self):
    #     input = Program([
    #         VarDecl('a', IntegerType()),
    #         FuncDecl('b', VoidType(), [], None, BlockStmt([
    #             VarDecl('a', IntegerType()),
    #         ])),
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('a', IntegerType()),
    #         ]))
    #     ])
    #     expected = str([])
    #     self.assertTrue(TestChecker.test(input, expected, 423))

    # def test_424(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('x', IntegerType()),
    #             BlockStmt([
    #                 VarDecl('x', IntegerType()),
    #                 VarDecl('x', IntegerType()),
    #             ])
    #         ]))
    #     ])
    #     expected = str(Redeclared(Variable(), 'x'))
    #     self.assertTrue(TestChecker.test(input, expected, 424))

    # def test_425(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [ParamDecl('x', IntegerType()),], None, BlockStmt([
    #             VarDecl('x', IntegerType()),
    #         ]))
    #     ])
    #     expected = str(Redeclared(Variable(), 'x'))
    #     self.assertTrue(TestChecker.test(input, expected, 425))

    # # # --------------- Check Assign Stmt - ----------------------

    # def test_426(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             AssignStmt(Id('a'), IntegerLit(1))
    #         ]))
    #     ])
    #     expected = str(Undeclared(Variable(), 'a'))
    #     self.assertTrue(TestChecker.test(input, expected, 426))

    # def test_427(self):
    #     input = Program([
    #         VarDecl('a', IntegerType()),
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             AssignStmt(Id('a'), IntegerLit(1))
    #         ]))
    #     ])
    #     expected = str([])
    #     self.assertTrue(TestChecker.test(input, expected, 427))

    # def test_428(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('x', FloatType()),
    #             VarDecl('y', IntegerType()),
    #             AssignStmt(Id('x'), Id('y'))
    #         ]))
    #     ])
    #     expected = str(TypeMismatchInStatement(AssignStmt(Id('x'), Id('y'))))
    #     self.assertTrue(TestChecker.test(input, expected, 428))

    # def test_429(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [ParamDecl('x', IntegerType())], None, BlockStmt([
    #             AssignStmt(Id('x'), IntegerLit(2))
    #         ]))
    #     ])
    #     expected = str([])
    #     self.assertTrue(TestChecker.test(input, expected, 429))

    # # # -------------- If stmt - ----------------------------

    # def test_430(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             IfStmt(BooleanLit(True), BlockStmt([]))
    #         ]))
    #     ])
    #     expected = str([])
    #     self.assertTrue(TestChecker.test(input, expected, 430))

    # def test_431(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             IfStmt(IntegerLit(1), BlockStmt([]), BlockStmt([]))
    #         ]))
    #     ])
    #     expected = str(TypeMismatchInExpression(IntegerLit(1)))
    #     self.assertTrue(TestChecker.test(input, expected, 431))

    # def test_432(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('a', BooleanType(), BooleanLit(True)),
    #             IfStmt(Id('a'), BlockStmt([]), BlockStmt([]))
    #         ]))
    #     ])
    #     expected = str([])
    #     self.assertTrue(TestChecker.test(input, expected, 432))

    # def test_433(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('a', BooleanType(), BooleanLit(True)),
    #             IfStmt(Id('a'), BlockStmt([
    #                 VarDecl('a', IntegerType())
    #             ]))
    #         ]))
    #     ])
    #     expected = str([])
    #     self.assertTrue(TestChecker.test(input, expected, 433))

    # def test_434(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('a', BooleanType(), BooleanLit(True)),
    #             IfStmt(Id('a'), AssignStmt(Id('a'), IntegerLit(1)))
    #         ]))
    #     ])
    #     expected = str(TypeMismatchInStatement(
    #         AssignStmt(Id('a'), IntegerLit(1))))
    #     self.assertTrue(TestChecker.test(input, expected, 434))

    # def test_435(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('a', BooleanType(), BooleanLit(True)),
    #             IfStmt(
    #                 Id('a'),
    #                 IfStmt(BooleanLit(False), VarDecl('a', BooleanType()))
    #             )
    #         ]))
    #     ])
    #     expected = str(Redeclared(Variable(), 'a'))
    #     self.assertTrue(TestChecker.test(input, expected, 435))

    # def test_436(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('a', BooleanType(), BooleanLit(True)),
    #             IfStmt(
    #                 Id('a'),
    #                 BlockStmt([VarDecl('x', IntegerType())]),
    #                 BlockStmt([AssignStmt(Id('x'), IntegerLit(1))])
    #             )
    #         ]))
    #     ])
    #     expected = str(Undeclared(Variable(), 'x'))
    #     self.assertTrue(TestChecker.test(input, expected, 436))

    # # # # # #---------------------- BinExpr - --------------------
    # # # # # #---------------------- + - * / -----------------------

    # def test_437(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl(
    #                 'a',
    #                 IntegerType(),
    #                 BinExpr('+', IntegerLit(1), IntegerLit(2))
    #             )
    #         ]))
    #     ])
    #     expected = str([])
    #     self.assertTrue(TestChecker.test(input, expected, 437))

    # def test_438(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl(
    #                 'a',
    #                 FloatType(),
    #                 BinExpr('-', FloatLit(2.0), IntegerLit(1))
    #             )
    #         ]))
    #     ])
    #     expected = str([])
    #     self.assertTrue(TestChecker.test(input, expected, 438))

    # def test_439(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl(
    #                 'a',
    #                 FloatType(),
    #                 BinExpr('+', BooleanLit(True), IntegerLit(1))
    #             )
    #         ]))
    #     ])
    #     expected = str(TypeMismatchInExpression(
    #         BinExpr('+', BooleanLit(True), IntegerLit(1))))
    #     self.assertTrue(TestChecker.test(input, expected, 439))

    # def test_440(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl(
    #                 'a',
    #                 FloatType(),
    #                 BinExpr('+', FloatLit(1), FloatLit(1))
    #             )
    #         ]))
    #     ])
    #     expected = str([])
    #     self.assertTrue(TestChecker.test(input, expected, 440))

    # # # # # # ------------------------- % ------------------------------

    # def test_441(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl(
    #                 'abc',
    #                 FloatType(),
    #                 BinExpr('%', IntegerLit(1), IntegerLit(1))
    #             )
    #         ]))
    #     ])
    #     expected = str([])
    #     self.assertTrue(TestChecker.test(input, expected, 441))

    # def test_442(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl(
    #                 'abc',
    #                 BooleanType(),
    #                 BinExpr('%', FloatLit(1.2), IntegerLit(1))
    #             )
    #         ]))
    #     ])
    #     expected = str(TypeMismatchInExpression(
    #         BinExpr('%', FloatLit(1.2), IntegerLit(1))))
    #     self.assertTrue(TestChecker.test(input, expected, 442))

    # # ------------------------- && || ------------------------
    # def test_443(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl(
    #                 'abc',
    #                 BooleanType(),
    #                 BinExpr('&&', BooleanLit(True), BooleanLit(False))
    #             )
    #         ]))
    #     ])
    #     expected = str([])
    #     self.assertTrue(TestChecker.test(input, expected, 443))

    # def test_444(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl(
    #                 'abc',
    #                 BooleanType(),
    #                 BinExpr('||', FloatLit(1.2), BooleanLit(True))
    #             )
    #         ]))
    #     ])
    #     expected = str(TypeMismatchInExpression(
    #         BinExpr('||', FloatLit(1.2), BooleanLit(True))))
    #     self.assertTrue(TestChecker.test(input, expected, 444))

    # def test_445(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl(
    #                 'abc',
    #                 BooleanType(),
    #                 BinExpr('||', FloatLit(1.2), BooleanLit(True))
    #             )
    #         ]))
    #     ])
    #     expected = str(TypeMismatchInExpression(
    #         BinExpr('||', FloatLit(1.2), BooleanLit(True))))
    #     self.assertTrue(TestChecker.test(input, expected, 445))

    # # # # #---------------------: : String - ------------------------

    # def test_446(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl(
    #                 'abc',
    #                 StringType(),
    #                 BinExpr('::', StringLit('avc'), StringLit('def'))
    #             )
    #         ]))
    #     ])
    #     expected = str([])
    #     self.assertTrue(TestChecker.test(input, expected, 446))

    # def test_447(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl(
    #                 'abc',
    #                 StringType(),
    #                 BinExpr('::', FloatLit(1.2), IntegerLit(0))
    #             )
    #         ]))
    #     ])
    #     expected = str(TypeMismatchInExpression(
    #         BinExpr('::', FloatLit(1.2), IntegerLit(0))))
    #     self.assertTrue(TestChecker.test(input, expected, 447))

    # # # # #---------------------- == != ----------------------------

    # def test_448(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl(
    #                 'abc',
    #                 BooleanType(),
    #                 BinExpr('==', IntegerLit(1), IntegerLit(1))
    #             )
    #         ]))
    #     ])
    #     expected = str([])
    #     self.assertTrue(TestChecker.test(input, expected, 448))

    # def test_449(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl(
    #                 'abc',
    #                 BooleanType(),
    #                 BinExpr('==', IntegerLit(123), StringLit('1'))
    #             )
    #         ]))
    #     ])
    #     expected = str(TypeMismatchInExpression(
    #         BinExpr('==', IntegerLit(123), StringLit('1'))))
    #     self.assertTrue(TestChecker.test(input, expected, 449))

    # def test_450(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl(
    #                 'abc',
    #                 BooleanType(),
    #                 BinExpr('!=', StringLit('a'), StringLit('1'))
    #             )
    #         ]))
    #     ])
    #     expected = str(TypeMismatchInExpression(
    #         BinExpr('!=', StringLit('a'), StringLit('1'))))
    #     self.assertTrue(TestChecker.test(input, expected, 450))

    # def test_451(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl(
    #                 'abc',
    #                 BooleanType(),
    #                 BinExpr('==', BooleanLit(True), IntegerLit('1'))
    #             )
    #         ]))
    #     ])
    #     expected = str(TypeMismatchInExpression(
    #         BinExpr('==', BooleanLit(True), IntegerLit('1'))))
    #     self.assertTrue(TestChecker.test(input, expected, 451))

    # def test_452(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl(
    #                 'abc',
    #                 BooleanType(),
    #                 BinExpr('!=', BooleanLit(True), IntegerLit('1'))
    #             )
    #         ]))
    #     ])
    #     expected = str(TypeMismatchInExpression(
    #         BinExpr('!=', BooleanLit(True), IntegerLit('1'))))
    #     self.assertTrue(TestChecker.test(input, expected, 452))

    # # # # # #----------------------- > < >= <= ------------------------

    # def test_453(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl(
    #                 'abc',
    #                 BooleanType(),
    #                 BinExpr('>', IntegerLit(1), IntegerLit(2))
    #             )
    #         ]))
    #     ])
    #     expected = str([])
    #     self.assertTrue(TestChecker.test(input, expected, 453))

    # def test_454(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl(
    #                 'comp',
    #                 BooleanType(),
    #                 BinExpr('<', FloatLit(1.4), IntegerLit(5))
    #             )
    #         ]))
    #     ])
    #     expected = str([])
    #     self.assertTrue(TestChecker.test(input, expected, 454))

    # def test_455(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl(
    #                 'comp',
    #                 BooleanType(),
    #                 BinExpr('>=', StringLit('a'), IntegerLit(5))
    #             )
    #         ]))
    #     ])
    #     expected = str(TypeMismatchInExpression(
    #         BinExpr('>=', StringLit('a'), IntegerLit(5))))
    #     self.assertTrue(TestChecker.test(input, expected, 455))

    # def test_455(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl(
    #                 'comp',
    #                 IntegerType(),
    #                 BinExpr('<=', IntegerLit(10), IntegerLit(9))
    #             )
    #         ]))
    #     ])
    #     expected = str(TypeMismatchInVarDecl(VarDecl(
    #         'comp',
    #         IntegerType(),
    #         BinExpr('<=', IntegerLit(10), IntegerLit(9))
    #     )))
    #     self.assertTrue(TestChecker.test(input, expected, 455))

    # #  # # #------------------------- UnExpr-----------------------

    # def test_456(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl(
    #                 'un',
    #                 BooleanType(),
    #                 UnExpr('!', BooleanLit(True))
    #             )
    #         ]))
    #     ])
    #     expected = str([])
    #     self.assertTrue(TestChecker.test(input, expected, 456))

    # def test_457(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl(
    #                 'un',
    #                 BooleanType(),
    #                 UnExpr('!', IntegerLit(1))
    #             )
    #         ]))
    #     ])
    #     expected = str(TypeMismatchInExpression(UnExpr('!', IntegerLit(1))))
    #     self.assertTrue(TestChecker.test(input, expected, 457))

    # def test_458(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl(
    #                 'sub',
    #                 IntegerType(),
    #                 UnExpr('-', IntegerLit(1))
    #             )
    #         ]))
    #     ])
    #     expected = str([])
    #     self.assertTrue(TestChecker.test(input, expected, 458))

    # def test_459(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl(
    #                 'sub',
    #                 IntegerType(),
    #                 UnExpr('-', FloatLit(1.2))
    #             )
    #         ]))
    #     ])
    #     expected = str(TypeMismatchInVarDecl(VarDecl(
    #         'sub',
    #         IntegerType(),
    #         UnExpr('-', FloatLit(1.2))
    #     )))
    #     self.assertTrue(TestChecker.test(input, expected, 459))

    # def test_460(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl(
    #                 'sub',
    #                 AutoType(),
    #                 UnExpr('-', BooleanLit(True))
    #             )
    #         ]))
    #     ])
    #     expected = str(TypeMismatchInExpression(UnExpr('-', BooleanLit(True))))
    #     self.assertTrue(TestChecker.test(input, expected, 460))

    # # # # ----------------------- FOR STMT -----------------
    # def test_460(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             ForStmt(
    #                 AssignStmt(Id('i'), IntegerLit(0)),
    #                 BinExpr('<', Id('i'), IntegerLit(10)),
    #                 BinExpr('+', Id('i'), IntegerLit(1)),
    #                 BlockStmt([])
    #             )
    #         ]))
    #     ])
    #     expected = str(Undeclared(Variable(), 'i'))
    #     self.assertTrue(TestChecker.test(input, expected, 460))

    # def test_461(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('i', IntegerType()),
    #             ForStmt(
    #                 AssignStmt(Id('i'), IntegerLit(0)),
    #                 BinExpr('<', Id('i'), IntegerLit(10)),
    #                 BinExpr('+', Id('i'), IntegerLit(1)),
    #                 BlockStmt([])
    #             )
    #         ]))
    #     ])
    #     expected = str([])
    #     self.assertTrue(TestChecker.test(input, expected, 461))

    # def test_462(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('i', IntegerType()),
    #             ForStmt(
    #                 AssignStmt(Id('i'), FloatLit(1.2)),
    #                 BinExpr('<', Id('i'), IntegerLit(10)),
    #                 BinExpr('+', Id('i'), IntegerLit(1)),
    #                 BlockStmt([])
    #             )
    #         ]))
    #     ])
    #     expected = str(TypeMismatchInStatement(
    #         AssignStmt(Id('i'), FloatLit(1.2))))
    #     self.assertTrue(TestChecker.test(input, expected, 462))

    # def test_463(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('i', FloatType()),
    #             ForStmt(
    #                 AssignStmt(Id('i'), FloatLit(1.2)),
    #                 BinExpr('<', Id('i'), IntegerLit(10)),
    #                 BinExpr('+', Id('i'), IntegerLit(1)),
    #                 BlockStmt([])
    #             )
    #         ]))
    #     ])
    #     expected = str(TypeMismatchInExpression(
    #         AssignStmt(Id('i'), FloatLit(1.2))))
    #     self.assertTrue(TestChecker.test(input, expected, 463))

    # def test_463(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('i', IntegerType()),
    #             ForStmt(
    #                 AssignStmt(Id('i'), IntegerLit(1)),
    #                 BinExpr('+', Id('i'), IntegerLit(10)),
    #                 BinExpr('+', Id('i'), IntegerLit(1)),
    #                 BlockStmt([])
    #             )
    #         ]))
    #     ])
    #     expected = str(TypeMismatchInExpression(
    #         BinExpr('+', Id('i'), IntegerLit(10))))
    #     self.assertTrue(TestChecker.test(input, expected, 463))

    # def test_464(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('i', IntegerType()),
    #             ForStmt(
    #                 AssignStmt(Id('i'), IntegerLit(1)),
    #                 BinExpr('<', Id('i'), IntegerLit(10)),
    #                 BinExpr('>', Id('i'), IntegerLit(1)),
    #                 BlockStmt([])
    #             )
    #         ]))
    #     ])
    #     expected = str(TypeMismatchInExpression(
    #         BinExpr('>', Id('i'), IntegerLit(1))))
    #     self.assertTrue(TestChecker.test(input, expected, 464))

    # def test_465(self):
    #     input = Program([
    #         VarDecl('i', IntegerType()),
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             ForStmt(
    #                 AssignStmt(Id('i'), IntegerLit(1)),
    #                 BinExpr('<', Id('i'), IntegerLit(10)),
    #                 BinExpr('+', Id('i'), IntegerLit(0)),
    #                 AssignStmt(Id('i'), BinExpr('+', Id('i'), IntegerLit(1)))
    #             )
    #         ]))
    #     ])
    #     expected = str([])
    #     self.assertTrue(TestChecker.test(input, expected, 465))

    # # # -------------------- While Stmt -----------------------
    # def test_466(self):
    #     input = Program([
    #         VarDecl('i', IntegerType()),
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             WhileStmt(
    #                 BooleanLit(True),
    #                 BlockStmt([])
    #             )
    #         ]))
    #     ])
    #     expected = str([])
    #     self.assertTrue(TestChecker.test(input, expected, 466))

    # def test_467(self):
    #     input = Program([
    #         VarDecl('i', IntegerType()),
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             WhileStmt(
    #                 IntegerLit(1),
    #                 BlockStmt([])
    #             )
    #         ]))
    #     ])
    #     expected = str(TypeMismatchInExpression(IntegerLit(1)))
    #     self.assertTrue(TestChecker.test(input, expected, 467))

    # # # ----------------------- Do While Stmt ---------------
    # def test_467(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('a', IntegerType()),
    #             DoWhileStmt(
    #                 BinExpr('<', Id('a'), IntegerLit(10)),
    #                 BlockStmt([
    #                     VarDecl('a', BooleanType())
    #                 ])
    #             )
    #         ]))
    #     ])
    #     expected = str([])
    #     self.assertTrue(TestChecker.test(input, expected, 467))

    # def test_468(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('a', IntegerType()),
    #             DoWhileStmt(
    #                 FloatLit(1.2),
    #                 BlockStmt([])
    #             )
    #         ]))
    #     ])
    #     expected = str(TypeMismatchInExpression(FloatLit(1.2)))
    #     self.assertTrue(TestChecker.test(input, expected, 468))

    # # # # -------------------- BREAK CONTINUE -----------------
    # def test_469(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('a', IntegerType()),
    #             DoWhileStmt(
    #                 BooleanLit(True),
    #                 BlockStmt([])
    #             ),
    #             ContinueStmt()
    #         ]))
    #     ])
    #     expected = str(MustInLoop(ContinueStmt()))
    #     self.assertTrue(TestChecker.test(input, expected, 469))

    # def test_470(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('i', IntegerType()),
    #             ForStmt(
    #                 AssignStmt(Id('i'), IntegerLit(0)),
    #                 BinExpr('<', Id('i'), IntegerLit(10)),
    #                 BinExpr('+', Id('i'), IntegerLit(1)),
    #                 BlockStmt([BreakStmt()])
    #             ),
    #         ]))
    #     ])
    #     expected = str([])
    #     self.assertTrue(TestChecker.test(input, expected, 470))

    # def test_471(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('i', IntegerType()),
    #             ForStmt(
    #                 AssignStmt(Id('i'), IntegerLit(0)),
    #                 BinExpr('<', Id('i'), IntegerLit(10)),
    #                 BinExpr('+', Id('i'), IntegerLit(1)),
    #                 BlockStmt([
    #                     IfStmt(BooleanLit(True), BreakStmt())
    #                 ])
    #             ),
    #         ]))
    #     ])
    #     expected = str([])
    #     self.assertTrue(TestChecker.test(input, expected, 471))

    # # # # ----------------- Array Lit ---------------------------
    # def test_472(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl(
    #                 'arr',
    #                 ArrayType([2], IntegerType()),
    #                 ArrayLit([IntegerLit(1), IntegerLit(2)])
    #             ),
    #         ]))
    #     ])
    #     expected = str([])
    #     self.assertTrue(TestChecker.test(input, expected, 472))

    # def test_473(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl(
    #                 'arr',
    #                 ArrayType([2], IntegerType()),
    #                 ArrayLit([IntegerLit(1), BooleanLit(True)])
    #             ),
    #         ]))
    #     ])
    #     expected = str(IllegalArrayLiteral(
    #         ArrayLit([IntegerLit(1), BooleanLit(True)])))
    #     self.assertTrue(TestChecker.test(input, expected, 473))

    # def test_474(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl(
    #                 'arr',
    #                 ArrayType([3], IntegerType()),
    #                 ArrayLit([IntegerLit(1), IntegerLit(1)])
    #             ),
    #         ]))
    #     ])
    #     expected = str(TypeMismatchInVarDecl(VarDecl(
    #         'arr',
    #         ArrayType([3], IntegerType()),
    #         ArrayLit([IntegerLit(1), IntegerLit(1)])
    #     )))
    #     self.assertTrue(TestChecker.test(input, expected, 474))

    # def test_475(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('arr', ArrayType([3], IntegerType())),
    #             AssignStmt(
    #                 Id('arr'),
    #                 ArrayLit([
    #                     IntegerLit(1),
    #                     IntegerLit(2),
    #                     IntegerLit(3),
    #                 ])
    #             )
    #         ]))
    #     ])
    #     expected = str([])
    #     self.assertTrue(TestChecker.test(input, expected, 475))

    # def test_476(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('arr', ArrayType([3], IntegerType())),
    #             AssignStmt(
    #                 Id('arr'),
    #                 ArrayLit([
    #                     IntegerLit(1),
    #                     IntegerLit(2),
    #                 ])
    #             )
    #         ]))
    #     ])
    #     expected = str(TypeMismatchInStatement(
    #         AssignStmt(
    #             Id('arr'),
    #             ArrayLit([
    #                 IntegerLit(1),
    #                 IntegerLit(2),
    #             ])
    #         )
    #     ))
    #     self.assertTrue(TestChecker.test(input, expected, 476))

    # def test_477(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('arr', ArrayType([1], IntegerType())),
    #             AssignStmt(
    #                 Id('arr'),
    #                 ArrayLit([
    #                     FloatLit(1),
    #                 ])
    #             )
    #         ]))
    #     ])
    #     expected = str(TypeMismatchInStatement(
    #         AssignStmt(
    #             Id('arr'),
    #             ArrayLit([
    #                 FloatLit(1),
    #             ])
    #         )
    #     ))
    #     self.assertTrue(TestChecker.test(input, expected, 477))

    # def test_478(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('arr', ArrayType([2, 2], IntegerType())),
    #             AssignStmt(
    #                 Id('arr'),
    #                 ArrayLit([
    #                     ArrayLit([
    #                         IntegerLit(1),
    #                         IntegerLit(1),
    #                     ]),
    #                     ArrayLit([
    #                         IntegerLit(1),
    #                         IntegerLit(1),
    #                     ])
    #                 ])
    #             )
    #         ]))
    #     ])
    #     expected = str([])
    #     self.assertTrue(TestChecker.test(input, expected, 478))

    # def test_479(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('arr', ArrayType([2, 2], IntegerType())),
    #             AssignStmt(
    #                 Id('arr'),
    #                 ArrayLit([
    #                     ArrayLit([
    #                         IntegerLit(1),
    #                         IntegerLit(1),
    #                     ]),
    #                     ArrayLit([
    #                         ArrayLit([
    #                             IntegerLit(1),
    #                             IntegerLit(1),
    #                         ]),
    #                         ArrayLit([
    #                             IntegerLit(1),
    #                             IntegerLit(1),
    #                         ])
    #                     ])
    #                 ])
    #             )
    #         ]))
    #     ])
    #     expected = str(IllegalArrayLiteral(
    #         ArrayLit([
    #             ArrayLit([
    #                 IntegerLit(1),
    #                 IntegerLit(1),
    #             ]),
    #             ArrayLit([
    #                 ArrayLit([
    #                     IntegerLit(1),
    #                     IntegerLit(1),
    #                 ]),
    #                 ArrayLit([
    #                     IntegerLit(1),
    #                     IntegerLit(1),
    #                 ])
    #             ])
    #         ])
    #     ))
    #     self.assertTrue(TestChecker.test(input, expected, 479))

    # # # # -------------------- Funcall --------------------
    # def test_480(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('arr', IntegerType(), FuncCall('foo', []))
    #         ])),
    #         FuncDecl('foo', IntegerType(), [], None, BlockStmt([])),
    #     ])
    #     expected = str([])
    #     self.assertTrue(TestChecker.test(input, expected, 480))

    # def test_481(self):
    #     input = Program([
    #         FuncDecl('abc', VoidType(), [], None, BlockStmt([])),
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('arr', IntegerType(), FuncCall('foo', []))
    #         ]))
    #     ])
    #     expected = str(Undeclared(Function(), 'foo'))
    #     self.assertTrue(TestChecker.test(input, expected, 481))

    # def test_482(self):
    #     input = Program([
    #         VarDecl('abc', IntegerType()),
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('arr', IntegerType(), FuncCall('abc', []))
    #         ])),
    #     ])
    #     expected = str(Undeclared(Function(), 'abc'))
    #     self.assertTrue(TestChecker.test(input, expected, 482))

    # def test_483(self):
    #     input = Program([
    #         FuncDecl(
    #             'add',
    #             IntegerType(),
    #             [
    #                 ParamDecl('x', IntegerType()),
    #                 ParamDecl('y', IntegerType()),
    #             ],
    #             None,
    #             BlockStmt([])
    #         ),
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('a', IntegerType()),
    #             VarDecl('arr', IntegerType(), FuncCall(
    #                 'add', [Id('a'), IntegerLit(20)]))
    #         ])),
    #     ])
    #     expected = str([])
    #     self.assertTrue(TestChecker.test(input, expected, 483))

    # def test_484(self):
    #     input = Program([
    #         FuncDecl(
    #             'add',
    #             IntegerType(),
    #             [
    #                 ParamDecl('x', IntegerType()),
    #                 ParamDecl('y', IntegerType()),
    #             ],
    #             None,
    #             BlockStmt([])
    #         ),
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('a', FloatType()),
    #             VarDecl(
    #                 'arr',
    #                 IntegerType(),
    #                 FuncCall(
    #                     'add', [Id('a'), IntegerLit(20)]
    #                 )
    #             )
    #         ])),
    #     ])
    #     expected = str(TypeMismatchInExpression(Id('a')))
    #     self.assertTrue(TestChecker.test(input, expected, 484))

    # def test_485(self):
    #     input = Program([
    #         FuncDecl(
    #             'add',
    #             IntegerType(),
    #             [
    #                 ParamDecl('x', IntegerType()),
    #                 ParamDecl('y', AutoType()),
    #             ],
    #             None,
    #             BlockStmt([])
    #         ),
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl(
    #                 'arr',
    #                 IntegerType(),
    #                 FuncCall(
    #                     'add', [IntegerLit(1), StringLit('arr')]
    #                 )
    #             )
    #         ])),
    #     ])
    #     expected = str([])
    #     self.assertTrue(TestChecker.test(input, expected, 485))

    # # # # -------------------- ARRAY CELL -----------------------
    # def test_486(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('arr', ArrayType([3], IntegerType())),
    #             AssignStmt(ArrayCell('arr', [IntegerLit(2)]), IntegerLit(1))
    #         ])),
    #     ])
    #     expected = str([])
    #     self.assertTrue(TestChecker.test(input, expected, 486))

    # def test_487(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('arr', ArrayType([3, 2], IntegerType())),
    #             AssignStmt(
    #                 ArrayCell('arr', [IntegerLit(2), FloatLit(3.0)]), IntegerLit(1))
    #         ])),
    #     ])
    #     expected = str(TypeMismatchInExpression(FloatLit(3.0)))
    #     self.assertTrue(TestChecker.test(input, expected, 487))

    # def test_488(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('arr', ArrayType([1], IntegerType())),
    #             AssignStmt(
    #                 ArrayCell('arr', [IntegerLit(2), IntegerLit(3)]), IntegerLit(1))
    #         ])),
    #     ])
    #     expected = str(
    #         TypeMismatchInExpression(
    #             ArrayCell('arr', [IntegerLit(2), IntegerLit(3)])
    #         )
    #     )
    #     self.assertTrue(TestChecker.test(input, expected, 488))

    # # # # ------------------- CALL STMT -------------------------------
    # def test_489(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             CallStmt('foo', [])
    #         ])),
    #         FuncDecl('foo', IntegerType(), [], None, BlockStmt([])),
    #     ])
    #     expected = str([])
    #     self.assertTrue(TestChecker.test(input, expected, 489))

    # def test_490(self):
    #     input = Program([
    #         FuncDecl(
    #             'mul',
    #             IntegerType(),
    #             [
    #                 ParamDecl('x', IntegerType()),
    #                 ParamDecl('y', IntegerType()),
    #             ],
    #             None,
    #             BlockStmt([])
    #         ),
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             CallStmt('mul', [IntegerLit(30), IntegerLit(10)])
    #         ])),
    #     ])
    #     expected = str([])
    #     self.assertTrue(TestChecker.test(input, expected, 490))

    # # # # -------------------- INHERIT FUNCTION ----------------------
    # def test_490(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([])),
    #         FuncDecl('parent', VoidType(), [], None, BlockStmt([])),
    #         FuncDecl('child', VoidType(), [], 'parent', BlockStmt([])),
    #     ])
    #     expected = str([])
    #     self.assertTrue(TestChecker.test(input, expected, 490))

    # def test_491(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([])),
    #         FuncDecl('child', VoidType(), [], 'parent', BlockStmt([])),
    #     ])
    #     expected = str(Undeclared(Function(), 'parent'))
    #     self.assertTrue(TestChecker.test(input, expected, 491))

    # def test_492(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([])),
    #         FuncDecl('child', VoidType(), [
    #             ParamDecl('x', IntegerType())
    #         ], 'parent', BlockStmt([])),
    #         FuncDecl('parent', VoidType(), [
    #             ParamDecl('x', IntegerType(), False, True)
    #         ], None, BlockStmt([])),
    #     ])
    #     expected = str(Invalid(Parameter(), 'x'))
    #     self.assertTrue(TestChecker.test(input, expected, 492))

    # # # # # ---------------------- FIRST STATEMENT ------------------
    # def test_493(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([])),
    #         FuncDecl('child', VoidType(), [], 'parent', BlockStmt([
    #             CallStmt('preventDefault', [])
    #         ])),
    #         FuncDecl('parent', VoidType(), [], None, BlockStmt([])),
    #     ])
    #     expected = str([])
    #     self.assertTrue(TestChecker.test(input, expected, 493))

    # def test_494(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([])),
    #         FuncDecl('child', VoidType(), [], 'parent', BlockStmt([
    #             CallStmt('super', [IntegerLit(1)])
    #         ])),
    #         FuncDecl('parent', VoidType(), [
    #             ParamDecl('x', IntegerType(), False, True)
    #         ], None, BlockStmt([])),
    #     ])
    #     expected = str([])
    #     self.assertTrue(TestChecker.test(input, expected, 494))

    # def test_495(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([])),
    #         FuncDecl('child', VoidType(), [], 'parent', BlockStmt([
    #             CallStmt('super', [FloatLit(1.0)]),
    #             VarDecl('a', IntegerType()),
    #         ])),
    #         FuncDecl('parent', VoidType(), [
    #             ParamDecl('x', IntegerType(), False, True)
    #         ], None, BlockStmt([])),
    #     ])
    #     expected = str(TypeMismatchInExpression(FloatLit(1.0)))
    #     self.assertTrue(TestChecker.test(input, expected, 495))

    # def test_496(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([])),
    #         FuncDecl('child', VoidType(), [], 'parent', BlockStmt([
    #             VarDecl('a', IntegerType()),
    #             CallStmt('preventDefault', [])
    #         ])),
    #         FuncDecl('parent', VoidType(), [], None, BlockStmt([])),
    #     ])
    #     expected = str(InvalidStatementInFunction('child'))
    #     self.assertTrue(TestChecker.test(input, expected, 496))

    # def test_497(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([])),
    #         FuncDecl('child', VoidType(), [], 'parent', BlockStmt([
    #             CallStmt('super', []),
    #             VarDecl('a', IntegerType()),
    #         ])),
    #         FuncDecl('parent', VoidType(), [], None, BlockStmt([])),
    #     ])
    #     expected = str(InvalidStatementInFunction('child'))
    #     self.assertTrue(TestChecker.test(input, expected, 497))

    # def test_498(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([])),
    #         FuncDecl('child', VoidType(), [], 'parent', BlockStmt([
    #             CallStmt('preventDefault', []),
    #             AssignStmt(
    #                 Id('x'),
    #                 BinExpr('+', IntegerLit(1), IntegerLit(2))
    #             )
    #         ])),
    #         FuncDecl('parent', VoidType(), [
    #             ParamDecl('x', IntegerType(), False, True)
    #         ], None, BlockStmt([])),
    #     ])
    #     expected = str([])
    #     self.assertTrue(TestChecker.test(input, expected, 498))

    # def test_499(self):
    #     input = Program([
    #         FuncDecl('parent', VoidType(), [], None, BlockStmt([])),
    #     ])
    #     expected = str(NoEntryPoint())
    #     self.assertTrue(TestChecker.test(input, expected, 499))

    # def test_500(self):
    #     input = Program([
    #         FuncDecl('child', VoidType(), [], 'parent', BlockStmt([
    #             CallStmt('preventDefault', []),
    #             AssignStmt(
    #                 Id('x'),
    #                 BinExpr('+', Id('x'), Id('x'))
    #             )
    #         ])),
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([])),
    #         FuncDecl('parent', VoidType(), [
    #             ParamDecl('x', IntegerType())
    #         ], None, BlockStmt([])),
    #     ])
    #     expected = str(Undeclared(Variable(), 'x'))
    #     self.assertTrue(TestChecker.test(input, expected, 500))
