import re

def comment_remover(text):
    def replacer(match):
        s = match.group(0)
        if s.startswith('/'):
            return ""
        else:
            return s
    p = re.compile(
        r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"',
        re.S | re.M
    )
    return re.sub(p, replacer, text)

def emptyline_remover(text):
    return '\n'.join([l.strip() for l in text.split('\n') if l.strip() != ""])

def multiple_space_remover(text):
    return re.sub(r'\s{2,}', ' ', text)

def get_clear_file(data):
    data = comment_remover(data)
    data = emptyline_remover(data)
    data = multiple_space_remover(data)
    data, defined_macro = define_remover(data)
    return data, defined_macro

# todo 
def define_remover(text):
    p = re.compile(r'#\s?define\s?.+')
    m = p.findall(text)    
    if m:
        return re.sub(p, '', text), sorted(m)

# fname = 'header2.h'
# data = open('header2.h').read()
data1, data1_def = get_clear_file(open('header1.h').read())
data2, data2_def = get_clear_file(open('header2.h').read())

print('=======')
print(data1)
print('=======')
print(data1==data2)
print(data1_def==data2_def)


