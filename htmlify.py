#!/usr/bin/env python
"""Apply HTML markup to a python file.

Watch out - there are bugs.
"""

import re,sys,cgi

keywords1 = ['assert','break','continue','del','elif','else','except',
             'exec','finally','from','global','import','lambda',
             'pass','print','raise','return','while','eval', 'SyntaxError',
             'TypeError', 'yield', 'as']

keywords2 = ['if','in','is','not','or','and', 'try', 'for', 'as']

builtin1 = ['int', 'str', 'float', 'bool', 'type', 'help', 'len', 'range',
            'open', 'dict', 'repr', 'raw_input', 'iter', 'next', 'xrange',
            'all', 'any', 'enumerate']
builtin2 = ['True', 'False', 'None', 'help', 'object', 'Exception', 'ValueError',
            'ZeroDivisionError', 'NameError', 'SyntaxError', 'StopIteration']

matcher = re.compile(r"""
            \"\"\".*?\"\"\" |
            '[^']*?' |   # '
            "[^"]*?" |   # "
            \#.*?$|
            ^:.*?$ |
            !!!.*?!!! |
            \sand\s |
            assert |
            break |
            ^class [^:(]*[:(] |
            continue |
            def [^:(]*[:(]|
            del |
            elif |
            else |
            except |
            exec |
            finally |
            \sfor\s |
            from |
            global |
            \sif\s |
            import |
            \sin\s |
            \sis\s |
            lambda |
            \snot\s |
            \sor\s |
            pass |
            print |
            raise |
            return |
            yield |
            SyntaxError |
            TypeError |
            StopIteration |
            \stry: |
	    as |
            while |
            eval |
            object |
            xrange\( |
            enumerate\( |
            int\( |
            str\( |
            all\( |
            any \( |
            float\( |
            bool\( |
            type\( |
            len\( |
            range\( |
            raw_input\( |
            iter\( |
            next\( |
            help\( |
            open\( |
            dict\( |
            repr\( |
            True |
            False |
            None |
            Exception |
            ValueError | 
            ZeroDivisionError | 
            NameError |
            SyntaxError |
            &gt;&gt;&gt;
            """, re.VERBOSE | re.DOTALL | re.MULTILINE)  # "

defclassmatch = re.compile(r"(class|def) (.*[:(])")
deftypematch = re.compile(r"<type([^>]*)>")

tagmatch = re.compile(r"<|>")

def tagrepl(matchobj):
    text = matchobj.group(0)
    if text[0] == '<':
        return "&lt;"
    else:
        return "&gt;"

def repl(matchobj):
    text = matchobj.group(0)
    if text[:3] == '"""':           # "
        return '<span class="string">'+re.sub(tagmatch, tagrepl, text)+'</span>'
    elif text[0] == ':':
        typem = re.match(deftypematch, text[1:])
        if typem:
            return '<span class="result">&lt;type'+typem.group(1)+'&gt;</span>'
        else:
            return '<span class="result">'+text[1:]+'</span>'
    elif text[0] == '#':
        return '<span class="comment">'+text+'</span>'
    elif text == '&gt;&gt;&gt;':
        return '<span class="prompt">&gt;&gt;&gt;</span>'
    elif text[0] == "'":
        return '<span class="string">'+re.sub(tagmatch, tagrepl, text)+'</span>'
    elif text[0] == '"':
        return '<span class="string">'+re.sub(tagmatch, tagrepl, text)+'</span>'
    elif text in keywords1:
        return '<span class="keyword">'+text+'</span>'
    elif text[1:-1] in keywords2:
        return '<span class="keyword">'+text+'</span>'
    elif text[:-1] in builtin1:
        return '<span class="builtin">'+text[:-1]+'</span>'+text[-1]
    elif text in builtin2:
        return '<span class="builtin">'+text+'</span>'
    elif text[:5] == 'class':
        f = re.search(defclassmatch,text).group(2)
        return '<span class="keyword">class</span> <span class="classordef">'+f[:-1]+'</span>'+f[-1]
    elif text[:3] == 'def':
        f = re.search(defclassmatch,text).group(2)
        return '<span class="keyword">def</span> <span class="classordef">'+f[:-1]+'</span>'+f[-1]
    elif text[:3] == '!!!':
        transstr = re.sub(tagmatch, tagrepl, text[3:-3].rstrip(' '))
        return '<span class="error">'+transstr+'</span>'	
    else:
        return ''
    
def htmlify(text):
    return re.sub(matcher, repl, cgi.escape(text))
                     

if  __name__ == '__main__':
    argc = len(sys.argv)
    if argc >= 2:
        f = open(sys.argv[1], 'rU')
    else:
        f = sys.stdin
    output = htmlify(f.read().strip())
    print "<pre>"
    print output
    print "</pre>"
    #for i in f:
    #    print htmlify(i),
    f.close()
   
