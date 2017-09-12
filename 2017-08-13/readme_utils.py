import os


def list_experiment_directories():

    unix_files = os.listdir('.')

    dirs = []
    for unix_file in unix_files:
        if os.path.isdir(unix_file):
            dirs.append(unix_file)
    dirs.sort()
    dirs.reverse()

    return dirs



def fff(dirs):
    
    readme = ''

    readme += '| Id | Neurons (membrane) | Neurons (membrane) | Muscles (membrane) | Muscles (membrane) | Neurons (activity) | Neurons (activity) | Muscles (activity) | Muscles (activity) |\n'    
    readme += '| :---         |     :---:      |     :---:     |     :---:     |     :---:     |     :---:     |     :---:     |     :---:     |     :---:     |\n'

    for edir in dirs:
        exp_arr = edir.split('_')[1:]
        exp = '_'.join(exp_arr)

        fig_dir = '%s/generated_files/figures' % edir

        figures = os.listdir(fig_dir)

        muscle_activity = None
        
        for fig in figures:

            
            if fig.startswith('neurons'):
                neuron = '%s/%s' % (fig_dir, fig)

            elif fig.startswith('neuron_activity'):
                neuron_activity = '%s/%s' % (fig_dir, fig)

            elif fig.startswith('muscles'):
                muscle = '%s/%s' % (fig_dir, fig)

            elif fig.startswith('muscle_activity'):
                muscle_activity = '%s/%s' % (fig_dir, fig)

            elif fig.startswith('traces_neuron_activity'):
                traces_neuron_activity = '%s/%s' % (fig_dir, fig)

            elif fig.startswith('traces_neuron'):
                traces_neuron = '%s/%s' % (fig_dir, fig)
    
            elif fig.startswith('traces_muscles_activity'):
                traces_muscle_activity = '%s/%s' % (fig_dir, fig)

            elif fig.startswith('traces_muscles'):
                traces_muscle = '%s/%s' % (fig_dir, fig)


        readme += '| [%s](%s) | ![%s](%s "%s") | ![%s](%s "%s") | ![%s](%s "%s") | ![%s](%s "%s") |' % (exp, edir, neuron, neuron, neuron.split('.')[0], traces_neuron, traces_neuron, traces_neuron.split('.')[0], muscle, muscle, muscle.split('.')[0], traces_muscle, traces_muscle, traces_muscle.split('.')[0],)

        if muscle_activity:
            readme += ' ![%s](%s "%s") | ![%s](%s "%s") | ![%s](%s "%s") | ![%s](%s "%s") |' % (neuron_activity, neuron_activity, neuron_activity.split('.')[0], traces_neuron_activity, traces_neuron_activity, traces_neuron_activity.split('.')[0], muscle_activity, muscle_activity, muscle_activity.split('.')[0], traces_muscle_activity, traces_muscle_activity, traces_muscle_activity.split('.')[0])
        else:
            readme += ' | | | |'
        readme += '\n'

    return readme
        
               


def main():
    dirs = list_experiment_directories()
    readme = fff(dirs)
    print readme

if __name__ == '__main__':
    main()
    
