@echo off
setlocal enabledelayedexpansion

for /f "tokens=*" %%i in (BatList.txt) do (
  if exist "%%i" (
    start "" "%%i"
  ) else (
    echo File "%%i" not found.
  )
)

timeout /t 3 /nobreak >nul
exit
