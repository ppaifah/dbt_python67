#ธนาคารแห่งหนึ่ง ให้บริการแลกเงินแก่ลูกค้า จงเขียนโปรแกรมแลกเงินสกุล USD และ JPY 
country = input("กรุณาป้อนสกุลเงินที่คุณต้องการ (USD,JPY) : ")
money = float(input("กรุณาป้อนจำนวนเงินที่คุณต้องการแลก : "))

if country == "USD":
    bath = money * 32.5
    print(f"จำนวนเงิน USD ที่แลก : {money}")
    print(f"จำนวนเงิน THB ที่ใช้แลก : {bath:.2f}")

elif country == "JPY":
    bath = money * 0.29
    print(f"จำนวนเงิน JPY ที่แลก : {money}")
    print(f"จำนวนเงิน THB ที่ใช้แลก : {bath:.2f}")

else :
    print("ข้อมูลไม่ถูกต้อง กรุณาตรวจสอบอีกครั้ง")