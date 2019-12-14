# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 19:15:47 2019
import matplotlib.pyplot as plt
@author: Jackson
"""
import matplotlib.pyplot as plt


mcode_add = [0.8582558086036347, 0.7204181863536703, 0.5358778638683358]
mcode_remove = [0.6761359280554327, 0.613859649122807, 0.24981203007518796]
cnm_add = [0.9926496221215444, 0.9539975842198298, 0.9105724037617173]
cnm_remove = [0.9934991746345139, 0.96838081261558, 0.9362713610111696]
girvan_add = [0.987151360464399, 0.9460393823783642, 0.9120310275985005]
girvan_remove =[0.792520852347151, 0.7822273364207859, 0.7660224504480072]

add_names = ['add_1%', 'add_5%', 'add_10%']
remove_names =['remove_1%','remove_5%', 'remove_10%']


plt.figure(1)
plt.plot(add_names, mcode_add, linewidth=2.5)
plt.plot(add_names, cnm_add, linewidth=2.5, color='red')
plt.plot(add_names, girvan_add, linewidth=2.5, color='green')
plt.legend(['MCODE', 'Clauset-Newman-Moore', 'Girvan-Newman'], loc='bottom left')
plt.ylim(0,1)


plt.figure(2)
plt.plot(add_names, mcode_remove, linewidth=2.5)
plt.plot(add_names, cnm_remove, linewidth=2.5, color='red')
plt.plot(add_names, girvan_remove, linewidth=2.5, color='green')
plt.legend(['MCODE', 'Clauset-Newman-Moore', 'Girvan-Newman'], loc='bottom left')
plt.ylim(0,1)

plt.show()
