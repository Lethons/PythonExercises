slow_v = 6*60 + 10
fast_v = 4*60 + 30
run_time_m = (1.6*slow_v + 4.8*fast_v + 1.6*slow_v)//60
breakfast_time_h = 6 + run_time_m//60
breakfast_time_m = 52 + run_time_m%60
if breakfast_time_m >= 60:
    breakfast_time_h += 1
    breakfast_time_m -= 60
print(str(int(breakfast_time_h)) + ':' + str(int(breakfast_time_m)))
