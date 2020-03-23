# Reading an excel file using Python 
import xlrd
import numpy as np
  
# Give the location of the file
loc = ('C:\\Users\\Vladimir\\Documents\\GitHub\\SVV_FD_B34\\reference_data.xlsx')   #reference_data.xlsx')
loc2 = ('C:\\Users\\Vladimir\\Documents\\GitHub\\SVV_FD_B34\\m_f_moment.xlsx')
  
# To open Workbook 
wb = xlrd.open_workbook(loc)
wb2 = xlrd.open_workbook(loc2)
sheet = wb.sheet_by_index(0)
sheet2 = wb2.sheet_by_index(0)


###############################################################################

##                  Mass fuel used - cg data - time                  ##

n_c = sheet.ncols
n_r = sheet.nrows
grid = []
for rows in range(n_r):
    col = []
    for cols in range(n_c):
        element = sheet.cell_value(rows,cols)
        col.append(element)
    grid.append(col)



m = []
for i in range(7,16):
    m.append((grid[i][7]))


st_fused = []
st_time = []
for i in range(27,33):
    st_fused.append(float(grid[i][8]))
    st_time.append(float(grid[i][1]))



elev_fused = []
elev_time = []
for i in range(58,65):
    elev_fused.append(float(grid[i][11]))
    elev_time.append(float(grid[i][1]))


cg = []
for i in range(74,76):
    cg.append((grid[i]))
cg = np.array(cg).reshape(2,13)


mass = np.array(m)/0.453592             #lbs
fu = np.concatenate(([0],st_fused, elev_fused, cg[:,-2]))    #lbs
ti = np.concatenate(([0],st_time, elev_time, cg[:,1]))       #days

fuel_used = []
time = []
for i in range(len(ti)):
    fuel_used.append(float(fu[i]))     #lbs
    time.append(float(ti[i])*24*60)           #min



###############################################################################

##                  Mass fuel - Moment                  ##


n_c2 = sheet2.ncols
n_r2 = sheet2.nrows
grid2 = []
for rows in range(n_r2):
    col = []
    for cols in range(n_c2):
        element = sheet2.cell_value(rows,cols)
        col.append(element)
    grid2.append(col)



m_f = []
M = []
for i in range(50):
    m_f.append((grid2[i][0]))  #lbs
    M.append(grid2[i][1]*100)      #lbs



