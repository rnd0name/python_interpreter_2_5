from turtle import *

var = {}
def check_if_var(to_check, int_ = 1) :
    ret = to_check
    ret = var[ret] if ret in var else int(ret) if type(ret) == str and ret.isdigit() and int_ else ret
    return ret

__all__= ["fd", "bk", "rt", "lt", "set_color", "set_speed"]

def init_module(command_all, command0, command1, command2, command3, command4, command_any, variables):
    global var
    var = variables
    command_all.update(all)
    command0.update(comm_0)
    command1.update(comm_1)
    command2.update(comm_2)
    command_any.update(comm_any)
    return command_all, command0, command1, command2, command3, command4, command_any, variables

def draw_goto(values) :
    goto(check_if_var(values[0]), check_if_var(values[1]))

def draw_fd(value) :
    forward(check_if_var(value))

def draw_bk(value) :
    forward(-check_if_var(value))

def draw_rt(value) :
    right(check_if_var(value))

def draw_lt(value) :
    left(check_if_var(value))

def set_color(values) :
    if len(values) > 1 :
        bgcolor(check_if_var(values[1]))
    pencolor(check_if_var(values[0]))

def set_speed(value) :
    speed(check_if_var(value))

def set_size(value) :
    pensize(check_if_var(value))

comm_0 = {
    'clear' : clear    ,
    'up'    : penup    ,
    'down'  : pendown
}
comm_1 = {
    'size'  : set_size ,
    'speed' : set_speed,
    'fd'    : draw_fd  ,
    'bk'    : draw_bk  ,
    'lt'    : draw_lt  ,
    'rt'    : draw_rt
}
comm_2 = {
    'goto'  : draw_goto
}
comm_any = {
    'color' : set_color
}
all = {
    'goto'  : draw_goto,
    'clear' : clear    ,
    'up'    : penup    ,
    'down'  : pendown  ,
    'size'  : set_size ,
    'speed' : set_speed,
    'fd'    : draw_fd  ,
    'bk'    : draw_bk  ,
    'lt'    : draw_lt  ,
    'rt'    : draw_rt  ,
    'color' : set_color
}