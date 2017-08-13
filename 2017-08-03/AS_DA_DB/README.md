<img src="AS-DA-DB_all_conns.jpeg" width="380"><img src="AS-DA-DB_subset_conns.jpeg" width="380">

# Network:

### Neural Circuit:

- Command neurons: AVA, AVB
- Motor neurons: AS, DA, DB
- Muscles: All

### Connections:

See experiment

### Simulation Setup:

- duration: see experiment
- dt: 0.05
- Injected current: see experiment


# Description

In these experiments we wanted to recreate Figure 6 (A2) of *"A ventral nerve cord CPG may underlie locomotion in C. elegans"* (Olivares et al.)

They described an oscillating circuit with AS, DA, and DB motor neurons.  
AS reaches an active steady state without any synaptic input.
AS stimulates DA through excitatory synapses and DA stimulates DB also through excitatory synapses.
DB inhibits AS through inhibitory synapses, thus diminished excitatory synaptic current to DA, thus also the activity of DB reduces, thus diminished inhibitory input to AS.
Without inhibitory input to AS, they can reach an active state again and we have come full circle.

In the first experiments (case01-06) we included all connections from the connectome we use and injected current into AVB or AVA and AS motor neurons to approximate the active state of AS.

Then we included only a subset (the same subset for every experiment) of connections and changed the conductance of excitatory and inhibitory synapses - only one value for all the excitatory and one value for all the inhibitory synapses.

We couldn't manage to get oscillatory behavior. This could be due to electrical synapses with a too high conductance.


