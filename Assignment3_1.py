#เขียนโปรแกรมวงล้อสีโดยรับค่าจากคีย์บอร์ดเป็นเลขจํานวนเต็มที่มีค่า 0 - 36 เป็นเลขที่ได้จากการหมุนวงล้อ

number = float(input("กรุณาป้อนตัวเลขของท่าน : "))        #กไหนดตัวแปรให้ผู้ใช้ป้อนตัวเลขที่ต้องการ

if number == 0 :             
    print("หมายเลข 0 มีค่าเป็นสีเขียว")
elif (number >= 1) and (number <=10):
    if number %2 != 0:
        print(f"{number} เป็นเลขคี่ มีค่าเป็นสีแดง")
    else :
        print(f"{number} เป็นเลขที่คู่ มีค่าเป็นสีดำ")

elif (number >= 11) and (number <= 18):
    if number %2 != 0:
        print(f"{number} เป็นเลขคี่ มีค่าเป็นสีดำ")
    else :
        print(f"{number} เป็นเลขคู่ มีค่าเป็นสีแดง")

elif (number >= 19) and (number <= 28):
    if number %2 != 0:
        print(f"{number} เป็นเลขคี่ มีค่าเป็นสีแดง")
    else :
        print(f"{number} เป็นเลขคู่ มีค่าเป็นสีดำ")

elif (number >= 29) and (number <= 36):
    if number %2 != 0:
        print(f"{number} เป็นเลขคี่ มีค่าเป็นสีดำ")
    else :
        print(f"{number} เป็นเลขคู่ มีค่าเป็นสีแดง")

else :
    print(f"หมายเลข {number} ไม่ได้อยู่ในตัวเลขที่ตัวหนดกรุณาลองใหม่อีกครั้ง")
