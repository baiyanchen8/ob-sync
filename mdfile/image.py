import os
import re

# 定義目標目錄路徑
dir_path = 'md'

# 讀取目錄中的所有檔案
for filename in os.listdir(dir_path):
    # 檢查檔案是否為Markdown檔案
    if filename.endswith('.md'):
        # 以utf-8方式讀取檔案
        with open(os.path.join(dir_path, filename), 'r', encoding='utf-8') as file:
            # 讀取檔案內容
            content = file.read()
            # 將[[/ 替換為 [[
            new_content = content.replace("\\\n", "\n")
            # 寫入修改後的內容到原始檔案中
            with open(os.path.join(dir_path, filename), 'w', encoding='utf-8') as f:
                f.write(new_content)

print("所有 Markdown 檔案中的連結轉換完成。")
