n = int(input("Input number: "))
i = 0  # ตัวแปรเพื่อวนลูปแถว
j = 0  # ตัวแปรเพื่อวนลูปหลักสำหรับการเขียนช่องว่าง
k = 1  # ตัวแปรเพื่อวนลูปนับการเขียน *  โดยเพิ่มครั้งละ 2  จาก 1 เป็น 3 เป็น 5 เป็น 7
l = 0  # ตัวแปรเพื่อวนลูปหลักสำหรับการเขียน * เริ่มจาก 0 จนถึง k-1

while i < n:  # เริ่มวนลูปเพื่อนับจำนวนบรรทัดให้เท่ากับ n
    j = 0
    while j <= n - i - 2:  # เริ่มวนลูปหลักในแต่ละบรรทัดเพื่อใส่ช่วงว่างด้านหน้า
        print("  ", end='')
        j += 1
    l = 0
    j = 0
    while l < k:  # เริ่มวนลูปหลักเพื่อเขียน * ตามค่า  k
        print("* ", end='')
        l += 1

    k += 2  # เพิ่มค่า k  ขึ้นครั้งละ 2  สังเกตแต่ละบรรทัด  จะพิมพ์ * ตามค่า k  เช่น 1, 3, 5, 7, 9
    print()
    i += 1