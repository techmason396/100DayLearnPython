
from bs4 import BeautifulSoup
import codecs


with codecs.open("website.html", 'r', encoding='utf-8', errors='ignore') as web_file:
    html = web_file.read()

soup = BeautifulSoup(html, 'html.parser')

# lấy thẻ title đầu tiên
# print(soup.title)

# lấy nội dung thẻ title đầu tiên
# print(soup.title.string)

# lấy các thẻ khác tương tự vs soup.h1, soup.p... lưu ý chỉ lấy thẻ đầu tiên

# lấy toàn bộ nội dung
# print(soup.prettify())

# lấy toàn bộ một loại thẻ trong trang html
all_anchor_tags = soup.find_all(name="a")

# hiện nội dung trong thẻ a

for tag in all_anchor_tags:
    # hiện text trong trẻ a
    print(tag.getText())
    # hiện link
    print(tag.get('href'))


# lấy một thẻ theo tên và id
main_head = soup.find(name='h1', id="name")
print(main_head)

# chọn thẻ dựa trên bộ chọn selecter
company_url = soup.select_one(selector="p a")
print("company url: ", company_url.get("href"))
# chọn theo id
name = soup.select_one(selector="#name")
print("name :", name.getText())
# chọn các thẻ theo class
heading = soup.select(selector=".heading")
print(heading)
