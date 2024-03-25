import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import csv
#fonte Temp
#https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/global/time-series/globe/land_ocean/ytd/12/1918-2018?tr

#fonte Co2
#https://www.ildatomancante.it/opendata/tag/datipubblici/
#ricavato da dati noaa

#benzina
#https://dgsaie.mise.gov.it/prezzi-annuali-carburanti?pid=1

annoT = []
temp = []

annoC = []
co2 = []

annoB = []
prezzo = []
data_file1 = open("./Temp.csv")
data_reader1 = csv.reader(data_file1, delimiter=',')

data_file2 = open("./Co2.csv") 
data_reader2 = csv.reader(data_file2, delimiter=',')

data_file3 = open("./Benzina.csv") 
data_reader3 = csv.reader(data_file3, delimiter=',')

for row in data_reader1:
    annoT.append(int(row[0]))
    temp.append(float(row[1]))
data_file1.close()

for row in data_reader2:
    annoC.append(int(row[0]))
    co2.append(float(row[1]))
data_file2.close()

for row in data_reader3:
    annoB.append(int(row[0]))
    prezzo.append(float(row[1]) / 1000)
data_file3.close()
    
fig, (ax1,ax2,ax3) = plt.subplots(3, 1, figsize= (12, 7))
fig.suptitle('Ed civica')

ax1.plot(annoT, temp, 'red', linewidth = 3)
ax1.set_xlabel('Anno')
ax1.set_ylabel('Temperatura  \n media °C')
ax1.grid()
ax1.set_xlim([annoC[0], annoT[-1]])
ax1.set_xticks(range(annoC[0], annoT[-1] + 1, 5))#ogni 5 anni
ax1.set_ylim([-0.5, 1.5])

ax2.plot(annoC, co2, 'blue', linewidth = 3)
ax2.set_xlabel('Anno')
ax2.set_ylabel('Parti per milione')
ax2.grid()
ax2.set_xlim([annoC[0], annoC[-1]])
ax2.set_xticks(range(annoC[0], annoC[-1] + 1, 5))#ogni 5 anni

ax3.plot(annoB, prezzo, 'green', linewidth = 3)
ax3.set_xlabel('Anno')
ax3.set_ylabel('euro al litro')
ax3.grid()
ax3.set_xlim([annoB[0], annoB[-1]])
ax3.set_xticks(annoB)

plt.show()