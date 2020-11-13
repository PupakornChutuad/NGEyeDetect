# import pandas as pd

# df = pd.read_excel('testpandas.xlsx', index_col=None, header=None)
# print(df)
# data = {'วันที่':[input()],
#         'คะแนนแบบทดสอบ':[input()],
#         }

# df = pd.DataFrame(data, columns=['วันที่','คะแนนแบบทดสอบ'])
#
#
# while data != 0 :
#     new_row = {'วันที่':input(),'คะแนนแบบทดสอบ':input(),}
#
#     df = df.append(new_row ,ignore_index=True)
#     df.to_excel('testpandas.xlsx')
#
#     print(df)

# import xlsxwriter
# import pandas as pd
#
# # อ่านข้อมูลที่มีอยู่ในไฟล์เดิม
# readDataframe = pd.read_excel(r'fruits.xlsx')
#
# # สร้างข้อมูลใหม่เป็นข้อมูลของ orange
# newDataframe = pd.DataFrame({'Name': ['orange'], 'Price': [88], 'Amount': [15]})
#
# # นำข้อมูล orange ที่สร้างใหม่รวมเข้ากับข้อมูลเก่าที่อ่านจากไฟล์
# frames = [readDataframe, newDataframe]
# result = pd.concat(frames)
#
# # สร้าง Writer เหมือนกับตอนเขียนไฟล์
# writer = pd.ExcelWriter('fruits.xlsx', engine='xlsxwriter')
#
# # นำข้อมูลชุดใหม่เขียนลงไฟล์และจบการทำงาน
# result.to_excel(writer, index=False)
# writer.save()