"""
    Lists the exception from the Exception argument until indicated level
"""
def list_exception( Exception_base, level=0 ):
    """
    Lists the exception from the Exception argument until indicated level

    :param Exception_base: Exception base to list
    :param level: under level to go to
    :return: None
    """
    if level == 0:
        print("Base :", Exception_base.__base__.__name__)
    print(f"{'|    '*level}{Exception_base.__name__}")
    for i in Exception_base.__subclasses__():
        list_exception( i, level+1)

list_exception(BaseException)

# Base : object
# BaseException
# |    BaseExceptionGroup
# |    |    ExceptionGroup
# |    Exception
# |    |    ArithmeticError
# |    |    |    FloatingPointError
# |    |    |    OverflowError
# |    |    |    ZeroDivisionError
# |    |    AssertionError
# |    |    AttributeError
# |    |    BufferError
# |    |    EOFError
# |    |    ImportError
# |    |    |    ModuleNotFoundError
# |    |    |    ZipImportError
# |    |    LookupError
# |    |    |    IndexError
# |    |    |    KeyError
# |    |    |    CodecRegistryError
# |    |    MemoryError
# |    |    NameError
# |    |    |    UnboundLocalError
# |    |    OSError
# |    |    |    BlockingIOError
# |    |    |    ChildProcessError
# |    |    |    ConnectionError
# |    |    |    |    BrokenPipeError
# |    |    |    |    ConnectionAbortedError
# |    |    |    |    ConnectionRefusedError
# |    |    |    |    ConnectionResetError
# |    |    |    FileExistsError
# |    |    |    FileNotFoundError
# |    |    |    InterruptedError
# |    |    |    IsADirectoryError
# |    |    |    NotADirectoryError
# |    |    |    PermissionError
# |    |    |    ProcessLookupError
# |    |    |    TimeoutError
# |    |    |    UnsupportedOperation
# |    |    ReferenceError
# |    |    RuntimeError
# |    |    |    NotImplementedError
# |    |    |    RecursionError
# |    |    |    _DeadlockError
# |    |    StopAsyncIteration
# |    |    StopIteration
# |    |    SyntaxError
# |    |    |    IndentationError
# |    |    |    |    TabError
# |    |    SystemError
# |    |    |    CodecRegistryError
# |    |    TypeError
# |    |    ValueError
# |    |    |    UnicodeError
# |    |    |    |    UnicodeDecodeError
# |    |    |    |    UnicodeEncodeError
# |    |    |    |    UnicodeTranslateError
# |    |    |    UnsupportedOperation
# |    |    Warning
# |    |    |    BytesWarning
# |    |    |    DeprecationWarning
# |    |    |    EncodingWarning
# |    |    |    FutureWarning
# |    |    |    ImportWarning
# |    |    |    PendingDeprecationWarning
# |    |    |    ResourceWarning
# |    |    |    RuntimeWarning
# |    |    |    SyntaxWarning
# |    |    |    UnicodeWarning
# |    |    |    UserWarning
# |    |    ExceptionGroup
# |    |    error
# |    |    TokenError
# |    |    StopTokenizing
# |    |    E
# |    GeneratorExit
# |    KeyboardInterrupt
# |    SystemExit


"""
    NOTES : IOError is an alias of OSError since Python 3.6
"""
print("\nNote : IOError is OSError", IOError is OSError, IOError, OSError)

