file_name="demofile2.mag"
grid_size=0.05
length=1
width=1

length_size=length/grid_size
length_size=width/grid_size
f = open(file_name, "w")
f.write("""magic
tech sky130A
timestamp 1694482379
""")
f.close()

f = open(file_name, "a")
f.write("<< nwell >>\n")
f.write("rect 0 0 10 10")
f.close()
#open and read the file after the appending:
f = open(file_name, "r")
print(f.read()) 