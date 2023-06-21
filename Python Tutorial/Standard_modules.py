# In Python, standard modules are pre-built modules that come with the Python 
# programming language. These modules provide a wide range of functionalities 
# and features that you can utilize in your Python programs without needing to 
# install any additional libraries or packages. 

# sys is a core standard module that provides access to some system specefic param
# -eters and functions

# Code in interpretor:
# >>> import sys 
# >>> sys.ps1
# '>>> '
# >>> sys.ps2
# '... '
# >>>

# sys.ps1  represents primary prompt('>>>') when the interpetor is waiting for user input
# sys.ps2 represents secondary prompt ('...') when interprtor expects more input to complete 
# the code block

# You can also change these prompts as following:

# >>> sys.ps1 = 'C> '
# C> print('Yuck!')
# Yuck!
# C>

# dir() function:
# the built in dir() is used to find out which names the module defines.
# it returns a sorted list of strings

# >>> dir(sys)
# ['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__', '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__', '__stderr__', '__stdin__', '__stdout__', '__unraisablehook__', '_base_executable', '_clear_type_cache', '_current_exceptions', '_current_frames', '_deactivate_opcache', '_debugmallocstats', '_enablelegacywindowsfsencoding', '_framework', '_getframe', '_git', '_home', '_xoptions', 'addaudithook', 'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix', 'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing', 'copyright', 'displayhook', 'dllhandle', 'dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth', 'getallocatedblocks', 'getdefaultencoding', 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval', 'gettrace', 'getwindowsversion', 'hash_info', 'hexversion', 'implementation', 'int_info', 'intern', 'is_finalizing', 'last_traceback', 'last_type', 'last_value', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'orig_argv', 'path', 'path_hooks', 'path_importer_cache', 'platform', 'platlibdir', 'prefix', 'ps1', 'ps2', 'pycache_prefix', 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'setprofile', 'setrecursionlimit', 
# 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdlib_module_names', 'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info', 'warnoptions', 'winver']
# >>>