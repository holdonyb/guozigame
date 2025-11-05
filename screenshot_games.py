import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 游戏列表
games = [
    {"file": "match3game.html", "name": "match3", "wait_time": 5},
    {"file": "evolution.html", "name": "evolution", "wait_time": 5},
    {"file": "langwizard.html", "name": "langwizard", "wait_time": 3},
    {"file": "engmatchgame.html", "name": "engmatch", "wait_time": 3},
    {"file": "lucidmaze2.html", "name": "lucidmaze", "wait_time": 5},
    {"file": "lucidgame3d.html", "name": "lucidgame3d", "wait_time": 5},
    {"file": "lucidgame.html", "name": "lucidgame", "wait_time": 3},
    {"file": "lazerbox2D.html", "name": "lazerbox", "wait_time": 3},
    {"file": "interactivedist.html", "name": "interactivedist", "wait_time": 3},
    {"file": "learnarea.html", "name": "learnarea", "wait_time": 3},
    {"file": "learnareadot.html", "name": "learnareadot", "wait_time": 3},
    {"file": "longjuangeng.html", "name": "longjuangeng", "wait_time": 3},
    {"file": "yuanxingjinshu.html", "name": "yuanxingjinshu", "wait_time": 3},
    {"file": "mathgame.html", "name": "mathgame", "wait_time": 4},
    {"file": "mathgame2.html", "name": "mathgame2", "wait_time": 4},
]

def take_screenshots(games_list):
    # 确保截图目录存在
    screenshot_dir = "resources/screenshots"
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)
    
    # 设置Selenium选项
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # 无头模式，不显示浏览器窗口
    chrome_options.add_argument("--window-size=1024,768")  # 设置窗口大小
    
    # 初始化WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    
    # 获取当前工作目录的绝对路径
    current_dir = os.getcwd()
    
    for game in games_list:
        try:
            # 构建游戏HTML文件的完整URL
            file_path = os.path.join(current_dir, game["file"])
            url = f"file:///{file_path}"
            
            print(f"正在截取 {game['name']} 的截图...")
            driver.get(url)
            
            # 等待页面加载
            time.sleep(game["wait_time"])
            
            # 保存截图
            screenshot_path = os.path.join(screenshot_dir, f"{game['name']}.png")
            driver.save_screenshot(screenshot_path)
            print(f"截图已保存至 {screenshot_path}")
            
        except Exception as e:
            print(f"截取 {game['name']} 时出错: {str(e)}")
    
    # 关闭WebDriver
    driver.quit()
    print("所有截图已完成!")

if __name__ == "__main__":
    take_screenshots(games) 