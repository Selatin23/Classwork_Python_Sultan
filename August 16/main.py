class Levels:
    Error = 0
    Warning = 1
    Info = 2
    Debug = 3
    Trace = 4
    names = ['[E]','[W]','[I]','[D]','[T]']

def log(level, *args, **kwargs):
    if level <= current_log_level:
        print(Levels.names[level], *args, **kwargs)

def logE(*args, **kwargs):
    log(Levels.Error, *args, **kwargs)
def logW(*args, **kwargs):
    log(Levels.Warning, *args, **kwargs)
def logI(*args, **kwargs):
    log(Levels.Info, *args, **kwargs)
def logD(*args, **kwargs):
    log(Levels.Debug, *args, **kwargs)
def logT(*args, **kwargs):
    log(Levels.Trace, *args, **kwargs)

def logOther(*args, **kwargs):
    print('logOther:')
    for x in args:
        print(x)
    for key, val in kwargs.items():
        print(key, ':', val)

arr = ['ololo', 5,6,8, []]
kwr = {'end' : '', 'sep': '|'}
logOther(0, 0, *arr, **kwr)

def my_function(the_list, num):
    logT(f'my_function({the_list}, {num})')
    if not the_list:
        logE('the list is empty!', len(the_list), sep='-=-')
    result = False
    for x in the_list:
        if x == num:
            logD(f'num={num} is found')
            result = True
    logT(f'my_function(..) result = {result}')
    return result

set_log_level()
print(my_function([1,5,2,6,3,6], 5))
print(my_function([], 9))