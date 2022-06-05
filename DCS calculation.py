import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import *

### Define the direction folder and import DCS file into DCS list

root = tk.Tk()
files_csv = fd.askopenfilenames()
df = pd.DataFrame()
DCS_list = []
for n in range(len(files_csv)):
    file_name = files_csv[n]
    data = pd.read_csv(file_name)
    DCS_list.append(data)
root.destroy()

### Input campaign ID for each table

def input():
    global i1
    i1 = input1.get()
    window.destroy()

window = tk.Tk()
tk.Label(window, text="Experiment ID").grid(row=0)
input1 = tk.Entry(window)
input1.grid(row=0, column=1)

tk.Button(window, text="Enter", command=input).grid(row=1, column=0)

window.mainloop()

### Definition of all calculation

def calculation(DCS):
    
    # Henry Constant
    DCS["Henry Constant"] = 0.034*np.exp(2400*(1/(DCS["TEMP"]+273.15)-1/298.15))
    
    # Recalculated dCO2
    DCS["Recalculated dCO2"] = (((DCS["Henry Constant"]*DCS["CO2_OUT"])*((DCS["press"]/14.5)+1.01))*440)
    
    # PUMP 2 feed rate
    FeedRate2 = np.array([])
    for n in range(len(DCS['LH'])):
        if n == 0:
            new_value = 0
        else:
            new_value = (DCS["PUMP2_SCL_G"][n-1]-DCS["PUMP2_SCL_G"][n])/(DCS["LH"][n]-DCS["LH"][n-1])
        FeedRate2 = np.append(FeedRate2,[new_value])
    DCS["PUMP 2 Feed Rate"] = FeedRate2.tolist()
    
    # PUMP 2 Feed Rate - 2hr 
    FeedRate2_2 = np.array([])
    for n in range(len(DCS['PUMP 2 Feed Rate'])):
        if n <= 1:
            new_value = 0
        else:
            new_value = np.average(DCS['PUMP 2 Feed Rate'][n-2:n+4])
        FeedRate2_2 = np.append(FeedRate2_2,[new_value])
    DCS['PUMP 2 Feed Rate - 2hr'] = FeedRate2_2.tolist()
    
    
    # PUMP 1 feed rate
    FeedRate1 = np.array([])
    for n in range(len(DCS['LH'])):
        if n == 0:
            new_value = 0
        else:
            new_value = (DCS["PUMP1_SCL_G"][n-1]-DCS["PUMP1_SCL_G"][n])/(DCS["LH"][n]-DCS["LH"][n-1])
        FeedRate1 = np.append(FeedRate1,[new_value])
    DCS["PUMP 1 Feed Rate"] = FeedRate1.tolist()
    
    # PUMP 1 Feed Rate - 2hr
    FeedRate1_2 = np.array([])
    for n in range(len(DCS['PUMP 1 Feed Rate'])):
        if n <= 1:
            new_value = 0
        else:
            new_value = np.average(DCS['PUMP 1 Feed Rate'][n-2:n+4])
        FeedRate1_2 = np.append(FeedRate1_2,[new_value])
    DCS['PUMP 1 Feed Rate - 2hr'] = FeedRate1_2.tolist()
    
     # PUMP 3 feed rate
    FeedRate3 = np.array([])
    for n in range(len(DCS['LH'])):
        if n == 0:
            new_value = 0
        else:
            new_value = (DCS["PUMP3_SCL_G"][n-1]-DCS["PUMP3_SCL_G"][n])/(DCS["LH"][n]-DCS["LH"][n-1])
        FeedRate3 = np.append(FeedRate3,[new_value])
    DCS["PUMP 3 Feed Rate"] = FeedRate3.tolist()
    
    # PUMP 3 Feed Rate - 2hr 
    FeedRate3_2 = np.array([])
    for n in range(len(DCS['PUMP 3 Feed Rate'])):
        if n <= 1:
            new_value = 0
        else:
            new_value = np.average(DCS['PUMP 3 Feed Rate'][n-2:n+4])
        FeedRate3_2 = np.append(FeedRate3_2,[new_value])
    DCS['PUMP 3 Feed Rate - 2hr'] = FeedRate3_2.tolist()
    
     # PUMP 4 feed rate
    FeedRate4 = np.array([])
    for n in range(len(DCS['LH'])):
        if n == 0:
            new_value = 0
        else:
            new_value = (DCS["PUMP4_SCL_G"][n-1]-DCS["PUMP4_SCL_G"][n])/(DCS["LH"][n]-DCS["LH"][n-1])
        FeedRate4 = np.append(FeedRate4,[new_value])
    DCS["PUMP 4 Feed Rate"] = FeedRate4.tolist()
    
    # PUMP 4 Feed Rate - 2hr 
    FeedRate4_2 = np.array([])
    for n in range(len(DCS['PUMP 4 Feed Rate'])):
        if n <= 1:
            new_value = 0
        else:
            new_value = np.average(DCS['PUMP 4 Feed Rate'][n-2:n+4])
        FeedRate4_2 = np.append(FeedRate4_2,[new_value])
    DCS['PUMP 4 Feed Rate - 2hr'] = FeedRate4_2.tolist()
    
     # PUMP 5 feed rate
    FeedRate5 = np.array([])
    for n in range(len(DCS['LH'])):
        if n == 0:
            new_value = 0
        else:
            new_value = (DCS["PUMP5_SCL_G"][n-1]-DCS["PUMP5_SCL_G"][n])/(DCS["LH"][n]-DCS["LH"][n-1])
        FeedRate5 = np.append(FeedRate5,[new_value])
    DCS["PUMP 5 Feed Rate"] = FeedRate5.tolist()
    
    # PUMP 5 Feed Rate - 2hr 
    FeedRate5_2 = np.array([])
    for n in range(len(DCS['PUMP 5 Feed Rate'])):
        if n <= 1:
            new_value = 0
        else:
            new_value = np.average(DCS['PUMP 5 Feed Rate'][n-2:n+4])
        FeedRate5_2 = np.append(FeedRate5_2,[new_value])
    DCS['PUMP 5 Feed Rate - 2hr'] = FeedRate5_2.tolist()
    
     # PUMP 6 feed rate
    FeedRate6 = np.array([])
    for n in range(len(DCS['LH'])):
        if n == 0:
            new_value = 0
        else:
            new_value = (DCS["PUMP6_SCL_G"][n-1]-DCS["PUMP6_SCL_G"][n])/(DCS["LH"][n]-DCS["LH"][n-1])
        FeedRate6 = np.append(FeedRate6,[new_value])
    DCS["PUMP 6 Feed Rate"] = FeedRate6.tolist()
    
    # PUMP 6 Feed Rate - 2hr 
    FeedRate6_2 = np.array([])
    for n in range(len(DCS['PUMP 6 Feed Rate'])):
        if n <= 1:
            new_value = 0
        else:
            new_value = np.average(DCS['PUMP 6 Feed Rate'][n-2:n+4])
        FeedRate6_2 = np.append(FeedRate6_2,[new_value])
    DCS['PUMP 6 Feed Rate - 2hr'] = FeedRate6_2.tolist()
    
    # Broth Wt_calc (kg)
    #Broth_Wt_Calc = np.array([])
    #for n in DCS['load']:
        #new_value = Broth_Wt + (n - DCS['load'][0])/1000 
        #Broth_Wt_Calc = np.append(Broth_Wt_Calc,[new_value])
    #DCS["Broth Wt_Calc, kg"] = Broth_Wt_Calc.tolist()   

    # Broth Density (g/L)
    DCS["Broth Density (g/L)"] = 1.000


    # CER_Calc (mmol/L-hr)
    DCS["CER_Calc"] = (600 * DCS["TOTFLOW"]/(DCS["broth_wt"]/DCS["Broth Density (g/L)"])) * (((DCS['CO2_OUT'] * (DCS["N2_IN"]/DCS["N2_OUT"]))-DCS["CO2_IN"])/(0.08206 * (273+25)))   

    # OUR_Calc (mmol/L-hr)
    DCS["OUR_Calc"] = (600*DCS["TOTFLOW"]/(DCS["broth_wt"]/DCS["Broth Density (g/L)"]))*((DCS["O2_IN"]-(DCS["O2_OUT"]*(DCS["N2_IN"]/DCS["N2_OUT"])))/(0.08206*(273+25)))


    # RQ
    DCS["RQ_Calc"] = DCS["CER_Calc"]/DCS["OUR_Calc"]

    # R_O2 (mmol/hr)
    DCS["R_O2, mmol/hr"] = DCS["broth_wt"] * DCS["OUR_Calc"]

    # R_CO2 (mmol/hr)
    DCS["R_CO2, mmol/hr"] = DCS["broth_wt"] * DCS["CER_Calc"]

    # Total O2 (mol)
    Total_O2 = np.array([])
    for n in range(len(DCS['R_O2, mmol/hr'])):
        if n == 0:
            new_value = 0
        else:
            new_value = (Total_O2[n-1] + (DCS['R_O2, mmol/hr'][n-1] + DCS['R_O2, mmol/hr'][n])/2 * (DCS["LH"][n] - DCS["LH"][n-1])/1000) 
        Total_O2 = np.append(Total_O2,[new_value])
    DCS["Total O2, mol"] = Total_O2.tolist() 

    # Total CO2 (mol)
    Total_CO2 = np.array([])
    for n in range(len(DCS['R_CO2, mmol/hr'])):
        if n == 0:
            new_value = 0
        else:
            new_value = (Total_CO2[n-1] + (DCS['R_CO2, mmol/hr'][n-1] + DCS['R_CO2, mmol/hr'][n])/2 * (DCS["LH"][n] - DCS["LH"][n-1])/1000) 
        Total_CO2 = np.append(Total_CO2,[new_value])
    DCS["Total CO2, mol"] = Total_CO2.tolist() 


    # dCO2 Calc (ppm)
    DCS["dCO2_Calc,ppm"] = 0.0298*(DCS['CO2_OUT'])*(1.5/14.5+1.01)*440

    # N2_IN mass (g)
    N2_IN = np.array([])
    for n in range(len(DCS["N2_IN"])):
        if n == 0:
            new_value = 0
        else:
            new_value = DCS["TOTFLOW"][n]*(0.009701*DCS["N2_IN"][n]+0.011525*DCS["O2_IN"][n]+0.007541*DCS["CO2_IN"][n])*DCS["N2_IN"][n]/100*28.014*0.040853*(DCS["LH"][n] - DCS["LH"][n-1])*60
        N2_IN = np.append(N2_IN,[new_value])
    DCS["N2_IN mass, g"] = N2_IN.tolist()

    # O2_IN mass (g)
    O2_IN = np.array([])
    for n in range(len(DCS["O2_IN"])):
        if n == 0:
            new_value = 0
        else:
            new_value = DCS["TOTFLOW"][n]*(0.009701*DCS["N2_IN"][n]+0.011525*DCS["O2_IN"][n]+0.007541*DCS["CO2_IN"][n])*DCS["O2_IN"][n]/100*31.998*0.040853*(DCS["LH"][n] - DCS["LH"][n-1])*60
        O2_IN = np.append(O2_IN,[new_value])
    DCS["O2_IN mass, g"] = O2_IN.tolist()

    # CO2_IN mass (g)
    CO2_IN = np.array([])
    for n in range(len(DCS["CO2_IN"])):
        if n == 0:
            new_value = 0
        else:
            new_value = DCS["TOTFLOW"][n]*(0.009701*DCS["N2_IN"][n]+0.011525*DCS["O2_IN"][n]+0.007541*DCS["CO2_IN"][n])*DCS["CO2_IN"][n]/100*44.009*0.040853*(DCS["LH"][n] - DCS["LH"][n-1])*60
        CO2_IN = np.append(CO2_IN,[new_value])
    DCS["CO2_IN mass, g"] = CO2_IN.tolist()

    # Total flow out
    DCS["Total flow_OUT"] = DCS["N2_IN"]/DCS["N2_OUT"]*DCS["TOTFLOW"]*(0.009701*DCS["N2_IN"]+0.011525*DCS["O2_IN"]+0.007541*DCS["CO2_IN"])


    # N2_OUT mass (g)
    N2_OUT = np.array([])
    for n in range(len(DCS["N2_OUT"])):
        if n == 0:
            new_value = 0
        else:
            new_value =DCS["Total flow_OUT"][n]*DCS["N2_OUT"][n]/100*28.014*0.040853*(DCS["LH"][n] - DCS["LH"][n-1])*60
        N2_OUT = np.append(N2_OUT,[new_value])
    DCS["N2_OUT mass, g"] = N2_OUT.tolist()


    # N2_OUT mass (g)
    N2_OUT = np.array([])
    for n in range(len(DCS["N2_OUT"])):
        if n == 0:
            new_value = 0
        else:
            new_value =DCS["Total flow_OUT"][n]*DCS["N2_OUT"][n]/100*28.014*0.040853*(DCS["LH"][n] - DCS["LH"][n-1])*60
        N2_OUT = np.append(N2_OUT,[new_value])
    DCS["N2_OUT mass, g"] = N2_OUT.tolist()

    # O2_OUT mass (g)
    O2_OUT = np.array([])
    for n in range(len(DCS["O2_OUT"])):
        if n == 0:
            new_value = 0
        else:
            new_value =DCS["Total flow_OUT"][n]*DCS["O2_OUT"][n]/100*31.998*0.040853*(DCS["LH"][n] - DCS["LH"][n-1])*60
        O2_OUT = np.append(O2_OUT,[new_value])
    DCS["O2_OUT mass, g"] = O2_OUT.tolist()


    # CO2_OUT mass (g)
    CO2_OUT = np.array([])
    for n in range(len(DCS["CO2_OUT"])):
        if n == 0:
            new_value = 0
        else:
            new_value =DCS["Total flow_OUT"][n]*DCS["CO2_OUT"][n]/100*44.009*0.040853*(DCS["LH"][n] - DCS["LH"][n-1])*60
        CO2_OUT = np.append(CO2_OUT,[new_value])
    DCS["CO2_OUT mass, g"] = CO2_OUT.tolist()


    # N2_IN Total (g)
    N2_IN_total = np.array([])
    for n in range(len(DCS["N2_IN mass, g"])):
        if n == 0:
            new_value = 0
        else:
            new_value = DCS["N2_IN mass, g"][n] + N2_IN_total[n-1]
        N2_IN_total = np.append(N2_IN_total, [new_value])
    DCS["N2_IN Total, g"] = N2_IN_total.tolist()


    # O2_IN Total (g)
    O2_IN_total = np.array([])
    for n in range(len(DCS["O2_IN mass, g"])):
        if n == 0:
            new_value = 0
        else:
            new_value = DCS["O2_IN mass, g"][n] + O2_IN_total[n-1]
        O2_IN_total = np.append(O2_IN_total, [new_value])
    DCS["O2_IN Total, g"] = O2_IN_total.tolist()


    # CO2_IN Total (g)
    CO2_IN_total = np.array([])
    for n in range(len(DCS["CO2_IN mass, g"])):
        if n == 0:
            new_value = 0
        else:
            new_value = DCS["CO2_IN mass, g"][n] + CO2_IN_total[n-1]
        CO2_IN_total = np.append(CO2_IN_total, [new_value])
    DCS["CO2_IN Total, g"] = CO2_IN_total.tolist()


    # N2_OUT Total (g)
    N2_OUT_total = np.array([])
    for n in range(len(DCS["N2_OUT mass, g"])):
        if n == 0:
            new_value = 0
        else:
            new_value = DCS["N2_OUT mass, g"][n] + N2_OUT_total[n-1]
        N2_OUT_total = np.append(N2_OUT_total, [new_value])
    DCS["N2_OUT Total, g"] = N2_OUT_total.tolist()


    # O2_OUT Total (g)
    O2_OUT_total = np.array([])
    for n in range(len(DCS["O2_OUT mass, g"])):
        if n == 0:
            new_value = 0
        else:
            new_value = DCS["O2_OUT mass, g"][n] + O2_OUT_total[n-1]
        O2_OUT_total = np.append(O2_OUT_total, [new_value])
    DCS["O2_OUT Total, g"] = O2_OUT_total.tolist()

    # CO2_OUT Total (g)
    CO2_OUT_total = np.array([])
    for n in range(len(DCS["CO2_OUT mass, g"])):
        if n == 0:
            new_value = 0
        else:
            new_value = DCS["CO2_OUT mass, g"][n] + CO2_OUT_total[n-1]
        CO2_OUT_total = np.append(CO2_OUT_total, [new_value])
    DCS["CO2_OUT Total, g"] = CO2_OUT_total.tolist()

    return 0


