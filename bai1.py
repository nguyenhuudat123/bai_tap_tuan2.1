# vay von ngan hang

print('Ngân Hàng Vietcombank xin chào quý khách')
age = int(input('Mời quý khách nhập số tuổi của mình: '))
income = int(input('Mời quý khách nhập thu nhập hàng năm của mình($): '))
if age > 18 and income >= 2500:
    print("Quý khách đủ điều kiện vay tiền.")
else:
    print("Xin lỗi, quý khách không đủ điều kiện vay tiền.")