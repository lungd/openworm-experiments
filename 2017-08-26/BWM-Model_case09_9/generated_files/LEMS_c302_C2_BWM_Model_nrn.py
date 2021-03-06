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
    CaPool (Type: fixedFactorConcentrationModel:  restingConc=0.0 (SI concentration) decayConstant=0.43081187094550927 (SI time) rho=9.19E-7 (SI rho_factor))
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

        trec = h.Vector()
        trec.record(h._ref_t)

        h.tstop = tstop

        h.dt = dt

        h.steps_per_ms = 1/h.dt



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

        f_neurons_v_f2 = open('c302_C2_BWM_Model.dat', 'w')
        num_points = len(py_v_time)  # Simulation may have been stopped before tstop...

        for i in range(num_points):
            f_neurons_v_f2.write('%e\t'% py_v_time[i] + '\n')
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

