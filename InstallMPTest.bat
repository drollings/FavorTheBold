move scripts scripts_norm
if not exist scripts_mp goto make
	del /s /f scripts_mp
	deltree scripts_mp

:make
scripts_11.exe
mpscripts.exe

move scripts scripts_mp
move scripts_norm scripts