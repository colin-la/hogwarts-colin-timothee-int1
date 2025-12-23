@echo off
cd %userprofile%\Documents
echo Hello, welcome to the hogwarts legacy game !
echo We will first check if python and git are install on your computer in order to install our game.
set /p temp=Press Enter to continue ...
cls
python --version 2>&1 >nul
if %errorlevel% equ 0 (
    echo Python is installed.
) else (
    echo Python is not installed, please install it
    goto end 
)

git --version 2>&1 >nul
if %errorlevel% equ 0 (
    echo Git is installed
) else (
    echo Git is not installed, please install it
    goto end 
)

set /p installation_validation=Do you want to install the game ? (y/n) : 

if "%installation_validation%" == "y" (
    goto Installation_script    
) else if "%installation_validation%" == "Y" (
    goto Installation_script    
) else if "%installation_validation%" == "yes" (
    goto Installation_script    
) else (
    goto Non_agreement
)

:Installation_script
cls 
cd %userprofile%\Documents
git init 
cls
git clone https://github.com/colin-la/hogwarts-colin-timothee-int1 
cls
rmdir /s /q .git
echo The game has been install successfully !

set launch_file="%userprofile%\Desktop\Launch_Hogwarts-colin-timothee-int1.cmd"
echo @echo off > %launch_file%
echo cd %userprofile%\Documents\hogwarts-colin-timothee-int1 >> %launch_file% 
echo python main.py >> %launch_file%   
echo 'Launch_Hogwarts-colin-timothee-int1.cmd' file has been created on the desktop to launch the game
goto end 


:Non_agreement
echo No problem, see you next time !

:end
set /p temp2=Press Enter to exit the terminal ...
del "%~f0" 