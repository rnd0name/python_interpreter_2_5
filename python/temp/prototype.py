__version__='1.2.5'

import math
import random
import importlib

def check_if_var(to_check, int_ = 1):
    ret = to_check
    ret = variables[ret] if ret in variables else int(ret) if type(ret) == str and ret.isdigit() and int_ else ret
    return ret

def add(values):
    try :
        return check_if_var(values[0]) + check_if_var(values[1])
    except TypeError :
        global target_line, current_line
        print(f'Error on line {current_line} : can not add \'{values[1]}\' to \'{values[0]}\'')
        target_line = 'EOF'

def substract(values):
    try :
        return check_if_var(values[0]) - check_if_var(values[1])
    except TypeError :
        global target_line, current_line
        print(f'Error on line {current_line} : can not substract \'{values[1]}\' to \'{values[0]}\'')
        target_line = 'EOF'

def mult(values):
    try :
        return check_if_var(values[0]) * check_if_var(values[1])
    except TypeError :
        global target_line, current_line
        print(f'Error on line {current_line} : can not multiply \'{values[0]}\' by \'{values[1]}\'')
        target_line = 'EOF'

def div(values):
    try :
        return check_if_var(values[0]) / check_if_var(values[1])
    except TypeError :
        global target_line, current_line
        print(f'Error on line {current_line} : can not divid \'{values[0]}\' by \'{values[1]}\'')
        target_line = 'EOF'

def exposant(values):
    try :
        return check_if_var(values[0])**check_if_var(values[1])
    except TypeError :
        global target_line, current_line
        print(f'Error on line {current_line} : can not raise \'{values[0]}\' to the power of \'{values[1]}\'')
        target_line = 'EOF'

def prt(args):
    global defaultnone
    output=defaultnone
    for arg in args:
        if arg in variables :
            arg = variables[arg]
        if output==defaultnone:
            output=f'{str(arg).strip()}'
        else:
            output=f'{output} {str(arg).strip()}'
    print(output) if output != defaultnone else print()

def inpt(args) :
    global defaultnone
    output=defaultnone
    for arg in args:
        if arg in variables :
            arg = variables[arg]
        if output==defaultnone:
            output=f'{str(arg).strip()}'
        else:
            output=f'{output} {str(arg).strip()}'
    return input(output) if output != defaultnone else input()

def lprt(args) :
    global defaultnone
    output=defaultnone
    for arg in args:
        if arg in variables :
            arg = variables[arg]
        if output==defaultnone:
            output=f'{str(arg).strip()}'
        else:
            output=f'{output} {str(arg).strip()}'
    print(output, end=' ') if output != defaultnone else None

def sqrt(values):
    try :
        value = values
        return math.sqrt(check_if_var(value))
    except TypeError :
        global target_line, current_line
        print(f'Error on line {current_line} : can not find the square root of {value}')
        target_line = 'EOF'

def c_abs(values):
    try :
        value = values
        return abs(check_if_var(value))
    except TypeError :
        global target_line, current_line
        print(f'Error on line {current_line} : can not find the absolute value of {value}')
        target_line = 'EOF'

def rad(values):
    try :
        value = values
        return math.radians(check_if_var(value))
    except TypeError :
        global target_line, current_line
        print(f'Error on line {current_line} : can not find the value in radiant of {value}')
        target_line = 'EOF'

def deg(values):
    try :
        value = values
        return math.degrees(check_if_var(value))
    except TypeError :
        global target_line, current_line
        print(f'Error on line {current_line} : can not find the value in degree of {value}')
        target_line = 'EOF'

def radsin(values):
    try :
        value = values
        return math.sin(check_if_var(value))
    except TypeError :
        global target_line, current_line
        print(f'Error on line {current_line} : can not find the sin of {value} radiant')
        target_line = 'EOF'

def degsin(values):
    try :
        value = values
        return math.sin(math.radians(check_if_var(value)))
    except TypeError :
        global target_line, current_line
        print(f'Error on line {current_line} : can not find the sin of {value} degree')
        target_line = 'EOF'

