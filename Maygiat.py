import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fz
import skfuzzy.intervals as _intervals


def define_membership_functions():
    # Định nghĩa các hàm thuộc tính cho độ bẩn, độ dầu mỡ và thời gian giặt
    X = np.arange(0, 101, 1)
    Z = np.arange(0, 61, 1)

    # Độ bẩn
    Ds = fz.trimf(X, [0, 0, 50])
    Dm = fz.trimf(X, [0, 50, 100])
    Dl = fz.trimf(X, [50, 100, 100])

    # Độ dầu mỡ
    Gs = fz.trimf(X, [0, 0, 50])
    Gm = fz.trimf(X, [0, 50, 100])
    Gl = fz.trimf(X, [50, 100, 100])

    # Thời gian giặt
    Tv = fz.trimf(Z, [0, 0, 15])
    Ts = fz.trimf(Z, [0, 15, 30])
    Tm = fz.trimf(Z, [15, 30, 45])
    Tl = fz.trimf(Z, [30, 45, 60])
    Tf = fz.trimf(Z, [45, 60, 60])

    # Hiển thị các hàm thuộc tính
    plt.figure(figsize=(10, 6))

    plt.subplot(3, 1, 1)
    plt.plot(X, Ds, label="Bẩn ít")
    plt.plot(X, Dm, label="Trung bình")
    plt.plot(X, Dl, label="Bẩn nhiều")
    plt.xlabel("Độ bẩn (%)")
    plt.ylabel("Mức độ")
    plt.title("Độ bẩn")
    plt.legend()

    plt.subplot(3, 1, 2)
    plt.plot(X, Gs, label="Dầu ít")
    plt.plot(X, Gm, label="Trung bình")
    plt.plot(X, Gl, label="Dầu nhiều")
    plt.xlabel("Độ dầu mỡ (%)")
    plt.ylabel("Mức độ")
    plt.title("Độ dầu mỡ")
    plt.legend()

    plt.subplot(3, 1, 3)
    plt.plot(Z, Tv, label="Rất ngắn")
    plt.plot(Z, Ts, label="Ngắn")
    plt.plot(Z, Tm, label="Vừa")
    plt.plot(Z, Tl, label="Dài")
    plt.plot(Z, Tf, label="Rất dài")
    plt.xlabel("Thời gian (phút)")
    plt.ylabel("Mức độ")
    plt.title("Thời gian giặt")
    plt.legend()

define_membership_functions()

plt.tight_layout()
plt.show()
#Ham thuoc do ban/dau mo it
def dg_s(x:int):
    if x >= 50: return 0
    else: return round ((50 - x)/50,2)
#Ham thuoc do ban/dau mo trung binh
def dg_m(x:int):
    if x >= 50: return round ((100 - x)/50,2)
    else: return round ((x)/50,2)
# Ham thuoc do ban/dau mo nhieu
def dg_l(x:int):
    if x <= 50: return 0
    else: return round ((x - 50)/50,2)
#Ham thuoc do thoi gian giat rat nhanh
def t_f(t:int):
    if t <= 4: return 1
    elif t >= 18: return 0
    else: return round((18 - t)/14,2)
#Ham thuoc do thoi gian giat nhanh
def t_s(t:int):
    if (t <= 4 ) or (t >= 32): return 0
    elif t <= 18: return round((t - 4)/14,2)
    else: return round ((32 - t)/14,2)
#Ham thuoc do thoi gian giat trung binh
def t_m(t:int):
    if (t <= 18) or (t >= 46): return 0
    elif t <= 32: return round((t - 18)/14,2)
    else: return round((46 - t)/14,2)
#Ham thuoc do thoi gian giat cham
def t_l(t:int):
    if (t <= 32) or (t >= 60):
        return 0
    elif t < 46:
        return round((t - 32) / 14, 2)
    else:
        return round((60 - t) / 14, 2)
    
#Ham thuoc thoi gian giat rat cham
def t_v(t:int):
    if t <=46: return 0
    elif  t > 60 :return 1
    else: return round((t-46)/14,2)
x = int(input('Nhập độ bẩn: '))
y = int(input('Nhập lượng dầu mỡ: '))

w1 = float(min(dg_l(x), dg_l(y)))
w2 = float(min(dg_m(x), dg_l(y)))
w3 = float(min(dg_s(x), dg_l(y)))
w4 = float(min(dg_l(x), dg_m(y)))
w5 = float(min(dg_m(x), dg_m(y)))
w6 = float(min(dg_s(x), dg_m(y)))
w7 = float(min(dg_l(x), dg_s(y)))
w8 = float(min(dg_m(x), dg_s(y)))
w9 = float(min(dg_s(x), dg_s(y)))

Y = range(61); sum = 0; m = 0
for i in Y:
    T = w1*float(t_v(i)) + (w2+w3+w4)*float(t_l(i)) + (w5+w6+w7)*float(t_m(i)) + w8*float(t_s(i)) + w9*float(t_f(i))
    sum = sum + i*T
    m = m + T
t0 = round(sum/m,2)
if x <= 25:
    dirt_level = "bẩn ít"
elif x <= 75:
    dirt_level = "bẩn vừa"
else:
    dirt_level = "bẩn nhiều"

if y <= 25:
    grease_level = "dầu mỡ ít"
elif y <= 75:
    grease_level = "dầu mỡ vừa"
else:
    grease_level = "dầu mỡ nhiều"

if t0 <= 4:
    wash_time = "giặt rất nhanh"
elif t0 <= 18:
    wash_time = "giặt nhanh"
elif t0 <= 32:
    wash_time = "giặt nhanh bình thường"
elif t0 <= 46:
    wash_time = "giặt chậm"
else:
    wash_time = "giặt rất chậm"

print(f'Với độ bẩn {x} và lượng dầu mỡ {y} thì thời gian giặt là: {t0} phút')
print(f'Độ {dirt_level} và lượng {grease_level} thì {wash_time}')