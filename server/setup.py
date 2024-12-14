from cx_Freeze import setup, Executable

setup(
    name="monitoring server",
    version="0.1",
    description="모니터링 서버",
    executables=[Executable("server.py", base="Win32GUI")]
)