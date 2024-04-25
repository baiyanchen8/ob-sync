import os
import re
import requests

# 定義目標目錄路徑
dir_path = 'md'

# 定義正規表達式來搜尋https://*.jpg或https://*.png格式的連結
pattern = r'https?://[^\s]+?\.(?:jpg|png)'

# 建立一個空的清單來存放符合條件的連結
image_links = []
cannotopem=[]
# 讀取目錄中的所有檔案
for filename in os.listdir("md"):
    # 檢查檔案是否為Markdown檔案
    if filename.endswith('.md'):
        # 以二進制方式讀取檔案
        with open(os.path.join("md", filename), 'rb') as file:
            # 讀取檔案內容
            content = file.read().decode('utf-8')
            # 使用正規表達式搜尋連結並加入清單中
            image_links.extend(re.findall(pattern, content))
            try:
                response = requests.get(re.findall(pattern, content)[0])
                if response.status_code == 200:
                    pass
                else:
                    cannotopem.append(filename)
            except:
                 pass
            with open(os.path.join(dir_path, filename), 'r', encoding='utf-8') as f:
                    md_content = f.read()
            md_content = md_content.replace("{{%hackmd theme-dark %}", "")
            with open(os.path.join(dir_path, filename), 'w', encoding='utf-8') as f:
                f.write(md_content)
                

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
    'Referer': 'https://www.example.com'
}

# 下載圖片並替換連結
for link in image_links:
    # 下載圖片
    response = requests.get(link,headers)
    if response.status_code == 200:
        # 取得檔案名稱
        filename = os.path.basename(link)
        # 儲存圖片
        with open(os.path.join("md/image", filename), 'wb') as img_file:
            img_file.write(response.content)
        # 替換原始連結為路徑
        new_link = os.path.join("image", filename)
        # 在Markdown檔案中替換連結
        for md_file in os.listdir(dir_path):
            if md_file.endswith('.md'):
                with open(os.path.join(dir_path, md_file), 'r', encoding='utf-8') as f:
                    md_content = f.read()
                md_content = md_content.replace(link, new_link)
                with open(os.path.join(dir_path, md_file), 'w', encoding='utf-8') as f:
                    f.write(md_content)
    else:
        print(f"無法下載圖片：{link}")

with open('black.txt',"w") as f:
        for i in list(set(cannotopem)):
            f.write(str(i))
            f.write("\n")
