import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np

df = pd.read_csv('sales_data.csv')

profitList = df['total_profit'].tolist()
monthList = df['month_number'].tolist()

all_product_list = df[['facecream','facewash','toothpaste','bathingsoap','shampoo','moisturizer']]
product01_list = df['facecream']
product02_list = df['facewash']
product03_list = df['bathingsoap']
sum_all_product_list = df[['facecream','facewash','toothpaste','bathingsoap','shampoo','moisturizer']].sum()
sum_product_month3 = df.groupby('month_number')[['facecream','facewash','toothpaste','bathingsoap','shampoo','moisturizer']].sum().loc()[3]


#Biểu đồ đoạn thẳng
plt.figure('Biểu đồ đoạn thẳng',figsize=(10,6))
plt.plot(monthList, profitList)
plt.xlabel('Tháng')
plt.ylabel('Lợi nhuận ($)')
plt.title('Lợi nhuận hàng tháng năm 2021')
plt.yticks([100000,200000,300000,400000,500000])
plt.xticks(monthList)
plt.show()

#Biểu đồ đoạn thẳng
plt.figure('Biểu đồ đoạn thẳng',figsize=(10,6))
plt.plot(monthList, profitList,'o--',color='#007f3f')
plt.xlabel('Tháng')
plt.ylabel('Lợi nhuận ($)')
plt.title('Lợi nhuận hàng tháng năm 2021')
plt.yticks([100000,200000,300000,400000,500000])
plt.xticks(monthList)
plt.show()

#Biểu đồ đường
plt.figure('Biểu đồ nhiều đoạn thẳng',figsize=(10,6))
plt.plot(monthList, all_product_list,'o-')
plt.xlabel('Tháng')
plt.ylabel('Số lượng bán')
plt.title('Số lượng bán của từng sản phẩm')
plt.yticks([1000,3000,5000,7000,9000,12000,15000,18000])
plt.xticks(monthList)
plt.legend(['Facecream','Facewash','Toothpaste','Bathingsoap','Shampoo','Moisturizer'],loc='upper left')
plt.show()

#Biểu đồ tán xạ
plt.figure('Biểu đồ tán xạ',figsize=(10,6))
plt.scatter(monthList, product01_list, c=['pink'])
plt.scatter(monthList, product02_list, c=['green'])
plt.xlabel('Tháng')
plt.ylabel('Số lượng bán')
plt.yticks([1000,3000,5000,7000])
plt.xticks(monthList)
plt.legend(['Facecream','Facewash'],loc='upper left')
plt.title('Số lượng bán của sửa rửa mặt và kem dưỡng da mặt theo tháng')
plt.show()

#Biểu đồ cột
plt.figure('Biểu đồ cột',figsize=(10,6))
plt.bar(monthList, product03_list,color ='pink')
plt.xlabel('Tháng')
plt.ylabel('Số lượng bán')
plt.xticks(monthList)
plt.yticks([1000,3000,5000,7000,9000,12000,15000])
plt.title('Số lượng bán của xà bông tắm theo tháng')
plt.show()

#Biểu đồ cột đôi 
plt.figure('Biểu đồ cột đôi',figsize=(12,6))
X_axis = np.arange(len(monthList)) 
plt.bar(X_axis - 0.2, product01_list,0.4,color ='green')
plt.bar(X_axis + 0.2, product02_list,0.4,color ='pink')
plt.xlabel('Tháng')
plt.ylabel('Số lượng bán')
plt.xticks(X_axis,monthList)
plt.yticks([1000,3000,5000,7000])
plt.title('So sánh số lượng bán của sửa rửa mặt và kem dưỡng da mặt theo tháng')
plt.legend(['Facecream','Facewash'],loc='upper right')
plt.show()


#Biều đồ hình tròn
plt.figure('Biểu đồ hình tròn',figsize=(10,6))
product = np.array(['Facecream','Facewash','Toothpaste','Bathingsoap','Shampoo','Moisturizer'])
plt.pie(sum_all_product_list,labels=product,autopct='%1.1f%%')
plt.title('Thống kê mặt hàng đã bán năm 2021')
plt.show()

#Biểu đồ hình tròn
plt.figure('Biểu đồ hình tròn',figsize=(10,6))
product = np.array(['Facecream','Facewash','Toothpaste','Bathingsoap','Shampoo','Moisturizer'])
plt.pie(sum_product_month3,labels=product,autopct='%1.1f%%')
plt.title('Thống kê mặt hàng đã bán năm 2021')
plt.show()


#Biểu đồ con 
fig,(ax1, ax2) = plt.subplots(nrows=2,sharex=True)

ax1.plot(monthList, product03_list,'o-',color='green')
ax2.plot(monthList, product02_list,'o-',color='pink')
ax2.set_xticks(monthList)
ax1.set_title('Số lượng xà bông tắm đã bán',color='green')
ax2.set_title('Số lượng sửa rửa mặt đã bán',color='pink')
ax2.set_xlabel('Tháng')
ax2.set_ylabel('Số lượng')
plt.show()
