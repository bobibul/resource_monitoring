from cx_Freeze import setup, Executable

setup(
    name="resource_monitoring",
    version="0.1",
    description="리소스 모니터링",
    executables=[Executable("client.py", base="Win32GUI")]
)