### Organize raw dataframe, removing useless columne, do calculation and then save into new_DCS_list
### Summary file = compile all individual tables together, which is for AWS data calculation input
n = 0
new_DCS_list = []
for DCS in DCS_list:
    #if "PUMP3_SCL_G" and "PUMP3_SCL_T" in list(DCS.columns):
    #    DCS.drop(['PUMP3_SCL_G','PUMP3_SCL_T'], axis = 1, inplace=True)          # Remove column scale3_g and scale3_t
    DCS.insert(0, "Experiment_ID", i1)                                                    # Assign Experiment ID
    DCS.insert(1, "data_table", "online_data") 
    DCS['press'] = 1.5                                                            # assign pressure value
    DCS.insert(2,'bioreactor_ID','')                                                  # Insert Vessel to the first column and assign vessel ID
    DCS["bioreactor_ID"] = files_csv[n][-29:-26]   
    n += 1
    calculation(DCS)
    new_DCS_list.append(DCS)
summary = pd.concat(new_DCS_list, sort=False)


### Write all calculated dataframe into excel

data = pd.ExcelWriter('DCS_suammry.xlsx', engine='xlsxwriter')
n = 0
for table in new_DCS_list:
    table.to_excel(data,
                  sheet_name = "DCS-" + files_csv[n][-29:-26])
    n += 1
