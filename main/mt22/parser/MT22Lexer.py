# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2=")
        buf.write("\u01c5\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\3\2\3\2\3\2\3\2\7")
        buf.write("\2\u0086\n\2\f\2\16\2\u0089\13\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\3\3\3\3\3\3\3\7\3\u0094\n\3\f\3\16\3\u0097\13\3\3\3\5")
        buf.write("\3\u009a\n\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3")
        buf.write("\16\3\16\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3 \3 \3")
        buf.write("!\3!\3\"\3\"\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3\'\3\'\3(")
        buf.write("\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60")
        buf.write("\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\65")
        buf.write("\3\65\3\65\7\65\u0160\n\65\f\65\16\65\u0163\13\65\3\65")
        buf.write("\5\65\u0166\n\65\3\66\3\66\7\66\u016a\n\66\f\66\16\66")
        buf.write("\u016d\13\66\3\67\3\67\5\67\u0171\n\67\3\67\6\67\u0174")
        buf.write("\n\67\r\67\16\67\u0175\38\38\38\38\38\38\38\38\38\38\3")
        buf.write("8\38\38\58\u0185\n8\38\38\39\39\59\u018b\n9\39\59\u018e")
        buf.write("\n9\3:\3:\3:\5:\u0193\n:\5:\u0195\n:\3;\3;\7;\u0199\n")
        buf.write(";\f;\16;\u019c\13;\3;\3;\3;\3<\3<\7<\u01a3\n<\f<\16<\u01a6")
        buf.write("\13<\3=\6=\u01a9\n=\r=\16=\u01aa\3=\3=\3>\3>\7>\u01b1")
        buf.write("\n>\f>\16>\u01b4\13>\3>\3>\3>\3?\3?\7?\u01bb\n?\f?\16")
        buf.write("?\u01be\13?\3?\3?\3?\3@\3@\3@\4\u0087\u0095\2A\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63")
        buf.write("\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-")
        buf.write("Y.[/]\60_\61a\62c\63e\64g\65i\66k\2m\2o\67q\2s\2u8w9y")
        buf.write(":{;}<\177=\3\2\16\3\3\f\f\3\2\62\62\3\2\63;\3\2aa\3\2")
        buf.write("\62;\4\2GGgg\4\2--//\n\2$$))^^ddhhppttvv\6\2\f\f\17\17")
        buf.write("$$^^\5\2C\\aac|\6\2\62;C\\aac|\5\2\n\f\16\17\"\"\2\u01d2")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2o\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y")
        buf.write("\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\3\u0081\3")
        buf.write("\2\2\2\5\u008f\3\2\2\2\7\u009d\3\2\2\2\t\u00a2\3\2\2\2")
        buf.write("\13\u00a8\3\2\2\2\r\u00b1\3\2\2\2\17\u00b8\3\2\2\2\21")
        buf.write("\u00bb\3\2\2\2\23\u00c0\3\2\2\2\25\u00c4\3\2\2\2\27\u00cd")
        buf.write("\3\2\2\2\31\u00d3\3\2\2\2\33\u00d6\3\2\2\2\35\u00da\3")
        buf.write("\2\2\2\37\u00dd\3\2\2\2!\u00e5\3\2\2\2#\u00eb\3\2\2\2")
        buf.write("%\u00f3\3\2\2\2\'\u00f9\3\2\2\2)\u0101\3\2\2\2+\u0108")
        buf.write("\3\2\2\2-\u010d\3\2\2\2/\u0112\3\2\2\2\61\u0117\3\2\2")
        buf.write("\2\63\u011d\3\2\2\2\65\u0120\3\2\2\2\67\u0123\3\2\2\2")
        buf.write("9\u0126\3\2\2\2;\u0129\3\2\2\2=\u012c\3\2\2\2?\u012e\3")
        buf.write("\2\2\2A\u0130\3\2\2\2C\u0132\3\2\2\2E\u0134\3\2\2\2G\u0136")
        buf.write("\3\2\2\2I\u0139\3\2\2\2K\u013c\3\2\2\2M\u013e\3\2\2\2")
        buf.write("O\u0140\3\2\2\2Q\u0142\3\2\2\2S\u0144\3\2\2\2U\u0146\3")
        buf.write("\2\2\2W\u0148\3\2\2\2Y\u014a\3\2\2\2[\u014c\3\2\2\2]\u014e")
        buf.write("\3\2\2\2_\u0150\3\2\2\2a\u0152\3\2\2\2c\u0154\3\2\2\2")
        buf.write("e\u0156\3\2\2\2g\u0158\3\2\2\2i\u0165\3\2\2\2k\u0167\3")
        buf.write("\2\2\2m\u016e\3\2\2\2o\u0184\3\2\2\2q\u018d\3\2\2\2s\u0194")
        buf.write("\3\2\2\2u\u0196\3\2\2\2w\u01a0\3\2\2\2y\u01a8\3\2\2\2")
        buf.write("{\u01ae\3\2\2\2}\u01b8\3\2\2\2\177\u01c2\3\2\2\2\u0081")
        buf.write("\u0082\7\61\2\2\u0082\u0083\7,\2\2\u0083\u0087\3\2\2\2")
        buf.write("\u0084\u0086\13\2\2\2\u0085\u0084\3\2\2\2\u0086\u0089")
        buf.write("\3\2\2\2\u0087\u0088\3\2\2\2\u0087\u0085\3\2\2\2\u0088")
        buf.write("\u008a\3\2\2\2\u0089\u0087\3\2\2\2\u008a\u008b\7,\2\2")
        buf.write("\u008b\u008c\7\61\2\2\u008c\u008d\3\2\2\2\u008d\u008e")
        buf.write("\b\2\2\2\u008e\4\3\2\2\2\u008f\u0090\7\61\2\2\u0090\u0091")
        buf.write("\7\61\2\2\u0091\u0095\3\2\2\2\u0092\u0094\13\2\2\2\u0093")
        buf.write("\u0092\3\2\2\2\u0094\u0097\3\2\2\2\u0095\u0096\3\2\2\2")
        buf.write("\u0095\u0093\3\2\2\2\u0096\u0099\3\2\2\2\u0097\u0095\3")
        buf.write("\2\2\2\u0098\u009a\t\2\2\2\u0099\u0098\3\2\2\2\u009a\u009b")
        buf.write("\3\2\2\2\u009b\u009c\b\3\2\2\u009c\6\3\2\2\2\u009d\u009e")
        buf.write("\7o\2\2\u009e\u009f\7c\2\2\u009f\u00a0\7k\2\2\u00a0\u00a1")
        buf.write("\7p\2\2\u00a1\b\3\2\2\2\u00a2\u00a3\7d\2\2\u00a3\u00a4")
        buf.write("\7t\2\2\u00a4\u00a5\7g\2\2\u00a5\u00a6\7c\2\2\u00a6\u00a7")
        buf.write("\7m\2\2\u00a7\n\3\2\2\2\u00a8\u00a9\7e\2\2\u00a9\u00aa")
        buf.write("\7q\2\2\u00aa\u00ab\7p\2\2\u00ab\u00ac\7v\2\2\u00ac\u00ad")
        buf.write("\7k\2\2\u00ad\u00ae\7p\2\2\u00ae\u00af\7w\2\2\u00af\u00b0")
        buf.write("\7g\2\2\u00b0\f\3\2\2\2\u00b1\u00b2\7t\2\2\u00b2\u00b3")
        buf.write("\7g\2\2\u00b3\u00b4\7v\2\2\u00b4\u00b5\7w\2\2\u00b5\u00b6")
        buf.write("\7t\2\2\u00b6\u00b7\7p\2\2\u00b7\16\3\2\2\2\u00b8\u00b9")
        buf.write("\7k\2\2\u00b9\u00ba\7h\2\2\u00ba\20\3\2\2\2\u00bb\u00bc")
        buf.write("\7g\2\2\u00bc\u00bd\7n\2\2\u00bd\u00be\7u\2\2\u00be\u00bf")
        buf.write("\7g\2\2\u00bf\22\3\2\2\2\u00c0\u00c1\7h\2\2\u00c1\u00c2")
        buf.write("\7q\2\2\u00c2\u00c3\7t\2\2\u00c3\24\3\2\2\2\u00c4\u00c5")
        buf.write("\7h\2\2\u00c5\u00c6\7w\2\2\u00c6\u00c7\7p\2\2\u00c7\u00c8")
        buf.write("\7e\2\2\u00c8\u00c9\7v\2\2\u00c9\u00ca\7k\2\2\u00ca\u00cb")
        buf.write("\7q\2\2\u00cb\u00cc\7p\2\2\u00cc\26\3\2\2\2\u00cd\u00ce")
        buf.write("\7y\2\2\u00ce\u00cf\7j\2\2\u00cf\u00d0\7k\2\2\u00d0\u00d1")
        buf.write("\7n\2\2\u00d1\u00d2\7g\2\2\u00d2\30\3\2\2\2\u00d3\u00d4")
        buf.write("\7f\2\2\u00d4\u00d5\7q\2\2\u00d5\32\3\2\2\2\u00d6\u00d7")
        buf.write("\7q\2\2\u00d7\u00d8\7w\2\2\u00d8\u00d9\7v\2\2\u00d9\34")
        buf.write("\3\2\2\2\u00da\u00db\7q\2\2\u00db\u00dc\7h\2\2\u00dc\36")
        buf.write("\3\2\2\2\u00dd\u00de\7k\2\2\u00de\u00df\7p\2\2\u00df\u00e0")
        buf.write("\7j\2\2\u00e0\u00e1\7g\2\2\u00e1\u00e2\7t\2\2\u00e2\u00e3")
        buf.write("\7k\2\2\u00e3\u00e4\7v\2\2\u00e4 \3\2\2\2\u00e5\u00e6")
        buf.write("\7c\2\2\u00e6\u00e7\7t\2\2\u00e7\u00e8\7t\2\2\u00e8\u00e9")
        buf.write("\7c\2\2\u00e9\u00ea\7{\2\2\u00ea\"\3\2\2\2\u00eb\u00ec")
        buf.write("\7k\2\2\u00ec\u00ed\7p\2\2\u00ed\u00ee\7v\2\2\u00ee\u00ef")
        buf.write("\7g\2\2\u00ef\u00f0\7i\2\2\u00f0\u00f1\7g\2\2\u00f1\u00f2")
        buf.write("\7t\2\2\u00f2$\3\2\2\2\u00f3\u00f4\7h\2\2\u00f4\u00f5")
        buf.write("\7n\2\2\u00f5\u00f6\7q\2\2\u00f6\u00f7\7c\2\2\u00f7\u00f8")
        buf.write("\7v\2\2\u00f8&\3\2\2\2\u00f9\u00fa\7d\2\2\u00fa\u00fb")
        buf.write("\7q\2\2\u00fb\u00fc\7q\2\2\u00fc\u00fd\7n\2\2\u00fd\u00fe")
        buf.write("\7g\2\2\u00fe\u00ff\7c\2\2\u00ff\u0100\7p\2\2\u0100(\3")
        buf.write("\2\2\2\u0101\u0102\7u\2\2\u0102\u0103\7v\2\2\u0103\u0104")
        buf.write("\7t\2\2\u0104\u0105\7k\2\2\u0105\u0106\7p\2\2\u0106\u0107")
        buf.write("\7i\2\2\u0107*\3\2\2\2\u0108\u0109\7x\2\2\u0109\u010a")
        buf.write("\7q\2\2\u010a\u010b\7k\2\2\u010b\u010c\7f\2\2\u010c,\3")
        buf.write("\2\2\2\u010d\u010e\7c\2\2\u010e\u010f\7w\2\2\u010f\u0110")
        buf.write("\7v\2\2\u0110\u0111\7q\2\2\u0111.\3\2\2\2\u0112\u0113")
        buf.write("\7v\2\2\u0113\u0114\7t\2\2\u0114\u0115\7w\2\2\u0115\u0116")
        buf.write("\7g\2\2\u0116\60\3\2\2\2\u0117\u0118\7h\2\2\u0118\u0119")
        buf.write("\7c\2\2\u0119\u011a\7n\2\2\u011a\u011b\7u\2\2\u011b\u011c")
        buf.write("\7g\2\2\u011c\62\3\2\2\2\u011d\u011e\7?\2\2\u011e\u011f")
        buf.write("\7?\2\2\u011f\64\3\2\2\2\u0120\u0121\7#\2\2\u0121\u0122")
        buf.write("\7?\2\2\u0122\66\3\2\2\2\u0123\u0124\7>\2\2\u0124\u0125")
        buf.write("\7?\2\2\u01258\3\2\2\2\u0126\u0127\7@\2\2\u0127\u0128")
        buf.write("\7?\2\2\u0128:\3\2\2\2\u0129\u012a\7<\2\2\u012a\u012b")
        buf.write("\7<\2\2\u012b<\3\2\2\2\u012c\u012d\7-\2\2\u012d>\3\2\2")
        buf.write("\2\u012e\u012f\7/\2\2\u012f@\3\2\2\2\u0130\u0131\7,\2")
        buf.write("\2\u0131B\3\2\2\2\u0132\u0133\7\61\2\2\u0133D\3\2\2\2")
        buf.write("\u0134\u0135\7\'\2\2\u0135F\3\2\2\2\u0136\u0137\7(\2\2")
        buf.write("\u0137\u0138\7(\2\2\u0138H\3\2\2\2\u0139\u013a\7~\2\2")
        buf.write("\u013a\u013b\7~\2\2\u013bJ\3\2\2\2\u013c\u013d\7?\2\2")
        buf.write("\u013dL\3\2\2\2\u013e\u013f\7#\2\2\u013fN\3\2\2\2\u0140")
        buf.write("\u0141\7>\2\2\u0141P\3\2\2\2\u0142\u0143\7@\2\2\u0143")
        buf.write("R\3\2\2\2\u0144\u0145\7<\2\2\u0145T\3\2\2\2\u0146\u0147")
        buf.write("\7\60\2\2\u0147V\3\2\2\2\u0148\u0149\7*\2\2\u0149X\3\2")
        buf.write("\2\2\u014a\u014b\7+\2\2\u014bZ\3\2\2\2\u014c\u014d\7]")
        buf.write("\2\2\u014d\\\3\2\2\2\u014e\u014f\7_\2\2\u014f^\3\2\2\2")
        buf.write("\u0150\u0151\7}\2\2\u0151`\3\2\2\2\u0152\u0153\7\177\2")
        buf.write("\2\u0153b\3\2\2\2\u0154\u0155\7.\2\2\u0155d\3\2\2\2\u0156")
        buf.write("\u0157\7=\2\2\u0157f\3\2\2\2\u0158\u0159\7$\2\2\u0159")
        buf.write("h\3\2\2\2\u015a\u0166\t\3\2\2\u015b\u0161\t\4\2\2\u015c")
        buf.write("\u015d\t\5\2\2\u015d\u0160\t\6\2\2\u015e\u0160\t\6\2\2")
        buf.write("\u015f\u015c\3\2\2\2\u015f\u015e\3\2\2\2\u0160\u0163\3")
        buf.write("\2\2\2\u0161\u015f\3\2\2\2\u0161\u0162\3\2\2\2\u0162\u0164")
        buf.write("\3\2\2\2\u0163\u0161\3\2\2\2\u0164\u0166\b\65\3\2\u0165")
        buf.write("\u015a\3\2\2\2\u0165\u015b\3\2\2\2\u0166j\3\2\2\2\u0167")
        buf.write("\u016b\7\60\2\2\u0168\u016a\t\6\2\2\u0169\u0168\3\2\2")
        buf.write("\2\u016a\u016d\3\2\2\2\u016b\u0169\3\2\2\2\u016b\u016c")
        buf.write("\3\2\2\2\u016cl\3\2\2\2\u016d\u016b\3\2\2\2\u016e\u0170")
        buf.write("\t\7\2\2\u016f\u0171\t\b\2\2\u0170\u016f\3\2\2\2\u0170")
        buf.write("\u0171\3\2\2\2\u0171\u0173\3\2\2\2\u0172\u0174\t\6\2\2")
        buf.write("\u0173\u0172\3\2\2\2\u0174\u0175\3\2\2\2\u0175\u0173\3")
        buf.write("\2\2\2\u0175\u0176\3\2\2\2\u0176n\3\2\2\2\u0177\u0178")
        buf.write("\5i\65\2\u0178\u0179\5k\66\2\u0179\u017a\5m\67\2\u017a")
        buf.write("\u0185\3\2\2\2\u017b\u017c\5i\65\2\u017c\u017d\5k\66\2")
        buf.write("\u017d\u0185\3\2\2\2\u017e\u017f\5i\65\2\u017f\u0180\5")
        buf.write("m\67\2\u0180\u0185\3\2\2\2\u0181\u0182\5k\66\2\u0182\u0183")
        buf.write("\5m\67\2\u0183\u0185\3\2\2\2\u0184\u0177\3\2\2\2\u0184")
        buf.write("\u017b\3\2\2\2\u0184\u017e\3\2\2\2\u0184\u0181\3\2\2\2")
        buf.write("\u0185\u0186\3\2\2\2\u0186\u0187\b8\4\2\u0187p\3\2\2\2")
        buf.write("\u0188\u018a\7^\2\2\u0189\u018b\t\t\2\2\u018a\u0189\3")
        buf.write("\2\2\2\u018b\u018e\3\2\2\2\u018c\u018e\n\n\2\2\u018d\u0188")
        buf.write("\3\2\2\2\u018d\u018c\3\2\2\2\u018er\3\2\2\2\u018f\u0190")
        buf.write("\7^\2\2\u0190\u0195\n\t\2\2\u0191\u0193\t\n\2\2\u0192")
        buf.write("\u0191\3\2\2\2\u0193\u0195\3\2\2\2\u0194\u018f\3\2\2\2")
        buf.write("\u0194\u0192\3\2\2\2\u0195t\3\2\2\2\u0196\u019a\5g\64")
        buf.write("\2\u0197\u0199\5q9\2\u0198\u0197\3\2\2\2\u0199\u019c\3")
        buf.write("\2\2\2\u019a\u0198\3\2\2\2\u019a\u019b\3\2\2\2\u019b\u019d")
        buf.write("\3\2\2\2\u019c\u019a\3\2\2\2\u019d\u019e\5g\64\2\u019e")
        buf.write("\u019f\b;\5\2\u019fv\3\2\2\2\u01a0\u01a4\t\13\2\2\u01a1")
        buf.write("\u01a3\t\f\2\2\u01a2\u01a1\3\2\2\2\u01a3\u01a6\3\2\2\2")
        buf.write("\u01a4\u01a2\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5x\3\2\2")
        buf.write("\2\u01a6\u01a4\3\2\2\2\u01a7\u01a9\t\r\2\2\u01a8\u01a7")
        buf.write("\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aa\u01a8\3\2\2\2\u01aa")
        buf.write("\u01ab\3\2\2\2\u01ab\u01ac\3\2\2\2\u01ac\u01ad\b=\2\2")
        buf.write("\u01adz\3\2\2\2\u01ae\u01b2\5g\64\2\u01af\u01b1\5q9\2")
        buf.write("\u01b0\u01af\3\2\2\2\u01b1\u01b4\3\2\2\2\u01b2\u01b0\3")
        buf.write("\2\2\2\u01b2\u01b3\3\2\2\2\u01b3\u01b5\3\2\2\2\u01b4\u01b2")
        buf.write("\3\2\2\2\u01b5\u01b6\5s:\2\u01b6\u01b7\b>\6\2\u01b7|\3")
        buf.write("\2\2\2\u01b8\u01bc\5g\64\2\u01b9\u01bb\5q9\2\u01ba\u01b9")
        buf.write("\3\2\2\2\u01bb\u01be\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bc")
        buf.write("\u01bd\3\2\2\2\u01bd\u01bf\3\2\2\2\u01be\u01bc\3\2\2\2")
        buf.write("\u01bf\u01c0\7\2\2\3\u01c0\u01c1\b?\7\2\u01c1~\3\2\2\2")
        buf.write("\u01c2\u01c3\13\2\2\2\u01c3\u01c4\b@\b\2\u01c4\u0080\3")
        buf.write("\2\2\2\26\2\u0087\u0095\u0099\u015f\u0161\u0165\u016b")
        buf.write("\u0170\u0175\u0184\u018a\u018d\u0192\u0194\u019a\u01a4")
        buf.write("\u01aa\u01b2\u01bc\t\b\2\2\3\65\2\38\3\3;\4\3>\5\3?\6")
        buf.write("\3@\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BLOCK_COMMENT = 1
    INLINE_COMMENT = 2
    MAIN = 3
    BREAK = 4
    CONTINUE = 5
    RETURN = 6
    IF = 7
    ELSE = 8
    FOR = 9
    FUNCTION = 10
    WHILE = 11
    DO = 12
    OUT = 13
    OF = 14
    INHERIT = 15
    ARRAY = 16
    INTEGER = 17
    FLOAT = 18
    BOOLEAN = 19
    STRING = 20
    VOID = 21
    AUTO = 22
    TRUE = 23
    FALSE = 24
    DOUBLE_EQUAL = 25
    NOT_EQUAL = 26
    LESS_EQUAL = 27
    GREATER_EQUAL = 28
    DOUBLE_COLON = 29
    ADD = 30
    SUB = 31
    MUL = 32
    DIV = 33
    MOD = 34
    AND = 35
    OR = 36
    EQUAL = 37
    NOT = 38
    LESS = 39
    GREATER = 40
    COLON = 41
    DOT = 42
    LP = 43
    RP = 44
    LSB = 45
    RSB = 46
    LCB = 47
    RCB = 48
    COMMA = 49
    SEMICOLON = 50
    DOUBLE_QUOTE = 51
    INTEGER_LIT = 52
    FLOAT_LIT = 53
    STRING_LIT = 54
    ID = 55
    WS = 56
    ILLEGAL_ESCAPE = 57
    UNCLOSE_STRING = 58
    ERROR_CHAR = 59

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'break'", "'continue'", "'return'", "'if'", "'else'", 
            "'for'", "'function'", "'while'", "'do'", "'out'", "'of'", "'inherit'", 
            "'array'", "'integer'", "'float'", "'boolean'", "'string'", 
            "'void'", "'auto'", "'true'", "'false'", "'=='", "'!='", "'<='", 
            "'>='", "'::'", "'+'", "'-'", "'*'", "'/'", "'%'", "'&&'", "'||'", 
            "'='", "'!'", "'<'", "'>'", "':'", "'.'", "'('", "')'", "'['", 
            "']'", "'{'", "'}'", "','", "';'", "'\"'" ]

    symbolicNames = [ "<INVALID>",
            "BLOCK_COMMENT", "INLINE_COMMENT", "MAIN", "BREAK", "CONTINUE", 
            "RETURN", "IF", "ELSE", "FOR", "FUNCTION", "WHILE", "DO", "OUT", 
            "OF", "INHERIT", "ARRAY", "INTEGER", "FLOAT", "BOOLEAN", "STRING", 
            "VOID", "AUTO", "TRUE", "FALSE", "DOUBLE_EQUAL", "NOT_EQUAL", 
            "LESS_EQUAL", "GREATER_EQUAL", "DOUBLE_COLON", "ADD", "SUB", 
            "MUL", "DIV", "MOD", "AND", "OR", "EQUAL", "NOT", "LESS", "GREATER", 
            "COLON", "DOT", "LP", "RP", "LSB", "RSB", "LCB", "RCB", "COMMA", 
            "SEMICOLON", "DOUBLE_QUOTE", "INTEGER_LIT", "FLOAT_LIT", "STRING_LIT", 
            "ID", "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    ruleNames = [ "BLOCK_COMMENT", "INLINE_COMMENT", "MAIN", "BREAK", "CONTINUE", 
                  "RETURN", "IF", "ELSE", "FOR", "FUNCTION", "WHILE", "DO", 
                  "OUT", "OF", "INHERIT", "ARRAY", "INTEGER", "FLOAT", "BOOLEAN", 
                  "STRING", "VOID", "AUTO", "TRUE", "FALSE", "DOUBLE_EQUAL", 
                  "NOT_EQUAL", "LESS_EQUAL", "GREATER_EQUAL", "DOUBLE_COLON", 
                  "ADD", "SUB", "MUL", "DIV", "MOD", "AND", "OR", "EQUAL", 
                  "NOT", "LESS", "GREATER", "COLON", "DOT", "LP", "RP", 
                  "LSB", "RSB", "LCB", "RCB", "COMMA", "SEMICOLON", "DOUBLE_QUOTE", 
                  "INTEGER_LIT", "DECIMAL_PART", "EXPONENT_PART", "FLOAT_LIT", 
                  "LEGAL_CHARATER", "ILLEGAL_CHARACTER", "STRING_LIT", "ID", 
                  "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[51] = self.INTEGER_LIT_action 
            actions[54] = self.FLOAT_LIT_action 
            actions[57] = self.STRING_LIT_action 
            actions[60] = self.ILLEGAL_ESCAPE_action 
            actions[61] = self.UNCLOSE_STRING_action 
            actions[62] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTEGER_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            				self.text = self.text.replace('_', '');
            			
     

    def FLOAT_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            		self.text = self.text.replace('_', '');
            	
     

    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	self.text = self.text[1:];
            	self.text = self.text[:-1];

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            	raise IllegalEscape(self.text[1:]);

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            	raise UncloseString(self.text[1:]);

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

            	raise ErrorToken(self.text);

     


