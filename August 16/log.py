class Levels:
    Error = 0
    Warning = 1
    Info = 2
    Debug = 3
    Trace = 4
    names = ['[E]','[W]','[I]','[D]','[T]']


def set_log_level(level):
    global current_log_level