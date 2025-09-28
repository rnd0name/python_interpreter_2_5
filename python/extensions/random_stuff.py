import random

__all__ = ['rnd_word', 'rand_from_seq', 'add_to_rnd_words', 'rnd_words']

def rnd_word() :
    return [
        'it\'s random time!',
        'hi, i am random',
        'random text',
        'i use the random module'
    ].random.choice() if len(rnd_words) == 0 else random.choice(rnd_words)

def rand_from_seq(seq) :
    return random.choice(seq)

def add_to_rnd_words(words) :
    ret = ''
    for word in words :
        ret+=word+' '
    rnd_words.append(ret)
    return None

def init_module(command_all, command0, command1, command2, command3, command4, command_any, variables) :
    command_all.update(all)
    command0.update(comm_0)
    command_any.update(comm_any)
    return command_all, command0, command1, command2, command3, command4, command_any, variables

rnd_words = []


all = {
    'rnd_word'         : rnd_word         ,
    'rand_from_seq'    : rand_from_seq    ,
    'add_to_rud_words' : add_to_rnd_words
}

comm_0 = {
    'rnd_word'         : rnd_word         ,
}

comm_any = {
    'rand_from_seq'    : rand_from_seq    ,
    'add_to_rud_words' : add_to_rnd_words
}