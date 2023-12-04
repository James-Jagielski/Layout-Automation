def SPICE_read(x_lab1, y_lab1,pin_name1, x_lab2, y_lab2, pin_name2, file_name, cap_x, cap_y, cap_value):
    #names="inverter.sch"
    f = open(file_name, "a")
    f.write(f"\nC {{devices/lab_pin.sym}} {x_lab1} {y_lab1} 0 0 {{name=p1 sig_type=std_logic lab={pin_name1}}}\n")
    f.write(f"C {{devices/lab_pin.sym}} {x_lab2} {y_lab2} 0 0 {{name=p1 sig_type=std_logic lab={pin_name2}}}\n")
    f.write(f"C {{devices/lab_pin.sym}} {cap_x} {cap_y+30} 0 0 {{name=p1 sig_type=std_logic lab={pin_name1}}}\n")
    f.write(f"C {{devices/lab_pin.sym}} {cap_x} {cap_y-30} 0 0 {{name=p1 sig_type=std_logic lab={pin_name2}}}\n")
    f.write(f"C {{madvlsi/capacitor.sym}} {cap_x} {cap_y} 0 0 {{name=C1 value={cap_value}p m=1}}")
    f.close()
SPICE_read(190, -80, "Y",140, 0,"VN","inverter.sch",0,0,10)
