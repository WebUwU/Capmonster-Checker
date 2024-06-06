@echo off

pip install httpx 
pip install pystyle
echo @echo off > start.bat
echo python main.py >> start.bat

REM Step 3: Delete install.bat
del /F /Q install.bat
