#การสร้างลิสต์

nums = [5 , 7 , 10 , 4 , 6 , 12]

lst1 = list()

lst2 = ['a' , 'b' , 'c' , 'o']

lst3 = [4 , 5.5 , 0 , "Leo"]

print ('nums:' , nums,'\nlst1:', lst1, '\nlst2:' , lst2, '\nlst3' , lst3)

#การเข้าถึงสมาชิกในลิสต์

sum = nums[2] + nums[4]
print(sum)

#เข้าถึงสมาชิกของ lst2 ทุกตัว และแสดงผงเป็นตัวพิมพ์ใหญ่
for x in lst2:
    print(x.upper())

#การเพิ่มข้อมูลเก็บในลิสต์
lst1.append(5)
print(lst1)
lst1.append(10)
print(lst1)

#การเพิ่มข้อมูลเก็บในลิสต์
lst1.insert(1,9)
print(lst1)
lst1.insert(2,14)
print(lst1)

mylst = lst1+lst3  #เอาลิสต์มารวมกัน
print(mylst)

mylst.pop(7)  #ลบสมาชิกในลิสต์
print(mylst)

mylst.remove(5.5)  #ลบสมาชิกออกโดยไม่ต้องนับ index
print(mylst)





