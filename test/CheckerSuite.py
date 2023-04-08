import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *


class CheckerSuite(unittest.TestCase):
    # def test_401(self):
    #     input = Program([VarDecl('x', IntegerType())])
    #     expected = """[]"""
    #     self.assertTrue(TestChecker.test(input, expected, 401))

    # def test_402(self):
    #     input = Program([VarDecl('x', IntegerType()),
    #                     VarDecl('y', IntegerType())])
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
    #     input = Program([VarDecl('a', IntegerType(), IntegerLit(1))])
    #     expected = str([])
    #     self.assertTrue(TestChecker.test(input, expected, 405))

    # def test_406(self):
    #     input = Program([VarDecl('a', IntegerType(), IntegerLit(
    #         1)), VarDecl('b', FloatType(), FloatLit(1.2))])
    #     expected = str([])
    #     self.assertTrue(TestChecker.test(input, expected, 406))

    # def test_407(self):
    #     input = Program([VarDecl('x', IntegerType(), IntegerLit(
    #         1)), VarDecl('x', FloatType(), FloatLit(3.4))])
    #     expected = str(Redeclared(Variable(), 'x'))
    #     self.assertTrue(TestChecker.test(input, expected, 407))

    # # # --------------------------IntegerLit thay FloatLit-------------------------

    # def test_408(self):
    #     input = Program([VarDecl('x', FloatType(), IntegerLit(1))])
    #     expected = str([])
    #     self.assertTrue(TestChecker.test(input, expected, 408))

    # def test_409(self):
    #     input = Program([VarDecl('x', IntegerType(), FloatLit(2.123))])
    #     expected = str(TypeMismatchInVarDecl(
    #         VarDecl('x', IntegerType(), FloatLit(2.123))))
    #     self.assertTrue(TestChecker.test(input, expected, 409))

    # # ---------------------- Check Auto Invalid ---------------------
    # def test_410(self):
    #     input = Program([VarDecl('x', AutoType())])
    #     expected = str(Invalid(Variable(), 'x'))
    #     self.assertTrue(TestChecker.test(input, expected, 410))

    # def test_411(self):
    #     input = Program([VarDecl('x', AutoType(), FloatLit(2.123))])
    #     expected = str([])
    #     self.assertTrue(TestChecker.test(input, expected, 411))

    # def test_412(self):
    #     input = Program([VarDecl('x', AutoType(), IntegerLit(0)),
    #                     VarDecl('y', AutoType(), FloatLit(2.123))])
    #     expected = str([])
    #     self.assertTrue(TestChecker.test(input, expected, 412))

    # def test_413(self):
    #     input = Program([VarDecl('a', AutoType(), IntegerLit(2)),
    #                     VarDecl('a', AutoType(), FloatLit(1.9))])
    #     expected = str(Redeclared(Variable(), 'a'))
    #     self.assertTrue(TestChecker.test(input, expected, 413))

    # # ------------------ Function Check - --------------------

    # def test_414(self):
    #     input = Program([FuncDecl('foo', VoidType(), [], None, BlockStmt([]))])
    #     expected = str([])
    #     self.assertTrue(TestChecker.test(input, expected, 414))

    # def test_415(self):
    #     input = Program([VarDecl('a', IntegerType()), FuncDecl(
    #         'b', VoidType(), [], None, BlockStmt([]))])
    #     expected = str([])
    #     self.assertTrue(TestChecker.test(input, expected, 415))

    # def test_416(self):
    #     input = Program([VarDecl('same', IntegerType()), FuncDecl(
    #         'same', VoidType(), [], None, BlockStmt([]))])
    #     expected = str(Redeclared(Function(), 'same'))
    #     self.assertTrue(TestChecker.test(input, expected, 416))

    # def test_416(self):
    #     input = Program([FuncDecl('a', VoidType(), [], None, BlockStmt([])), FuncDecl(
    #         'a', VoidType(), [], None, BlockStmt([])), FuncDecl('a', VoidType(), [], None, BlockStmt([]))])
    #     expected = str(Redeclared(Function(), 'a'))
    #     self.assertTrue(TestChecker.test(input, expected, 416))

    # # -------------------- Check Redeclared Param Scope ---------------------
    # def test_417(self):
    #     input = Program([
    #         FuncDecl('a', VoidType(),
    #                  [ParamDecl('a', IntegerType())], None, BlockStmt([])
    #                  )
    #     ])
    #     expected = str([])
    #     self.assertTrue(TestChecker.test(input, expected, 417))

    # def test_418(self):
    #     input = Program([
    #         FuncDecl('a', VoidType(),
    #                  [ParamDecl('x', IntegerType()),
    #                   ParamDecl('x', IntegerType())],
    #                  None, BlockStmt([])
    #                  )
    #     ])
    #     expected = str(Redeclared(Parameter(), 'x'))
    #     self.assertTrue(TestChecker.test(input, expected, 418))

    # def test_419(self):
    #     input = Program([
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

    # # --------------- Check Redclare In Block - -------------------

    # def test_420(self):
    #     input = Program([
    #         FuncDecl('a', VoidType(), [], None, BlockStmt([
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
    #         FuncDecl('b', VoidType(), [], None, BlockStmt([
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
    #         FuncDecl('c', VoidType(), [], None, BlockStmt([
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

    # # --------------- Check Assign Stmt - ----------------------

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

    # # -------------- If stmt - ----------------------------

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

    def test_436(self):
        input = Program([
            FuncDecl('main', VoidType(), [], None, BlockStmt([
                VarDecl('a', BooleanType(), BooleanLit(True)),
                IfStmt(
                    Id('a'),
                    BlockStmt([VarDecl('x', IntegerType())]),
                    BlockStmt([AssignStmt(Id('x'), IntegerLit(1))])
                )
            ]))
        ])
        expected = str(Undeclared(Variable(), 'x'))
        self.assertTrue(TestChecker.test(input, expected, 436))
