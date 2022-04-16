#from pyperclip import copy

print("坐标转换器")
print("-"*15)
print("当前版本：0.2")
print("-"*15)
print("更新日志：")
print("0.1  新增：WGS-84：转换为Endless ATC")
print("0.2  新增：PMDG：转换为Endless ATC")
print("     新增：WGS-84：可选择度分秒模式或度分模式")
print("     优化：WGS-84：转换方式")
print("-"*15)
print("© 2021 Jared Hu. All rights reserved.")
print("-"*15)

print("模式1 - GWS-84 → Endless ATC")
print("模式2 - PMDG → Endless ATC")
model = eval(input("请选择想进入的模式："))
print("-"*15)

if model == 1:
    print("模式11 - 度分秒（XX°XX′XX.X″）")
    print("模式12 - 度分（XX°XX.X′）")
    model1 = eval(input("请选择想进入的模式："))
    print("-" * 15)

    if model1 == 11:
        print("输入示例：")
        print("原始格式：N305103 E1214010")
        print("输入格式：30 51 03 121 40 10")
        print("输出格式：N30.850833, E121.669444")
        print("-" * 15)
        print("当前版本保留小数点后六位，并四舍五入")
        print("-" * 15)
        print("开始转换")
        print("-" * 15)
        judge = True
        while judge:
            raw = input()
            raw_list = raw.split()
            latitude_raw = int(raw_list[0]) + (int(raw_list[1]) + (float(raw_list[2]) / 60)) / 60
            longitude_raw = int(raw_list[3]) + (int(raw_list[4]) + (float(raw_list[5]) / 60)) / 60
            latitude = '%.6f' % latitude_raw
            longitude = '%.6f' % longitude_raw
            print("N{}, E{}".format(latitude, longitude))
            # copy("N{}, E{}".format(latitude, longitude))

    if model1 == 12:
        print("输入示例：")
        print("原始格式：N4002.9 E11644.1")
        print("输入格式：40 02.9 116 44.1")
        print("输出格式：N40.048333, E116.735000")
        print("-" * 15)
        print("当前版本保留小数点后六位，并四舍五入")
        print("-" * 15)
        print("开始转换")
        print("-" * 15)
        judge = True
        while judge:
            raw = input()
            raw_list = raw.split()
            latitude_raw = int(raw_list[0]) + float(raw_list[1]) / 60
            longitude_raw = int(raw_list[2]) + float(raw_list[3]) / 60
            latitude = '%.6f' % latitude_raw
            longitude = '%.6f' % longitude_raw
            print("N{}, E{}".format(latitude, longitude))
            # copy("N{}, E{}".format(latitude, longitude))

elif model == 2:
    print("输入示例：")
    print("输入格式：FIX PEK LATLON N 40 2.9 E 116 44.1")
    print("输出格式：PEK, N40.048333, E116.735000")
    print("-" * 15)
    print("当前版本保留小数点后六位，并四舍五入")
    print("-" * 15)
    print("开始转换")
    print("-" * 15)
    judge = True
    while judge:
        raw = input()
        raw_list = raw.split()
        waypoint = raw_list[1]
        latitude_raw = int(raw_list[4]) + float(raw_list[5]) / 60
        longitude_raw = int(raw_list[7]) + float(raw_list[8]) / 60
        latitude = '%.6f' % latitude_raw
        longitude = '%.6f' % longitude_raw
        print("{}, {}{}, {}{}".format(waypoint, raw_list[3], latitude, raw_list[6], longitude))

else:
    print("输入的模式不存在噢(⊙o⊙)")
    input('使用 <Enter> 键以关闭程序。')
