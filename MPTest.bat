@echo off
if exist scripts_norm goto run
move scripts scripts_norm
move scripts_mp scripts

:run
stbc.exe -TestMode
move scripts scripts_mp
move scripts_norm scripts