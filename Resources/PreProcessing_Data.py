# flake8: noqa W605

import pandas as pd

df_raw = pd.read_csv('D:\Data Analysis\Final Project\DataSet\Raw_Data_Sales_Records.csv')

# Xem thông tin chi tiết dữ liệu
df_raw.info()

# Dư thừa cột trống tên --> Xóa vì dư thừa và tốn không gian lưu trữ 
del df_raw['Unnamed: 0']

# Nhận thấy dataFrame có tổng 5043 dòng mà có 5012 (not null) 
# --> Có thể các dòng còn lại là null nên tiến hành kiểm tra
df_check_null = df_raw.isnull().sum()
print(df_check_null)

# Xóa các dòng Blank
df_raw.dropna(inplace=True)


# Xử lý các cột liên quan đến tiền có ký tự "$" và chuyển về kiểu float vì đang ở string
df_raw['Unit Price'] = df_raw['Unit Price'].str.replace('$', '').astype(float)
df_raw['Unit Cost'] = df_raw['Unit Cost'].str.replace('$', '').astype(float)
df_raw['Total Revenue'] = df_raw['Total Revenue'].str.replace('$', '').astype(float)
df_raw['Total Cost'] = df_raw['Total Cost'].str.replace('$', '').astype(float)
df_raw['Total Profit'] = df_raw['Total Profit'].str.replace('$', '').astype(float)


# Xem chi tiết DataFrame sau khi hoàn thành quá trình làm sạch
print(df_raw)


df_raw.to_csv('Cleaned_Data_Sales_Records.csv', index=False)
