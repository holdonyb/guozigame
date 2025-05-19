import os
import re
from bs4 import BeautifulSoup

def update_index_html():
    # 读取index.html
    with open('index.html', 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    # 解析HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # 获取所有游戏卡片
    game_cards = soup.find_all('div', class_='game-card')
    
    # 游戏文件名到截图名称的映射
    game_to_screenshot = {
        'match3game.html': 'match3.png',
        'evolution.html': 'evolution.png',
        'langwizard.html': 'langwizard.png',
        'engmatchgame.html': 'engmatch.png',
        'lucidmaze2.html': 'lucidmaze.png',
        'lucidgame3d.html': 'lucidgame3d.png',
        'lucidgame.html': 'lucidgame.png',
        'lazerbox2D.html': 'lazerbox.png',
        'interactivedist.html': 'interactivedist.png',
        'learnarea.html': 'learnarea.png',
        'learnareadot.html': 'learnareadot.png',
        'longjuangeng.html': 'longjuangeng.png',
        'yuanxingjinshu.html': 'yuanxingjinshu.png'
    }
    
    # 截图目录
    screenshot_dir = "resources/screenshots"
    
    # 检查哪些截图文件存在
    existing_screenshots = set()
    if os.path.exists(screenshot_dir):
        existing_screenshots = set(os.listdir(screenshot_dir))
    
    updated_count = 0
    
    # 处理每个游戏卡片
    for card in game_cards:
        # 找到游戏链接
        link_tag = card.find('a', class_='play-button')
        if not link_tag:
            continue
            
        game_url = link_tag.get('href')
        
        # 如果存在该游戏的截图
        if game_url in game_to_screenshot and game_to_screenshot[game_url] in existing_screenshots:
            # 找到图片容器
            image_container = card.find('div', class_='game-image')
            if not image_container:
                continue
                
            # 获取游戏标题用于alt文本
            title_tag = card.find('h3', class_='game-title')
            alt_text = title_tag.text if title_tag else "游戏截图"
            
            # 清空图片容器
            image_container.clear()
            
            # 创建新的img标签
            img_tag = soup.new_tag('img')
            img_tag['src'] = f'{screenshot_dir}/{game_to_screenshot[game_url]}'
            img_tag['alt'] = alt_text
            img_tag['style'] = 'width: 100%; height: 100%; object-fit: cover;'
            
            # 添加到容器
            image_container.append(img_tag)
            updated_count += 1
    
    # 更新样式，为图片添加CSS
    style_tag = soup.find('style')
    if style_tag and '.game-image img' not in style_tag.text:
        style_tag.append("""
        .game-image img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            border-radius: 10px 10px 0 0;
        }
        """)
    
    # 保存更新后的HTML
    with open('index.html', 'w', encoding='utf-8') as file:
        file.write(str(soup))
    
    print(f"已更新 {updated_count} 个游戏卡片的截图")

if __name__ == '__main__':
    update_index_html() 