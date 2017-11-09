from cx_Freeze import setup,Executable
import cx_Freeze

#executables = [cx_Freeze.Executable("SimpleGUI.py", base = "Win32GUI")]
executables = [cx_Freeze.Executable("allignment.py")]
Packages = [ ]

#Include = ["images"]

cx_Freeze.setup(
        name="Side_Scroller",
        options={"build_exe":{"packages":Packages}},
        description = "Base Engine for development",
        executables = executables
)
