@echo off
echo ===== 果子游戏集截图更新工具 =====
echo.

:: 运行截图脚本
echo 步骤1: 获取游戏截图
call take_screenshots.bat

:: 环境已经激活，安装BeautifulSoup
echo.
echo 步骤2: 安装HTML处理所需的包
call .venv\Scripts\activate.bat
pip install beautifulsoup4

:: 运行更新主页脚本
echo.
echo 步骤3: 更新主页显示截图
python update_index_with_screenshots.py

echo.
echo ===== 所有操作已完成! =====
echo 请在浏览器中查看 index.html 以确认截图是否正确显示。
pause 