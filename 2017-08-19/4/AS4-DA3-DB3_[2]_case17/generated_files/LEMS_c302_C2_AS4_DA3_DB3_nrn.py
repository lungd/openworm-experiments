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
    neuron_to_neuron_elec_syn (Type: gapJunction:  conductance=1.252E-11 (SI conductance))
    AVAL_to_DA3_elec_syn (Type: gapJunction:  conductance=5.2E-13 (SI conductance))
    AVAR_to_DA3_elec_syn (Type: gapJunction:  conductance=5.2E-13 (SI conductance))
    AVBL_to_DB3_elec_syn (Type: gapJunction:  conductance=5.52E-12 (SI conductance))
    AVBR_to_DB3_elec_syn (Type: gapJunction:  conductance=5.52E-12 (SI conductance))
    DA3_to_AVAL_elec_syn (Type: gapJunction:  conductance=5.2E-13 (SI conductance))
    DA3_to_AVAR_elec_syn (Type: gapJunction:  conductance=5.2E-13 (SI conductance))
    DB3_to_AVBL_elec_syn (Type: gapJunction:  conductance=5.52E-12 (SI conductance))
    DB3_to_AVBR_elec_syn (Type: gapJunction:  conductance=5.52E-12 (SI conductance))
    silent (Type: silentSynapse)
    neuron_to_neuron_exc_syn (Type: gradedSynapse:  conductance=4.900000000000001E-10 (SI conductance) delta=0.005 (SI voltage) k=500.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.01 (SI voltage))
    AVAL_to_AVBL_inh_syn (Type: gradedSynapse:  conductance=1.9000000000000002E-11 (SI conductance) delta=0.005 (SI voltage) k=15.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.07 (SI voltage))
    AVAL_to_DA3_exc_syn (Type: gradedSynapse:  conductance=1.0000000000000001E-11 (SI conductance) delta=0.005 (SI voltage) k=500.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.01 (SI voltage))
    AVAR_to_AVBL_inh_syn (Type: gradedSynapse:  conductance=1.9000000000000002E-11 (SI conductance) delta=0.005 (SI voltage) k=15.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.07 (SI voltage))
    AVAR_to_AVBR_inh_syn (Type: gradedSynapse:  conductance=1.9000000000000002E-11 (SI conductance) delta=0.005 (SI voltage) k=15.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.07 (SI voltage))
    AVAR_to_DA3_exc_syn (Type: gradedSynapse:  conductance=1.0000000000000001E-11 (SI conductance) delta=0.005 (SI voltage) k=500.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.01 (SI voltage))
    AVBL_to_AVAL_inh_syn (Type: gradedSynapse:  conductance=1.9000000000000002E-11 (SI conductance) delta=0.005 (SI voltage) k=15.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.07 (SI voltage))
    AVBL_to_AVAR_inh_syn (Type: gradedSynapse:  conductance=1.9000000000000002E-11 (SI conductance) delta=0.005 (SI voltage) k=15.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.07 (SI voltage))
    AVBR_to_AVAL_inh_syn (Type: gradedSynapse:  conductance=1.9000000000000002E-11 (SI conductance) delta=0.005 (SI voltage) k=15.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.07 (SI voltage))
    AVBR_to_AVAR_inh_syn (Type: gradedSynapse:  conductance=1.9000000000000002E-11 (SI conductance) delta=0.005 (SI voltage) k=15.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.07 (SI voltage))
    DA3_to_DB3_exc_syn (Type: gradedSynapse:  conductance=1.0000000000000002E-10 (SI conductance) delta=0.005 (SI voltage) k=500.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.01 (SI voltage))
    DB3_to_AS4_inh_syn (Type: gradedSynapse:  conductance=5.0E-10 (SI conductance) delta=0.005 (SI voltage) k=15.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.07 (SI voltage))
    AS4_to_DA3_exc_syn (Type: gradedSynapse:  conductance=1.0000000000000002E-10 (SI conductance) delta=0.005 (SI voltage) k=500.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.01 (SI voltage))
    GenericMuscleCell (Type: cell)
    GenericNeuronCell (Type: cell)
    offset_current (Type: pulseGenerator:  delay=0.0 (SI time) duration=2.0 (SI time) amplitude=0.0 (SI current))
    stim_AVBL_1 (Type: pulseGenerator:  delay=0.0 (SI time) duration=1.0 (SI time) amplitude=5.0E-12 (SI current))
    stim_AVBR_1 (Type: pulseGenerator:  delay=0.0 (SI time) duration=1.0 (SI time) amplitude=5.0E-12 (SI current))
    stim_AVAL_1 (Type: pulseGenerator:  delay=1.0 (SI time) duration=1.0 (SI time) amplitude=5.0E-12 (SI current))
    stim_AVAR_1 (Type: pulseGenerator:  delay=1.0 (SI time) duration=1.0 (SI time) amplitude=5.0E-12 (SI current))
    stim_AVBL_2 (Type: pulseGenerator:  delay=2.0 (SI time) duration=0.9 (SI time) amplitude=5.0E-12 (SI current))
    stim_AVBR_2 (Type: pulseGenerator:  delay=2.0 (SI time) duration=0.9 (SI time) amplitude=5.0E-12 (SI current))
    stim_AS4_1 (Type: pulseGenerator:  delay=0.0 (SI time) duration=2.9 (SI time) amplitude=5.0E-12 (SI current))
    c302_C2_AS4_DA3_DB3 (Type: network)
    sim_c302_C2_AS4_DA3_DB3 (Type: Simulation:  length=3.0 (SI time) step=5.0E-5 (SI time))


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
        Adding simulation Component(id=sim_c302_C2_AS4_DA3_DB3 type=Simulation) of network/component: c302_C2_AS4_DA3_DB3 (Type: network)
        
        '''
        # ######################   Population: AS4
        print("Population AS4 contains 1 instance(s) of component: GenericNeuronCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericNeuronCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericNeuronCell.hoc")
        a_AS4 = []
        h("{ n_AS4 = 1 }")
        h("objectvar a_AS4[n_AS4]")
        for i in range(int(h.n_AS4)):
            h("a_AS4[%i] = new GenericNeuronCell()"%i)
            h("access a_AS4[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_AS4[0].position(-1.8750001, -90.200005000000004, -65.375) }")

        h("proc initialiseV_AS4() { for i = 0, n_AS4-1 { a_AS4[i].set_initial_v() } }")
        h("objref fih_AS4")
        h('{fih_AS4 = new FInitializeHandler(0, "initialiseV_AS4()")}')

        h("proc initialiseIons_AS4() { for i = 0, n_AS4-1 { a_AS4[i].set_initial_ion_properties() } }")
        h("objref fih_ion_AS4")
        h('{fih_ion_AS4 = new FInitializeHandler(1, "initialiseIons_AS4()")}')

        # ######################   Population: AVAL
        print("Population AVAL contains 1 instance(s) of component: GenericNeuronCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericNeuronCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericNeuronCell.hoc")
        a_AVAL = []
        h("{ n_AVAL = 1 }")
        h("objectvar a_AVAL[n_AVAL]")
        for i in range(int(h.n_AVAL)):
            h("a_AVAL[%i] = new GenericNeuronCell()"%i)
            h("access a_AVAL[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_AVAL[0].position(-0.55, -271.5, 37.982999999999997) }")

        h("proc initialiseV_AVAL() { for i = 0, n_AVAL-1 { a_AVAL[i].set_initial_v() } }")
        h("objref fih_AVAL")
        h('{fih_AVAL = new FInitializeHandler(0, "initialiseV_AVAL()")}')

        h("proc initialiseIons_AVAL() { for i = 0, n_AVAL-1 { a_AVAL[i].set_initial_ion_properties() } }")
        h("objref fih_ion_AVAL")
        h('{fih_ion_AVAL = new FInitializeHandler(1, "initialiseIons_AVAL()")}')

        # ######################   Population: AVAR
        print("Population AVAR contains 1 instance(s) of component: GenericNeuronCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericNeuronCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericNeuronCell.hoc")
        a_AVAR = []
        h("{ n_AVAR = 1 }")
        h("objectvar a_AVAR[n_AVAR]")
        for i in range(int(h.n_AVAR)):
            h("a_AVAR[%i] = new GenericNeuronCell()"%i)
            h("access a_AVAR[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_AVAR[0].position(-3.5, -271.5, 37.982999999999997) }")

        h("proc initialiseV_AVAR() { for i = 0, n_AVAR-1 { a_AVAR[i].set_initial_v() } }")
        h("objref fih_AVAR")
        h('{fih_AVAR = new FInitializeHandler(0, "initialiseV_AVAR()")}')

        h("proc initialiseIons_AVAR() { for i = 0, n_AVAR-1 { a_AVAR[i].set_initial_ion_properties() } }")
        h("objref fih_ion_AVAR")
        h('{fih_ion_AVAR = new FInitializeHandler(1, "initialiseIons_AVAR()")}')

        # ######################   Population: AVBL
        print("Population AVBL contains 1 instance(s) of component: GenericNeuronCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericNeuronCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericNeuronCell.hoc")
        a_AVBL = []
        h("{ n_AVBL = 1 }")
        h("objectvar a_AVBL[n_AVBL]")
        for i in range(int(h.n_AVBL)):
            h("a_AVBL[%i] = new GenericNeuronCell()"%i)
            h("access a_AVBL[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_AVBL[0].position(0.225, -269.793999999999983, 37.863002999999999) }")

        h("proc initialiseV_AVBL() { for i = 0, n_AVBL-1 { a_AVBL[i].set_initial_v() } }")
        h("objref fih_AVBL")
        h('{fih_AVBL = new FInitializeHandler(0, "initialiseV_AVBL()")}')

        h("proc initialiseIons_AVBL() { for i = 0, n_AVBL-1 { a_AVBL[i].set_initial_ion_properties() } }")
        h("objref fih_ion_AVBL")
        h('{fih_ion_AVBL = new FInitializeHandler(1, "initialiseIons_AVBL()")}')

        # ######################   Population: AVBR
        print("Population AVBR contains 1 instance(s) of component: GenericNeuronCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericNeuronCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericNeuronCell.hoc")
        a_AVBR = []
        h("{ n_AVBR = 1 }")
        h("objectvar a_AVBR[n_AVBR]")
        for i in range(int(h.n_AVBR)):
            h("a_AVBR[%i] = new GenericNeuronCell()"%i)
            h("access a_AVBR[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_AVBR[0].position(-4.581, -269.793999999999983, 37.863002999999999) }")

        h("proc initialiseV_AVBR() { for i = 0, n_AVBR-1 { a_AVBR[i].set_initial_v() } }")
        h("objref fih_AVBR")
        h('{fih_AVBR = new FInitializeHandler(0, "initialiseV_AVBR()")}')

        h("proc initialiseIons_AVBR() { for i = 0, n_AVBR-1 { a_AVBR[i].set_initial_ion_properties() } }")
        h("objref fih_ion_AVBR")
        h('{fih_ion_AVBR = new FInitializeHandler(1, "initialiseIons_AVBR()")}')

        # ######################   Population: DA3
        print("Population DA3 contains 1 instance(s) of component: GenericNeuronCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericNeuronCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericNeuronCell.hoc")
        a_DA3 = []
        h("{ n_DA3 = 1 }")
        h("objectvar a_DA3[n_DA3]")
        for i in range(int(h.n_DA3)):
            h("a_DA3[%i] = new GenericNeuronCell()"%i)
            h("access a_DA3[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_DA3[0].position(-1.65, -123.650000000000006, -58.350002000000003) }")

        h("proc initialiseV_DA3() { for i = 0, n_DA3-1 { a_DA3[i].set_initial_v() } }")
        h("objref fih_DA3")
        h('{fih_DA3 = new FInitializeHandler(0, "initialiseV_DA3()")}')

        h("proc initialiseIons_DA3() { for i = 0, n_DA3-1 { a_DA3[i].set_initial_ion_properties() } }")
        h("objref fih_ion_DA3")
        h('{fih_ion_DA3 = new FInitializeHandler(1, "initialiseIons_DA3()")}')

        # ######################   Population: DB3
        print("Population DB3 contains 1 instance(s) of component: GenericNeuronCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericNeuronCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericNeuronCell.hoc")
        a_DB3 = []
        h("{ n_DB3 = 1 }")
        h("objectvar a_DB3[n_DB3]")
        for i in range(int(h.n_DB3)):
            h("a_DB3[%i] = new GenericNeuronCell()"%i)
            h("access a_DB3[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_DB3[0].position(-1.85, -195.275000000000006, -18.524999999999999) }")

        h("proc initialiseV_DB3() { for i = 0, n_DB3-1 { a_DB3[i].set_initial_v() } }")
        h("objref fih_DB3")
        h('{fih_DB3 = new FInitializeHandler(0, "initialiseV_DB3()")}')

        h("proc initialiseIons_DB3() { for i = 0, n_DB3-1 { a_DB3[i].set_initial_ion_properties() } }")
        h("objref fih_ion_DB3")
        h('{fih_ion_DB3 = new FInitializeHandler(1, "initialiseIons_DB3()")}')

        # ######################   Electrical Projection: NC_AVAL_AVAR_Generic_GJ
        print("Adding electrical projection: NC_AVAL_AVAR_Generic_GJ from AVAL to AVAR, with 1 connection(s)")

        h("objectvar syn_NC_AVAL_AVAR_Generic_GJ_neuron_to_neuron_elec_syn_A[1]")
        h("objectvar syn_NC_AVAL_AVAR_Generic_GJ_neuron_to_neuron_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVAL[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVAR[0].soma], weight: 18.0
        h("a_AVAL[0].soma { syn_NC_AVAL_AVAR_Generic_GJ_neuron_to_neuron_elec_syn_A[0] = new neuron_to_neuron_elec_syn(0.5) }")
        h("a_AVAR[0].soma { syn_NC_AVAL_AVAR_Generic_GJ_neuron_to_neuron_elec_syn_B[0] = new neuron_to_neuron_elec_syn(0.5) }")
        h("a_AVAL[0].soma { syn_NC_AVAL_AVAR_Generic_GJ_neuron_to_neuron_elec_syn_A[0].weight = 18.0 }")
        h("a_AVAR[0].soma { syn_NC_AVAL_AVAR_Generic_GJ_neuron_to_neuron_elec_syn_B[0].weight = 18.0 }")
        h("setpointer syn_NC_AVAL_AVAR_Generic_GJ_neuron_to_neuron_elec_syn_A[0].vpeer, a_AVAR[0].soma.v(0.5)")
        h("setpointer syn_NC_AVAL_AVAR_Generic_GJ_neuron_to_neuron_elec_syn_B[0].vpeer, a_AVAL[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_AVAL_DA3_Generic_GJ
        print("Adding electrical projection: NC_AVAL_DA3_Generic_GJ from AVAL to DA3, with 1 connection(s)")

        h("objectvar syn_NC_AVAL_DA3_Generic_GJ_AVAL_to_DA3_elec_syn_A[1]")
        h("objectvar syn_NC_AVAL_DA3_Generic_GJ_AVAL_to_DA3_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVAL[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DA3[0].soma], weight: 6.0
        h("a_AVAL[0].soma { syn_NC_AVAL_DA3_Generic_GJ_AVAL_to_DA3_elec_syn_A[0] = new AVAL_to_DA3_elec_syn(0.5) }")
        h("a_DA3[0].soma { syn_NC_AVAL_DA3_Generic_GJ_AVAL_to_DA3_elec_syn_B[0] = new AVAL_to_DA3_elec_syn(0.5) }")
        h("a_AVAL[0].soma { syn_NC_AVAL_DA3_Generic_GJ_AVAL_to_DA3_elec_syn_A[0].weight = 6.0 }")
        h("a_DA3[0].soma { syn_NC_AVAL_DA3_Generic_GJ_AVAL_to_DA3_elec_syn_B[0].weight = 6.0 }")
        h("setpointer syn_NC_AVAL_DA3_Generic_GJ_AVAL_to_DA3_elec_syn_A[0].vpeer, a_DA3[0].soma.v(0.5)")
        h("setpointer syn_NC_AVAL_DA3_Generic_GJ_AVAL_to_DA3_elec_syn_B[0].vpeer, a_AVAL[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_AVAR_AVAL_Generic_GJ
        print("Adding electrical projection: NC_AVAR_AVAL_Generic_GJ from AVAR to AVAL, with 1 connection(s)")

        h("objectvar syn_NC_AVAR_AVAL_Generic_GJ_neuron_to_neuron_elec_syn_A[1]")
        h("objectvar syn_NC_AVAR_AVAL_Generic_GJ_neuron_to_neuron_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVAR[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVAL[0].soma], weight: 18.0
        h("a_AVAR[0].soma { syn_NC_AVAR_AVAL_Generic_GJ_neuron_to_neuron_elec_syn_A[0] = new neuron_to_neuron_elec_syn(0.5) }")
        h("a_AVAL[0].soma { syn_NC_AVAR_AVAL_Generic_GJ_neuron_to_neuron_elec_syn_B[0] = new neuron_to_neuron_elec_syn(0.5) }")
        h("a_AVAR[0].soma { syn_NC_AVAR_AVAL_Generic_GJ_neuron_to_neuron_elec_syn_A[0].weight = 18.0 }")
        h("a_AVAL[0].soma { syn_NC_AVAR_AVAL_Generic_GJ_neuron_to_neuron_elec_syn_B[0].weight = 18.0 }")
        h("setpointer syn_NC_AVAR_AVAL_Generic_GJ_neuron_to_neuron_elec_syn_A[0].vpeer, a_AVAL[0].soma.v(0.5)")
        h("setpointer syn_NC_AVAR_AVAL_Generic_GJ_neuron_to_neuron_elec_syn_B[0].vpeer, a_AVAR[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_AVAR_AVBL_Generic_GJ
        print("Adding electrical projection: NC_AVAR_AVBL_Generic_GJ from AVAR to AVBL, with 1 connection(s)")

        h("objectvar syn_NC_AVAR_AVBL_Generic_GJ_neuron_to_neuron_elec_syn_A[1]")
        h("objectvar syn_NC_AVAR_AVBL_Generic_GJ_neuron_to_neuron_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVAR[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVBL[0].soma], weight: 3.0
        h("a_AVAR[0].soma { syn_NC_AVAR_AVBL_Generic_GJ_neuron_to_neuron_elec_syn_A[0] = new neuron_to_neuron_elec_syn(0.5) }")
        h("a_AVBL[0].soma { syn_NC_AVAR_AVBL_Generic_GJ_neuron_to_neuron_elec_syn_B[0] = new neuron_to_neuron_elec_syn(0.5) }")
        h("a_AVAR[0].soma { syn_NC_AVAR_AVBL_Generic_GJ_neuron_to_neuron_elec_syn_A[0].weight = 3.0 }")
        h("a_AVBL[0].soma { syn_NC_AVAR_AVBL_Generic_GJ_neuron_to_neuron_elec_syn_B[0].weight = 3.0 }")
        h("setpointer syn_NC_AVAR_AVBL_Generic_GJ_neuron_to_neuron_elec_syn_A[0].vpeer, a_AVBL[0].soma.v(0.5)")
        h("setpointer syn_NC_AVAR_AVBL_Generic_GJ_neuron_to_neuron_elec_syn_B[0].vpeer, a_AVAR[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_AVAR_DA3_Generic_GJ
        print("Adding electrical projection: NC_AVAR_DA3_Generic_GJ from AVAR to DA3, with 1 connection(s)")

        h("objectvar syn_NC_AVAR_DA3_Generic_GJ_AVAR_to_DA3_elec_syn_A[1]")
        h("objectvar syn_NC_AVAR_DA3_Generic_GJ_AVAR_to_DA3_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVAR[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DA3[0].soma], weight: 7.0
        h("a_AVAR[0].soma { syn_NC_AVAR_DA3_Generic_GJ_AVAR_to_DA3_elec_syn_A[0] = new AVAR_to_DA3_elec_syn(0.5) }")
        h("a_DA3[0].soma { syn_NC_AVAR_DA3_Generic_GJ_AVAR_to_DA3_elec_syn_B[0] = new AVAR_to_DA3_elec_syn(0.5) }")
        h("a_AVAR[0].soma { syn_NC_AVAR_DA3_Generic_GJ_AVAR_to_DA3_elec_syn_A[0].weight = 7.0 }")
        h("a_DA3[0].soma { syn_NC_AVAR_DA3_Generic_GJ_AVAR_to_DA3_elec_syn_B[0].weight = 7.0 }")
        h("setpointer syn_NC_AVAR_DA3_Generic_GJ_AVAR_to_DA3_elec_syn_A[0].vpeer, a_DA3[0].soma.v(0.5)")
        h("setpointer syn_NC_AVAR_DA3_Generic_GJ_AVAR_to_DA3_elec_syn_B[0].vpeer, a_AVAR[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_AVBL_AVAR_Generic_GJ
        print("Adding electrical projection: NC_AVBL_AVAR_Generic_GJ from AVBL to AVAR, with 1 connection(s)")

        h("objectvar syn_NC_AVBL_AVAR_Generic_GJ_neuron_to_neuron_elec_syn_A[1]")
        h("objectvar syn_NC_AVBL_AVAR_Generic_GJ_neuron_to_neuron_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVBL[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVAR[0].soma], weight: 3.0
        h("a_AVBL[0].soma { syn_NC_AVBL_AVAR_Generic_GJ_neuron_to_neuron_elec_syn_A[0] = new neuron_to_neuron_elec_syn(0.5) }")
        h("a_AVAR[0].soma { syn_NC_AVBL_AVAR_Generic_GJ_neuron_to_neuron_elec_syn_B[0] = new neuron_to_neuron_elec_syn(0.5) }")
        h("a_AVBL[0].soma { syn_NC_AVBL_AVAR_Generic_GJ_neuron_to_neuron_elec_syn_A[0].weight = 3.0 }")
        h("a_AVAR[0].soma { syn_NC_AVBL_AVAR_Generic_GJ_neuron_to_neuron_elec_syn_B[0].weight = 3.0 }")
        h("setpointer syn_NC_AVBL_AVAR_Generic_GJ_neuron_to_neuron_elec_syn_A[0].vpeer, a_AVAR[0].soma.v(0.5)")
        h("setpointer syn_NC_AVBL_AVAR_Generic_GJ_neuron_to_neuron_elec_syn_B[0].vpeer, a_AVBL[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_AVBL_AVBR_Generic_GJ
        print("Adding electrical projection: NC_AVBL_AVBR_Generic_GJ from AVBL to AVBR, with 1 connection(s)")

        h("objectvar syn_NC_AVBL_AVBR_Generic_GJ_neuron_to_neuron_elec_syn_A[1]")
        h("objectvar syn_NC_AVBL_AVBR_Generic_GJ_neuron_to_neuron_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVBL[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVBR[0].soma], weight: 17.0
        h("a_AVBL[0].soma { syn_NC_AVBL_AVBR_Generic_GJ_neuron_to_neuron_elec_syn_A[0] = new neuron_to_neuron_elec_syn(0.5) }")
        h("a_AVBR[0].soma { syn_NC_AVBL_AVBR_Generic_GJ_neuron_to_neuron_elec_syn_B[0] = new neuron_to_neuron_elec_syn(0.5) }")
        h("a_AVBL[0].soma { syn_NC_AVBL_AVBR_Generic_GJ_neuron_to_neuron_elec_syn_A[0].weight = 17.0 }")
        h("a_AVBR[0].soma { syn_NC_AVBL_AVBR_Generic_GJ_neuron_to_neuron_elec_syn_B[0].weight = 17.0 }")
        h("setpointer syn_NC_AVBL_AVBR_Generic_GJ_neuron_to_neuron_elec_syn_A[0].vpeer, a_AVBR[0].soma.v(0.5)")
        h("setpointer syn_NC_AVBL_AVBR_Generic_GJ_neuron_to_neuron_elec_syn_B[0].vpeer, a_AVBL[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_AVBL_DB3_Generic_GJ
        print("Adding electrical projection: NC_AVBL_DB3_Generic_GJ from AVBL to DB3, with 1 connection(s)")

        h("objectvar syn_NC_AVBL_DB3_Generic_GJ_AVBL_to_DB3_elec_syn_A[1]")
        h("objectvar syn_NC_AVBL_DB3_Generic_GJ_AVBL_to_DB3_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVBL[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DB3[0].soma], weight: 9.0
        h("a_AVBL[0].soma { syn_NC_AVBL_DB3_Generic_GJ_AVBL_to_DB3_elec_syn_A[0] = new AVBL_to_DB3_elec_syn(0.5) }")
        h("a_DB3[0].soma { syn_NC_AVBL_DB3_Generic_GJ_AVBL_to_DB3_elec_syn_B[0] = new AVBL_to_DB3_elec_syn(0.5) }")
        h("a_AVBL[0].soma { syn_NC_AVBL_DB3_Generic_GJ_AVBL_to_DB3_elec_syn_A[0].weight = 9.0 }")
        h("a_DB3[0].soma { syn_NC_AVBL_DB3_Generic_GJ_AVBL_to_DB3_elec_syn_B[0].weight = 9.0 }")
        h("setpointer syn_NC_AVBL_DB3_Generic_GJ_AVBL_to_DB3_elec_syn_A[0].vpeer, a_DB3[0].soma.v(0.5)")
        h("setpointer syn_NC_AVBL_DB3_Generic_GJ_AVBL_to_DB3_elec_syn_B[0].vpeer, a_AVBL[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_AVBR_AVBL_Generic_GJ
        print("Adding electrical projection: NC_AVBR_AVBL_Generic_GJ from AVBR to AVBL, with 1 connection(s)")

        h("objectvar syn_NC_AVBR_AVBL_Generic_GJ_neuron_to_neuron_elec_syn_A[1]")
        h("objectvar syn_NC_AVBR_AVBL_Generic_GJ_neuron_to_neuron_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVBR[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVBL[0].soma], weight: 17.0
        h("a_AVBR[0].soma { syn_NC_AVBR_AVBL_Generic_GJ_neuron_to_neuron_elec_syn_A[0] = new neuron_to_neuron_elec_syn(0.5) }")
        h("a_AVBL[0].soma { syn_NC_AVBR_AVBL_Generic_GJ_neuron_to_neuron_elec_syn_B[0] = new neuron_to_neuron_elec_syn(0.5) }")
        h("a_AVBR[0].soma { syn_NC_AVBR_AVBL_Generic_GJ_neuron_to_neuron_elec_syn_A[0].weight = 17.0 }")
        h("a_AVBL[0].soma { syn_NC_AVBR_AVBL_Generic_GJ_neuron_to_neuron_elec_syn_B[0].weight = 17.0 }")
        h("setpointer syn_NC_AVBR_AVBL_Generic_GJ_neuron_to_neuron_elec_syn_A[0].vpeer, a_AVBL[0].soma.v(0.5)")
        h("setpointer syn_NC_AVBR_AVBL_Generic_GJ_neuron_to_neuron_elec_syn_B[0].vpeer, a_AVBR[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_AVBR_DB3_Generic_GJ
        print("Adding electrical projection: NC_AVBR_DB3_Generic_GJ from AVBR to DB3, with 1 connection(s)")

        h("objectvar syn_NC_AVBR_DB3_Generic_GJ_AVBR_to_DB3_elec_syn_A[1]")
        h("objectvar syn_NC_AVBR_DB3_Generic_GJ_AVBR_to_DB3_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVBR[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DB3[0].soma], weight: 2.0
        h("a_AVBR[0].soma { syn_NC_AVBR_DB3_Generic_GJ_AVBR_to_DB3_elec_syn_A[0] = new AVBR_to_DB3_elec_syn(0.5) }")
        h("a_DB3[0].soma { syn_NC_AVBR_DB3_Generic_GJ_AVBR_to_DB3_elec_syn_B[0] = new AVBR_to_DB3_elec_syn(0.5) }")
        h("a_AVBR[0].soma { syn_NC_AVBR_DB3_Generic_GJ_AVBR_to_DB3_elec_syn_A[0].weight = 2.0 }")
        h("a_DB3[0].soma { syn_NC_AVBR_DB3_Generic_GJ_AVBR_to_DB3_elec_syn_B[0].weight = 2.0 }")
        h("setpointer syn_NC_AVBR_DB3_Generic_GJ_AVBR_to_DB3_elec_syn_A[0].vpeer, a_DB3[0].soma.v(0.5)")
        h("setpointer syn_NC_AVBR_DB3_Generic_GJ_AVBR_to_DB3_elec_syn_B[0].vpeer, a_AVBR[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_DA3_AVAL_Generic_GJ
        print("Adding electrical projection: NC_DA3_AVAL_Generic_GJ from DA3 to AVAL, with 1 connection(s)")

        h("objectvar syn_NC_DA3_AVAL_Generic_GJ_DA3_to_AVAL_elec_syn_A[1]")
        h("objectvar syn_NC_DA3_AVAL_Generic_GJ_DA3_to_AVAL_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DA3[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVAL[0].soma], weight: 6.0
        h("a_DA3[0].soma { syn_NC_DA3_AVAL_Generic_GJ_DA3_to_AVAL_elec_syn_A[0] = new DA3_to_AVAL_elec_syn(0.5) }")
        h("a_AVAL[0].soma { syn_NC_DA3_AVAL_Generic_GJ_DA3_to_AVAL_elec_syn_B[0] = new DA3_to_AVAL_elec_syn(0.5) }")
        h("a_DA3[0].soma { syn_NC_DA3_AVAL_Generic_GJ_DA3_to_AVAL_elec_syn_A[0].weight = 6.0 }")
        h("a_AVAL[0].soma { syn_NC_DA3_AVAL_Generic_GJ_DA3_to_AVAL_elec_syn_B[0].weight = 6.0 }")
        h("setpointer syn_NC_DA3_AVAL_Generic_GJ_DA3_to_AVAL_elec_syn_A[0].vpeer, a_AVAL[0].soma.v(0.5)")
        h("setpointer syn_NC_DA3_AVAL_Generic_GJ_DA3_to_AVAL_elec_syn_B[0].vpeer, a_DA3[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_DA3_AVAR_Generic_GJ
        print("Adding electrical projection: NC_DA3_AVAR_Generic_GJ from DA3 to AVAR, with 1 connection(s)")

        h("objectvar syn_NC_DA3_AVAR_Generic_GJ_DA3_to_AVAR_elec_syn_A[1]")
        h("objectvar syn_NC_DA3_AVAR_Generic_GJ_DA3_to_AVAR_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DA3[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVAR[0].soma], weight: 7.0
        h("a_DA3[0].soma { syn_NC_DA3_AVAR_Generic_GJ_DA3_to_AVAR_elec_syn_A[0] = new DA3_to_AVAR_elec_syn(0.5) }")
        h("a_AVAR[0].soma { syn_NC_DA3_AVAR_Generic_GJ_DA3_to_AVAR_elec_syn_B[0] = new DA3_to_AVAR_elec_syn(0.5) }")
        h("a_DA3[0].soma { syn_NC_DA3_AVAR_Generic_GJ_DA3_to_AVAR_elec_syn_A[0].weight = 7.0 }")
        h("a_AVAR[0].soma { syn_NC_DA3_AVAR_Generic_GJ_DA3_to_AVAR_elec_syn_B[0].weight = 7.0 }")
        h("setpointer syn_NC_DA3_AVAR_Generic_GJ_DA3_to_AVAR_elec_syn_A[0].vpeer, a_AVAR[0].soma.v(0.5)")
        h("setpointer syn_NC_DA3_AVAR_Generic_GJ_DA3_to_AVAR_elec_syn_B[0].vpeer, a_DA3[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_DB3_AVBL_Generic_GJ
        print("Adding electrical projection: NC_DB3_AVBL_Generic_GJ from DB3 to AVBL, with 1 connection(s)")

        h("objectvar syn_NC_DB3_AVBL_Generic_GJ_DB3_to_AVBL_elec_syn_A[1]")
        h("objectvar syn_NC_DB3_AVBL_Generic_GJ_DB3_to_AVBL_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB3[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVBL[0].soma], weight: 9.0
        h("a_DB3[0].soma { syn_NC_DB3_AVBL_Generic_GJ_DB3_to_AVBL_elec_syn_A[0] = new DB3_to_AVBL_elec_syn(0.5) }")
        h("a_AVBL[0].soma { syn_NC_DB3_AVBL_Generic_GJ_DB3_to_AVBL_elec_syn_B[0] = new DB3_to_AVBL_elec_syn(0.5) }")
        h("a_DB3[0].soma { syn_NC_DB3_AVBL_Generic_GJ_DB3_to_AVBL_elec_syn_A[0].weight = 9.0 }")
        h("a_AVBL[0].soma { syn_NC_DB3_AVBL_Generic_GJ_DB3_to_AVBL_elec_syn_B[0].weight = 9.0 }")
        h("setpointer syn_NC_DB3_AVBL_Generic_GJ_DB3_to_AVBL_elec_syn_A[0].vpeer, a_AVBL[0].soma.v(0.5)")
        h("setpointer syn_NC_DB3_AVBL_Generic_GJ_DB3_to_AVBL_elec_syn_B[0].vpeer, a_DB3[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_DB3_AVBR_Generic_GJ
        print("Adding electrical projection: NC_DB3_AVBR_Generic_GJ from DB3 to AVBR, with 1 connection(s)")

        h("objectvar syn_NC_DB3_AVBR_Generic_GJ_DB3_to_AVBR_elec_syn_A[1]")
        h("objectvar syn_NC_DB3_AVBR_Generic_GJ_DB3_to_AVBR_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB3[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVBR[0].soma], weight: 2.0
        h("a_DB3[0].soma { syn_NC_DB3_AVBR_Generic_GJ_DB3_to_AVBR_elec_syn_A[0] = new DB3_to_AVBR_elec_syn(0.5) }")
        h("a_AVBR[0].soma { syn_NC_DB3_AVBR_Generic_GJ_DB3_to_AVBR_elec_syn_B[0] = new DB3_to_AVBR_elec_syn(0.5) }")
        h("a_DB3[0].soma { syn_NC_DB3_AVBR_Generic_GJ_DB3_to_AVBR_elec_syn_A[0].weight = 2.0 }")
        h("a_AVBR[0].soma { syn_NC_DB3_AVBR_Generic_GJ_DB3_to_AVBR_elec_syn_B[0].weight = 2.0 }")
        h("setpointer syn_NC_DB3_AVBR_Generic_GJ_DB3_to_AVBR_elec_syn_A[0].vpeer, a_AVBR[0].soma.v(0.5)")
        h("setpointer syn_NC_DB3_AVBR_Generic_GJ_DB3_to_AVBR_elec_syn_B[0].vpeer, a_DB3[0].soma.v(0.5)")

        # ######################   Continuous Projection: NC_AVAL_AVAR_Acetylcholine
        print("Adding continuous projection: NC_AVAL_AVAR_Acetylcholine from AVAL to AVAR, with 1 connection(s)")

        h("objectvar syn_NC_AVAL_AVAR_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_AVAL_AVAR_Acetylcholine_neuron_to_neuron_exc_syn_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVAL[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVAR[0].soma], weight: 12.0
        h("a_AVAL[0].soma { syn_NC_AVAL_AVAR_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_AVAR[0].soma { syn_NC_AVAL_AVAR_Acetylcholine_neuron_to_neuron_exc_syn_post[0] = new neuron_to_neuron_exc_syn(0.500000) }")
        h("a_AVAL[0].soma { syn_NC_AVAL_AVAR_Acetylcholine_silent_pre[0].weight = 12.0 }")
        h("a_AVAR[0].soma { syn_NC_AVAL_AVAR_Acetylcholine_neuron_to_neuron_exc_syn_post[0].weight = 12.0 }")
        h("setpointer syn_NC_AVAL_AVAR_Acetylcholine_silent_pre[0].vpeer, a_AVAR[0].soma.v(0.500000)")
        h("setpointer syn_NC_AVAL_AVAR_Acetylcholine_neuron_to_neuron_exc_syn_post[0].vpeer, a_AVAL[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_AVAL_AVBL_Acetylcholine
        print("Adding continuous projection: NC_AVAL_AVBL_Acetylcholine from AVAL to AVBL, with 1 connection(s)")

        h("objectvar syn_NC_AVAL_AVBL_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_AVAL_AVBL_Acetylcholine_AVAL_to_AVBL_inh_syn_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVAL[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVBL[0].soma], weight: 2.0
        h("a_AVAL[0].soma { syn_NC_AVAL_AVBL_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_AVBL[0].soma { syn_NC_AVAL_AVBL_Acetylcholine_AVAL_to_AVBL_inh_syn_post[0] = new AVAL_to_AVBL_inh_syn(0.500000) }")
        h("a_AVAL[0].soma { syn_NC_AVAL_AVBL_Acetylcholine_silent_pre[0].weight = 2.0 }")
        h("a_AVBL[0].soma { syn_NC_AVAL_AVBL_Acetylcholine_AVAL_to_AVBL_inh_syn_post[0].weight = 2.0 }")
        h("setpointer syn_NC_AVAL_AVBL_Acetylcholine_silent_pre[0].vpeer, a_AVBL[0].soma.v(0.500000)")
        h("setpointer syn_NC_AVAL_AVBL_Acetylcholine_AVAL_to_AVBL_inh_syn_post[0].vpeer, a_AVAL[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_AVAL_DA3_Acetylcholine
        print("Adding continuous projection: NC_AVAL_DA3_Acetylcholine from AVAL to DA3, with 1 connection(s)")

        h("objectvar syn_NC_AVAL_DA3_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_AVAL_DA3_Acetylcholine_AVAL_to_DA3_exc_syn_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVAL[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DA3[0].soma], weight: 12.0
        h("a_AVAL[0].soma { syn_NC_AVAL_DA3_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_DA3[0].soma { syn_NC_AVAL_DA3_Acetylcholine_AVAL_to_DA3_exc_syn_post[0] = new AVAL_to_DA3_exc_syn(0.500000) }")
        h("a_AVAL[0].soma { syn_NC_AVAL_DA3_Acetylcholine_silent_pre[0].weight = 12.0 }")
        h("a_DA3[0].soma { syn_NC_AVAL_DA3_Acetylcholine_AVAL_to_DA3_exc_syn_post[0].weight = 12.0 }")
        h("setpointer syn_NC_AVAL_DA3_Acetylcholine_silent_pre[0].vpeer, a_DA3[0].soma.v(0.500000)")
        h("setpointer syn_NC_AVAL_DA3_Acetylcholine_AVAL_to_DA3_exc_syn_post[0].vpeer, a_AVAL[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_AVAR_AVAL_Acetylcholine
        print("Adding continuous projection: NC_AVAR_AVAL_Acetylcholine from AVAR to AVAL, with 1 connection(s)")

        h("objectvar syn_NC_AVAR_AVAL_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_AVAR_AVAL_Acetylcholine_neuron_to_neuron_exc_syn_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVAR[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVAL[0].soma], weight: 7.0
        h("a_AVAR[0].soma { syn_NC_AVAR_AVAL_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_AVAL[0].soma { syn_NC_AVAR_AVAL_Acetylcholine_neuron_to_neuron_exc_syn_post[0] = new neuron_to_neuron_exc_syn(0.500000) }")
        h("a_AVAR[0].soma { syn_NC_AVAR_AVAL_Acetylcholine_silent_pre[0].weight = 7.0 }")
        h("a_AVAL[0].soma { syn_NC_AVAR_AVAL_Acetylcholine_neuron_to_neuron_exc_syn_post[0].weight = 7.0 }")
        h("setpointer syn_NC_AVAR_AVAL_Acetylcholine_silent_pre[0].vpeer, a_AVAL[0].soma.v(0.500000)")
        h("setpointer syn_NC_AVAR_AVAL_Acetylcholine_neuron_to_neuron_exc_syn_post[0].vpeer, a_AVAR[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_AVAR_AVBL_Acetylcholine
        print("Adding continuous projection: NC_AVAR_AVBL_Acetylcholine from AVAR to AVBL, with 1 connection(s)")

        h("objectvar syn_NC_AVAR_AVBL_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_AVAR_AVBL_Acetylcholine_AVAR_to_AVBL_inh_syn_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVAR[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVBL[0].soma], weight: 3.0
        h("a_AVAR[0].soma { syn_NC_AVAR_AVBL_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_AVBL[0].soma { syn_NC_AVAR_AVBL_Acetylcholine_AVAR_to_AVBL_inh_syn_post[0] = new AVAR_to_AVBL_inh_syn(0.500000) }")
        h("a_AVAR[0].soma { syn_NC_AVAR_AVBL_Acetylcholine_silent_pre[0].weight = 3.0 }")
        h("a_AVBL[0].soma { syn_NC_AVAR_AVBL_Acetylcholine_AVAR_to_AVBL_inh_syn_post[0].weight = 3.0 }")
        h("setpointer syn_NC_AVAR_AVBL_Acetylcholine_silent_pre[0].vpeer, a_AVBL[0].soma.v(0.500000)")
        h("setpointer syn_NC_AVAR_AVBL_Acetylcholine_AVAR_to_AVBL_inh_syn_post[0].vpeer, a_AVAR[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_AVAR_AVBR_Acetylcholine
        print("Adding continuous projection: NC_AVAR_AVBR_Acetylcholine from AVAR to AVBR, with 1 connection(s)")

        h("objectvar syn_NC_AVAR_AVBR_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_AVAR_AVBR_Acetylcholine_AVAR_to_AVBR_inh_syn_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVAR[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVBR[0].soma], weight: 4.0
        h("a_AVAR[0].soma { syn_NC_AVAR_AVBR_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_AVBR[0].soma { syn_NC_AVAR_AVBR_Acetylcholine_AVAR_to_AVBR_inh_syn_post[0] = new AVAR_to_AVBR_inh_syn(0.500000) }")
        h("a_AVAR[0].soma { syn_NC_AVAR_AVBR_Acetylcholine_silent_pre[0].weight = 4.0 }")
        h("a_AVBR[0].soma { syn_NC_AVAR_AVBR_Acetylcholine_AVAR_to_AVBR_inh_syn_post[0].weight = 4.0 }")
        h("setpointer syn_NC_AVAR_AVBR_Acetylcholine_silent_pre[0].vpeer, a_AVBR[0].soma.v(0.500000)")
        h("setpointer syn_NC_AVAR_AVBR_Acetylcholine_AVAR_to_AVBR_inh_syn_post[0].vpeer, a_AVAR[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_AVAR_DA3_Acetylcholine
        print("Adding continuous projection: NC_AVAR_DA3_Acetylcholine from AVAR to DA3, with 1 connection(s)")

        h("objectvar syn_NC_AVAR_DA3_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_AVAR_DA3_Acetylcholine_AVAR_to_DA3_exc_syn_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVAR[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DA3[0].soma], weight: 8.0
        h("a_AVAR[0].soma { syn_NC_AVAR_DA3_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_DA3[0].soma { syn_NC_AVAR_DA3_Acetylcholine_AVAR_to_DA3_exc_syn_post[0] = new AVAR_to_DA3_exc_syn(0.500000) }")
        h("a_AVAR[0].soma { syn_NC_AVAR_DA3_Acetylcholine_silent_pre[0].weight = 8.0 }")
        h("a_DA3[0].soma { syn_NC_AVAR_DA3_Acetylcholine_AVAR_to_DA3_exc_syn_post[0].weight = 8.0 }")
        h("setpointer syn_NC_AVAR_DA3_Acetylcholine_silent_pre[0].vpeer, a_DA3[0].soma.v(0.500000)")
        h("setpointer syn_NC_AVAR_DA3_Acetylcholine_AVAR_to_DA3_exc_syn_post[0].vpeer, a_AVAR[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_AVBL_AVAL_Acetylcholine
        print("Adding continuous projection: NC_AVBL_AVAL_Acetylcholine from AVBL to AVAL, with 1 connection(s)")

        h("objectvar syn_NC_AVBL_AVAL_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_AVBL_AVAL_Acetylcholine_AVBL_to_AVAL_inh_syn_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVBL[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVAL[0].soma], weight: 9.0
        h("a_AVBL[0].soma { syn_NC_AVBL_AVAL_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_AVAL[0].soma { syn_NC_AVBL_AVAL_Acetylcholine_AVBL_to_AVAL_inh_syn_post[0] = new AVBL_to_AVAL_inh_syn(0.500000) }")
        h("a_AVBL[0].soma { syn_NC_AVBL_AVAL_Acetylcholine_silent_pre[0].weight = 9.0 }")
        h("a_AVAL[0].soma { syn_NC_AVBL_AVAL_Acetylcholine_AVBL_to_AVAL_inh_syn_post[0].weight = 9.0 }")
        h("setpointer syn_NC_AVBL_AVAL_Acetylcholine_silent_pre[0].vpeer, a_AVAL[0].soma.v(0.500000)")
        h("setpointer syn_NC_AVBL_AVAL_Acetylcholine_AVBL_to_AVAL_inh_syn_post[0].vpeer, a_AVBL[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_AVBL_AVAR_Acetylcholine
        print("Adding continuous projection: NC_AVBL_AVAR_Acetylcholine from AVBL to AVAR, with 1 connection(s)")

        h("objectvar syn_NC_AVBL_AVAR_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_AVBL_AVAR_Acetylcholine_AVBL_to_AVAR_inh_syn_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVBL[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVAR[0].soma], weight: 14.0
        h("a_AVBL[0].soma { syn_NC_AVBL_AVAR_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_AVAR[0].soma { syn_NC_AVBL_AVAR_Acetylcholine_AVBL_to_AVAR_inh_syn_post[0] = new AVBL_to_AVAR_inh_syn(0.500000) }")
        h("a_AVBL[0].soma { syn_NC_AVBL_AVAR_Acetylcholine_silent_pre[0].weight = 14.0 }")
        h("a_AVAR[0].soma { syn_NC_AVBL_AVAR_Acetylcholine_AVBL_to_AVAR_inh_syn_post[0].weight = 14.0 }")
        h("setpointer syn_NC_AVBL_AVAR_Acetylcholine_silent_pre[0].vpeer, a_AVAR[0].soma.v(0.500000)")
        h("setpointer syn_NC_AVBL_AVAR_Acetylcholine_AVBL_to_AVAR_inh_syn_post[0].vpeer, a_AVBL[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_AVBL_AVBR_Acetylcholine
        print("Adding continuous projection: NC_AVBL_AVBR_Acetylcholine from AVBL to AVBR, with 1 connection(s)")

        h("objectvar syn_NC_AVBL_AVBR_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_AVBL_AVBR_Acetylcholine_neuron_to_neuron_exc_syn_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVBL[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVBR[0].soma], weight: 6.0
        h("a_AVBL[0].soma { syn_NC_AVBL_AVBR_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_AVBR[0].soma { syn_NC_AVBL_AVBR_Acetylcholine_neuron_to_neuron_exc_syn_post[0] = new neuron_to_neuron_exc_syn(0.500000) }")
        h("a_AVBL[0].soma { syn_NC_AVBL_AVBR_Acetylcholine_silent_pre[0].weight = 6.0 }")
        h("a_AVBR[0].soma { syn_NC_AVBL_AVBR_Acetylcholine_neuron_to_neuron_exc_syn_post[0].weight = 6.0 }")
        h("setpointer syn_NC_AVBL_AVBR_Acetylcholine_silent_pre[0].vpeer, a_AVBR[0].soma.v(0.500000)")
        h("setpointer syn_NC_AVBL_AVBR_Acetylcholine_neuron_to_neuron_exc_syn_post[0].vpeer, a_AVBL[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_AVBR_AVAL_Acetylcholine
        print("Adding continuous projection: NC_AVBR_AVAL_Acetylcholine from AVBR to AVAL, with 1 connection(s)")

        h("objectvar syn_NC_AVBR_AVAL_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_AVBR_AVAL_Acetylcholine_AVBR_to_AVAL_inh_syn_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVBR[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVAL[0].soma], weight: 10.0
        h("a_AVBR[0].soma { syn_NC_AVBR_AVAL_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_AVAL[0].soma { syn_NC_AVBR_AVAL_Acetylcholine_AVBR_to_AVAL_inh_syn_post[0] = new AVBR_to_AVAL_inh_syn(0.500000) }")
        h("a_AVBR[0].soma { syn_NC_AVBR_AVAL_Acetylcholine_silent_pre[0].weight = 10.0 }")
        h("a_AVAL[0].soma { syn_NC_AVBR_AVAL_Acetylcholine_AVBR_to_AVAL_inh_syn_post[0].weight = 10.0 }")
        h("setpointer syn_NC_AVBR_AVAL_Acetylcholine_silent_pre[0].vpeer, a_AVAL[0].soma.v(0.500000)")
        h("setpointer syn_NC_AVBR_AVAL_Acetylcholine_AVBR_to_AVAL_inh_syn_post[0].vpeer, a_AVBR[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_AVBR_AVAR_Acetylcholine
        print("Adding continuous projection: NC_AVBR_AVAR_Acetylcholine from AVBR to AVAR, with 1 connection(s)")

        h("objectvar syn_NC_AVBR_AVAR_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_AVBR_AVAR_Acetylcholine_AVBR_to_AVAR_inh_syn_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVBR[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVAR[0].soma], weight: 14.0
        h("a_AVBR[0].soma { syn_NC_AVBR_AVAR_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_AVAR[0].soma { syn_NC_AVBR_AVAR_Acetylcholine_AVBR_to_AVAR_inh_syn_post[0] = new AVBR_to_AVAR_inh_syn(0.500000) }")
        h("a_AVBR[0].soma { syn_NC_AVBR_AVAR_Acetylcholine_silent_pre[0].weight = 14.0 }")
        h("a_AVAR[0].soma { syn_NC_AVBR_AVAR_Acetylcholine_AVBR_to_AVAR_inh_syn_post[0].weight = 14.0 }")
        h("setpointer syn_NC_AVBR_AVAR_Acetylcholine_silent_pre[0].vpeer, a_AVAR[0].soma.v(0.500000)")
        h("setpointer syn_NC_AVBR_AVAR_Acetylcholine_AVBR_to_AVAR_inh_syn_post[0].vpeer, a_AVBR[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_AVBR_AVBL_Acetylcholine
        print("Adding continuous projection: NC_AVBR_AVBL_Acetylcholine from AVBR to AVBL, with 1 connection(s)")

        h("objectvar syn_NC_AVBR_AVBL_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_AVBR_AVBL_Acetylcholine_neuron_to_neuron_exc_syn_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVBR[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVBL[0].soma], weight: 2.0
        h("a_AVBR[0].soma { syn_NC_AVBR_AVBL_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_AVBL[0].soma { syn_NC_AVBR_AVBL_Acetylcholine_neuron_to_neuron_exc_syn_post[0] = new neuron_to_neuron_exc_syn(0.500000) }")
        h("a_AVBR[0].soma { syn_NC_AVBR_AVBL_Acetylcholine_silent_pre[0].weight = 2.0 }")
        h("a_AVBL[0].soma { syn_NC_AVBR_AVBL_Acetylcholine_neuron_to_neuron_exc_syn_post[0].weight = 2.0 }")
        h("setpointer syn_NC_AVBR_AVBL_Acetylcholine_silent_pre[0].vpeer, a_AVBL[0].soma.v(0.500000)")
        h("setpointer syn_NC_AVBR_AVBL_Acetylcholine_neuron_to_neuron_exc_syn_post[0].vpeer, a_AVBR[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DA3_DB3_Acetylcholine
        print("Adding continuous projection: NC_DA3_DB3_Acetylcholine from DA3 to DB3, with 1 connection(s)")

        h("objectvar syn_NC_DA3_DB3_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DA3_DB3_Acetylcholine_DA3_to_DB3_exc_syn_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DA3[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DB3[0].soma], weight: 2.0
        h("a_DA3[0].soma { syn_NC_DA3_DB3_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_DB3[0].soma { syn_NC_DA3_DB3_Acetylcholine_DA3_to_DB3_exc_syn_post[0] = new DA3_to_DB3_exc_syn(0.500000) }")
        h("a_DA3[0].soma { syn_NC_DA3_DB3_Acetylcholine_silent_pre[0].weight = 2.0 }")
        h("a_DB3[0].soma { syn_NC_DA3_DB3_Acetylcholine_DA3_to_DB3_exc_syn_post[0].weight = 2.0 }")
        h("setpointer syn_NC_DA3_DB3_Acetylcholine_silent_pre[0].vpeer, a_DB3[0].soma.v(0.500000)")
        h("setpointer syn_NC_DA3_DB3_Acetylcholine_DA3_to_DB3_exc_syn_post[0].vpeer, a_DA3[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB3_AS4_Acetylcholine
        print("Adding continuous projection: NC_DB3_AS4_Acetylcholine from DB3 to AS4, with 1 connection(s)")

        h("objectvar syn_NC_DB3_AS4_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB3_AS4_Acetylcholine_DB3_to_AS4_inh_syn_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB3[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AS4[0].soma], weight: 2.0
        h("a_DB3[0].soma { syn_NC_DB3_AS4_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_AS4[0].soma { syn_NC_DB3_AS4_Acetylcholine_DB3_to_AS4_inh_syn_post[0] = new DB3_to_AS4_inh_syn(0.500000) }")
        h("a_DB3[0].soma { syn_NC_DB3_AS4_Acetylcholine_silent_pre[0].weight = 2.0 }")
        h("a_AS4[0].soma { syn_NC_DB3_AS4_Acetylcholine_DB3_to_AS4_inh_syn_post[0].weight = 2.0 }")
        h("setpointer syn_NC_DB3_AS4_Acetylcholine_silent_pre[0].vpeer, a_AS4[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB3_AS4_Acetylcholine_DB3_to_AS4_inh_syn_post[0].vpeer, a_DB3[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_AS4_DA3_Acetylcholine
        print("Adding continuous projection: NC_AS4_DA3_Acetylcholine from AS4 to DA3, with 1 connection(s)")

        h("objectvar syn_NC_AS4_DA3_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_AS4_DA3_Acetylcholine_AS4_to_DA3_exc_syn_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AS4[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DA3[0].soma], weight: 2.0
        h("a_AS4[0].soma { syn_NC_AS4_DA3_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_DA3[0].soma { syn_NC_AS4_DA3_Acetylcholine_AS4_to_DA3_exc_syn_post[0] = new AS4_to_DA3_exc_syn(0.500000) }")
        h("a_AS4[0].soma { syn_NC_AS4_DA3_Acetylcholine_silent_pre[0].weight = 2.0 }")
        h("a_DA3[0].soma { syn_NC_AS4_DA3_Acetylcholine_AS4_to_DA3_exc_syn_post[0].weight = 2.0 }")
        h("setpointer syn_NC_AS4_DA3_Acetylcholine_silent_pre[0].vpeer, a_DA3[0].soma.v(0.500000)")
        h("setpointer syn_NC_AS4_DA3_Acetylcholine_AS4_to_DA3_exc_syn_post[0].vpeer, a_AS4[0].soma.v(0.500000)")

        # ######################   Input List: Input_AVBL_stim_AVBL_1
        print("Adding input list: Input_AVBL_stim_AVBL_1 to AVBL, with 1 inputs of type stim_AVBL_1")

        # Adding single input: Component(id=0 type=input)
        h("objref Input_AVBL_stim_AVBL_1_0")
        h("a_AVBL[0].soma { Input_AVBL_stim_AVBL_1_0 = new stim_AVBL_1(0.5) } ")

        # ######################   Input List: Input_AVBR_stim_AVBR_1
        print("Adding input list: Input_AVBR_stim_AVBR_1 to AVBR, with 1 inputs of type stim_AVBR_1")

        # Adding single input: Component(id=0 type=input)
        h("objref Input_AVBR_stim_AVBR_1_0")
        h("a_AVBR[0].soma { Input_AVBR_stim_AVBR_1_0 = new stim_AVBR_1(0.5) } ")

        # ######################   Input List: Input_AVAL_stim_AVAL_1
        print("Adding input list: Input_AVAL_stim_AVAL_1 to AVAL, with 1 inputs of type stim_AVAL_1")

        # Adding single input: Component(id=0 type=input)
        h("objref Input_AVAL_stim_AVAL_1_0")
        h("a_AVAL[0].soma { Input_AVAL_stim_AVAL_1_0 = new stim_AVAL_1(0.5) } ")

        # ######################   Input List: Input_AVAR_stim_AVAR_1
        print("Adding input list: Input_AVAR_stim_AVAR_1 to AVAR, with 1 inputs of type stim_AVAR_1")

        # Adding single input: Component(id=0 type=input)
        h("objref Input_AVAR_stim_AVAR_1_0")
        h("a_AVAR[0].soma { Input_AVAR_stim_AVAR_1_0 = new stim_AVAR_1(0.5) } ")

        # ######################   Input List: Input_AVBL_stim_AVBL_2
        print("Adding input list: Input_AVBL_stim_AVBL_2 to AVBL, with 1 inputs of type stim_AVBL_2")

        # Adding single input: Component(id=0 type=input)
        h("objref Input_AVBL_stim_AVBL_2_0")
        h("a_AVBL[0].soma { Input_AVBL_stim_AVBL_2_0 = new stim_AVBL_2(0.5) } ")

        # ######################   Input List: Input_AVBR_stim_AVBR_2
        print("Adding input list: Input_AVBR_stim_AVBR_2 to AVBR, with 1 inputs of type stim_AVBR_2")

        # Adding single input: Component(id=0 type=input)
        h("objref Input_AVBR_stim_AVBR_2_0")
        h("a_AVBR[0].soma { Input_AVBR_stim_AVBR_2_0 = new stim_AVBR_2(0.5) } ")

        # ######################   Input List: Input_AS4_stim_AS4_1
        print("Adding input list: Input_AS4_stim_AS4_1 to AS4, with 1 inputs of type stim_AS4_1")

        # Adding single input: Component(id=0 type=input)
        h("objref Input_AS4_stim_AS4_1_0")
        h("a_AS4[0].soma { Input_AS4_stim_AS4_1_0 = new stim_AS4_1(0.5) } ")

        trec = h.Vector()
        trec.record(h._ref_t)

        h.tstop = tstop

        h.dt = dt

        h.steps_per_ms = 1/h.dt



        # ######################   File to save: c302_C2_AS4_DA3_DB3.activity.dat (neurons_activity)
        # Column: AS4/0/GenericNeuronCell/caConc
        h(' objectvar v_AS4_v_neurons_activity ')
        h(' { v_AS4_v_neurons_activity = new Vector() } ')
        h(' { v_AS4_v_neurons_activity.record(&a_AS4[0].soma.cai(0.5)) } ')
        h.v_AS4_v_neurons_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: AVAL/0/GenericNeuronCell/caConc
        h(' objectvar v_AVAL_v_neurons_activity ')
        h(' { v_AVAL_v_neurons_activity = new Vector() } ')
        h(' { v_AVAL_v_neurons_activity.record(&a_AVAL[0].soma.cai(0.5)) } ')
        h.v_AVAL_v_neurons_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: AVAR/0/GenericNeuronCell/caConc
        h(' objectvar v_AVAR_v_neurons_activity ')
        h(' { v_AVAR_v_neurons_activity = new Vector() } ')
        h(' { v_AVAR_v_neurons_activity.record(&a_AVAR[0].soma.cai(0.5)) } ')
        h.v_AVAR_v_neurons_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: AVBL/0/GenericNeuronCell/caConc
        h(' objectvar v_AVBL_v_neurons_activity ')
        h(' { v_AVBL_v_neurons_activity = new Vector() } ')
        h(' { v_AVBL_v_neurons_activity.record(&a_AVBL[0].soma.cai(0.5)) } ')
        h.v_AVBL_v_neurons_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: AVBR/0/GenericNeuronCell/caConc
        h(' objectvar v_AVBR_v_neurons_activity ')
        h(' { v_AVBR_v_neurons_activity = new Vector() } ')
        h(' { v_AVBR_v_neurons_activity.record(&a_AVBR[0].soma.cai(0.5)) } ')
        h.v_AVBR_v_neurons_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: DA3/0/GenericNeuronCell/caConc
        h(' objectvar v_DA3_v_neurons_activity ')
        h(' { v_DA3_v_neurons_activity = new Vector() } ')
        h(' { v_DA3_v_neurons_activity.record(&a_DA3[0].soma.cai(0.5)) } ')
        h.v_DA3_v_neurons_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: DB3/0/GenericNeuronCell/caConc
        h(' objectvar v_DB3_v_neurons_activity ')
        h(' { v_DB3_v_neurons_activity = new Vector() } ')
        h(' { v_DB3_v_neurons_activity.record(&a_DB3[0].soma.cai(0.5)) } ')
        h.v_DB3_v_neurons_activity.resize((h.tstop * h.steps_per_ms) + 1)

        # ######################   File to save: c302_C2_AS4_DA3_DB3.dat (neurons_v)
        # Column: AS4/0/GenericNeuronCell/v
        h(' objectvar v_AS4_v_neurons_v ')
        h(' { v_AS4_v_neurons_v = new Vector() } ')
        h(' { v_AS4_v_neurons_v.record(&a_AS4[0].soma.v(0.5)) } ')
        h.v_AS4_v_neurons_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: AVAL/0/GenericNeuronCell/v
        h(' objectvar v_AVAL_v_neurons_v ')
        h(' { v_AVAL_v_neurons_v = new Vector() } ')
        h(' { v_AVAL_v_neurons_v.record(&a_AVAL[0].soma.v(0.5)) } ')
        h.v_AVAL_v_neurons_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: AVAR/0/GenericNeuronCell/v
        h(' objectvar v_AVAR_v_neurons_v ')
        h(' { v_AVAR_v_neurons_v = new Vector() } ')
        h(' { v_AVAR_v_neurons_v.record(&a_AVAR[0].soma.v(0.5)) } ')
        h.v_AVAR_v_neurons_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: AVBL/0/GenericNeuronCell/v
        h(' objectvar v_AVBL_v_neurons_v ')
        h(' { v_AVBL_v_neurons_v = new Vector() } ')
        h(' { v_AVBL_v_neurons_v.record(&a_AVBL[0].soma.v(0.5)) } ')
        h.v_AVBL_v_neurons_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: AVBR/0/GenericNeuronCell/v
        h(' objectvar v_AVBR_v_neurons_v ')
        h(' { v_AVBR_v_neurons_v = new Vector() } ')
        h(' { v_AVBR_v_neurons_v.record(&a_AVBR[0].soma.v(0.5)) } ')
        h.v_AVBR_v_neurons_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: DA3/0/GenericNeuronCell/v
        h(' objectvar v_DA3_v_neurons_v ')
        h(' { v_DA3_v_neurons_v = new Vector() } ')
        h(' { v_DA3_v_neurons_v.record(&a_DA3[0].soma.v(0.5)) } ')
        h.v_DA3_v_neurons_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: DB3/0/GenericNeuronCell/v
        h(' objectvar v_DB3_v_neurons_v ')
        h(' { v_DB3_v_neurons_v = new Vector() } ')
        h(' { v_DB3_v_neurons_v.record(&a_DB3[0].soma.v(0.5)) } ')
        h.v_DB3_v_neurons_v.resize((h.tstop * h.steps_per_ms) + 1)

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

        # ######################   File to save: c302_C2_AS4_DA3_DB3.activity.dat (neurons_activity)
        py_v_AS4_v_neurons_activity = [ float(x ) for x in h.v_AS4_v_neurons_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_AVAL_v_neurons_activity = [ float(x ) for x in h.v_AVAL_v_neurons_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_AVAR_v_neurons_activity = [ float(x ) for x in h.v_AVAR_v_neurons_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_AVBL_v_neurons_activity = [ float(x ) for x in h.v_AVBL_v_neurons_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_AVBR_v_neurons_activity = [ float(x ) for x in h.v_AVBR_v_neurons_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_DA3_v_neurons_activity = [ float(x ) for x in h.v_DA3_v_neurons_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_DB3_v_neurons_activity = [ float(x ) for x in h.v_DB3_v_neurons_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration

        f_neurons_activity_f2 = open('c302_C2_AS4_DA3_DB3.activity.dat', 'w')
        num_points = len(py_v_time)  # Simulation may have been stopped before tstop...

        for i in range(num_points):
            f_neurons_activity_f2.write('%e\t'% py_v_time[i]  + '%e\t'%(py_v_AS4_v_neurons_activity[i])  + '%e\t'%(py_v_AVAL_v_neurons_activity[i])  + '%e\t'%(py_v_AVAR_v_neurons_activity[i])  + '%e\t'%(py_v_AVBL_v_neurons_activity[i])  + '%e\t'%(py_v_AVBR_v_neurons_activity[i])  + '%e\t'%(py_v_DA3_v_neurons_activity[i])  + '%e\t'%(py_v_DB3_v_neurons_activity[i]) + '\n')
        f_neurons_activity_f2.close()
        print("Saved data to: c302_C2_AS4_DA3_DB3.activity.dat")

        # ######################   File to save: c302_C2_AS4_DA3_DB3.dat (neurons_v)
        py_v_AS4_v_neurons_v = [ float(x  / 1000.0) for x in h.v_AS4_v_neurons_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_AVAL_v_neurons_v = [ float(x  / 1000.0) for x in h.v_AVAL_v_neurons_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_AVAR_v_neurons_v = [ float(x  / 1000.0) for x in h.v_AVAR_v_neurons_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_AVBL_v_neurons_v = [ float(x  / 1000.0) for x in h.v_AVBL_v_neurons_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_AVBR_v_neurons_v = [ float(x  / 1000.0) for x in h.v_AVBR_v_neurons_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_DA3_v_neurons_v = [ float(x  / 1000.0) for x in h.v_DA3_v_neurons_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_DB3_v_neurons_v = [ float(x  / 1000.0) for x in h.v_DB3_v_neurons_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage

        f_neurons_v_f2 = open('c302_C2_AS4_DA3_DB3.dat', 'w')
        num_points = len(py_v_time)  # Simulation may have been stopped before tstop...

        for i in range(num_points):
            f_neurons_v_f2.write('%e\t'% py_v_time[i]  + '%e\t'%(py_v_AS4_v_neurons_v[i])  + '%e\t'%(py_v_AVAL_v_neurons_v[i])  + '%e\t'%(py_v_AVAR_v_neurons_v[i])  + '%e\t'%(py_v_AVBL_v_neurons_v[i])  + '%e\t'%(py_v_AVBR_v_neurons_v[i])  + '%e\t'%(py_v_DA3_v_neurons_v[i])  + '%e\t'%(py_v_DB3_v_neurons_v[i]) + '\n')
        f_neurons_v_f2.close()
        print("Saved data to: c302_C2_AS4_DA3_DB3.dat")

        save_end = time.time()
        save_time = save_end - self.sim_end
        print("Finished saving results in %f seconds"%(save_time))

        print("Done")

        quit()


if __name__ == '__main__':

    ns = NeuronSimulation(tstop=3000, dt=0.05, seed=123456789)

    ns.run()

