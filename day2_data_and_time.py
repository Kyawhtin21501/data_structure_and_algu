import time#この関数は現在の時間を示しなたらloopする

for _ in range(10):
    print("現在の時刻:", time.ctime())
    time.sleep(1)
