@echo off
echo 正在设置Python环境和所需依赖...

:: 检查是否已安装Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo 未找到Python! 请安装Python 3.6或更高版本。
    echo 可以从 https://www.python.org/downloads/ 下载Python。
    pause
    exit /b
)

:: 创建虚拟环境 (如果不存在)
if not exist .venv (
    echo 正在创建虚拟环境...
    python -m venv .venv
)

:: 激活虚拟环境
call .venv\Scripts\activate.bat

:: 安装所需包
echo 正在安装所需Python包...
pip install selenium webdriver-manager

:: 运行脚本
echo 正在启动截图脚本...
python screenshot_games.py

:: 完成后显示信息
echo.
echo 截图过程已完成!
echo 截图保存在 resources/screenshots 目录中
echo 现在您可以将这些截图整合到您的网站中

pause 