# Result of experiments
| Id | Neurons (membrane) | Neurons (membrane) | Muscles (membrane) | Muscles (membrane) | Neurons (activity) | Neurons (activity) | Muscles (activity) | Muscles (activity) |
| :---         |     :---:      |     :---:     |     :---:     |     :---:     |     :---:     |     :---:     |     :---:     |     :---:     |
| [case22](case22) | ![case22/generated_files/figures/neurons_C2_AS_DA_DB.png](case22/generated_files/figures/neurons_C2_AS_DA_DB.png "case22/generated_files/figures/neurons_C2_AS_DA_DB") | ![case22/generated_files/figures/traces_neuron_AS_DA_DB_C2.png](case22/generated_files/figures/traces_neuron_AS_DA_DB_C2.png "case22/generated_files/figures/traces_neuron_AS_DA_DB_C2") | ![case22/generated_files/figures/muscles_C2_AS_DA_DB.png](case22/generated_files/figures/muscles_C2_AS_DA_DB.png "case22/generated_files/figures/muscles_C2_AS_DA_DB") | ![case22/generated_files/figures/traces_muscles_AS_DA_DB_C2.png](case22/generated_files/figures/traces_muscles_AS_DA_DB_C2.png "case22/generated_files/figures/traces_muscles_AS_DA_DB_C2") | ![case22/generated_files/figures/neuron_activity_C2_AS_DA_DB.png](case22/generated_files/figures/neuron_activity_C2_AS_DA_DB.png "case22/generated_files/figures/neuron_activity_C2_AS_DA_DB") | ![case22/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2.png](case22/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2.png "case22/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2") | ![case22/generated_files/figures/muscle_activity_C2_AS_DA_DB.png](case22/generated_files/figures/muscle_activity_C2_AS_DA_DB.png "case22/generated_files/figures/muscle_activity_C2_AS_DA_DB") | ![case22/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2.png](case22/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2.png "case22/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2") |
| [case21](case21) | ![case21/generated_files/figures/neurons_C2_AS_DA_DB.png](case21/generated_files/figures/neurons_C2_AS_DA_DB.png "case21/generated_files/figures/neurons_C2_AS_DA_DB") | ![case21/generated_files/figures/traces_neuron_AS_DA_DB_C2.png](case21/generated_files/figures/traces_neuron_AS_DA_DB_C2.png "case21/generated_files/figures/traces_neuron_AS_DA_DB_C2") | ![case21/generated_files/figures/muscles_C2_AS_DA_DB.png](case21/generated_files/figures/muscles_C2_AS_DA_DB.png "case21/generated_files/figures/muscles_C2_AS_DA_DB") | ![case21/generated_files/figures/traces_muscles_AS_DA_DB_C2.png](case21/generated_files/figures/traces_muscles_AS_DA_DB_C2.png "case21/generated_files/figures/traces_muscles_AS_DA_DB_C2") | ![case21/generated_files/figures/neuron_activity_C2_AS_DA_DB.png](case21/generated_files/figures/neuron_activity_C2_AS_DA_DB.png "case21/generated_files/figures/neuron_activity_C2_AS_DA_DB") | ![case21/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2.png](case21/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2.png "case21/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2") | ![case21/generated_files/figures/muscle_activity_C2_AS_DA_DB.png](case21/generated_files/figures/muscle_activity_C2_AS_DA_DB.png "case21/generated_files/figures/muscle_activity_C2_AS_DA_DB") | ![case21/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2.png](case21/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2.png "case21/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2") |
| [case20](case20) | ![case20/generated_files/figures/neurons_C2_AS_DA_DB.png](case20/generated_files/figures/neurons_C2_AS_DA_DB.png "case20/generated_files/figures/neurons_C2_AS_DA_DB") | ![case20/generated_files/figures/traces_neuron_AS_DA_DB_C2.png](case20/generated_files/figures/traces_neuron_AS_DA_DB_C2.png "case20/generated_files/figures/traces_neuron_AS_DA_DB_C2") | ![case20/generated_files/figures/muscles_C2_AS_DA_DB.png](case20/generated_files/figures/muscles_C2_AS_DA_DB.png "case20/generated_files/figures/muscles_C2_AS_DA_DB") | ![case20/generated_files/figures/traces_muscles_AS_DA_DB_C2.png](case20/generated_files/figures/traces_muscles_AS_DA_DB_C2.png "case20/generated_files/figures/traces_muscles_AS_DA_DB_C2") | ![case20/generated_files/figures/neuron_activity_C2_AS_DA_DB.png](case20/generated_files/figures/neuron_activity_C2_AS_DA_DB.png "case20/generated_files/figures/neuron_activity_C2_AS_DA_DB") | ![case20/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2.png](case20/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2.png "case20/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2") | ![case20/generated_files/figures/muscle_activity_C2_AS_DA_DB.png](case20/generated_files/figures/muscle_activity_C2_AS_DA_DB.png "case20/generated_files/figures/muscle_activity_C2_AS_DA_DB") | ![case20/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2.png](case20/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2.png "case20/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2") |
| [case19](case19) | ![case19/generated_files/figures/neurons_C2_AS_DA_DB.png](case19/generated_files/figures/neurons_C2_AS_DA_DB.png "case19/generated_files/figures/neurons_C2_AS_DA_DB") | ![case19/generated_files/figures/traces_neuron_AS_DA_DB_C2.png](case19/generated_files/figures/traces_neuron_AS_DA_DB_C2.png "case19/generated_files/figures/traces_neuron_AS_DA_DB_C2") | ![case19/generated_files/figures/muscles_C2_AS_DA_DB.png](case19/generated_files/figures/muscles_C2_AS_DA_DB.png "case19/generated_files/figures/muscles_C2_AS_DA_DB") | ![case19/generated_files/figures/traces_muscles_AS_DA_DB_C2.png](case19/generated_files/figures/traces_muscles_AS_DA_DB_C2.png "case19/generated_files/figures/traces_muscles_AS_DA_DB_C2") | ![case19/generated_files/figures/neuron_activity_C2_AS_DA_DB.png](case19/generated_files/figures/neuron_activity_C2_AS_DA_DB.png "case19/generated_files/figures/neuron_activity_C2_AS_DA_DB") | ![case19/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2.png](case19/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2.png "case19/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2") | ![case19/generated_files/figures/muscle_activity_C2_AS_DA_DB.png](case19/generated_files/figures/muscle_activity_C2_AS_DA_DB.png "case19/generated_files/figures/muscle_activity_C2_AS_DA_DB") | ![case19/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2.png](case19/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2.png "case19/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2") |
| [case18](case18) | ![case18/generated_files/figures/neurons_C2_AS_DA_DB.png](case18/generated_files/figures/neurons_C2_AS_DA_DB.png "case18/generated_files/figures/neurons_C2_AS_DA_DB") | ![case18/generated_files/figures/traces_neuron_AS_DA_DB_C2.png](case18/generated_files/figures/traces_neuron_AS_DA_DB_C2.png "case18/generated_files/figures/traces_neuron_AS_DA_DB_C2") | ![case18/generated_files/figures/muscles_C2_AS_DA_DB.png](case18/generated_files/figures/muscles_C2_AS_DA_DB.png "case18/generated_files/figures/muscles_C2_AS_DA_DB") | ![case18/generated_files/figures/traces_muscles_AS_DA_DB_C2.png](case18/generated_files/figures/traces_muscles_AS_DA_DB_C2.png "case18/generated_files/figures/traces_muscles_AS_DA_DB_C2") | ![case18/generated_files/figures/neuron_activity_C2_AS_DA_DB.png](case18/generated_files/figures/neuron_activity_C2_AS_DA_DB.png "case18/generated_files/figures/neuron_activity_C2_AS_DA_DB") | ![case18/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2.png](case18/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2.png "case18/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2") | ![case18/generated_files/figures/muscle_activity_C2_AS_DA_DB.png](case18/generated_files/figures/muscle_activity_C2_AS_DA_DB.png "case18/generated_files/figures/muscle_activity_C2_AS_DA_DB") | ![case18/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2.png](case18/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2.png "case18/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2") |
| [case17](case17) | ![case17/generated_files/figures/neurons_C2_AS_DA_DB.png](case17/generated_files/figures/neurons_C2_AS_DA_DB.png "case17/generated_files/figures/neurons_C2_AS_DA_DB") | ![case17/generated_files/figures/traces_neuron_AS_DA_DB_C2.png](case17/generated_files/figures/traces_neuron_AS_DA_DB_C2.png "case17/generated_files/figures/traces_neuron_AS_DA_DB_C2") | ![case17/generated_files/figures/muscles_C2_AS_DA_DB.png](case17/generated_files/figures/muscles_C2_AS_DA_DB.png "case17/generated_files/figures/muscles_C2_AS_DA_DB") | ![case17/generated_files/figures/traces_muscles_AS_DA_DB_C2.png](case17/generated_files/figures/traces_muscles_AS_DA_DB_C2.png "case17/generated_files/figures/traces_muscles_AS_DA_DB_C2") | ![case17/generated_files/figures/neuron_activity_C2_AS_DA_DB.png](case17/generated_files/figures/neuron_activity_C2_AS_DA_DB.png "case17/generated_files/figures/neuron_activity_C2_AS_DA_DB") | ![case17/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2.png](case17/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2.png "case17/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2") | ![case17/generated_files/figures/muscle_activity_C2_AS_DA_DB.png](case17/generated_files/figures/muscle_activity_C2_AS_DA_DB.png "case17/generated_files/figures/muscle_activity_C2_AS_DA_DB") | ![case17/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2.png](case17/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2.png "case17/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2") |
| [case16](case16) | ![case16/generated_files/figures/neurons_C2_AS_DA_DB.png](case16/generated_files/figures/neurons_C2_AS_DA_DB.png "case16/generated_files/figures/neurons_C2_AS_DA_DB") | ![case16/generated_files/figures/traces_neuron_AS_DA_DB_C2.png](case16/generated_files/figures/traces_neuron_AS_DA_DB_C2.png "case16/generated_files/figures/traces_neuron_AS_DA_DB_C2") | ![case16/generated_files/figures/muscles_C2_AS_DA_DB.png](case16/generated_files/figures/muscles_C2_AS_DA_DB.png "case16/generated_files/figures/muscles_C2_AS_DA_DB") | ![case16/generated_files/figures/traces_muscles_AS_DA_DB_C2.png](case16/generated_files/figures/traces_muscles_AS_DA_DB_C2.png "case16/generated_files/figures/traces_muscles_AS_DA_DB_C2") | ![case16/generated_files/figures/neuron_activity_C2_AS_DA_DB.png](case16/generated_files/figures/neuron_activity_C2_AS_DA_DB.png "case16/generated_files/figures/neuron_activity_C2_AS_DA_DB") | ![case16/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2.png](case16/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2.png "case16/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2") | ![case16/generated_files/figures/muscle_activity_C2_AS_DA_DB.png](case16/generated_files/figures/muscle_activity_C2_AS_DA_DB.png "case16/generated_files/figures/muscle_activity_C2_AS_DA_DB") | ![case16/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2.png](case16/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2.png "case16/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2") |
| [case15](case15) | ![case15/generated_files/figures/neurons_C2_AS_DA_DB.png](case15/generated_files/figures/neurons_C2_AS_DA_DB.png "case15/generated_files/figures/neurons_C2_AS_DA_DB") | ![case15/generated_files/figures/traces_neuron_AS_DA_DB_C2.png](case15/generated_files/figures/traces_neuron_AS_DA_DB_C2.png "case15/generated_files/figures/traces_neuron_AS_DA_DB_C2") | ![case15/generated_files/figures/muscles_C2_AS_DA_DB.png](case15/generated_files/figures/muscles_C2_AS_DA_DB.png "case15/generated_files/figures/muscles_C2_AS_DA_DB") | ![case15/generated_files/figures/traces_muscles_AS_DA_DB_C2.png](case15/generated_files/figures/traces_muscles_AS_DA_DB_C2.png "case15/generated_files/figures/traces_muscles_AS_DA_DB_C2") | ![case15/generated_files/figures/neuron_activity_C2_AS_DA_DB.png](case15/generated_files/figures/neuron_activity_C2_AS_DA_DB.png "case15/generated_files/figures/neuron_activity_C2_AS_DA_DB") | ![case15/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2.png](case15/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2.png "case15/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2") | ![case15/generated_files/figures/muscle_activity_C2_AS_DA_DB.png](case15/generated_files/figures/muscle_activity_C2_AS_DA_DB.png "case15/generated_files/figures/muscle_activity_C2_AS_DA_DB") | ![case15/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2.png](case15/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2.png "case15/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2") |
| [case14](case14) | ![case14/generated_files/figures/neurons_C2_AS_DA_DB.png](case14/generated_files/figures/neurons_C2_AS_DA_DB.png "case14/generated_files/figures/neurons_C2_AS_DA_DB") | ![case14/generated_files/figures/traces_neuron_AS_DA_DB_C2.png](case14/generated_files/figures/traces_neuron_AS_DA_DB_C2.png "case14/generated_files/figures/traces_neuron_AS_DA_DB_C2") | ![case14/generated_files/figures/muscles_C2_AS_DA_DB.png](case14/generated_files/figures/muscles_C2_AS_DA_DB.png "case14/generated_files/figures/muscles_C2_AS_DA_DB") | ![case14/generated_files/figures/traces_muscles_AS_DA_DB_C2.png](case14/generated_files/figures/traces_muscles_AS_DA_DB_C2.png "case14/generated_files/figures/traces_muscles_AS_DA_DB_C2") | ![case14/generated_files/figures/neuron_activity_C2_AS_DA_DB.png](case14/generated_files/figures/neuron_activity_C2_AS_DA_DB.png "case14/generated_files/figures/neuron_activity_C2_AS_DA_DB") | ![case14/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2.png](case14/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2.png "case14/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2") | ![case14/generated_files/figures/muscle_activity_C2_AS_DA_DB.png](case14/generated_files/figures/muscle_activity_C2_AS_DA_DB.png "case14/generated_files/figures/muscle_activity_C2_AS_DA_DB") | ![case14/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2.png](case14/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2.png "case14/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2") |
| [case13](case13) | ![case13/generated_files/figures/neurons_C2_AS_DA_DB.png](case13/generated_files/figures/neurons_C2_AS_DA_DB.png "case13/generated_files/figures/neurons_C2_AS_DA_DB") | ![case13/generated_files/figures/traces_neuron_AS_DA_DB_C2.png](case13/generated_files/figures/traces_neuron_AS_DA_DB_C2.png "case13/generated_files/figures/traces_neuron_AS_DA_DB_C2") | ![case13/generated_files/figures/muscles_C2_AS_DA_DB.png](case13/generated_files/figures/muscles_C2_AS_DA_DB.png "case13/generated_files/figures/muscles_C2_AS_DA_DB") | ![case13/generated_files/figures/traces_muscles_AS_DA_DB_C2.png](case13/generated_files/figures/traces_muscles_AS_DA_DB_C2.png "case13/generated_files/figures/traces_muscles_AS_DA_DB_C2") | ![case13/generated_files/figures/neuron_activity_C2_AS_DA_DB.png](case13/generated_files/figures/neuron_activity_C2_AS_DA_DB.png "case13/generated_files/figures/neuron_activity_C2_AS_DA_DB") | ![case13/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2.png](case13/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2.png "case13/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2") | ![case13/generated_files/figures/muscle_activity_C2_AS_DA_DB.png](case13/generated_files/figures/muscle_activity_C2_AS_DA_DB.png "case13/generated_files/figures/muscle_activity_C2_AS_DA_DB") | ![case13/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2.png](case13/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2.png "case13/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2") |
| [case12](case12) | ![case12/generated_files/figures/neurons_C2_AS_DA_DB.png](case12/generated_files/figures/neurons_C2_AS_DA_DB.png "case12/generated_files/figures/neurons_C2_AS_DA_DB") | ![case12/generated_files/figures/traces_neuron_AS_DA_DB_C2.png](case12/generated_files/figures/traces_neuron_AS_DA_DB_C2.png "case12/generated_files/figures/traces_neuron_AS_DA_DB_C2") | ![case12/generated_files/figures/muscles_C2_AS_DA_DB.png](case12/generated_files/figures/muscles_C2_AS_DA_DB.png "case12/generated_files/figures/muscles_C2_AS_DA_DB") | ![case12/generated_files/figures/traces_muscles_AS_DA_DB_C2.png](case12/generated_files/figures/traces_muscles_AS_DA_DB_C2.png "case12/generated_files/figures/traces_muscles_AS_DA_DB_C2") | ![case12/generated_files/figures/neuron_activity_C2_AS_DA_DB.png](case12/generated_files/figures/neuron_activity_C2_AS_DA_DB.png "case12/generated_files/figures/neuron_activity_C2_AS_DA_DB") | ![case12/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2.png](case12/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2.png "case12/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2") | ![case12/generated_files/figures/muscle_activity_C2_AS_DA_DB.png](case12/generated_files/figures/muscle_activity_C2_AS_DA_DB.png "case12/generated_files/figures/muscle_activity_C2_AS_DA_DB") | ![case12/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2.png](case12/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2.png "case12/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2") |
| [case11](case11) | ![case11/generated_files/figures/neurons_C2_AS_DA_DB.png](case11/generated_files/figures/neurons_C2_AS_DA_DB.png "case11/generated_files/figures/neurons_C2_AS_DA_DB") | ![case11/generated_files/figures/traces_neuron_AS_DA_DB_C2.png](case11/generated_files/figures/traces_neuron_AS_DA_DB_C2.png "case11/generated_files/figures/traces_neuron_AS_DA_DB_C2") | ![case11/generated_files/figures/muscles_C2_AS_DA_DB.png](case11/generated_files/figures/muscles_C2_AS_DA_DB.png "case11/generated_files/figures/muscles_C2_AS_DA_DB") | ![case11/generated_files/figures/traces_muscles_AS_DA_DB_C2.png](case11/generated_files/figures/traces_muscles_AS_DA_DB_C2.png "case11/generated_files/figures/traces_muscles_AS_DA_DB_C2") | ![case11/generated_files/figures/neuron_activity_C2_AS_DA_DB.png](case11/generated_files/figures/neuron_activity_C2_AS_DA_DB.png "case11/generated_files/figures/neuron_activity_C2_AS_DA_DB") | ![case11/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2.png](case11/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2.png "case11/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2") | ![case11/generated_files/figures/muscle_activity_C2_AS_DA_DB.png](case11/generated_files/figures/muscle_activity_C2_AS_DA_DB.png "case11/generated_files/figures/muscle_activity_C2_AS_DA_DB") | ![case11/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2.png](case11/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2.png "case11/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2") |
| [case10](case10) | ![case10/generated_files/figures/neurons_C2_AS_DA_DB.png](case10/generated_files/figures/neurons_C2_AS_DA_DB.png "case10/generated_files/figures/neurons_C2_AS_DA_DB") | ![case10/generated_files/figures/traces_neuron_AS_DA_DB_C2.png](case10/generated_files/figures/traces_neuron_AS_DA_DB_C2.png "case10/generated_files/figures/traces_neuron_AS_DA_DB_C2") | ![case10/generated_files/figures/muscles_C2_AS_DA_DB.png](case10/generated_files/figures/muscles_C2_AS_DA_DB.png "case10/generated_files/figures/muscles_C2_AS_DA_DB") | ![case10/generated_files/figures/traces_muscles_AS_DA_DB_C2.png](case10/generated_files/figures/traces_muscles_AS_DA_DB_C2.png "case10/generated_files/figures/traces_muscles_AS_DA_DB_C2") | ![case10/generated_files/figures/neuron_activity_C2_AS_DA_DB.png](case10/generated_files/figures/neuron_activity_C2_AS_DA_DB.png "case10/generated_files/figures/neuron_activity_C2_AS_DA_DB") | ![case10/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2.png](case10/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2.png "case10/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2") | ![case10/generated_files/figures/muscle_activity_C2_AS_DA_DB.png](case10/generated_files/figures/muscle_activity_C2_AS_DA_DB.png "case10/generated_files/figures/muscle_activity_C2_AS_DA_DB") | ![case10/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2.png](case10/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2.png "case10/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2") |
| [case09](case09) | ![case09/generated_files/figures/neurons_C2_AS_DA_DB.png](case09/generated_files/figures/neurons_C2_AS_DA_DB.png "case09/generated_files/figures/neurons_C2_AS_DA_DB") | ![case09/generated_files/figures/traces_neuron_AS_DA_DB_C2.png](case09/generated_files/figures/traces_neuron_AS_DA_DB_C2.png "case09/generated_files/figures/traces_neuron_AS_DA_DB_C2") | ![case09/generated_files/figures/muscles_C2_AS_DA_DB.png](case09/generated_files/figures/muscles_C2_AS_DA_DB.png "case09/generated_files/figures/muscles_C2_AS_DA_DB") | ![case09/generated_files/figures/traces_muscles_AS_DA_DB_C2.png](case09/generated_files/figures/traces_muscles_AS_DA_DB_C2.png "case09/generated_files/figures/traces_muscles_AS_DA_DB_C2") | ![case09/generated_files/figures/neuron_activity_C2_AS_DA_DB.png](case09/generated_files/figures/neuron_activity_C2_AS_DA_DB.png "case09/generated_files/figures/neuron_activity_C2_AS_DA_DB") | ![case09/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2.png](case09/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2.png "case09/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2") | ![case09/generated_files/figures/muscle_activity_C2_AS_DA_DB.png](case09/generated_files/figures/muscle_activity_C2_AS_DA_DB.png "case09/generated_files/figures/muscle_activity_C2_AS_DA_DB") | ![case09/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2.png](case09/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2.png "case09/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2") |
| [case08](case08) | ![case08/generated_files/figures/neurons_C2_AS_DA_DB.png](case08/generated_files/figures/neurons_C2_AS_DA_DB.png "case08/generated_files/figures/neurons_C2_AS_DA_DB") | ![case08/generated_files/figures/traces_neuron_AS_DA_DB_C2.png](case08/generated_files/figures/traces_neuron_AS_DA_DB_C2.png "case08/generated_files/figures/traces_neuron_AS_DA_DB_C2") | ![case08/generated_files/figures/muscles_C2_AS_DA_DB.png](case08/generated_files/figures/muscles_C2_AS_DA_DB.png "case08/generated_files/figures/muscles_C2_AS_DA_DB") | ![case08/generated_files/figures/traces_muscles_AS_DA_DB_C2.png](case08/generated_files/figures/traces_muscles_AS_DA_DB_C2.png "case08/generated_files/figures/traces_muscles_AS_DA_DB_C2") | ![case08/generated_files/figures/neuron_activity_C2_AS_DA_DB.png](case08/generated_files/figures/neuron_activity_C2_AS_DA_DB.png "case08/generated_files/figures/neuron_activity_C2_AS_DA_DB") | ![case08/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2.png](case08/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2.png "case08/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2") | ![case08/generated_files/figures/muscle_activity_C2_AS_DA_DB.png](case08/generated_files/figures/muscle_activity_C2_AS_DA_DB.png "case08/generated_files/figures/muscle_activity_C2_AS_DA_DB") | ![case08/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2.png](case08/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2.png "case08/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2") |
| [case07](case07) | ![case07/generated_files/figures/neurons_C2_AS_DA_DB.png](case07/generated_files/figures/neurons_C2_AS_DA_DB.png "case07/generated_files/figures/neurons_C2_AS_DA_DB") | ![case07/generated_files/figures/traces_neuron_AS_DA_DB_C2.png](case07/generated_files/figures/traces_neuron_AS_DA_DB_C2.png "case07/generated_files/figures/traces_neuron_AS_DA_DB_C2") | ![case07/generated_files/figures/muscles_C2_AS_DA_DB.png](case07/generated_files/figures/muscles_C2_AS_DA_DB.png "case07/generated_files/figures/muscles_C2_AS_DA_DB") | ![case07/generated_files/figures/traces_muscles_AS_DA_DB_C2.png](case07/generated_files/figures/traces_muscles_AS_DA_DB_C2.png "case07/generated_files/figures/traces_muscles_AS_DA_DB_C2") | ![case07/generated_files/figures/neuron_activity_C2_AS_DA_DB.png](case07/generated_files/figures/neuron_activity_C2_AS_DA_DB.png "case07/generated_files/figures/neuron_activity_C2_AS_DA_DB") | ![case07/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2.png](case07/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2.png "case07/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2") | ![case07/generated_files/figures/muscle_activity_C2_AS_DA_DB.png](case07/generated_files/figures/muscle_activity_C2_AS_DA_DB.png "case07/generated_files/figures/muscle_activity_C2_AS_DA_DB") | ![case07/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2.png](case07/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2.png "case07/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2") |
| [case06](case06) | ![case06/generated_files/figures/neurons_C2_AS_DA_DB.png](case06/generated_files/figures/neurons_C2_AS_DA_DB.png "case06/generated_files/figures/neurons_C2_AS_DA_DB") | ![case06/generated_files/figures/traces_neuron_AS_DA_DB_C2.png](case06/generated_files/figures/traces_neuron_AS_DA_DB_C2.png "case06/generated_files/figures/traces_neuron_AS_DA_DB_C2") | ![case06/generated_files/figures/muscles_C2_AS_DA_DB.png](case06/generated_files/figures/muscles_C2_AS_DA_DB.png "case06/generated_files/figures/muscles_C2_AS_DA_DB") | ![case06/generated_files/figures/traces_muscles_AS_DA_DB_C2.png](case06/generated_files/figures/traces_muscles_AS_DA_DB_C2.png "case06/generated_files/figures/traces_muscles_AS_DA_DB_C2") | ![case06/generated_files/figures/neuron_activity_C2_AS_DA_DB.png](case06/generated_files/figures/neuron_activity_C2_AS_DA_DB.png "case06/generated_files/figures/neuron_activity_C2_AS_DA_DB") | ![case06/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2.png](case06/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2.png "case06/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2") | ![case06/generated_files/figures/muscle_activity_C2_AS_DA_DB.png](case06/generated_files/figures/muscle_activity_C2_AS_DA_DB.png "case06/generated_files/figures/muscle_activity_C2_AS_DA_DB") | ![case06/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2.png](case06/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2.png "case06/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2") |
| [case05](case05) | ![case05/generated_files/figures/neurons_C2_AS_DA_DB.png](case05/generated_files/figures/neurons_C2_AS_DA_DB.png "case05/generated_files/figures/neurons_C2_AS_DA_DB") | ![case05/generated_files/figures/traces_neuron_AS_DA_DB_C2.png](case05/generated_files/figures/traces_neuron_AS_DA_DB_C2.png "case05/generated_files/figures/traces_neuron_AS_DA_DB_C2") | ![case05/generated_files/figures/muscles_C2_AS_DA_DB.png](case05/generated_files/figures/muscles_C2_AS_DA_DB.png "case05/generated_files/figures/muscles_C2_AS_DA_DB") | ![case05/generated_files/figures/traces_muscles_AS_DA_DB_C2.png](case05/generated_files/figures/traces_muscles_AS_DA_DB_C2.png "case05/generated_files/figures/traces_muscles_AS_DA_DB_C2") | ![case05/generated_files/figures/neuron_activity_C2_AS_DA_DB.png](case05/generated_files/figures/neuron_activity_C2_AS_DA_DB.png "case05/generated_files/figures/neuron_activity_C2_AS_DA_DB") | ![case05/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2.png](case05/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2.png "case05/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2") | ![case05/generated_files/figures/muscle_activity_C2_AS_DA_DB.png](case05/generated_files/figures/muscle_activity_C2_AS_DA_DB.png "case05/generated_files/figures/muscle_activity_C2_AS_DA_DB") | ![case05/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2.png](case05/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2.png "case05/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2") |
| [case04](case04) | ![case04/generated_files/figures/neurons_C2_AS_DA_DB.png](case04/generated_files/figures/neurons_C2_AS_DA_DB.png "case04/generated_files/figures/neurons_C2_AS_DA_DB") | ![case04/generated_files/figures/traces_neuron_AS_DA_DB_C2.png](case04/generated_files/figures/traces_neuron_AS_DA_DB_C2.png "case04/generated_files/figures/traces_neuron_AS_DA_DB_C2") | ![case04/generated_files/figures/muscles_C2_AS_DA_DB.png](case04/generated_files/figures/muscles_C2_AS_DA_DB.png "case04/generated_files/figures/muscles_C2_AS_DA_DB") | ![case04/generated_files/figures/traces_muscles_AS_DA_DB_C2.png](case04/generated_files/figures/traces_muscles_AS_DA_DB_C2.png "case04/generated_files/figures/traces_muscles_AS_DA_DB_C2") | ![case04/generated_files/figures/neuron_activity_C2_AS_DA_DB.png](case04/generated_files/figures/neuron_activity_C2_AS_DA_DB.png "case04/generated_files/figures/neuron_activity_C2_AS_DA_DB") | ![case04/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2.png](case04/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2.png "case04/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2") | ![case04/generated_files/figures/muscle_activity_C2_AS_DA_DB.png](case04/generated_files/figures/muscle_activity_C2_AS_DA_DB.png "case04/generated_files/figures/muscle_activity_C2_AS_DA_DB") | ![case04/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2.png](case04/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2.png "case04/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2") |
| [case03](case03) | ![case03/generated_files/figures/neurons_C2_AS_DA_DB.png](case03/generated_files/figures/neurons_C2_AS_DA_DB.png "case03/generated_files/figures/neurons_C2_AS_DA_DB") | ![case03/generated_files/figures/traces_neuron_AS_DA_DB_C2.png](case03/generated_files/figures/traces_neuron_AS_DA_DB_C2.png "case03/generated_files/figures/traces_neuron_AS_DA_DB_C2") | ![case03/generated_files/figures/muscles_C2_AS_DA_DB.png](case03/generated_files/figures/muscles_C2_AS_DA_DB.png "case03/generated_files/figures/muscles_C2_AS_DA_DB") | ![case03/generated_files/figures/traces_muscles_AS_DA_DB_C2.png](case03/generated_files/figures/traces_muscles_AS_DA_DB_C2.png "case03/generated_files/figures/traces_muscles_AS_DA_DB_C2") | ![case03/generated_files/figures/neuron_activity_C2_AS_DA_DB.png](case03/generated_files/figures/neuron_activity_C2_AS_DA_DB.png "case03/generated_files/figures/neuron_activity_C2_AS_DA_DB") | ![case03/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2.png](case03/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2.png "case03/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2") | ![case03/generated_files/figures/muscle_activity_C2_AS_DA_DB.png](case03/generated_files/figures/muscle_activity_C2_AS_DA_DB.png "case03/generated_files/figures/muscle_activity_C2_AS_DA_DB") | ![case03/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2.png](case03/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2.png "case03/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2") |
| [case02](case02) | ![case02/generated_files/figures/neurons_C2_AS_DA_DB.png](case02/generated_files/figures/neurons_C2_AS_DA_DB.png "case02/generated_files/figures/neurons_C2_AS_DA_DB") | ![case02/generated_files/figures/traces_neuron_AS_DA_DB_C2.png](case02/generated_files/figures/traces_neuron_AS_DA_DB_C2.png "case02/generated_files/figures/traces_neuron_AS_DA_DB_C2") | ![case02/generated_files/figures/muscles_C2_AS_DA_DB.png](case02/generated_files/figures/muscles_C2_AS_DA_DB.png "case02/generated_files/figures/muscles_C2_AS_DA_DB") | ![case02/generated_files/figures/traces_muscles_AS_DA_DB_C2.png](case02/generated_files/figures/traces_muscles_AS_DA_DB_C2.png "case02/generated_files/figures/traces_muscles_AS_DA_DB_C2") | ![case02/generated_files/figures/neuron_activity_C2_AS_DA_DB.png](case02/generated_files/figures/neuron_activity_C2_AS_DA_DB.png "case02/generated_files/figures/neuron_activity_C2_AS_DA_DB") | ![case02/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2.png](case02/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2.png "case02/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2") | ![case02/generated_files/figures/muscle_activity_C2_AS_DA_DB.png](case02/generated_files/figures/muscle_activity_C2_AS_DA_DB.png "case02/generated_files/figures/muscle_activity_C2_AS_DA_DB") | ![case02/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2.png](case02/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2.png "case02/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2") |
| [case01](case01) | ![case01/generated_files/figures/neurons_C2_AS_DA_DB.png](case01/generated_files/figures/neurons_C2_AS_DA_DB.png "case01/generated_files/figures/neurons_C2_AS_DA_DB") | ![case01/generated_files/figures/traces_neuron_AS_DA_DB_C2.png](case01/generated_files/figures/traces_neuron_AS_DA_DB_C2.png "case01/generated_files/figures/traces_neuron_AS_DA_DB_C2") | ![case01/generated_files/figures/muscles_C2_AS_DA_DB.png](case01/generated_files/figures/muscles_C2_AS_DA_DB.png "case01/generated_files/figures/muscles_C2_AS_DA_DB") | ![case01/generated_files/figures/traces_muscles_AS_DA_DB_C2.png](case01/generated_files/figures/traces_muscles_AS_DA_DB_C2.png "case01/generated_files/figures/traces_muscles_AS_DA_DB_C2") | ![case01/generated_files/figures/neuron_activity_C2_AS_DA_DB.png](case01/generated_files/figures/neuron_activity_C2_AS_DA_DB.png "case01/generated_files/figures/neuron_activity_C2_AS_DA_DB") | ![case01/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2.png](case01/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2.png "case01/generated_files/figures/traces_neuron_activity_AS_DA_DB_C2") | ![case01/generated_files/figures/muscle_activity_C2_AS_DA_DB.png](case01/generated_files/figures/muscle_activity_C2_AS_DA_DB.png "case01/generated_files/figures/muscle_activity_C2_AS_DA_DB") | ![case01/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2.png](case01/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2.png "case01/generated_files/figures/traces_muscles_activity_AS_DA_DB_C2") |

# Citations

Olivares, Erick, Eduardo J. Izquierdo, and Randall D. Beer. ["A ventral nerve cord CPG may underlie locomotion in C. elegans."](https://arxiv.org/abs/1705.02301) arXiv preprint arXiv:1705.02301 (2017).