def radcos(values):
    try :
        value = values
        return math.cos(check_if_var(value))
    except TypeError :
        global target_line, current_line
        print(f'Error on line {current_line} : can not find the cosin of {value} radiant')
        target_line = 'EOF'

def degcos(values):
    try :
        value = values
        return math.cos(math.radians(check_if_var(value)))
    except TypeError :
        global target_line, current_line
        print(f'Error on line {current_line} : can not find the cosin of {value} degree')
        target_line = 'EOF'

def rnd(values):
    try :
        return random.randint(check_if_var(values[0]), check_if_var(values[1]))
    except TypeError :
        global target_line, current_line
        print(f'Error on line {current_line} : can not find a random integer between {values[0]} and {values[1]}')
        target_line = 'EOF'

def rnd01():
    return random.randint(0,100000)/100000


def c_import(package) :
    try :
        global command_all, command0, command1, command2, command3, command4, command_any, variables
        m = importlib.import_module(f'extensions.{package}')
        command_all, command0, command1, command2, command3, command4, command_any, variables = m.init_module(command_all, command0, command1, command2, command3, command4, command_any, variables)
        globals().update({name: getattr(m, name) for name in m.__all__})
        variables['__*packages*__'].append(package)
        del m
    except ModuleNotFoundError :
        global target_line, current_line
        print(f'Error on line {current_line} : can not find a module named : {package}')
        target_line = 'EOF'

def run(file) :
    global run_var
    run_var = file

def repl() :
    rep = ''
    while rep != 'exit' :
        rep = input('>>  ')
        if not rep == 'exit' :
            interpret_line(rep)
    pause()

def pause() :
    if input() == 'repl' :
        repl()
    else :
        print('Bye.')

def var(values) :
    var_name,var_value = values
    var_value = check_if_var(var_value, 1)
    var_value = var_value.strip() if type(var_value) == str else var_value
    variables[var_name]=var_value

def del_(values) :
    var = values[0]
    variables.pop(var, None)

def jmp(values):
    var1, operator, var2, line = values
    global target_line
    var1 = check_if_var(var1)
    var2 = check_if_var(var2)
    line = check_if_var(line)
    if evaluate_condition(var1,operator, var2) :
        if type(line) == int :
            target_line = int(line) - 1
        elif line.strip() == 'EOF' :
            target_line = 'EOF'

imports = []

variables = {'pi': math.pi ,
             'e': math.e ,
             '__*None*__' :  '__*None*__' ,
             '__*packages*__' : [],
             '__*vesion*__' : __version__
}

variables['__*variables*__'] = variables

defaultnone='__*None*__'


command0={
    'rnd01'      : rnd01      ,
    'repl'       : repl       ,
    'pause'      : pause
}

command1={
    'sqrt'       : sqrt       ,
    'abs'        : c_abs      ,
    'rad'        : rad        ,
    'deg'        : deg        ,
    'radsin'     : radsin     ,
    'degsin'     : degsin     ,
    'radcos'     : radcos     ,
    'degcos'     : degcos     ,
    'import'     : c_import   ,
    'run'        : run
}

command2={
    '+'          : add        ,
    '-'          : substract  ,
    '*'          : mult       ,
    '/'          : div        ,
    '**'         : exposant   ,
    '='          : var        ,
    'rnd'        : rnd        
}

command3={

}

command4={
    'jmp'       : jmp         ,
}

command_any={
    'prt'        : prt        ,
    'inpt'       : inpt       ,
    'lprt'       : lprt

}

