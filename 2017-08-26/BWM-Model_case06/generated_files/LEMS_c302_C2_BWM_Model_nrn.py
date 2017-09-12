'''
Neuron simulator export for:

Components:
    Leak (Type: ionChannelPassive:  conductance=1.0E-11 (SI conductance))
    k_fast (Type: ionChannelHH:  conductance=1.0E-11 (SI conductance))
    k_slow (Type: ionChannelHH:  conductance=1.0E-11 (SI conductance))
    ca_boyle (Type: ionChannelHH:  conductance=1.0E-11 (SI conductance))
    ca_simple (Type: ionChannelHH:  conductance=1.0E-11 (SI conductance))
    k_muscle (Type: ionChannelHH:  conductance=1.0E-11 (SI conductance))
    ca_muscle (Type: ionChannelHH:  conductance=1.0E-11 (SI conductance))
    null (Type: notes)
    CaPool (Type: fixedFactorConcentrationModel:  restingConc=0.0 (SI concentration) decayConstant=0.013811870945509265 (SI time) rho=2.38919E-4 (SI rho_factor))
    silent (Type: silentSynapse)
    neuron_to_muscle_exc_syn (Type: gradedSynapse:  conductance=1.0000000000000002E-10 (SI conductance) delta=0.019 (SI voltage) k=1205.0 (SI per_time) Vth=0.027 (SI voltage) erev=0.037 (SI voltage))
    neuron_to_muscle_inh_syn (Type: gradedSynapse:  conductance=1.29E-9 (SI conductance) delta=0.005 (SI voltage) k=25.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.05 (SI voltage))
    GenericMuscleCell (Type: cell)
    GenericNeuronCell (Type: cell)
    offset_current (Type: pulseGenerator:  delay=0.0 (SI time) duration=2.0 (SI time) amplitude=0.0 (SI current))
    c302_C2_BWM_Model (Type: network)
    sim_c302_C2_BWM_Model (Type: Simulation:  length=1.0 (SI time) step=5.0E-5 (SI time))


    This NEURON file has been generated by org.neuroml.export (see https://github.com/NeuroML/org.neuroml.export)
         org.neuroml.export  v1.5.3
         org.neuroml.model   v1.5.3
         jLEMS               v0.9.9.0

'''

import neuron

import time

import hashlib
h = neuron.h
h.load_file("stdlib.hoc")

h.load_file("stdgui.hoc")

h("objref p")
h("p = new PythonObject()")

