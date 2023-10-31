from reading_schematic import SPICE_read
length, width=SPICE_read()
length=int(length/0.15)
print(length,width)
file_name="demofile2.mag"
grid_size=0.05

length_size=length/grid_size
length_size=width/grid_size
f = open(file_name, "w")
f.write("""magic
tech sky130A
timestamp 1694482379
""")
f.close()
f = open(file_name, "a")
f.write("<< psubdiff >>\n")
f.write(f"rect 0 0 55 {85*width}\n")
f.write("<< ndiff >>\n")
f.write(f"rect 55 0 {170+15*(length-1)} {85*width}\n")
f.write("<< poly >>\n")
f.write(f"rect 105 -15 {120+15*(length-1)} {85*width}\n")
f.write("<< locali >>\n")
f.write(f"rect 5 5 100 {85*width}\n")
f.write(f"rect {125+15*(length-1)} 5 {165+15*(length-1)} {85*width}\n")
f.write("<< ndiffc >>\n")
f.write(f"rect {135+15*(length-1)} 15 {155+15*(length-1)} {85*width}\n")
f.write(f"rect 20 15 40 {85*width}\n")
f.write(f"rect 70 15 90 {85*width}\n")
f.write("<< viali >>\n")
f.write(f"rect 20 15 40 {85*width}\n")
f.write(f"rect 70 15 90 {85*width}\n")
f.write("<< metal1 >>\n")
f.write(f"rect -15 5 {185+15*(length-1)} {85*width}\n")


f.write(f"\
<< nmos >>\n\
rect 105 {85*width} {120+15*(length-1)} {85*width+15}\n\
<< ndiff >>\n\
rect 55 {85*width} 105 {85*width+15}\n\
rect 120 {85*width} {170+15*(length-1)} {85*width+15}\n\
<< psubdiff >>\n\
rect 0 {85*width} 55 {85*width+15}\n\
<< poly >>\n\
rect 105 {85*width+15} {120+15*(length-1)} {85*width+30}\n\
<< locali >>\n\
rect 5 {85*width} 100 {85*width+10}\n\
rect {125+15*(length-1)} {85*width} {165+15*(length-1)} {85*width+10}\n\
<< metal1 >>\n\
rect -15 {85*width} {185+15*(length-1)} {85*width+10}\n")
f.write("<< end >>\n")
f.close()
#open and read the file after the appending:
f = open(file_name, "r")
print(f.read()) 


"""
f = open(file_name, "a")
f.write("<< psubdiff >>\n")
f.write(f"rect 0 0 55 {100*width}\n")
f.write("<< ndiff >>\n")
f.write(f"rect 55 0 170 {100*width}\n")
f.write("<< poly >>\n")
f.write(f"rect 105 -15 120 {115*width}\n")
f.write("<< locali >>\n")
f.write(f"rect 5 5 100 {95*width}\n")
f.write(f"rect 125 5 165 {95*width}\n")
f.write("<< ndiffc >>\n")
f.write(f"rect 135 15 155 {85*width}\n")
f.write(f"rect 20 15 40 {85*width}\n")
f.write(f"rect 70 15 90 {85*width}\n")
f.write("<< viali >>\n")
f.write(f"rect 20 15 40 {85*width}\n")
f.write(f"rect 70 15 90 {85*width}\n")
f.write("<< metal1 >>\n")
f.write(f"rect -15 5 185 {95*width}\n")
f.write("<< end >>\n")
"""