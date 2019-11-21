# -*- coding: utf-8 -*-
"""
ГА
"""
from __future__ import division  # Учитывать будущие обновления
import numpy as np
import matplotlib.pyplot as plt
import math

import utils 
from selection import selection
from crossover import crossover
from mutation import mutation

# вычисление искомой функции
def aimFunction(x):
    y=x+5*math.sin(5*x)+2*math.cos(3*x)
    return y


x=[i/100 for i in range(900)]  # генерация списка из 899 значений от 0 до 8.99
y=[0 for i in range(900)]  # генерация списка из 899 значений
for i in range(900):  # инициализация списка y значениями функции от х
    y[i]=aimFunction(x[i])
#plt.plot(x,y)


#initiate population
population=[]
for i  in range(10):
    entity=''
    for j in range(17):  
        entity=entity+str(np.random.randint(0,2))  # По идее, лепится строчная хромосома из 0, 1 и 2
    population.append(entity)  # По идее, в список популяции добавляется слепленная хромосома

    
t=[]
for i in range(1000):
    #selection
    value=utils.fitness(population,aimFunction)  # вызывается фитнес-функция из utils, иниц-ся популяцией и целевой функцией
    population_new=selection(population,value)  # (импортируется отбор) инициализируется новая популяция
    #crossover
    offspring =crossover(population_new,0.7)  #(импортируется скрещивание) происходит скрещивание
    #mutation
    population=mutation(offspring,0.02)  #(импортируется мутация) происходит мутация
    result=[]
    for j in range(len(population)):  # перебирает все элементы популяции
        result.append(aimFunction(utils.decode(population[j])))  # формируется список результата ф-ии от декод. эл-в поп-ии
    t.append(max(result))  # в список t записывается макс. результат
    
plt.plot(t)  # Вероятно, строит график
plt.axhline(max(y), linewidth=1, color='r')            
        

    


