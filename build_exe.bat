@echo off
REM Excel文件合并工具 - 打包脚本
REM 使用PyInstaller将Python程序打包成exe文件

echo ========================================
echo Excel文件合并工具 - 打包程序
echo ========================================
echo.

REM 检查是否安装了PyInstaller
python -c "import PyInstaller" 2>nul
if errorlevel 1 (
    echo [错误] 未检测到PyInstaller，正在安装...
    pip install pyinstaller>=5.0.0
    if errorlevel 1 (
        echo [错误] PyInstaller安装失败，请手动运行: pip install pyinstaller
        pause
        exit /b 1
    )
)

echo [1/3] 清理之前的打包文件...
if exist "build" rmdir /s /q "build"
if exist "dist" rmdir /s /q "dist"
if exist "excel_merger.spec" del /q "excel_merger.spec"

echo [2/3] 开始打包，请稍候...
pyinstaller --onefile ^
    --windowed ^
    --name "Excel合并工具" ^
    --icon=NONE ^
    --add-data "README.md;." ^
    --hidden-import "pandas" ^
    --hidden-import "openpyxl" ^
    --hidden-import "xlrd" ^
    --collect-all "pandas" ^
    --collect-all "openpyxl" ^
    --collect-all "xlrd" ^
    excel_merger.py

if errorlevel 1 (
    echo.
    echo [错误] 打包失败！
    pause
    exit /b 1
)

echo [3/3] 打包完成！
echo.
echo ========================================
echo 打包成功！
echo 可执行文件位置: dist\Excel合并工具.exe
echo ========================================
echo.
echo 提示：
echo 1. 请测试 dist\Excel合并工具.exe 确保功能正常
echo 2. 可以将 dist\Excel合并工具.exe 分发给用户
echo 3. 用户无需安装Python即可直接运行
echo.

pause
