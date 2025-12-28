@echo off

setlocal enabledelayedexpansion

REM List of predefined expressions with left and right eyes
set "expressions[0]=angry|angry-left|angry-right"
set "expressions[1]=broken|broken|broken"
set "expressions[2]=happy|happy|happy"
set "expressions[3]=love|love|love"
set "expressions[4]=neutral|neutral|neutral"
set "expressions[5]=sad|sad-left|sad-right"
set "expressions[6]=skeptical|skeptical|skeptical"
set "expressions[7]=surprised|surprised|surprised"
set "expressions[8]=tired|tired|tired"

REM Process each expression
for /l %%i in (0,1,8) do (
  REM Parse expression line
  for /f "tokens=1,2,3 delims=|" %%a in ("!expressions[%%i]!") do (
    REM Assign variables
    set "expression=%%a"
    set "left=%%b"
    set "right=%%c"
    
    REM Create predefined expression
    echo|set /p=Creating expression: !expression! (left: !left!, right: !right!^) ... 
    python create_expression.py "!left!" "!right!" "!expression!"
    echo Done
  )
)

endlocal
