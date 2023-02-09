import pandas as pd
import os

PATH = os.path.abspath(os.path.dirname(__file__))
DATA_CSV_FILE = "/Data.csv"

# đọc file data
data = pd.read_csv(PATH+DATA_CSV_FILE)

# đếm mỗi color có bao nhiêu con
colors = data['Primary Fur Color'].value_counts()

colors_dict = colors.to_dict()
count_gray_color = colors_dict['Gray']
count_cinnamon_color = colors_dict['Cinnamon']
count_black_color = colors_dict['Black']

colors_dict = {
    "Fur color": ["Gray", "Cinnamon", "Black"],
    "Count": [count_gray_color, count_cinnamon_color, count_black_color]
}

data_color = pd.DataFrame(colors_dict)

# xuat file csv
data_color.to_csv(PATH+"/data_colors.csv")
