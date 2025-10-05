__version__='2.5'

import math
import random
import importlib

def check_if_var(to_check, int_ = 1):
    ret = to_check
    ret = variables[ret] if ret in variables else int(ret) if type(ret) == str and ret.isdigit() and int_ else ret
    return ret
def add(values):
    return check_if_var(values[0]) + check_if_var(values[1])

def substract(values):
    return check_if_var(values[0]) - check_if_var(values[1])

def mult(values):
    return check_if_var(values[0]) * check_if_var(values[1])

def div(values):
    return check_if_var(values[0]) / check_if_var(values[1])

def exposant(values):
    return check_if_var(values[0])**check_if_var(values[1])

def prt(args):
    global defaultnone
    output=defaultnone
    for arg in args:
        if arg in variables :
            arg = variables[arg]
        if output==defaultnone:
            output=f'{arg}'
        else:
            output=f'{output} {arg}'
    print(output) if output != defaultnone else print()

def inpt(args) :
    global defaultnone
    output=defaultnone
    for arg in args:
        if arg in variables :
            arg = variables[arg]
        if output==defaultnone:
            output=f'{arg}'
        else:
            output=f'{output} {arg}'
    return input(output) if output != defaultnone else input()

def lprt(args) :
    global defaultnone
    output=defaultnone
    for arg in args:
        if arg in variables :
            arg = variables[arg]
        if output==defaultnone:
            output=f'{arg}'
        else:
            output=f'{output} {arg}'
    print(output, end=' ') if output != defaultnone else None

def sqrt(values):
    value = values
    return math.sqrt(check_if_var(value))

def c_abs(values):
    value = values
    return abs(check_if_var(value))

def rad(values):
    value = values
    return math.radians(check_if_var(value))

def deg(values):
    value = values
    return math.degrees(check_if_var(value))

def radsin(values):
    value = values
    return math.sin(check_if_var(value))

def degsin(values):
    value = values
    return math.sin(math.radians(check_if_var(value)))

def radcos(values):
    value = values
    return math.cos(check_if_var(value))

def degcos(values):
    value = values
    return math.cos(math.radians(check_if_var(value)))

def rnd(values):
    return random.randint(check_if_var(values[0]), check_if_var(values[1]))

def rnd01():
    return random.randint(0,100000)/100000


def c_import(package) :
    global command_all, command0, command1, command2, command3, command4, command_any, variables
    m = importlib.import_module(f"extensions.{package}")
    command_all, command0, command1, command2, command3, command4, command_any, variables = m.init_module(command_all, command0, command1, command2, command3, command4, command_any, variables)
    globals().update({name: getattr(m, name) for name in m.__all__})
    del m

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
    variables[var_name]=var_value

def del_(values) :
    var = values[0]
    variables.pop(var, None)

def jmp(values):
    var1, operator, var2, line = values
    global target_line
    var1 = check_if_var(var1)
    var2 = check_if_var(var2)
    if evaluate_condition(var1,operator, var2) :
        target_line = int(line) - 1

imports = []

variables = {'pi': math.pi,
             'e' : math.e
}

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

def research_first_bakslash_in_list(line:list):
    return None if not '\\' in line else line.index("\\")


def interpret_line(line:str):
    global target_line, run_var
    target_line, run_var = defaultnone, defaultnone
    line=line.split()
    if "@" in line :
        while "@" in line :
            i = line.index("@")
            line[i] = check_if_var(line[i+1])
            del line[i+1]
    if len(line) == 0 or line[0] == '#':
        return [defaultnone, defaultnone]
    bkslash_idx = research_first_bakslash_in_list(line)
    if bkslash_idx:
        del line[bkslash_idx]
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
            line=str(lines[i].strip())
            ret = interpret_line(line=line)
            i += 1
            if ret[1] != defaultnone :
                interpret(ret[1])
            if ret[0] != defaultnone :
                if 0 <= ret[0] < len(lines):
                    i=ret[0]

if len(sys.argv) > 1 :
    interpret(sys.argv[1])
else :
    interpret_line('repl')
