from bs4 import BeautifulSoup

html_code = '''
<h1 class="style-scope ytd-watch-metadata">
    <yt-formatted-string force-default-style="" class="style-scope ytd-watch-metadata">
        Intel Arc GPUs Are FINALLY Worth Buying! 🙌
    </yt-formatted-string>
</h1>
'''

# 使用Beautiful Soup解析HTML
soup = BeautifulSoup(html_code, 'html.parser')

# 提取标题
title_element = soup.find('yt-formatted-string', class_='style-scope ytd-watch-metadata')
title = title_element.get_text(strip=True)

print("标题:", title)
