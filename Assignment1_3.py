#โปรแกรมการคำนวณอายุปัจจุบันของผู้ใช้

birthyear = int(input("โปรดระบุปีที่คุณเกิด (พ.ศ.) : "))  #ให้ผู้ใช้ใส่ปีที่เกิด
now = 2567                                           #ใส่ตัวแปรทีปัจจุบัน
result = now - birthyear                             #คำนวณผลลัพธ์

print("=" * 20) #เส้นบรรทัดเพื่อความสวยงาม

print(f"อายุของคุณปัจจุบัน : {result}")                  #แสดงผลลัพธ์

print("=" * 20) #เส้นบรรทัดเพื่อความสวยงาม