import sys
from cx_Freeze import setup, Executable
 
base = None
 
if sys.platform == 'win32':
    base = 'Win32GUI'
# CUIの場合はこのif文をコメントアウトしてください。
 
exe = Executable(script = "auto_capture2.py", base= base)
# "main.py"にはpygameを用いて作成したファイルの名前を入れてください。
 
setup(name = 'your_filename',
    version = '0.1',
    description = 'converter',
    executables = [exe])