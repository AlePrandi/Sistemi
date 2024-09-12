import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import csv

mese = []
temp = []
giacca = []
scuola = []
gio_gioco = []
data_file = open("./Ed_civica1.csv")
data_reader = csv.reader(data_file, delimiter=',')
for row in data_reader:
    mese.append(str(row[0]))
    temp.append(float(row[1]))
    giacca.append(float(row[2]))
    scuola.append(float(row[3]))
    gio_gioco.append(float(row[4]))
data_file.close()
    
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize= (11, 10))
fig.suptitle('Correlazione e causalità')

ax1.plot(mese, temp, 'red', linewidth = 5)
ax1.set_xlabel('Mese')
ax1.set_ylabel('Temperatura  \n media °C')
ax1.grid()

ax2.plot(mese, giacca, 'green', linewidth = 5)
ax2.set_xlabel('Mese')
ax2.set_ylabel('Giorni con \nla giacca')
ax2.grid()

ax3.plot(mese, scuola, 'blue', linewidth = 5)
ax3.set_xlabel('Mese')
ax3.set_ylabel('Giorni di \nscuola nel mese')
ax3.grid()

ax4.plot(mese, gio_gioco, 'yellow', linewidth = 5)
ax4.set_xlabel('Mese')
ax4.set_ylabel('Giorni di gioco')
ax4.grid()
ax4.set_ylim([10, 40])

plt.show()