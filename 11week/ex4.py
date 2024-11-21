import qrcode 

qr_name = input("이름을 입력하세요 : "), int(input("학번을 입력하세요 : ")), input("전공을 입력하세요 : ")
qr_img = qrcode.make(qr_name)

save_path = 'my_info_data.png'
qr_img.save(save_path)