command_all={
    '+'          : add        ,
    '-'          : substract  ,
    '*'          : mult       ,
    '/'          : div        ,
    '**'         : exposant   ,
    'prt'        : prt        ,
    'inpt'       : inpt       ,
    'lprt'       : lprt       ,
    'sqrt'       : sqrt       ,
    'abs'        : c_abs      ,
    'rad'        : rad        ,
    'deg'        : deg        ,
    'radsin'     : radsin     ,
    'degsin'     : degsin     ,
    'radcos'     : radcos     ,
    'degcos'     : degcos     ,
    'rnd'        : rnd        ,
    'rnd01'      : rnd01      ,
    'import'     : c_import   ,
    'run'        : run        ,
    'repl'       : repl       ,
    'pause'      : pause      ,
    '='          : var        ,
    'del'        : del_       ,
    'jmp'        : jmp
}


def interpret_expression(expresion:str,expression_index:int, line:list):
    try :
        if expresion in command0:
            line[expression_index]=command0[expresion]()
            return line
        if expresion in command1:
            if line[expression_index+1] != None:
                line[expression_index]=command1[expresion](line[expression_index+1])
                del line[expression_index+1]
            return line
        if expresion in command2:
            if line[expression_index+2] != None:
                line[expression_index]=command2[expresion](line[expression_index+1:expression_index+3])
                del line[expression_index+1:expression_index+3]
            return line
        if expresion in command3:
            if line[expression_index+3] != None:
                line[expression_index]=command3[expresion](line[expression_index+1:expression_index+4])
                del line[expression_index+1:expression_index+4]
            return line
        if expresion in command4:
            if line[expression_index+4] != None:
                line[expression_index]=command4[expresion](line[expression_index+1:expression_index+5])
                del line[expression_index+1:expression_index+5]
            return line
        if expresion in command_any:
            line[expression_index]=command_any[expresion](line[expression_index+1::])
            del line[expression_index+1::]
            return line
    except IndexError :
        print(f'Expresion {expresion} missing argument(s).')
    return line

def evaluate_condition(var1, operator, var2):
    if isinstance(var1, str):
        var1 = variables.get(var1, var1)
    if isinstance(var2, str):
        var2 = variables.get(var2, var2)

    if isinstance(var1, str) and var1.isdigit():
        var1 = int(var1)
    if isinstance(var2, str) and var2.isdigit():
        var2 = int(var2)

    if operator == '==':
        return var1 == var2
    elif operator == '!=':
        return var1 != var2
    elif operator == '>':
        return var1 > var2
    elif operator == '<':
        return var1 < var2
    elif operator == '>=':
        return var1 >= var2
    elif operator == '<=':
        return var1 <= var2
    return False


def interpret_line(line:str):
    global target_line, run_var
    target_line, run_var = defaultnone, defaultnone
    line=line.split()
    if '@' in line :
        while '@' in line :
            i = line.index('@')
            line[i] = check_if_var(line[i+1])
            del line[i+1]
    if len(line) == 0 or line[0] == '#':
        return [defaultnone, defaultnone]
    bkslash_idx = None if not '\\' in line else line.index('\\')
    if bkslash_idx:
        line[bkslash_idx] = ' '
        for idx, x in enumerate(line):
            if idx > bkslash_idx:
                line[bkslash_idx]=str(line[bkslash_idx])+' '+str(line[idx])
        idx=len(line)-1
        while idx > bkslash_idx :
            del line[idx]
            idx -= 1
    index=len(line)-1
    while True:
        if line[index] in command_all:
            line=interpret_expression(expresion=line[index],expression_index=index,line=line)
            index=len(line)-1
        index-=1
        if index<0:
            if not line[0]in command0:
                break
        if len(line)==0:
            break

    return [target_line, run_var]


import sys

def interpret(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        i=0
        while i < len(lines):
            current_line = i+1
            line=str(lines[i].strip())
            ret = interpret_line(line=line)
            i += 1
            if ret[1] != defaultnone :
                interpret(ret[1])
            if ret[0] != defaultnone :
                if ret[0] == 'EOF' :
                    i = len(lines)
                if 0 <= ret[0] < len(lines):
                    i=ret[0]

current_line = 0

if len(sys.argv) > 1 :
    interpret(sys.argv[1])
else :
    interpret_line('repl')
