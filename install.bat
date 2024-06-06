@echo off

pip install httpx 
pip install pystyle
echo @echo off > start.bat
echo python main.py >> start.bat

del /F /Q install.bat
