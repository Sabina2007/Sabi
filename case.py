#место для твоего кода
import pandas as pd 
import matplotlib.pyplot as plt
df = pd.read_csv('countries of the world.csv')
print(df.info())

df = df.dropna()
#df.info
#print(df['Deathrate'].value_counts())

def death_apply(death):
    death = death.replace(',','.')
    return float(death)

df['Deathrate'] = df['Deathrate'].apply(death_apply)   


def pop_apply(death):
    death = death.replace(',','.')
    return float(death)
df['Pop. Density (per sq. mi.)']=df['Pop. Density (per sq. mi.)'].apply(pop_apply)    
df.info()

counrty_up = 0
counrty_down = 0
c_up = 0
c_down = 0

def pop_dens_death(row):
    global c_down, c_up, counrty_down, counrty_up
    if row['Pop. Density (per sq. mi.)']>=295:
        counrty_up += row['Deathrate']
        c_up+=1
    else:
        counrty_down += row['Deathrate']
        c_down+=1
    return False

df.apply(pop_dens_death, axis = 1)
a = counrty_up/c_up
b = counrty_down/c_down
print('Средняя смертнотсь для большой плотности:', a,)
print('Средняя смертность для маленькой плотности:',b,)        

s = pd.Series(data = [a,b],
index = [' большая \n плотность население', ' маленькая \n плотность населения'])
s.plot(kind = 'barh')
plt.show()
