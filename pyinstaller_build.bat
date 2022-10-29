
pyinstaller run.py ^
    --name smallapp ^
    --onefile ^
    -w ^
    --clean ^
    --noupx ^
    -i "smallapp\assets\icons\appicons\smallapp.icns" ^
    --add-data "smallapp\assets;smallapp\assets"

:: Ensure blank line after cmd with caret
echo "OK"
