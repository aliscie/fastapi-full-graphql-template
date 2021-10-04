from pyparsing import unicode


def printJ(d):
    from pygments import highlight
    from pygments.lexers.web import JsonLexer
    from pygments.formatters.terminal256 import Terminal256Formatter
    from pygments.style import Style
    from pygments.token import Token
    from collections import OrderedDict

    import json

    from pygments.styles import get_all_styles

    class MyStyle(Style):
        styles = {
            Token.String: 'ansiwhite ansibrightgreen',
            Token.Number: 'ansiwhite ansired',
            Token.Generic: 'ansiwhite ansibrightred',
            Token.Punctuation: 'ansiwhite ansiyellow',
            Token.Keyword: 'ansiwhite ansibrightred',
            Token.Literal: 'ansiwhite ansibrightred',
            Token.Operator: 'ansiwhite ansibrightyellow',

        }
    try:
        d = json.dumps(d, indent=10,default=str)
    except:
        d = str(d)

    print(highlight(
        d,
        lexer=JsonLexer(),
        formatter=Terminal256Formatter(style=MyStyle), ))