class NeuronSimulation():

    def __init__(self, tstop, dt, seed=123456789):

        print("\n    Starting simulation in NEURON generated from NeuroML2 model...\n")

        self.seed = seed
        self.randoms = []
        self.next_global_id = 0  # Used in Random123 classes for elements using random(), etc. 

        self.next_spiking_input_id = 0  # Used in Random123 classes for elements using random(), etc. 

        '''
        Adding simulation Component(id=sim_c302_C2_BWM_Model type=Simulation) of network/component: c302_C2_BWM_Model (Type: network)
        
        '''
        # ######################   Population: DB2
        print("Population DB2 contains 1 instance(s) of component: GenericNeuronCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericNeuronCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericNeuronCell.hoc")
        a_DB2 = []
        h("{ n_DB2 = 1 }")
        h("objectvar a_DB2[n_DB2]")
        for i in range(int(h.n_DB2)):
            h("a_DB2[%i] = new GenericNeuronCell()"%i)
            h("access a_DB2[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_DB2[0].position(-0.2, -244.5, 15.787000000000001) }")

        h("proc initialiseV_DB2() { for i = 0, n_DB2-1 { a_DB2[i].set_initial_v() } }")
        h("objref fih_DB2")
        h('{fih_DB2 = new FInitializeHandler(0, "initialiseV_DB2()")}')

        h("proc initialiseIons_DB2() { for i = 0, n_DB2-1 { a_DB2[i].set_initial_ion_properties() } }")
        h("objref fih_ion_DB2")
        h('{fih_ion_DB2 = new FInitializeHandler(1, "initialiseIons_DB2()")}')

        # ######################   Population: DD2
        print("Population DD2 contains 1 instance(s) of component: GenericNeuronCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericNeuronCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericNeuronCell.hoc")
        a_DD2 = []
        h("{ n_DD2 = 1 }")
        h("objectvar a_DD2[n_DD2]")
        for i in range(int(h.n_DD2)):
            h("a_DD2[%i] = new GenericNeuronCell()"%i)
            h("access a_DD2[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_DD2[0].position(-1.85, -156.474989999999991, -42.850000000000001) }")

        h("proc initialiseV_DD2() { for i = 0, n_DD2-1 { a_DD2[i].set_initial_v() } }")
        h("objref fih_DD2")
        h('{fih_DD2 = new FInitializeHandler(0, "initialiseV_DD2()")}')

        h("proc initialiseIons_DD2() { for i = 0, n_DD2-1 { a_DD2[i].set_initial_ion_properties() } }")
        h("objref fih_ion_DD2")
        h('{fih_ion_DD2 = new FInitializeHandler(1, "initialiseIons_DD2()")}')

        # ######################   Population: MDL12
        print("Population MDL12 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MDL12 = []
        h("{ n_MDL12 = 1 }")
        h("objectvar a_MDL12[n_MDL12]")
        for i in range(int(h.n_MDL12)):
            h("a_MDL12[%i] = new GenericMuscleCell()"%i)
            h("access a_MDL12[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MDL12[0].position(80., 60., -80.) }")

        h("proc initialiseV_MDL12() { for i = 0, n_MDL12-1 { a_MDL12[i].set_initial_v() } }")
        h("objref fih_MDL12")
        h('{fih_MDL12 = new FInitializeHandler(0, "initialiseV_MDL12()")}')

        h("proc initialiseIons_MDL12() { for i = 0, n_MDL12-1 { a_MDL12[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MDL12")
        h('{fih_ion_MDL12 = new FInitializeHandler(1, "initialiseIons_MDL12()")}')

        # ######################   Continuous Projection: NC_DB2_MDL12_Acetylcholine
        print("Adding continuous projection: NC_DB2_MDL12_Acetylcholine from DB2 to MDL12, with 1 connection(s)")

        h("objectvar syn_NC_DB2_MDL12_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB2_MDL12_Acetylcholine_neuron_to_muscle_exc_syn_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB2[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL12[0].soma], weight: 1.0
        h("a_DB2[0].soma { syn_NC_DB2_MDL12_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDL12[0].soma { syn_NC_DB2_MDL12_Acetylcholine_neuron_to_muscle_exc_syn_post[0] = new neuron_to_muscle_exc_syn(0.500000) }")
        h("setpointer syn_NC_DB2_MDL12_Acetylcholine_silent_pre[0].vpeer, a_MDL12[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB2_MDL12_Acetylcholine_neuron_to_muscle_exc_syn_post[0].vpeer, a_DB2[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DD2_MDL12_GABA
        print("Adding continuous projection: NC_DD2_MDL12_GABA from DD2 to MDL12, with 1 connection(s)")

        h("objectvar syn_NC_DD2_MDL12_GABA_silent_pre[1]")
        h("objectvar syn_NC_DD2_MDL12_GABA_neuron_to_muscle_inh_syn_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DD2[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL12[0].soma], weight: 6.0
        h("a_DD2[0].soma { syn_NC_DD2_MDL12_GABA_silent_pre[0] = new silent(0.500000) }")
        h("a_MDL12[0].soma { syn_NC_DD2_MDL12_GABA_neuron_to_muscle_inh_syn_post[0] = new neuron_to_muscle_inh_syn(0.500000) }")
        h("a_DD2[0].soma { syn_NC_DD2_MDL12_GABA_silent_pre[0].weight = 6.0 }")
        h("a_MDL12[0].soma { syn_NC_DD2_MDL12_GABA_neuron_to_muscle_inh_syn_post[0].weight = 6.0 }")
        h("setpointer syn_NC_DD2_MDL12_GABA_silent_pre[0].vpeer, a_MDL12[0].soma.v(0.500000)")
        h("setpointer syn_NC_DD2_MDL12_GABA_neuron_to_muscle_inh_syn_post[0].vpeer, a_DD2[0].soma.v(0.500000)")

        trec = h.Vector()
        trec.record(h._ref_t)

        h.tstop = tstop

        h.dt = dt

        h.steps_per_ms = 1/h.dt



        # ######################   File to save: c302_C2_BWM_Model.activity.dat (neurons_activity)
        # Column: DB2/0/GenericNeuronCell/caConc
        h(' objectvar v_DB2_v_neurons_activity ')
        h(' { v_DB2_v_neurons_activity = new Vector() } ')
        h(' { v_DB2_v_neurons_activity.record(&a_DB2[0].soma.cai(0.5)) } ')
        h.v_DB2_v_neurons_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: DD2/0/GenericNeuronCell/caConc
        h(' objectvar v_DD2_v_neurons_activity ')
        h(' { v_DD2_v_neurons_activity = new Vector() } ')
        h(' { v_DD2_v_neurons_activity.record(&a_DD2[0].soma.cai(0.5)) } ')
        h.v_DD2_v_neurons_activity.resize((h.tstop * h.steps_per_ms) + 1)

        # ######################   File to save: c302_C2_BWM_Model.muscles.dat (muscles_v)
        # Column: MDL12/0/GenericMuscleCell/v
        h(' objectvar v_MDL12_v_muscles_v ')
        h(' { v_MDL12_v_muscles_v = new Vector() } ')
        h(' { v_MDL12_v_muscles_v.record(&a_MDL12[0].soma.v(0.5)) } ')
        h.v_MDL12_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)

        # ######################   File to save: c302_C2_BWM_Model.muscles.activity.dat (muscles_activity)
        # Column: MDL12/0/GenericMuscleCell/caConc
        h(' objectvar v_MDL12_v_muscles_activity ')
        h(' { v_MDL12_v_muscles_activity = new Vector() } ')
        h(' { v_MDL12_v_muscles_activity.record(&a_MDL12[0].soma.cai(0.5)) } ')
        h.v_MDL12_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)

        # ######################   File to save: c302_C2_BWM_Model.dat (neurons_v)
        # Column: DB2/0/GenericNeuronCell/v
        h(' objectvar v_DB2_v_neurons_v ')
        h(' { v_DB2_v_neurons_v = new Vector() } ')
        h(' { v_DB2_v_neurons_v.record(&a_DB2[0].soma.v(0.5)) } ')
        h.v_DB2_v_neurons_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: DD2/0/GenericNeuronCell/v
        h(' objectvar v_DD2_v_neurons_v ')
        h(' { v_DD2_v_neurons_v = new Vector() } ')
        h(' { v_DD2_v_neurons_v.record(&a_DD2[0].soma.v(0.5)) } ')
        h.v_DD2_v_neurons_v.resize((h.tstop * h.steps_per_ms) + 1)

        # ######################   File to save: time.dat (time)
        # Column: time
        h(' objectvar v_time ')
        h(' { v_time = new Vector() } ')
        h(' { v_time.record(&t) } ')
        h.v_time.resize((h.tstop * h.steps_per_ms) + 1)

        self.initialized = False

        self.sim_end = -1 # will be overwritten

    def run(self):

        self.initialized = True
        sim_start = time.time()
        print("Running a simulation of %sms (dt = %sms; seed=%s)" % (h.tstop, h.dt, self.seed))

        h.run()

        self.sim_end = time.time()
        sim_time = self.sim_end - sim_start
        print("Finished NEURON simulation in %f seconds (%f mins)..."%(sim_time, sim_time/60.0))

        self.save_results()


    def advance(self):

        if not self.initialized:
            h.finitialize()
            self.initialized = True

        h.fadvance()


    ###############################################################################
    # Hash function to use in generation of random value
    # This is copied from NetPyNE: https://github.com/Neurosim-lab/netpyne/blob/master/netpyne/simFuncs.py
    ###############################################################################
    def _id32 (self,obj): 
        return int(hashlib.md5(obj).hexdigest()[0:8],16)  # convert 8 first chars of md5 hash in base 16 to int


    ###############################################################################
    # Initialize the stim randomizer
    # This is copied from NetPyNE: https://github.com/Neurosim-lab/netpyne/blob/master/netpyne/simFuncs.py
    ###############################################################################
    def _init_stim_randomizer(self,rand, stimType, gid, seed): 
        rand.Random123(self._id32(stimType), gid, seed)


    def save_results(self):

        print("Saving results at t=%s..."%h.t)

        if self.sim_end < 0: self.sim_end = time.time()


        # ######################   File to save: time.dat (time)
        py_v_time = [ t/1000 for t in h.v_time.to_python() ]  # Convert to Python list for speed...

        f_time_f2 = open('time.dat', 'w')
        num_points = len(py_v_time)  # Simulation may have been stopped before tstop...

        for i in range(num_points):
            f_time_f2.write('%f'% py_v_time[i])  # Save in SI units...+ '\n')
        f_time_f2.close()
        print("Saved data to: time.dat")

        # ######################   File to save: c302_C2_BWM_Model.activity.dat (neurons_activity)
        py_v_DB2_v_neurons_activity = [ float(x ) for x in h.v_DB2_v_neurons_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_DD2_v_neurons_activity = [ float(x ) for x in h.v_DD2_v_neurons_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration

        f_neurons_activity_f2 = open('c302_C2_BWM_Model.activity.dat', 'w')
        num_points = len(py_v_time)  # Simulation may have been stopped before tstop...

        for i in range(num_points):
            f_neurons_activity_f2.write('%e\t'% py_v_time[i]  + '%e\t'%(py_v_DB2_v_neurons_activity[i])  + '%e\t'%(py_v_DD2_v_neurons_activity[i]) + '\n')
        f_neurons_activity_f2.close()
        print("Saved data to: c302_C2_BWM_Model.activity.dat")

        # ######################   File to save: c302_C2_BWM_Model.muscles.dat (muscles_v)
        py_v_MDL12_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MDL12_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage

        f_muscles_v_f2 = open('c302_C2_BWM_Model.muscles.dat', 'w')
        num_points = len(py_v_time)  # Simulation may have been stopped before tstop...

        for i in range(num_points):
            f_muscles_v_f2.write('%e\t'% py_v_time[i]  + '%e\t'%(py_v_MDL12_v_muscles_v[i]) + '\n')
        f_muscles_v_f2.close()
        print("Saved data to: c302_C2_BWM_Model.muscles.dat")

        # ######################   File to save: c302_C2_BWM_Model.muscles.activity.dat (muscles_activity)
        py_v_MDL12_v_muscles_activity = [ float(x ) for x in h.v_MDL12_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration

        f_muscles_activity_f2 = open('c302_C2_BWM_Model.muscles.activity.dat', 'w')
        num_points = len(py_v_time)  # Simulation may have been stopped before tstop...

        for i in range(num_points):
            f_muscles_activity_f2.write('%e\t'% py_v_time[i]  + '%e\t'%(py_v_MDL12_v_muscles_activity[i]) + '\n')
        f_muscles_activity_f2.close()
        print("Saved data to: c302_C2_BWM_Model.muscles.activity.dat")

        # ######################   File to save: c302_C2_BWM_Model.dat (neurons_v)
        py_v_DB2_v_neurons_v = [ float(x  / 1000.0) for x in h.v_DB2_v_neurons_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_DD2_v_neurons_v = [ float(x  / 1000.0) for x in h.v_DD2_v_neurons_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage

        f_neurons_v_f2 = open('c302_C2_BWM_Model.dat', 'w')
        num_points = len(py_v_time)  # Simulation may have been stopped before tstop...

        for i in range(num_points):
            f_neurons_v_f2.write('%e\t'% py_v_time[i]  + '%e\t'%(py_v_DB2_v_neurons_v[i])  + '%e\t'%(py_v_DD2_v_neurons_v[i]) + '\n')
        f_neurons_v_f2.close()
        print("Saved data to: c302_C2_BWM_Model.dat")

        save_end = time.time()
        save_time = save_end - self.sim_end
        print("Finished saving results in %f seconds"%(save_time))

        print("Done")

        quit()


if __name__ == '__main__':

    ns = NeuronSimulation(tstop=1000, dt=0.05, seed=123456789)

    ns.run()
