import matplotlib.pyplot as plt
import numpy as np
import re

from pyneuroml import pynml


#plt.style.use('ggplot')
natsort = lambda s: [int(t) if t.isdigit() else t for t in re.split('(\d+)', s)]


def create_current_to_muscles_plots():
    results = pynml.run_lems_with_jneuroml("LEMS_c302_C2_AVB_DB_OLD.xml", nogui=True, load_saved_data=True)
    
    x = results['t']
    
    y = []
    names = {}
    for key in results.keys():
        if key.startswith('MDL') and key.endswith('iSyn'):
            muscle_number = int(key.split('/')[0][-2:])
            names[muscle_number] = key
            y.append(muscle_number)
    #y.sort(key=natsort)
    y.sort()
    y.reverse()
    
    print y
    print names
    x_n, y_n = np.meshgrid(x, y)
    #x_n = np.array(x)
    #y_n = np.array(y)

    currents = []
    for muscle_number in y:
        current_traces = results[names[muscle_number]]
        currents.append(current_traces)

    print len(x)
    print len(currents)
    print len(currents[0])
    print len(currents[1])
    currents = np.array(currents)
    
    plt.pcolormesh(x_n, y_n, currents)
    plt.colorbar() #need a colorbar to show the current scale
    plt.savefig('currents.png')
    #plt.show() #boom

    plt.clf()
    plt.close()

    for muscle_number in y:
        current_traces = results[names[muscle_number]]
        plt.plot(current_traces, label=muscle_number)

    plt.legend(loc='upper right')
    plt.savefig('currents_traces.png')

    
    

def main():
    create_current_to_muscles_plots() 




if __name__ == '__main__':
    main()