summary.to_excel(data, sheet_name = "summary")
data.save()
data.close()


### Creat different table based on variables and then plot
# create all individual tables...
new_table = pd.DataFrame()
# determine the value of max row from each tables
max_row = 0
max_idx = 0
for i in range(len(new_DCS_list)):
    if len(new_DCS_list[i]) > max_row:
        max_row = len(new_DCS_list[i])
        max_idx = i

# Function: creating table based on column name
def making_table(index):
    new_table["LH"] = new_DCS_list[max_idx]["LH"]
    n = 0
    for table in new_DCS_list: 
        column_name = files_csv[n][-29:-26]
        new_table[column_name] = table[index]
        n += 1
    globals()[index] = new_table
    return globals()[index]


test_list = ['pH', 'pH2', 'TEMP', 'AGIT', 'DO1', 'DO2', 'AIR', 'O2',
       'TOTFLOW', 'CER', 'OUR', 'TOTCO2', 'TOTO2', 'RO2', 'RC02', 'RQ', 'CO2_IN', 'N2_IN', 'O2_IN', 'CO2_OUT',
       'N2_OUT', 'O2_OUT', 'PUMP1_SCL_G', 'PUMP1_SCL_T', 'PUMP2_SCL_G', 'PUMP2_SCL_T',
       'PUMP3_SCL_G', 'PUMP3_SCL_T', 'PUMP4_SCL_G', 'PUMP4_SCL_T',
       'PUMP5_SCL_G', 'PUMP5_SCL_T', 'PUMP6_SCL_G', 'PUMP6_SCL_T',
       'load', 'dco2', 'broth_wt', 'Henry Constant',
       'PUMP 1 Feed Rate', 'PUMP 1 Feed Rate - 2hr',
       'PUMP 2 Feed Rate', 'PUMP 2 Feed Rate - 2hr',
       'PUMP 3 Feed Rate', 'PUMP 3 Feed Rate - 2hr',
       'PUMP 4 Feed Rate', 'PUMP 4 Feed Rate - 2hr',
       'PUMP 5 Feed Rate', 'PUMP 5 Feed Rate - 2hr',
       'PUMP 6 Feed Rate', 'PUMP 6 Feed Rate - 2hr',
       'broth_wt',"CER_Calc","OUR_Calc",
       'RQ_Calc',
       'Total O2, mol', 'Total CO2, mol', 'dCO2_Calc,ppm', 'N2_IN mass, g',
       'O2_IN mass, g', 'CO2_IN mass, g', 'Total flow_OUT', 'N2_OUT mass, g',
       'O2_OUT mass, g', 'CO2_OUT mass, g', 'N2_IN Total, g', 'O2_IN Total, g',
       'CO2_IN Total, g', 'N2_OUT Total, g', 'O2_OUT Total, g',
       'CO2_OUT Total, g']

graph_data = pd.ExcelWriter('DCS_graph.xlsx', engine='xlsxwriter')

#max_row = len(new_DCS_list[max_idx])
for name in test_list:
    new_table = making_table(name)
    new_table.to_excel(graph_data,
                  sheet_name = name)
    
    # making the graph based on the table
    workbook = graph_data.book
    worksheet = graph_data.sheets[name]
    chart = workbook.add_chart({'type': 'scatter',
                             'subtype': 'straight_with_markers'})
   
    for n in range(len(files_csv)):
        col = n + 2
        chart.add_series({
                'name':       [name, 0, col],
                'categories': [name, 1, 1, max_row, 1],
                'values':     [name, 1, col, max_row, col],
                'marker':     {'type': 'circle', 'size': 4},
        })
    worksheet.insert_chart('K2', chart)
    
    
    
graph_data.save()  
graph_data.close()
