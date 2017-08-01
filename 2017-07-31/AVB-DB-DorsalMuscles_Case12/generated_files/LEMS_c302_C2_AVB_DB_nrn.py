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
    neuron_to_neuron_elec_syn_17conns (Type: gapJunction:  conductance=2.1284E-10 (SI conductance))
    AVBL_to_DB2_elec_syn_4conns (Type: delayedGapJunction:  weight=1.0 (dimensionless) conductance=1.0649687844400001E-10 (SI conductance) sigma=241.179861414 (SI per_voltage) mu=-0.0310977828928 (SI voltage))
    AVBL_to_DB3_elec_syn_9conns (Type: delayedGapJunction:  weight=1.0 (dimensionless) conductance=2.51115734931E-11 (SI conductance) sigma=231.454305083 (SI per_voltage) mu=-0.036332917764 (SI voltage))
    AVBL_to_DB4_elec_syn_4conns (Type: delayedGapJunction:  weight=1.0 (dimensionless) conductance=2.2329372984300001E-10 (SI conductance) sigma=10.0 (SI per_voltage) mu=-0.0662111522665 (SI voltage))
    AVBL_to_DB5_elec_syn_3conns (Type: delayedGapJunction:  weight=1.0 (dimensionless) conductance=6.78836753907E-11 (SI conductance) sigma=536.933455728 (SI per_voltage) mu=-0.0565883926767 (SI voltage))
    AVBL_to_DB6_elec_syn_4conns (Type: delayedGapJunction:  weight=1.0 (dimensionless) conductance=1.41247522585E-11 (SI conductance) sigma=640.309304721 (SI per_voltage) mu=-0.0362192802886 (SI voltage))
    AVBL_to_DB7_elec_syn_13conns (Type: delayedGapJunction:  weight=1.0 (dimensionless) conductance=5.70939587543E-11 (SI conductance) sigma=533.6559136120001 (SI per_voltage) mu=-0.0442515469934 (SI voltage))
    AVBR_to_DB1_elec_syn_15conns (Type: delayedGapJunction:  weight=1.0 (dimensionless) conductance=8.86758575613E-10 (SI conductance) sigma=388.91335924 (SI per_voltage) mu=-0.0636900218048 (SI voltage))
    AVBR_to_DB2_elec_syn_3conns (Type: delayedGapJunction:  weight=1.0 (dimensionless) conductance=1.8756000000000002E-10 (SI conductance) sigma=387.03925423699997 (SI per_voltage) mu=-0.062000341191 (SI voltage))
    AVBR_to_DB3_elec_syn_2conns (Type: delayedGapJunction:  weight=1.0 (dimensionless) conductance=3.96499608164E-11 (SI conductance) sigma=10.0 (SI per_voltage) mu=0.0032623740935800003 (SI voltage))
    AVBR_to_DB4_elec_syn_5conns (Type: delayedGapJunction:  weight=1.0 (dimensionless) conductance=1.61739293968E-11 (SI conductance) sigma=618.755178492 (SI per_voltage) mu=0.0030376469073100003 (SI voltage))
    AVBR_to_DB5_elec_syn_4conns (Type: delayedGapJunction:  weight=1.0 (dimensionless) conductance=3.4948353214700006E-11 (SI conductance) sigma=664.607583389 (SI per_voltage) mu=0.0038543086696 (SI voltage))
    AVBR_to_DB6_elec_syn_3conns (Type: delayedGapJunction:  weight=1.0 (dimensionless) conductance=3.74313000423E-11 (SI conductance) sigma=228.433033088 (SI per_voltage) mu=-0.00518875443492 (SI voltage))
    AVBR_to_DB7_elec_syn_3conns (Type: delayedGapJunction:  weight=1.0 (dimensionless) conductance=1.0741824954700001E-11 (SI conductance) sigma=206.916730813 (SI per_voltage) mu=8.969391093450001E-5 (SI voltage))
    DB1_to_AVBR_elec_syn_15conns (Type: delayedGapJunction:  weight=1.0 (dimensionless) conductance=8.86758575613E-10 (SI conductance) sigma=388.91335924 (SI per_voltage) mu=-0.0636900218048 (SI voltage))
    DB1_to_DB2_elec_syn_5conns (Type: gapJunction:  conductance=1.1260000000000002E-10 (SI conductance))
    DB2_to_AVBL_elec_syn_4conns (Type: delayedGapJunction:  weight=1.0 (dimensionless) conductance=1.0649687844400001E-10 (SI conductance) sigma=241.179861414 (SI per_voltage) mu=-0.0310977828928 (SI voltage))
    DB2_to_AVBR_elec_syn_3conns (Type: delayedGapJunction:  weight=1.0 (dimensionless) conductance=1.8756000000000002E-10 (SI conductance) sigma=387.03925423699997 (SI per_voltage) mu=-0.062000341191 (SI voltage))
    DB2_to_DB1_elec_syn_5conns (Type: gapJunction:  conductance=1.1260000000000002E-10 (SI conductance))
    DB2_to_DB3_elec_syn_14conns (Type: gapJunction:  conductance=3.1528E-10 (SI conductance))
    DB3_to_AVBL_elec_syn_9conns (Type: delayedGapJunction:  weight=1.0 (dimensionless) conductance=2.51115734931E-11 (SI conductance) sigma=231.454305083 (SI per_voltage) mu=-0.036332917764 (SI voltage))
    DB3_to_AVBR_elec_syn_2conns (Type: delayedGapJunction:  weight=1.0 (dimensionless) conductance=3.96499608164E-11 (SI conductance) sigma=10.0 (SI per_voltage) mu=0.0032623740935800003 (SI voltage))
    DB3_to_DB2_elec_syn_14conns (Type: gapJunction:  conductance=3.1528E-10 (SI conductance))
    DB3_to_DB4_elec_syn_1conns (Type: gapJunction:  conductance=2.252E-11 (SI conductance))
    DB4_to_AVBL_elec_syn_4conns (Type: delayedGapJunction:  weight=1.0 (dimensionless) conductance=2.2329372984300001E-10 (SI conductance) sigma=10.0 (SI per_voltage) mu=-0.0662111522665 (SI voltage))
    DB4_to_AVBR_elec_syn_5conns (Type: delayedGapJunction:  weight=1.0 (dimensionless) conductance=1.61739293968E-11 (SI conductance) sigma=618.755178492 (SI per_voltage) mu=0.0030376469073100003 (SI voltage))
    DB4_to_DB3_elec_syn_1conns (Type: gapJunction:  conductance=2.252E-11 (SI conductance))
    DB4_to_DB5_elec_syn_5conns (Type: gapJunction:  conductance=1.1260000000000002E-10 (SI conductance))
    DB5_to_AVBL_elec_syn_3conns (Type: delayedGapJunction:  weight=1.0 (dimensionless) conductance=6.78836753907E-11 (SI conductance) sigma=536.933455728 (SI per_voltage) mu=-0.0565883926767 (SI voltage))
    DB5_to_AVBR_elec_syn_4conns (Type: delayedGapJunction:  weight=1.0 (dimensionless) conductance=3.4948353214700006E-11 (SI conductance) sigma=664.607583389 (SI per_voltage) mu=0.0038543086696 (SI voltage))
    DB5_to_DB4_elec_syn_5conns (Type: gapJunction:  conductance=1.1260000000000002E-10 (SI conductance))
    DB5_to_DB6_elec_syn_5conns (Type: gapJunction:  conductance=1.1260000000000002E-10 (SI conductance))
    DB6_to_AVBL_elec_syn_3conns (Type: delayedGapJunction:  weight=1.0 (dimensionless) conductance=1.05935641939E-11 (SI conductance) sigma=640.309304721 (SI per_voltage) mu=-0.0362192802886 (SI voltage))
    DB6_to_AVBR_elec_syn_4conns (Type: delayedGapJunction:  weight=1.0 (dimensionless) conductance=4.9908400056400004E-11 (SI conductance) sigma=228.433033088 (SI per_voltage) mu=-0.00518875443492 (SI voltage))
    DB6_to_DB5_elec_syn_5conns (Type: gapJunction:  conductance=1.1260000000000002E-10 (SI conductance))
    DB6_to_DB7_elec_syn_5conns (Type: gapJunction:  conductance=1.1260000000000002E-10 (SI conductance))
    DB7_to_AVBL_elec_syn_13conns (Type: delayedGapJunction:  weight=1.0 (dimensionless) conductance=3.10939587543E-11 (SI conductance) sigma=533.6559136120001 (SI per_voltage) mu=-0.0442515469934 (SI voltage))
    DB7_to_AVBR_elec_syn_3conns (Type: delayedGapJunction:  weight=1.0 (dimensionless) conductance=1.0741824954700001E-11 (SI conductance) sigma=206.916730813 (SI per_voltage) mu=8.969391093450001E-5 (SI voltage))
    DB7_to_DB6_elec_syn_5conns (Type: gapJunction:  conductance=1.1260000000000002E-10 (SI conductance))
    muscle_to_muscle_elec_syn_15conns (Type: gapJunction:  conductance=2.25E-11 (SI conductance))
    muscle_to_muscle_elec_syn_2conns (Type: gapJunction:  conductance=3.0E-12 (SI conductance))
    silent (Type: silentSynapse)
    neuron_to_neuron_exc_syn_6conns (Type: gradedSynapse:  conductance=2.94E-9 (SI conductance) delta=0.005 (SI voltage) k=500.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.01 (SI voltage))
    neuron_to_neuron_exc_syn_2conns (Type: gradedSynapse:  conductance=9.800000000000001E-10 (SI conductance) delta=0.005 (SI voltage) k=500.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.01 (SI voltage))
    neuron_to_neuron_exc_syn_1conns (Type: gradedSynapse:  conductance=4.900000000000001E-10 (SI conductance) delta=0.005 (SI voltage) k=500.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.01 (SI voltage))
    neuron_to_muscle_exc_syn_1conns (Type: gradedSynapse:  conductance=1.0000000000000002E-10 (SI conductance) delta=0.019 (SI voltage) k=1205.0 (SI per_time) Vth=0.027 (SI voltage) erev=0.037 (SI voltage))
    DB1_to_MDL06_exc_syn_3conns (Type: gradedSynapse:  conductance=3.0E-10 (SI conductance) delta=0.019 (SI voltage) k=1205.0 (SI per_time) Vth=0.027 (SI voltage) erev=0.037 (SI voltage))
    DB1_to_MDL08_exc_syn_3conns (Type: gradedSynapse:  conductance=2.1E-10 (SI conductance) delta=0.019 (SI voltage) k=1205.0 (SI per_time) Vth=0.027 (SI voltage) erev=0.037 (SI voltage))
    DB1_to_MDL09_exc_syn_6conns (Type: gradedSynapse:  conductance=4.8E-11 (SI conductance) delta=0.019 (SI voltage) k=1205.0 (SI per_time) Vth=0.027 (SI voltage) erev=0.037 (SI voltage))
    DB1_to_MDR08_exc_syn_6conns (Type: gradedSynapse:  conductance=6.0E-10 (SI conductance) delta=0.019 (SI voltage) k=1205.0 (SI per_time) Vth=0.027 (SI voltage) erev=0.037 (SI voltage))
    DB1_to_MDR09_exc_syn_2conns (Type: gradedSynapse:  conductance=2.0000000000000003E-10 (SI conductance) delta=0.019 (SI voltage) k=1205.0 (SI per_time) Vth=0.027 (SI voltage) erev=0.037 (SI voltage))
    DB2_to_MDL09_exc_syn_2conns (Type: gradedSynapse:  conductance=2.0000000000000003E-10 (SI conductance) delta=0.019 (SI voltage) k=1205.0 (SI per_time) Vth=0.027 (SI voltage) erev=0.037 (SI voltage))
    DB2_to_MDL10_exc_syn_4conns (Type: gradedSynapse:  conductance=2.4E-10 (SI conductance) delta=0.019 (SI voltage) k=1205.0 (SI per_time) Vth=0.027 (SI voltage) erev=0.037 (SI voltage))
    DB2_to_MDL11_exc_syn_5conns (Type: gradedSynapse:  conductance=1.75E-10 (SI conductance) delta=0.019 (SI voltage) k=1205.0 (SI per_time) Vth=0.027 (SI voltage) erev=0.037 (SI voltage))
    DB2_to_MDL12_exc_syn_1conns (Type: gradedSynapse:  conductance=1.1500000000000002E-10 (SI conductance) delta=0.019 (SI voltage) k=1205.0 (SI per_time) Vth=0.027 (SI voltage) erev=0.037 (SI voltage))
    DB2_to_MDR09_exc_syn_1conns (Type: gradedSynapse:  conductance=1.0000000000000002E-10 (SI conductance) delta=0.019 (SI voltage) k=1205.0 (SI per_time) Vth=0.027 (SI voltage) erev=0.037 (SI voltage))
    DB2_to_MDR10_exc_syn_6conns (Type: gradedSynapse:  conductance=6.0E-10 (SI conductance) delta=0.019 (SI voltage) k=1205.0 (SI per_time) Vth=0.027 (SI voltage) erev=0.037 (SI voltage))
    DB2_to_MDR11_exc_syn_8conns (Type: gradedSynapse:  conductance=8.000000000000001E-10 (SI conductance) delta=0.019 (SI voltage) k=1205.0 (SI per_time) Vth=0.027 (SI voltage) erev=0.037 (SI voltage))
    DB3_to_MDL11_exc_syn_6conns (Type: gradedSynapse:  conductance=9.0E-11 (SI conductance) delta=0.019 (SI voltage) k=1205.0 (SI per_time) Vth=0.027 (SI voltage) erev=0.037 (SI voltage))
    DB3_to_MDL13_exc_syn_3conns (Type: gradedSynapse:  conductance=9.0E-11 (SI conductance) delta=0.019 (SI voltage) k=1205.0 (SI per_time) Vth=0.027 (SI voltage) erev=0.037 (SI voltage))
    DB3_to_MDL14_exc_syn_1conns (Type: gradedSynapse:  conductance=4.0000000000000004E-11 (SI conductance) delta=0.019 (SI voltage) k=1205.0 (SI per_time) Vth=0.027 (SI voltage) erev=0.037 (SI voltage))
    neuron_to_muscle_exc_syn_2conns (Type: gradedSynapse:  conductance=2.0000000000000003E-10 (SI conductance) delta=0.019 (SI voltage) k=1205.0 (SI per_time) Vth=0.027 (SI voltage) erev=0.037 (SI voltage))
    neuron_to_muscle_exc_syn_13conns (Type: gradedSynapse:  conductance=1.3E-9 (SI conductance) delta=0.019 (SI voltage) k=1205.0 (SI per_time) Vth=0.027 (SI voltage) erev=0.037 (SI voltage))
    DB4_to_MDL13_exc_syn_4conns (Type: gradedSynapse:  conductance=1.2E-10 (SI conductance) delta=0.019 (SI voltage) k=1205.0 (SI per_time) Vth=0.027 (SI voltage) erev=0.037 (SI voltage))
    DB4_to_MDL14_exc_syn_1conns (Type: gradedSynapse:  conductance=4.0000000000000004E-11 (SI conductance) delta=0.019 (SI voltage) k=1205.0 (SI per_time) Vth=0.027 (SI voltage) erev=0.037 (SI voltage))
    DB4_to_MDL15_exc_syn_3conns (Type: gradedSynapse:  conductance=6.6E-11 (SI conductance) delta=0.019 (SI voltage) k=1205.0 (SI per_time) Vth=0.027 (SI voltage) erev=0.037 (SI voltage))
    DB4_to_MDL16_exc_syn_3conns (Type: gradedSynapse:  conductance=6.3E-11 (SI conductance) delta=0.019 (SI voltage) k=1205.0 (SI per_time) Vth=0.027 (SI voltage) erev=0.037 (SI voltage))
    neuron_to_muscle_exc_syn_3conns (Type: gradedSynapse:  conductance=3.0E-10 (SI conductance) delta=0.019 (SI voltage) k=1205.0 (SI per_time) Vth=0.027 (SI voltage) erev=0.037 (SI voltage))
    neuron_to_muscle_exc_syn_5conns (Type: gradedSynapse:  conductance=5.0E-10 (SI conductance) delta=0.019 (SI voltage) k=1205.0 (SI per_time) Vth=0.027 (SI voltage) erev=0.037 (SI voltage))
    DB5_to_MDL16_exc_syn_2conns (Type: gradedSynapse:  conductance=8.000000000000001E-11 (SI conductance) delta=0.019 (SI voltage) k=1205.0 (SI per_time) Vth=0.027 (SI voltage) erev=0.037 (SI voltage))
    DB5_to_MDL17_exc_syn_2conns (Type: gradedSynapse:  conductance=1.8E-10 (SI conductance) delta=0.019 (SI voltage) k=1205.0 (SI per_time) Vth=0.027 (SI voltage) erev=0.037 (SI voltage))
    DB5_to_MDL18_exc_syn_2conns (Type: gradedSynapse:  conductance=1.6000000000000002E-10 (SI conductance) delta=0.019 (SI voltage) k=1205.0 (SI per_time) Vth=0.027 (SI voltage) erev=0.037 (SI voltage))
    DB5_to_MDL19_exc_syn_2conns (Type: gradedSynapse:  conductance=1.0000000000000002E-10 (SI conductance) delta=0.019 (SI voltage) k=1205.0 (SI per_time) Vth=0.027 (SI voltage) erev=0.037 (SI voltage))
    DB6_to_MDL19_exc_syn_2conns (Type: gradedSynapse:  conductance=1.2E-10 (SI conductance) delta=0.019 (SI voltage) k=1205.0 (SI per_time) Vth=0.027 (SI voltage) erev=0.037 (SI voltage))
    DB6_to_MDL20_exc_syn_2conns (Type: gradedSynapse:  conductance=2.8000000000000007E-10 (SI conductance) delta=0.019 (SI voltage) k=1205.0 (SI per_time) Vth=0.027 (SI voltage) erev=0.037 (SI voltage))
    DB6_to_MDL21_exc_syn_2conns (Type: gradedSynapse:  conductance=2.4E-10 (SI conductance) delta=0.019 (SI voltage) k=1205.0 (SI per_time) Vth=0.027 (SI voltage) erev=0.037 (SI voltage))
    DB7_to_MDL22_exc_syn_2conns (Type: gradedSynapse:  conductance=4.0000000000000007E-10 (SI conductance) delta=0.019 (SI voltage) k=1205.0 (SI per_time) Vth=0.027 (SI voltage) erev=0.037 (SI voltage))
    DB7_to_MDL23_exc_syn_2conns (Type: gradedSynapse:  conductance=3.6E-10 (SI conductance) delta=0.019 (SI voltage) k=1205.0 (SI per_time) Vth=0.027 (SI voltage) erev=0.037 (SI voltage))
    DB7_to_MDL24_exc_syn_2conns (Type: gradedSynapse:  conductance=3.2000000000000003E-10 (SI conductance) delta=0.019 (SI voltage) k=1205.0 (SI per_time) Vth=0.027 (SI voltage) erev=0.037 (SI voltage))
    GenericMuscleCell (Type: cell)
    GenericNeuronCell (Type: cell)
    offset_current (Type: pulseGenerator:  delay=0.0 (SI time) duration=2.0 (SI time) amplitude=0.0 (SI current))
    stim_AVBL_1 (Type: pulseGenerator:  delay=0.05 (SI time) duration=1.9000000000000001 (SI time) amplitude=1.5E-11 (SI current))
    stim_AVBR_1 (Type: pulseGenerator:  delay=0.05 (SI time) duration=1.9000000000000001 (SI time) amplitude=1.5E-11 (SI current))
    c302_C2_AVB_DB (Type: network)
    sim_c302_C2_AVB_DB (Type: Simulation:  length=2.0 (SI time) step=5.0E-5 (SI time))


    This NEURON file has been generated by org.neuroml.export (see https://github.com/NeuroML/org.neuroml.export)
         org.neuroml.export  v1.5.2
         org.neuroml.model   v1.5.2
         jLEMS               v0.9.8.9

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
        Adding simulation Component(id=sim_c302_C2_AVB_DB type=Simulation) of network/component: c302_C2_AVB_DB (Type: network)
        
        '''
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

        # ######################   Population: DB1
        print("Population DB1 contains 1 instance(s) of component: GenericNeuronCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericNeuronCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericNeuronCell.hoc")
        a_DB1 = []
        h("{ n_DB1 = 1 }")
        h("objectvar a_DB1[n_DB1]")
        for i in range(int(h.n_DB1)):
            h("a_DB1[%i] = new GenericNeuronCell()"%i)
            h("access a_DB1[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_DB1[0].position(-1.9, -230.349989999999991, 6.85) }")

        h("proc initialiseV_DB1() { for i = 0, n_DB1-1 { a_DB1[i].set_initial_v() } }")
        h("objref fih_DB1")
        h('{fih_DB1 = new FInitializeHandler(0, "initialiseV_DB1()")}')

        h("proc initialiseIons_DB1() { for i = 0, n_DB1-1 { a_DB1[i].set_initial_ion_properties() } }")
        h("objref fih_ion_DB1")
        h('{fih_ion_DB1 = new FInitializeHandler(1, "initialiseIons_DB1()")}')

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

        # ######################   Population: DB4
        print("Population DB4 contains 1 instance(s) of component: GenericNeuronCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericNeuronCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericNeuronCell.hoc")
        a_DB4 = []
        h("{ n_DB4 = 1 }")
        h("objectvar a_DB4[n_DB4]")
        for i in range(int(h.n_DB4)):
            h("a_DB4[%i] = new GenericNeuronCell()"%i)
            h("access a_DB4[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_DB4[0].position(-1.8750001, -96.275000000000006, -64.650000000000006) }")

        h("proc initialiseV_DB4() { for i = 0, n_DB4-1 { a_DB4[i].set_initial_v() } }")
        h("objref fih_DB4")
        h('{fih_DB4 = new FInitializeHandler(0, "initialiseV_DB4()")}')

        h("proc initialiseIons_DB4() { for i = 0, n_DB4-1 { a_DB4[i].set_initial_ion_properties() } }")
        h("objref fih_ion_DB4")
        h('{fih_ion_DB4 = new FInitializeHandler(1, "initialiseIons_DB4()")}')

        # ######################   Population: DB5
        print("Population DB5 contains 1 instance(s) of component: GenericNeuronCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericNeuronCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericNeuronCell.hoc")
        a_DB5 = []
        h("{ n_DB5 = 1 }")
        h("objectvar a_DB5[n_DB5]")
        for i in range(int(h.n_DB5)):
            h("a_DB5[%i] = new GenericNeuronCell()"%i)
            h("access a_DB5[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_DB5[0].position(-4.05, 35.25, -30.449999999999999) }")

        h("proc initialiseV_DB5() { for i = 0, n_DB5-1 { a_DB5[i].set_initial_v() } }")
        h("objref fih_DB5")
        h('{fih_DB5 = new FInitializeHandler(0, "initialiseV_DB5()")}')

        h("proc initialiseIons_DB5() { for i = 0, n_DB5-1 { a_DB5[i].set_initial_ion_properties() } }")
        h("objref fih_ion_DB5")
        h('{fih_ion_DB5 = new FInitializeHandler(1, "initialiseIons_DB5()")}')

        # ######################   Population: DB6
        print("Population DB6 contains 1 instance(s) of component: GenericNeuronCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericNeuronCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericNeuronCell.hoc")
        a_DB6 = []
        h("{ n_DB6 = 1 }")
        h("objectvar a_DB6[n_DB6]")
        for i in range(int(h.n_DB6)):
            h("a_DB6[%i] = new GenericNeuronCell()"%i)
            h("access a_DB6[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_DB6[0].position(-1.8249999, 178.099999999999994, -0.2) }")

        h("proc initialiseV_DB6() { for i = 0, n_DB6-1 { a_DB6[i].set_initial_v() } }")
        h("objref fih_DB6")
        h('{fih_DB6 = new FInitializeHandler(0, "initialiseV_DB6()")}')

        h("proc initialiseIons_DB6() { for i = 0, n_DB6-1 { a_DB6[i].set_initial_ion_properties() } }")
        h("objref fih_ion_DB6")
        h('{fih_ion_DB6 = new FInitializeHandler(1, "initialiseIons_DB6()")}')

        # ######################   Population: DB7
        print("Population DB7 contains 1 instance(s) of component: GenericNeuronCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericNeuronCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericNeuronCell.hoc")
        a_DB7 = []
        h("{ n_DB7 = 1 }")
        h("objectvar a_DB7[n_DB7]")
        for i in range(int(h.n_DB7)):
            h("a_DB7[%i] = new GenericNeuronCell()"%i)
            h("access a_DB7[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_DB7[0].position(-1.85, 267.75, -22.625) }")

        h("proc initialiseV_DB7() { for i = 0, n_DB7-1 { a_DB7[i].set_initial_v() } }")
        h("objref fih_DB7")
        h('{fih_DB7 = new FInitializeHandler(0, "initialiseV_DB7()")}')

        h("proc initialiseIons_DB7() { for i = 0, n_DB7-1 { a_DB7[i].set_initial_ion_properties() } }")
        h("objref fih_ion_DB7")
        h('{fih_ion_DB7 = new FInitializeHandler(1, "initialiseIons_DB7()")}')

        # ######################   Population: MDR01
        print("Population MDR01 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MDR01 = []
        h("{ n_MDR01 = 1 }")
        h("objectvar a_MDR01[n_MDR01]")
        for i in range(int(h.n_MDR01)):
            h("a_MDR01[%i] = new GenericMuscleCell()"%i)
            h("access a_MDR01[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MDR01[0].position(80., -270., 80.) }")

        h("proc initialiseV_MDR01() { for i = 0, n_MDR01-1 { a_MDR01[i].set_initial_v() } }")
        h("objref fih_MDR01")
        h('{fih_MDR01 = new FInitializeHandler(0, "initialiseV_MDR01()")}')

        h("proc initialiseIons_MDR01() { for i = 0, n_MDR01-1 { a_MDR01[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MDR01")
        h('{fih_ion_MDR01 = new FInitializeHandler(1, "initialiseIons_MDR01()")}')

        # ######################   Population: MDR02
        print("Population MDR02 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MDR02 = []
        h("{ n_MDR02 = 1 }")
        h("objectvar a_MDR02[n_MDR02]")
        for i in range(int(h.n_MDR02)):
            h("a_MDR02[%i] = new GenericMuscleCell()"%i)
            h("access a_MDR02[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MDR02[0].position(80., -240., 80.) }")

        h("proc initialiseV_MDR02() { for i = 0, n_MDR02-1 { a_MDR02[i].set_initial_v() } }")
        h("objref fih_MDR02")
        h('{fih_MDR02 = new FInitializeHandler(0, "initialiseV_MDR02()")}')

        h("proc initialiseIons_MDR02() { for i = 0, n_MDR02-1 { a_MDR02[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MDR02")
        h('{fih_ion_MDR02 = new FInitializeHandler(1, "initialiseIons_MDR02()")}')

        # ######################   Population: MDR03
        print("Population MDR03 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MDR03 = []
        h("{ n_MDR03 = 1 }")
        h("objectvar a_MDR03[n_MDR03]")
        for i in range(int(h.n_MDR03)):
            h("a_MDR03[%i] = new GenericMuscleCell()"%i)
            h("access a_MDR03[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MDR03[0].position(80., -210., 80.) }")

        h("proc initialiseV_MDR03() { for i = 0, n_MDR03-1 { a_MDR03[i].set_initial_v() } }")
        h("objref fih_MDR03")
        h('{fih_MDR03 = new FInitializeHandler(0, "initialiseV_MDR03()")}')

        h("proc initialiseIons_MDR03() { for i = 0, n_MDR03-1 { a_MDR03[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MDR03")
        h('{fih_ion_MDR03 = new FInitializeHandler(1, "initialiseIons_MDR03()")}')

        # ######################   Population: MDR04
        print("Population MDR04 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MDR04 = []
        h("{ n_MDR04 = 1 }")
        h("objectvar a_MDR04[n_MDR04]")
        for i in range(int(h.n_MDR04)):
            h("a_MDR04[%i] = new GenericMuscleCell()"%i)
            h("access a_MDR04[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MDR04[0].position(80., -180., 80.) }")

        h("proc initialiseV_MDR04() { for i = 0, n_MDR04-1 { a_MDR04[i].set_initial_v() } }")
        h("objref fih_MDR04")
        h('{fih_MDR04 = new FInitializeHandler(0, "initialiseV_MDR04()")}')

        h("proc initialiseIons_MDR04() { for i = 0, n_MDR04-1 { a_MDR04[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MDR04")
        h('{fih_ion_MDR04 = new FInitializeHandler(1, "initialiseIons_MDR04()")}')

        # ######################   Population: MDR05
        print("Population MDR05 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MDR05 = []
        h("{ n_MDR05 = 1 }")
        h("objectvar a_MDR05[n_MDR05]")
        for i in range(int(h.n_MDR05)):
            h("a_MDR05[%i] = new GenericMuscleCell()"%i)
            h("access a_MDR05[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MDR05[0].position(80., -150., 80.) }")

        h("proc initialiseV_MDR05() { for i = 0, n_MDR05-1 { a_MDR05[i].set_initial_v() } }")
        h("objref fih_MDR05")
        h('{fih_MDR05 = new FInitializeHandler(0, "initialiseV_MDR05()")}')

        h("proc initialiseIons_MDR05() { for i = 0, n_MDR05-1 { a_MDR05[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MDR05")
        h('{fih_ion_MDR05 = new FInitializeHandler(1, "initialiseIons_MDR05()")}')

        # ######################   Population: MDR06
        print("Population MDR06 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MDR06 = []
        h("{ n_MDR06 = 1 }")
        h("objectvar a_MDR06[n_MDR06]")
        for i in range(int(h.n_MDR06)):
            h("a_MDR06[%i] = new GenericMuscleCell()"%i)
            h("access a_MDR06[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MDR06[0].position(80., -120., 80.) }")

        h("proc initialiseV_MDR06() { for i = 0, n_MDR06-1 { a_MDR06[i].set_initial_v() } }")
        h("objref fih_MDR06")
        h('{fih_MDR06 = new FInitializeHandler(0, "initialiseV_MDR06()")}')

        h("proc initialiseIons_MDR06() { for i = 0, n_MDR06-1 { a_MDR06[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MDR06")
        h('{fih_ion_MDR06 = new FInitializeHandler(1, "initialiseIons_MDR06()")}')

        # ######################   Population: MDR07
        print("Population MDR07 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MDR07 = []
        h("{ n_MDR07 = 1 }")
        h("objectvar a_MDR07[n_MDR07]")
        for i in range(int(h.n_MDR07)):
            h("a_MDR07[%i] = new GenericMuscleCell()"%i)
            h("access a_MDR07[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MDR07[0].position(80., -90., 80.) }")

        h("proc initialiseV_MDR07() { for i = 0, n_MDR07-1 { a_MDR07[i].set_initial_v() } }")
        h("objref fih_MDR07")
        h('{fih_MDR07 = new FInitializeHandler(0, "initialiseV_MDR07()")}')

        h("proc initialiseIons_MDR07() { for i = 0, n_MDR07-1 { a_MDR07[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MDR07")
        h('{fih_ion_MDR07 = new FInitializeHandler(1, "initialiseIons_MDR07()")}')

        # ######################   Population: MDR08
        print("Population MDR08 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MDR08 = []
        h("{ n_MDR08 = 1 }")
        h("objectvar a_MDR08[n_MDR08]")
        for i in range(int(h.n_MDR08)):
            h("a_MDR08[%i] = new GenericMuscleCell()"%i)
            h("access a_MDR08[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MDR08[0].position(80., -60., 80.) }")

        h("proc initialiseV_MDR08() { for i = 0, n_MDR08-1 { a_MDR08[i].set_initial_v() } }")
        h("objref fih_MDR08")
        h('{fih_MDR08 = new FInitializeHandler(0, "initialiseV_MDR08()")}')

        h("proc initialiseIons_MDR08() { for i = 0, n_MDR08-1 { a_MDR08[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MDR08")
        h('{fih_ion_MDR08 = new FInitializeHandler(1, "initialiseIons_MDR08()")}')

        # ######################   Population: MDR09
        print("Population MDR09 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MDR09 = []
        h("{ n_MDR09 = 1 }")
        h("objectvar a_MDR09[n_MDR09]")
        for i in range(int(h.n_MDR09)):
            h("a_MDR09[%i] = new GenericMuscleCell()"%i)
            h("access a_MDR09[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MDR09[0].position(80., -30., 80.) }")

        h("proc initialiseV_MDR09() { for i = 0, n_MDR09-1 { a_MDR09[i].set_initial_v() } }")
        h("objref fih_MDR09")
        h('{fih_MDR09 = new FInitializeHandler(0, "initialiseV_MDR09()")}')

        h("proc initialiseIons_MDR09() { for i = 0, n_MDR09-1 { a_MDR09[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MDR09")
        h('{fih_ion_MDR09 = new FInitializeHandler(1, "initialiseIons_MDR09()")}')

        # ######################   Population: MDR10
        print("Population MDR10 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MDR10 = []
        h("{ n_MDR10 = 1 }")
        h("objectvar a_MDR10[n_MDR10]")
        for i in range(int(h.n_MDR10)):
            h("a_MDR10[%i] = new GenericMuscleCell()"%i)
            h("access a_MDR10[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MDR10[0].position(80., 0., 80.) }")

        h("proc initialiseV_MDR10() { for i = 0, n_MDR10-1 { a_MDR10[i].set_initial_v() } }")
        h("objref fih_MDR10")
        h('{fih_MDR10 = new FInitializeHandler(0, "initialiseV_MDR10()")}')

        h("proc initialiseIons_MDR10() { for i = 0, n_MDR10-1 { a_MDR10[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MDR10")
        h('{fih_ion_MDR10 = new FInitializeHandler(1, "initialiseIons_MDR10()")}')

        # ######################   Population: MDR11
        print("Population MDR11 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MDR11 = []
        h("{ n_MDR11 = 1 }")
        h("objectvar a_MDR11[n_MDR11]")
        for i in range(int(h.n_MDR11)):
            h("a_MDR11[%i] = new GenericMuscleCell()"%i)
            h("access a_MDR11[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MDR11[0].position(80., 30., 80.) }")

        h("proc initialiseV_MDR11() { for i = 0, n_MDR11-1 { a_MDR11[i].set_initial_v() } }")
        h("objref fih_MDR11")
        h('{fih_MDR11 = new FInitializeHandler(0, "initialiseV_MDR11()")}')

        h("proc initialiseIons_MDR11() { for i = 0, n_MDR11-1 { a_MDR11[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MDR11")
        h('{fih_ion_MDR11 = new FInitializeHandler(1, "initialiseIons_MDR11()")}')

        # ######################   Population: MDR12
        print("Population MDR12 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MDR12 = []
        h("{ n_MDR12 = 1 }")
        h("objectvar a_MDR12[n_MDR12]")
        for i in range(int(h.n_MDR12)):
            h("a_MDR12[%i] = new GenericMuscleCell()"%i)
            h("access a_MDR12[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MDR12[0].position(80., 60., 80.) }")

        h("proc initialiseV_MDR12() { for i = 0, n_MDR12-1 { a_MDR12[i].set_initial_v() } }")
        h("objref fih_MDR12")
        h('{fih_MDR12 = new FInitializeHandler(0, "initialiseV_MDR12()")}')

        h("proc initialiseIons_MDR12() { for i = 0, n_MDR12-1 { a_MDR12[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MDR12")
        h('{fih_ion_MDR12 = new FInitializeHandler(1, "initialiseIons_MDR12()")}')

        # ######################   Population: MDR13
        print("Population MDR13 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MDR13 = []
        h("{ n_MDR13 = 1 }")
        h("objectvar a_MDR13[n_MDR13]")
        for i in range(int(h.n_MDR13)):
            h("a_MDR13[%i] = new GenericMuscleCell()"%i)
            h("access a_MDR13[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MDR13[0].position(80., 90., 80.) }")

        h("proc initialiseV_MDR13() { for i = 0, n_MDR13-1 { a_MDR13[i].set_initial_v() } }")
        h("objref fih_MDR13")
        h('{fih_MDR13 = new FInitializeHandler(0, "initialiseV_MDR13()")}')

        h("proc initialiseIons_MDR13() { for i = 0, n_MDR13-1 { a_MDR13[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MDR13")
        h('{fih_ion_MDR13 = new FInitializeHandler(1, "initialiseIons_MDR13()")}')

        # ######################   Population: MDR14
        print("Population MDR14 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MDR14 = []
        h("{ n_MDR14 = 1 }")
        h("objectvar a_MDR14[n_MDR14]")
        for i in range(int(h.n_MDR14)):
            h("a_MDR14[%i] = new GenericMuscleCell()"%i)
            h("access a_MDR14[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MDR14[0].position(80., 120., 80.) }")

        h("proc initialiseV_MDR14() { for i = 0, n_MDR14-1 { a_MDR14[i].set_initial_v() } }")
        h("objref fih_MDR14")
        h('{fih_MDR14 = new FInitializeHandler(0, "initialiseV_MDR14()")}')

        h("proc initialiseIons_MDR14() { for i = 0, n_MDR14-1 { a_MDR14[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MDR14")
        h('{fih_ion_MDR14 = new FInitializeHandler(1, "initialiseIons_MDR14()")}')

        # ######################   Population: MDR15
        print("Population MDR15 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MDR15 = []
        h("{ n_MDR15 = 1 }")
        h("objectvar a_MDR15[n_MDR15]")
        for i in range(int(h.n_MDR15)):
            h("a_MDR15[%i] = new GenericMuscleCell()"%i)
            h("access a_MDR15[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MDR15[0].position(80., 150., 80.) }")

        h("proc initialiseV_MDR15() { for i = 0, n_MDR15-1 { a_MDR15[i].set_initial_v() } }")
        h("objref fih_MDR15")
        h('{fih_MDR15 = new FInitializeHandler(0, "initialiseV_MDR15()")}')

        h("proc initialiseIons_MDR15() { for i = 0, n_MDR15-1 { a_MDR15[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MDR15")
        h('{fih_ion_MDR15 = new FInitializeHandler(1, "initialiseIons_MDR15()")}')

        # ######################   Population: MDR16
        print("Population MDR16 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MDR16 = []
        h("{ n_MDR16 = 1 }")
        h("objectvar a_MDR16[n_MDR16]")
        for i in range(int(h.n_MDR16)):
            h("a_MDR16[%i] = new GenericMuscleCell()"%i)
            h("access a_MDR16[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MDR16[0].position(80., 180., 80.) }")

        h("proc initialiseV_MDR16() { for i = 0, n_MDR16-1 { a_MDR16[i].set_initial_v() } }")
        h("objref fih_MDR16")
        h('{fih_MDR16 = new FInitializeHandler(0, "initialiseV_MDR16()")}')

        h("proc initialiseIons_MDR16() { for i = 0, n_MDR16-1 { a_MDR16[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MDR16")
        h('{fih_ion_MDR16 = new FInitializeHandler(1, "initialiseIons_MDR16()")}')

        # ######################   Population: MDR17
        print("Population MDR17 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MDR17 = []
        h("{ n_MDR17 = 1 }")
        h("objectvar a_MDR17[n_MDR17]")
        for i in range(int(h.n_MDR17)):
            h("a_MDR17[%i] = new GenericMuscleCell()"%i)
            h("access a_MDR17[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MDR17[0].position(80., 210., 80.) }")

        h("proc initialiseV_MDR17() { for i = 0, n_MDR17-1 { a_MDR17[i].set_initial_v() } }")
        h("objref fih_MDR17")
        h('{fih_MDR17 = new FInitializeHandler(0, "initialiseV_MDR17()")}')

        h("proc initialiseIons_MDR17() { for i = 0, n_MDR17-1 { a_MDR17[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MDR17")
        h('{fih_ion_MDR17 = new FInitializeHandler(1, "initialiseIons_MDR17()")}')

        # ######################   Population: MDR18
        print("Population MDR18 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MDR18 = []
        h("{ n_MDR18 = 1 }")
        h("objectvar a_MDR18[n_MDR18]")
        for i in range(int(h.n_MDR18)):
            h("a_MDR18[%i] = new GenericMuscleCell()"%i)
            h("access a_MDR18[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MDR18[0].position(80., 240., 80.) }")

        h("proc initialiseV_MDR18() { for i = 0, n_MDR18-1 { a_MDR18[i].set_initial_v() } }")
        h("objref fih_MDR18")
        h('{fih_MDR18 = new FInitializeHandler(0, "initialiseV_MDR18()")}')

        h("proc initialiseIons_MDR18() { for i = 0, n_MDR18-1 { a_MDR18[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MDR18")
        h('{fih_ion_MDR18 = new FInitializeHandler(1, "initialiseIons_MDR18()")}')

        # ######################   Population: MDR19
        print("Population MDR19 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MDR19 = []
        h("{ n_MDR19 = 1 }")
        h("objectvar a_MDR19[n_MDR19]")
        for i in range(int(h.n_MDR19)):
            h("a_MDR19[%i] = new GenericMuscleCell()"%i)
            h("access a_MDR19[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MDR19[0].position(80., 270., 80.) }")

        h("proc initialiseV_MDR19() { for i = 0, n_MDR19-1 { a_MDR19[i].set_initial_v() } }")
        h("objref fih_MDR19")
        h('{fih_MDR19 = new FInitializeHandler(0, "initialiseV_MDR19()")}')

        h("proc initialiseIons_MDR19() { for i = 0, n_MDR19-1 { a_MDR19[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MDR19")
        h('{fih_ion_MDR19 = new FInitializeHandler(1, "initialiseIons_MDR19()")}')

        # ######################   Population: MDR20
        print("Population MDR20 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MDR20 = []
        h("{ n_MDR20 = 1 }")
        h("objectvar a_MDR20[n_MDR20]")
        for i in range(int(h.n_MDR20)):
            h("a_MDR20[%i] = new GenericMuscleCell()"%i)
            h("access a_MDR20[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MDR20[0].position(80., 300., 80.) }")

        h("proc initialiseV_MDR20() { for i = 0, n_MDR20-1 { a_MDR20[i].set_initial_v() } }")
        h("objref fih_MDR20")
        h('{fih_MDR20 = new FInitializeHandler(0, "initialiseV_MDR20()")}')

        h("proc initialiseIons_MDR20() { for i = 0, n_MDR20-1 { a_MDR20[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MDR20")
        h('{fih_ion_MDR20 = new FInitializeHandler(1, "initialiseIons_MDR20()")}')

        # ######################   Population: MDR21
        print("Population MDR21 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MDR21 = []
        h("{ n_MDR21 = 1 }")
        h("objectvar a_MDR21[n_MDR21]")
        for i in range(int(h.n_MDR21)):
            h("a_MDR21[%i] = new GenericMuscleCell()"%i)
            h("access a_MDR21[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MDR21[0].position(80., 330., 80.) }")

        h("proc initialiseV_MDR21() { for i = 0, n_MDR21-1 { a_MDR21[i].set_initial_v() } }")
        h("objref fih_MDR21")
        h('{fih_MDR21 = new FInitializeHandler(0, "initialiseV_MDR21()")}')

        h("proc initialiseIons_MDR21() { for i = 0, n_MDR21-1 { a_MDR21[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MDR21")
        h('{fih_ion_MDR21 = new FInitializeHandler(1, "initialiseIons_MDR21()")}')

        # ######################   Population: MDR22
        print("Population MDR22 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MDR22 = []
        h("{ n_MDR22 = 1 }")
        h("objectvar a_MDR22[n_MDR22]")
        for i in range(int(h.n_MDR22)):
            h("a_MDR22[%i] = new GenericMuscleCell()"%i)
            h("access a_MDR22[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MDR22[0].position(80., 360., 80.) }")

        h("proc initialiseV_MDR22() { for i = 0, n_MDR22-1 { a_MDR22[i].set_initial_v() } }")
        h("objref fih_MDR22")
        h('{fih_MDR22 = new FInitializeHandler(0, "initialiseV_MDR22()")}')

        h("proc initialiseIons_MDR22() { for i = 0, n_MDR22-1 { a_MDR22[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MDR22")
        h('{fih_ion_MDR22 = new FInitializeHandler(1, "initialiseIons_MDR22()")}')

        # ######################   Population: MDR23
        print("Population MDR23 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MDR23 = []
        h("{ n_MDR23 = 1 }")
        h("objectvar a_MDR23[n_MDR23]")
        for i in range(int(h.n_MDR23)):
            h("a_MDR23[%i] = new GenericMuscleCell()"%i)
            h("access a_MDR23[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MDR23[0].position(80., 390., 80.) }")

        h("proc initialiseV_MDR23() { for i = 0, n_MDR23-1 { a_MDR23[i].set_initial_v() } }")
        h("objref fih_MDR23")
        h('{fih_MDR23 = new FInitializeHandler(0, "initialiseV_MDR23()")}')

        h("proc initialiseIons_MDR23() { for i = 0, n_MDR23-1 { a_MDR23[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MDR23")
        h('{fih_ion_MDR23 = new FInitializeHandler(1, "initialiseIons_MDR23()")}')

        # ######################   Population: MDR24
        print("Population MDR24 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MDR24 = []
        h("{ n_MDR24 = 1 }")
        h("objectvar a_MDR24[n_MDR24]")
        for i in range(int(h.n_MDR24)):
            h("a_MDR24[%i] = new GenericMuscleCell()"%i)
            h("access a_MDR24[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MDR24[0].position(80., 420., 80.) }")

        h("proc initialiseV_MDR24() { for i = 0, n_MDR24-1 { a_MDR24[i].set_initial_v() } }")
        h("objref fih_MDR24")
        h('{fih_MDR24 = new FInitializeHandler(0, "initialiseV_MDR24()")}')

        h("proc initialiseIons_MDR24() { for i = 0, n_MDR24-1 { a_MDR24[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MDR24")
        h('{fih_ion_MDR24 = new FInitializeHandler(1, "initialiseIons_MDR24()")}')

        # ######################   Population: MVR01
        print("Population MVR01 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MVR01 = []
        h("{ n_MVR01 = 1 }")
        h("objectvar a_MVR01[n_MVR01]")
        for i in range(int(h.n_MVR01)):
            h("a_MVR01[%i] = new GenericMuscleCell()"%i)
            h("access a_MVR01[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MVR01[0].position(-80., -270., 80.) }")

        h("proc initialiseV_MVR01() { for i = 0, n_MVR01-1 { a_MVR01[i].set_initial_v() } }")
        h("objref fih_MVR01")
        h('{fih_MVR01 = new FInitializeHandler(0, "initialiseV_MVR01()")}')

        h("proc initialiseIons_MVR01() { for i = 0, n_MVR01-1 { a_MVR01[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MVR01")
        h('{fih_ion_MVR01 = new FInitializeHandler(1, "initialiseIons_MVR01()")}')

        # ######################   Population: MVR02
        print("Population MVR02 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MVR02 = []
        h("{ n_MVR02 = 1 }")
        h("objectvar a_MVR02[n_MVR02]")
        for i in range(int(h.n_MVR02)):
            h("a_MVR02[%i] = new GenericMuscleCell()"%i)
            h("access a_MVR02[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MVR02[0].position(-80., -240., 80.) }")

        h("proc initialiseV_MVR02() { for i = 0, n_MVR02-1 { a_MVR02[i].set_initial_v() } }")
        h("objref fih_MVR02")
        h('{fih_MVR02 = new FInitializeHandler(0, "initialiseV_MVR02()")}')

        h("proc initialiseIons_MVR02() { for i = 0, n_MVR02-1 { a_MVR02[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MVR02")
        h('{fih_ion_MVR02 = new FInitializeHandler(1, "initialiseIons_MVR02()")}')

        # ######################   Population: MVR03
        print("Population MVR03 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MVR03 = []
        h("{ n_MVR03 = 1 }")
        h("objectvar a_MVR03[n_MVR03]")
        for i in range(int(h.n_MVR03)):
            h("a_MVR03[%i] = new GenericMuscleCell()"%i)
            h("access a_MVR03[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MVR03[0].position(-80., -210., 80.) }")

        h("proc initialiseV_MVR03() { for i = 0, n_MVR03-1 { a_MVR03[i].set_initial_v() } }")
        h("objref fih_MVR03")
        h('{fih_MVR03 = new FInitializeHandler(0, "initialiseV_MVR03()")}')

        h("proc initialiseIons_MVR03() { for i = 0, n_MVR03-1 { a_MVR03[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MVR03")
        h('{fih_ion_MVR03 = new FInitializeHandler(1, "initialiseIons_MVR03()")}')

        # ######################   Population: MVR04
        print("Population MVR04 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MVR04 = []
        h("{ n_MVR04 = 1 }")
        h("objectvar a_MVR04[n_MVR04]")
        for i in range(int(h.n_MVR04)):
            h("a_MVR04[%i] = new GenericMuscleCell()"%i)
            h("access a_MVR04[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MVR04[0].position(-80., -180., 80.) }")

        h("proc initialiseV_MVR04() { for i = 0, n_MVR04-1 { a_MVR04[i].set_initial_v() } }")
        h("objref fih_MVR04")
        h('{fih_MVR04 = new FInitializeHandler(0, "initialiseV_MVR04()")}')

        h("proc initialiseIons_MVR04() { for i = 0, n_MVR04-1 { a_MVR04[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MVR04")
        h('{fih_ion_MVR04 = new FInitializeHandler(1, "initialiseIons_MVR04()")}')

        # ######################   Population: MVR05
        print("Population MVR05 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MVR05 = []
        h("{ n_MVR05 = 1 }")
        h("objectvar a_MVR05[n_MVR05]")
        for i in range(int(h.n_MVR05)):
            h("a_MVR05[%i] = new GenericMuscleCell()"%i)
            h("access a_MVR05[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MVR05[0].position(-80., -150., 80.) }")

        h("proc initialiseV_MVR05() { for i = 0, n_MVR05-1 { a_MVR05[i].set_initial_v() } }")
        h("objref fih_MVR05")
        h('{fih_MVR05 = new FInitializeHandler(0, "initialiseV_MVR05()")}')

        h("proc initialiseIons_MVR05() { for i = 0, n_MVR05-1 { a_MVR05[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MVR05")
        h('{fih_ion_MVR05 = new FInitializeHandler(1, "initialiseIons_MVR05()")}')

        # ######################   Population: MVR06
        print("Population MVR06 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MVR06 = []
        h("{ n_MVR06 = 1 }")
        h("objectvar a_MVR06[n_MVR06]")
        for i in range(int(h.n_MVR06)):
            h("a_MVR06[%i] = new GenericMuscleCell()"%i)
            h("access a_MVR06[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MVR06[0].position(-80., -120., 80.) }")

        h("proc initialiseV_MVR06() { for i = 0, n_MVR06-1 { a_MVR06[i].set_initial_v() } }")
        h("objref fih_MVR06")
        h('{fih_MVR06 = new FInitializeHandler(0, "initialiseV_MVR06()")}')

        h("proc initialiseIons_MVR06() { for i = 0, n_MVR06-1 { a_MVR06[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MVR06")
        h('{fih_ion_MVR06 = new FInitializeHandler(1, "initialiseIons_MVR06()")}')

        # ######################   Population: MVR07
        print("Population MVR07 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MVR07 = []
        h("{ n_MVR07 = 1 }")
        h("objectvar a_MVR07[n_MVR07]")
        for i in range(int(h.n_MVR07)):
            h("a_MVR07[%i] = new GenericMuscleCell()"%i)
            h("access a_MVR07[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MVR07[0].position(-80., -90., 80.) }")

        h("proc initialiseV_MVR07() { for i = 0, n_MVR07-1 { a_MVR07[i].set_initial_v() } }")
        h("objref fih_MVR07")
        h('{fih_MVR07 = new FInitializeHandler(0, "initialiseV_MVR07()")}')

        h("proc initialiseIons_MVR07() { for i = 0, n_MVR07-1 { a_MVR07[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MVR07")
        h('{fih_ion_MVR07 = new FInitializeHandler(1, "initialiseIons_MVR07()")}')

        # ######################   Population: MVR08
        print("Population MVR08 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MVR08 = []
        h("{ n_MVR08 = 1 }")
        h("objectvar a_MVR08[n_MVR08]")
        for i in range(int(h.n_MVR08)):
            h("a_MVR08[%i] = new GenericMuscleCell()"%i)
            h("access a_MVR08[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MVR08[0].position(-80., -60., 80.) }")

        h("proc initialiseV_MVR08() { for i = 0, n_MVR08-1 { a_MVR08[i].set_initial_v() } }")
        h("objref fih_MVR08")
        h('{fih_MVR08 = new FInitializeHandler(0, "initialiseV_MVR08()")}')

        h("proc initialiseIons_MVR08() { for i = 0, n_MVR08-1 { a_MVR08[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MVR08")
        h('{fih_ion_MVR08 = new FInitializeHandler(1, "initialiseIons_MVR08()")}')

        # ######################   Population: MVR09
        print("Population MVR09 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MVR09 = []
        h("{ n_MVR09 = 1 }")
        h("objectvar a_MVR09[n_MVR09]")
        for i in range(int(h.n_MVR09)):
            h("a_MVR09[%i] = new GenericMuscleCell()"%i)
            h("access a_MVR09[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MVR09[0].position(-80., -30., 80.) }")

        h("proc initialiseV_MVR09() { for i = 0, n_MVR09-1 { a_MVR09[i].set_initial_v() } }")
        h("objref fih_MVR09")
        h('{fih_MVR09 = new FInitializeHandler(0, "initialiseV_MVR09()")}')

        h("proc initialiseIons_MVR09() { for i = 0, n_MVR09-1 { a_MVR09[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MVR09")
        h('{fih_ion_MVR09 = new FInitializeHandler(1, "initialiseIons_MVR09()")}')

        # ######################   Population: MVR10
        print("Population MVR10 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MVR10 = []
        h("{ n_MVR10 = 1 }")
        h("objectvar a_MVR10[n_MVR10]")
        for i in range(int(h.n_MVR10)):
            h("a_MVR10[%i] = new GenericMuscleCell()"%i)
            h("access a_MVR10[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MVR10[0].position(-80., 0., 80.) }")

        h("proc initialiseV_MVR10() { for i = 0, n_MVR10-1 { a_MVR10[i].set_initial_v() } }")
        h("objref fih_MVR10")
        h('{fih_MVR10 = new FInitializeHandler(0, "initialiseV_MVR10()")}')

        h("proc initialiseIons_MVR10() { for i = 0, n_MVR10-1 { a_MVR10[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MVR10")
        h('{fih_ion_MVR10 = new FInitializeHandler(1, "initialiseIons_MVR10()")}')

        # ######################   Population: MVR11
        print("Population MVR11 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MVR11 = []
        h("{ n_MVR11 = 1 }")
        h("objectvar a_MVR11[n_MVR11]")
        for i in range(int(h.n_MVR11)):
            h("a_MVR11[%i] = new GenericMuscleCell()"%i)
            h("access a_MVR11[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MVR11[0].position(-80., 30., 80.) }")

        h("proc initialiseV_MVR11() { for i = 0, n_MVR11-1 { a_MVR11[i].set_initial_v() } }")
        h("objref fih_MVR11")
        h('{fih_MVR11 = new FInitializeHandler(0, "initialiseV_MVR11()")}')

        h("proc initialiseIons_MVR11() { for i = 0, n_MVR11-1 { a_MVR11[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MVR11")
        h('{fih_ion_MVR11 = new FInitializeHandler(1, "initialiseIons_MVR11()")}')

        # ######################   Population: MVR12
        print("Population MVR12 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MVR12 = []
        h("{ n_MVR12 = 1 }")
        h("objectvar a_MVR12[n_MVR12]")
        for i in range(int(h.n_MVR12)):
            h("a_MVR12[%i] = new GenericMuscleCell()"%i)
            h("access a_MVR12[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MVR12[0].position(-80., 60., 80.) }")

        h("proc initialiseV_MVR12() { for i = 0, n_MVR12-1 { a_MVR12[i].set_initial_v() } }")
        h("objref fih_MVR12")
        h('{fih_MVR12 = new FInitializeHandler(0, "initialiseV_MVR12()")}')

        h("proc initialiseIons_MVR12() { for i = 0, n_MVR12-1 { a_MVR12[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MVR12")
        h('{fih_ion_MVR12 = new FInitializeHandler(1, "initialiseIons_MVR12()")}')

        # ######################   Population: MVR13
        print("Population MVR13 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MVR13 = []
        h("{ n_MVR13 = 1 }")
        h("objectvar a_MVR13[n_MVR13]")
        for i in range(int(h.n_MVR13)):
            h("a_MVR13[%i] = new GenericMuscleCell()"%i)
            h("access a_MVR13[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MVR13[0].position(-80., 90., 80.) }")

        h("proc initialiseV_MVR13() { for i = 0, n_MVR13-1 { a_MVR13[i].set_initial_v() } }")
        h("objref fih_MVR13")
        h('{fih_MVR13 = new FInitializeHandler(0, "initialiseV_MVR13()")}')

        h("proc initialiseIons_MVR13() { for i = 0, n_MVR13-1 { a_MVR13[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MVR13")
        h('{fih_ion_MVR13 = new FInitializeHandler(1, "initialiseIons_MVR13()")}')

        # ######################   Population: MVR14
        print("Population MVR14 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MVR14 = []
        h("{ n_MVR14 = 1 }")
        h("objectvar a_MVR14[n_MVR14]")
        for i in range(int(h.n_MVR14)):
            h("a_MVR14[%i] = new GenericMuscleCell()"%i)
            h("access a_MVR14[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MVR14[0].position(-80., 120., 80.) }")

        h("proc initialiseV_MVR14() { for i = 0, n_MVR14-1 { a_MVR14[i].set_initial_v() } }")
        h("objref fih_MVR14")
        h('{fih_MVR14 = new FInitializeHandler(0, "initialiseV_MVR14()")}')

        h("proc initialiseIons_MVR14() { for i = 0, n_MVR14-1 { a_MVR14[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MVR14")
        h('{fih_ion_MVR14 = new FInitializeHandler(1, "initialiseIons_MVR14()")}')

        # ######################   Population: MVR15
        print("Population MVR15 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MVR15 = []
        h("{ n_MVR15 = 1 }")
        h("objectvar a_MVR15[n_MVR15]")
        for i in range(int(h.n_MVR15)):
            h("a_MVR15[%i] = new GenericMuscleCell()"%i)
            h("access a_MVR15[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MVR15[0].position(-80., 150., 80.) }")

        h("proc initialiseV_MVR15() { for i = 0, n_MVR15-1 { a_MVR15[i].set_initial_v() } }")
        h("objref fih_MVR15")
        h('{fih_MVR15 = new FInitializeHandler(0, "initialiseV_MVR15()")}')

        h("proc initialiseIons_MVR15() { for i = 0, n_MVR15-1 { a_MVR15[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MVR15")
        h('{fih_ion_MVR15 = new FInitializeHandler(1, "initialiseIons_MVR15()")}')

        # ######################   Population: MVR16
        print("Population MVR16 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MVR16 = []
        h("{ n_MVR16 = 1 }")
        h("objectvar a_MVR16[n_MVR16]")
        for i in range(int(h.n_MVR16)):
            h("a_MVR16[%i] = new GenericMuscleCell()"%i)
            h("access a_MVR16[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MVR16[0].position(-80., 180., 80.) }")

        h("proc initialiseV_MVR16() { for i = 0, n_MVR16-1 { a_MVR16[i].set_initial_v() } }")
        h("objref fih_MVR16")
        h('{fih_MVR16 = new FInitializeHandler(0, "initialiseV_MVR16()")}')

        h("proc initialiseIons_MVR16() { for i = 0, n_MVR16-1 { a_MVR16[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MVR16")
        h('{fih_ion_MVR16 = new FInitializeHandler(1, "initialiseIons_MVR16()")}')

        # ######################   Population: MVR17
        print("Population MVR17 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MVR17 = []
        h("{ n_MVR17 = 1 }")
        h("objectvar a_MVR17[n_MVR17]")
        for i in range(int(h.n_MVR17)):
            h("a_MVR17[%i] = new GenericMuscleCell()"%i)
            h("access a_MVR17[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MVR17[0].position(-80., 210., 80.) }")

        h("proc initialiseV_MVR17() { for i = 0, n_MVR17-1 { a_MVR17[i].set_initial_v() } }")
        h("objref fih_MVR17")
        h('{fih_MVR17 = new FInitializeHandler(0, "initialiseV_MVR17()")}')

        h("proc initialiseIons_MVR17() { for i = 0, n_MVR17-1 { a_MVR17[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MVR17")
        h('{fih_ion_MVR17 = new FInitializeHandler(1, "initialiseIons_MVR17()")}')

        # ######################   Population: MVR18
        print("Population MVR18 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MVR18 = []
        h("{ n_MVR18 = 1 }")
        h("objectvar a_MVR18[n_MVR18]")
        for i in range(int(h.n_MVR18)):
            h("a_MVR18[%i] = new GenericMuscleCell()"%i)
            h("access a_MVR18[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MVR18[0].position(-80., 240., 80.) }")

        h("proc initialiseV_MVR18() { for i = 0, n_MVR18-1 { a_MVR18[i].set_initial_v() } }")
        h("objref fih_MVR18")
        h('{fih_MVR18 = new FInitializeHandler(0, "initialiseV_MVR18()")}')

        h("proc initialiseIons_MVR18() { for i = 0, n_MVR18-1 { a_MVR18[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MVR18")
        h('{fih_ion_MVR18 = new FInitializeHandler(1, "initialiseIons_MVR18()")}')

        # ######################   Population: MVR19
        print("Population MVR19 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MVR19 = []
        h("{ n_MVR19 = 1 }")
        h("objectvar a_MVR19[n_MVR19]")
        for i in range(int(h.n_MVR19)):
            h("a_MVR19[%i] = new GenericMuscleCell()"%i)
            h("access a_MVR19[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MVR19[0].position(-80., 270., 80.) }")

        h("proc initialiseV_MVR19() { for i = 0, n_MVR19-1 { a_MVR19[i].set_initial_v() } }")
        h("objref fih_MVR19")
        h('{fih_MVR19 = new FInitializeHandler(0, "initialiseV_MVR19()")}')

        h("proc initialiseIons_MVR19() { for i = 0, n_MVR19-1 { a_MVR19[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MVR19")
        h('{fih_ion_MVR19 = new FInitializeHandler(1, "initialiseIons_MVR19()")}')

        # ######################   Population: MVR20
        print("Population MVR20 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MVR20 = []
        h("{ n_MVR20 = 1 }")
        h("objectvar a_MVR20[n_MVR20]")
        for i in range(int(h.n_MVR20)):
            h("a_MVR20[%i] = new GenericMuscleCell()"%i)
            h("access a_MVR20[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MVR20[0].position(-80., 300., 80.) }")

        h("proc initialiseV_MVR20() { for i = 0, n_MVR20-1 { a_MVR20[i].set_initial_v() } }")
        h("objref fih_MVR20")
        h('{fih_MVR20 = new FInitializeHandler(0, "initialiseV_MVR20()")}')

        h("proc initialiseIons_MVR20() { for i = 0, n_MVR20-1 { a_MVR20[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MVR20")
        h('{fih_ion_MVR20 = new FInitializeHandler(1, "initialiseIons_MVR20()")}')

        # ######################   Population: MVR21
        print("Population MVR21 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MVR21 = []
        h("{ n_MVR21 = 1 }")
        h("objectvar a_MVR21[n_MVR21]")
        for i in range(int(h.n_MVR21)):
            h("a_MVR21[%i] = new GenericMuscleCell()"%i)
            h("access a_MVR21[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MVR21[0].position(-80., 330., 80.) }")

        h("proc initialiseV_MVR21() { for i = 0, n_MVR21-1 { a_MVR21[i].set_initial_v() } }")
        h("objref fih_MVR21")
        h('{fih_MVR21 = new FInitializeHandler(0, "initialiseV_MVR21()")}')

        h("proc initialiseIons_MVR21() { for i = 0, n_MVR21-1 { a_MVR21[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MVR21")
        h('{fih_ion_MVR21 = new FInitializeHandler(1, "initialiseIons_MVR21()")}')

        # ######################   Population: MVR22
        print("Population MVR22 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MVR22 = []
        h("{ n_MVR22 = 1 }")
        h("objectvar a_MVR22[n_MVR22]")
        for i in range(int(h.n_MVR22)):
            h("a_MVR22[%i] = new GenericMuscleCell()"%i)
            h("access a_MVR22[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MVR22[0].position(-80., 360., 80.) }")

        h("proc initialiseV_MVR22() { for i = 0, n_MVR22-1 { a_MVR22[i].set_initial_v() } }")
        h("objref fih_MVR22")
        h('{fih_MVR22 = new FInitializeHandler(0, "initialiseV_MVR22()")}')

        h("proc initialiseIons_MVR22() { for i = 0, n_MVR22-1 { a_MVR22[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MVR22")
        h('{fih_ion_MVR22 = new FInitializeHandler(1, "initialiseIons_MVR22()")}')

        # ######################   Population: MVR23
        print("Population MVR23 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MVR23 = []
        h("{ n_MVR23 = 1 }")
        h("objectvar a_MVR23[n_MVR23]")
        for i in range(int(h.n_MVR23)):
            h("a_MVR23[%i] = new GenericMuscleCell()"%i)
            h("access a_MVR23[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MVR23[0].position(-80., 390., 80.) }")

        h("proc initialiseV_MVR23() { for i = 0, n_MVR23-1 { a_MVR23[i].set_initial_v() } }")
        h("objref fih_MVR23")
        h('{fih_MVR23 = new FInitializeHandler(0, "initialiseV_MVR23()")}')

        h("proc initialiseIons_MVR23() { for i = 0, n_MVR23-1 { a_MVR23[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MVR23")
        h('{fih_ion_MVR23 = new FInitializeHandler(1, "initialiseIons_MVR23()")}')

        # ######################   Population: MVL01
        print("Population MVL01 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MVL01 = []
        h("{ n_MVL01 = 1 }")
        h("objectvar a_MVL01[n_MVL01]")
        for i in range(int(h.n_MVL01)):
            h("a_MVL01[%i] = new GenericMuscleCell()"%i)
            h("access a_MVL01[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MVL01[0].position(-80., -270., -80.) }")

        h("proc initialiseV_MVL01() { for i = 0, n_MVL01-1 { a_MVL01[i].set_initial_v() } }")
        h("objref fih_MVL01")
        h('{fih_MVL01 = new FInitializeHandler(0, "initialiseV_MVL01()")}')

        h("proc initialiseIons_MVL01() { for i = 0, n_MVL01-1 { a_MVL01[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MVL01")
        h('{fih_ion_MVL01 = new FInitializeHandler(1, "initialiseIons_MVL01()")}')

        # ######################   Population: MVL02
        print("Population MVL02 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MVL02 = []
        h("{ n_MVL02 = 1 }")
        h("objectvar a_MVL02[n_MVL02]")
        for i in range(int(h.n_MVL02)):
            h("a_MVL02[%i] = new GenericMuscleCell()"%i)
            h("access a_MVL02[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MVL02[0].position(-80., -240., -80.) }")

        h("proc initialiseV_MVL02() { for i = 0, n_MVL02-1 { a_MVL02[i].set_initial_v() } }")
        h("objref fih_MVL02")
        h('{fih_MVL02 = new FInitializeHandler(0, "initialiseV_MVL02()")}')

        h("proc initialiseIons_MVL02() { for i = 0, n_MVL02-1 { a_MVL02[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MVL02")
        h('{fih_ion_MVL02 = new FInitializeHandler(1, "initialiseIons_MVL02()")}')

        # ######################   Population: MVL03
        print("Population MVL03 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MVL03 = []
        h("{ n_MVL03 = 1 }")
        h("objectvar a_MVL03[n_MVL03]")
        for i in range(int(h.n_MVL03)):
            h("a_MVL03[%i] = new GenericMuscleCell()"%i)
            h("access a_MVL03[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MVL03[0].position(-80., -210., -80.) }")

        h("proc initialiseV_MVL03() { for i = 0, n_MVL03-1 { a_MVL03[i].set_initial_v() } }")
        h("objref fih_MVL03")
        h('{fih_MVL03 = new FInitializeHandler(0, "initialiseV_MVL03()")}')

        h("proc initialiseIons_MVL03() { for i = 0, n_MVL03-1 { a_MVL03[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MVL03")
        h('{fih_ion_MVL03 = new FInitializeHandler(1, "initialiseIons_MVL03()")}')

        # ######################   Population: MVL04
        print("Population MVL04 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MVL04 = []
        h("{ n_MVL04 = 1 }")
        h("objectvar a_MVL04[n_MVL04]")
        for i in range(int(h.n_MVL04)):
            h("a_MVL04[%i] = new GenericMuscleCell()"%i)
            h("access a_MVL04[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MVL04[0].position(-80., -180., -80.) }")

        h("proc initialiseV_MVL04() { for i = 0, n_MVL04-1 { a_MVL04[i].set_initial_v() } }")
        h("objref fih_MVL04")
        h('{fih_MVL04 = new FInitializeHandler(0, "initialiseV_MVL04()")}')

        h("proc initialiseIons_MVL04() { for i = 0, n_MVL04-1 { a_MVL04[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MVL04")
        h('{fih_ion_MVL04 = new FInitializeHandler(1, "initialiseIons_MVL04()")}')

        # ######################   Population: MVL05
        print("Population MVL05 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MVL05 = []
        h("{ n_MVL05 = 1 }")
        h("objectvar a_MVL05[n_MVL05]")
        for i in range(int(h.n_MVL05)):
            h("a_MVL05[%i] = new GenericMuscleCell()"%i)
            h("access a_MVL05[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MVL05[0].position(-80., -150., -80.) }")

        h("proc initialiseV_MVL05() { for i = 0, n_MVL05-1 { a_MVL05[i].set_initial_v() } }")
        h("objref fih_MVL05")
        h('{fih_MVL05 = new FInitializeHandler(0, "initialiseV_MVL05()")}')

        h("proc initialiseIons_MVL05() { for i = 0, n_MVL05-1 { a_MVL05[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MVL05")
        h('{fih_ion_MVL05 = new FInitializeHandler(1, "initialiseIons_MVL05()")}')

        # ######################   Population: MVL06
        print("Population MVL06 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MVL06 = []
        h("{ n_MVL06 = 1 }")
        h("objectvar a_MVL06[n_MVL06]")
        for i in range(int(h.n_MVL06)):
            h("a_MVL06[%i] = new GenericMuscleCell()"%i)
            h("access a_MVL06[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MVL06[0].position(-80., -120., -80.) }")

        h("proc initialiseV_MVL06() { for i = 0, n_MVL06-1 { a_MVL06[i].set_initial_v() } }")
        h("objref fih_MVL06")
        h('{fih_MVL06 = new FInitializeHandler(0, "initialiseV_MVL06()")}')

        h("proc initialiseIons_MVL06() { for i = 0, n_MVL06-1 { a_MVL06[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MVL06")
        h('{fih_ion_MVL06 = new FInitializeHandler(1, "initialiseIons_MVL06()")}')

        # ######################   Population: MVL07
        print("Population MVL07 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MVL07 = []
        h("{ n_MVL07 = 1 }")
        h("objectvar a_MVL07[n_MVL07]")
        for i in range(int(h.n_MVL07)):
            h("a_MVL07[%i] = new GenericMuscleCell()"%i)
            h("access a_MVL07[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MVL07[0].position(-80., -90., -80.) }")

        h("proc initialiseV_MVL07() { for i = 0, n_MVL07-1 { a_MVL07[i].set_initial_v() } }")
        h("objref fih_MVL07")
        h('{fih_MVL07 = new FInitializeHandler(0, "initialiseV_MVL07()")}')

        h("proc initialiseIons_MVL07() { for i = 0, n_MVL07-1 { a_MVL07[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MVL07")
        h('{fih_ion_MVL07 = new FInitializeHandler(1, "initialiseIons_MVL07()")}')

        # ######################   Population: MVL08
        print("Population MVL08 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MVL08 = []
        h("{ n_MVL08 = 1 }")
        h("objectvar a_MVL08[n_MVL08]")
        for i in range(int(h.n_MVL08)):
            h("a_MVL08[%i] = new GenericMuscleCell()"%i)
            h("access a_MVL08[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MVL08[0].position(-80., -60., -80.) }")

        h("proc initialiseV_MVL08() { for i = 0, n_MVL08-1 { a_MVL08[i].set_initial_v() } }")
        h("objref fih_MVL08")
        h('{fih_MVL08 = new FInitializeHandler(0, "initialiseV_MVL08()")}')

        h("proc initialiseIons_MVL08() { for i = 0, n_MVL08-1 { a_MVL08[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MVL08")
        h('{fih_ion_MVL08 = new FInitializeHandler(1, "initialiseIons_MVL08()")}')

        # ######################   Population: MVL09
        print("Population MVL09 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MVL09 = []
        h("{ n_MVL09 = 1 }")
        h("objectvar a_MVL09[n_MVL09]")
        for i in range(int(h.n_MVL09)):
            h("a_MVL09[%i] = new GenericMuscleCell()"%i)
            h("access a_MVL09[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MVL09[0].position(-80., -30., -80.) }")

        h("proc initialiseV_MVL09() { for i = 0, n_MVL09-1 { a_MVL09[i].set_initial_v() } }")
        h("objref fih_MVL09")
        h('{fih_MVL09 = new FInitializeHandler(0, "initialiseV_MVL09()")}')

        h("proc initialiseIons_MVL09() { for i = 0, n_MVL09-1 { a_MVL09[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MVL09")
        h('{fih_ion_MVL09 = new FInitializeHandler(1, "initialiseIons_MVL09()")}')

        # ######################   Population: MVL10
        print("Population MVL10 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MVL10 = []
        h("{ n_MVL10 = 1 }")
        h("objectvar a_MVL10[n_MVL10]")
        for i in range(int(h.n_MVL10)):
            h("a_MVL10[%i] = new GenericMuscleCell()"%i)
            h("access a_MVL10[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MVL10[0].position(-80., 0., -80.) }")

        h("proc initialiseV_MVL10() { for i = 0, n_MVL10-1 { a_MVL10[i].set_initial_v() } }")
        h("objref fih_MVL10")
        h('{fih_MVL10 = new FInitializeHandler(0, "initialiseV_MVL10()")}')

        h("proc initialiseIons_MVL10() { for i = 0, n_MVL10-1 { a_MVL10[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MVL10")
        h('{fih_ion_MVL10 = new FInitializeHandler(1, "initialiseIons_MVL10()")}')

        # ######################   Population: MVL11
        print("Population MVL11 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MVL11 = []
        h("{ n_MVL11 = 1 }")
        h("objectvar a_MVL11[n_MVL11]")
        for i in range(int(h.n_MVL11)):
            h("a_MVL11[%i] = new GenericMuscleCell()"%i)
            h("access a_MVL11[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MVL11[0].position(-80., 30., -80.) }")

        h("proc initialiseV_MVL11() { for i = 0, n_MVL11-1 { a_MVL11[i].set_initial_v() } }")
        h("objref fih_MVL11")
        h('{fih_MVL11 = new FInitializeHandler(0, "initialiseV_MVL11()")}')

        h("proc initialiseIons_MVL11() { for i = 0, n_MVL11-1 { a_MVL11[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MVL11")
        h('{fih_ion_MVL11 = new FInitializeHandler(1, "initialiseIons_MVL11()")}')

        # ######################   Population: MVL12
        print("Population MVL12 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MVL12 = []
        h("{ n_MVL12 = 1 }")
        h("objectvar a_MVL12[n_MVL12]")
        for i in range(int(h.n_MVL12)):
            h("a_MVL12[%i] = new GenericMuscleCell()"%i)
            h("access a_MVL12[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MVL12[0].position(-80., 60., -80.) }")

        h("proc initialiseV_MVL12() { for i = 0, n_MVL12-1 { a_MVL12[i].set_initial_v() } }")
        h("objref fih_MVL12")
        h('{fih_MVL12 = new FInitializeHandler(0, "initialiseV_MVL12()")}')

        h("proc initialiseIons_MVL12() { for i = 0, n_MVL12-1 { a_MVL12[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MVL12")
        h('{fih_ion_MVL12 = new FInitializeHandler(1, "initialiseIons_MVL12()")}')

        # ######################   Population: MVL13
        print("Population MVL13 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MVL13 = []
        h("{ n_MVL13 = 1 }")
        h("objectvar a_MVL13[n_MVL13]")
        for i in range(int(h.n_MVL13)):
            h("a_MVL13[%i] = new GenericMuscleCell()"%i)
            h("access a_MVL13[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MVL13[0].position(-80., 90., -80.) }")

        h("proc initialiseV_MVL13() { for i = 0, n_MVL13-1 { a_MVL13[i].set_initial_v() } }")
        h("objref fih_MVL13")
        h('{fih_MVL13 = new FInitializeHandler(0, "initialiseV_MVL13()")}')

        h("proc initialiseIons_MVL13() { for i = 0, n_MVL13-1 { a_MVL13[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MVL13")
        h('{fih_ion_MVL13 = new FInitializeHandler(1, "initialiseIons_MVL13()")}')

        # ######################   Population: MVL14
        print("Population MVL14 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MVL14 = []
        h("{ n_MVL14 = 1 }")
        h("objectvar a_MVL14[n_MVL14]")
        for i in range(int(h.n_MVL14)):
            h("a_MVL14[%i] = new GenericMuscleCell()"%i)
            h("access a_MVL14[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MVL14[0].position(-80., 120., -80.) }")

        h("proc initialiseV_MVL14() { for i = 0, n_MVL14-1 { a_MVL14[i].set_initial_v() } }")
        h("objref fih_MVL14")
        h('{fih_MVL14 = new FInitializeHandler(0, "initialiseV_MVL14()")}')

        h("proc initialiseIons_MVL14() { for i = 0, n_MVL14-1 { a_MVL14[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MVL14")
        h('{fih_ion_MVL14 = new FInitializeHandler(1, "initialiseIons_MVL14()")}')

        # ######################   Population: MVL15
        print("Population MVL15 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MVL15 = []
        h("{ n_MVL15 = 1 }")
        h("objectvar a_MVL15[n_MVL15]")
        for i in range(int(h.n_MVL15)):
            h("a_MVL15[%i] = new GenericMuscleCell()"%i)
            h("access a_MVL15[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MVL15[0].position(-80., 150., -80.) }")

        h("proc initialiseV_MVL15() { for i = 0, n_MVL15-1 { a_MVL15[i].set_initial_v() } }")
        h("objref fih_MVL15")
        h('{fih_MVL15 = new FInitializeHandler(0, "initialiseV_MVL15()")}')

        h("proc initialiseIons_MVL15() { for i = 0, n_MVL15-1 { a_MVL15[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MVL15")
        h('{fih_ion_MVL15 = new FInitializeHandler(1, "initialiseIons_MVL15()")}')

        # ######################   Population: MVL16
        print("Population MVL16 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MVL16 = []
        h("{ n_MVL16 = 1 }")
        h("objectvar a_MVL16[n_MVL16]")
        for i in range(int(h.n_MVL16)):
            h("a_MVL16[%i] = new GenericMuscleCell()"%i)
            h("access a_MVL16[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MVL16[0].position(-80., 180., -80.) }")

        h("proc initialiseV_MVL16() { for i = 0, n_MVL16-1 { a_MVL16[i].set_initial_v() } }")
        h("objref fih_MVL16")
        h('{fih_MVL16 = new FInitializeHandler(0, "initialiseV_MVL16()")}')

        h("proc initialiseIons_MVL16() { for i = 0, n_MVL16-1 { a_MVL16[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MVL16")
        h('{fih_ion_MVL16 = new FInitializeHandler(1, "initialiseIons_MVL16()")}')

        # ######################   Population: MVL17
        print("Population MVL17 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MVL17 = []
        h("{ n_MVL17 = 1 }")
        h("objectvar a_MVL17[n_MVL17]")
        for i in range(int(h.n_MVL17)):
            h("a_MVL17[%i] = new GenericMuscleCell()"%i)
            h("access a_MVL17[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MVL17[0].position(-80., 210., -80.) }")

        h("proc initialiseV_MVL17() { for i = 0, n_MVL17-1 { a_MVL17[i].set_initial_v() } }")
        h("objref fih_MVL17")
        h('{fih_MVL17 = new FInitializeHandler(0, "initialiseV_MVL17()")}')

        h("proc initialiseIons_MVL17() { for i = 0, n_MVL17-1 { a_MVL17[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MVL17")
        h('{fih_ion_MVL17 = new FInitializeHandler(1, "initialiseIons_MVL17()")}')

        # ######################   Population: MVL18
        print("Population MVL18 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MVL18 = []
        h("{ n_MVL18 = 1 }")
        h("objectvar a_MVL18[n_MVL18]")
        for i in range(int(h.n_MVL18)):
            h("a_MVL18[%i] = new GenericMuscleCell()"%i)
            h("access a_MVL18[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MVL18[0].position(-80., 240., -80.) }")

        h("proc initialiseV_MVL18() { for i = 0, n_MVL18-1 { a_MVL18[i].set_initial_v() } }")
        h("objref fih_MVL18")
        h('{fih_MVL18 = new FInitializeHandler(0, "initialiseV_MVL18()")}')

        h("proc initialiseIons_MVL18() { for i = 0, n_MVL18-1 { a_MVL18[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MVL18")
        h('{fih_ion_MVL18 = new FInitializeHandler(1, "initialiseIons_MVL18()")}')

        # ######################   Population: MVL19
        print("Population MVL19 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MVL19 = []
        h("{ n_MVL19 = 1 }")
        h("objectvar a_MVL19[n_MVL19]")
        for i in range(int(h.n_MVL19)):
            h("a_MVL19[%i] = new GenericMuscleCell()"%i)
            h("access a_MVL19[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MVL19[0].position(-80., 270., -80.) }")

        h("proc initialiseV_MVL19() { for i = 0, n_MVL19-1 { a_MVL19[i].set_initial_v() } }")
        h("objref fih_MVL19")
        h('{fih_MVL19 = new FInitializeHandler(0, "initialiseV_MVL19()")}')

        h("proc initialiseIons_MVL19() { for i = 0, n_MVL19-1 { a_MVL19[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MVL19")
        h('{fih_ion_MVL19 = new FInitializeHandler(1, "initialiseIons_MVL19()")}')

        # ######################   Population: MVL20
        print("Population MVL20 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MVL20 = []
        h("{ n_MVL20 = 1 }")
        h("objectvar a_MVL20[n_MVL20]")
        for i in range(int(h.n_MVL20)):
            h("a_MVL20[%i] = new GenericMuscleCell()"%i)
            h("access a_MVL20[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MVL20[0].position(-80., 300., -80.) }")

        h("proc initialiseV_MVL20() { for i = 0, n_MVL20-1 { a_MVL20[i].set_initial_v() } }")
        h("objref fih_MVL20")
        h('{fih_MVL20 = new FInitializeHandler(0, "initialiseV_MVL20()")}')

        h("proc initialiseIons_MVL20() { for i = 0, n_MVL20-1 { a_MVL20[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MVL20")
        h('{fih_ion_MVL20 = new FInitializeHandler(1, "initialiseIons_MVL20()")}')

        # ######################   Population: MVL21
        print("Population MVL21 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MVL21 = []
        h("{ n_MVL21 = 1 }")
        h("objectvar a_MVL21[n_MVL21]")
        for i in range(int(h.n_MVL21)):
            h("a_MVL21[%i] = new GenericMuscleCell()"%i)
            h("access a_MVL21[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MVL21[0].position(-80., 330., -80.) }")

        h("proc initialiseV_MVL21() { for i = 0, n_MVL21-1 { a_MVL21[i].set_initial_v() } }")
        h("objref fih_MVL21")
        h('{fih_MVL21 = new FInitializeHandler(0, "initialiseV_MVL21()")}')

        h("proc initialiseIons_MVL21() { for i = 0, n_MVL21-1 { a_MVL21[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MVL21")
        h('{fih_ion_MVL21 = new FInitializeHandler(1, "initialiseIons_MVL21()")}')

        # ######################   Population: MVL22
        print("Population MVL22 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MVL22 = []
        h("{ n_MVL22 = 1 }")
        h("objectvar a_MVL22[n_MVL22]")
        for i in range(int(h.n_MVL22)):
            h("a_MVL22[%i] = new GenericMuscleCell()"%i)
            h("access a_MVL22[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MVL22[0].position(-80., 360., -80.) }")

        h("proc initialiseV_MVL22() { for i = 0, n_MVL22-1 { a_MVL22[i].set_initial_v() } }")
        h("objref fih_MVL22")
        h('{fih_MVL22 = new FInitializeHandler(0, "initialiseV_MVL22()")}')

        h("proc initialiseIons_MVL22() { for i = 0, n_MVL22-1 { a_MVL22[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MVL22")
        h('{fih_ion_MVL22 = new FInitializeHandler(1, "initialiseIons_MVL22()")}')

        # ######################   Population: MVL23
        print("Population MVL23 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MVL23 = []
        h("{ n_MVL23 = 1 }")
        h("objectvar a_MVL23[n_MVL23]")
        for i in range(int(h.n_MVL23)):
            h("a_MVL23[%i] = new GenericMuscleCell()"%i)
            h("access a_MVL23[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MVL23[0].position(-80., 390., -80.) }")

        h("proc initialiseV_MVL23() { for i = 0, n_MVL23-1 { a_MVL23[i].set_initial_v() } }")
        h("objref fih_MVL23")
        h('{fih_MVL23 = new FInitializeHandler(0, "initialiseV_MVL23()")}')

        h("proc initialiseIons_MVL23() { for i = 0, n_MVL23-1 { a_MVL23[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MVL23")
        h('{fih_ion_MVL23 = new FInitializeHandler(1, "initialiseIons_MVL23()")}')

        # ######################   Population: MVL24
        print("Population MVL24 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MVL24 = []
        h("{ n_MVL24 = 1 }")
        h("objectvar a_MVL24[n_MVL24]")
        for i in range(int(h.n_MVL24)):
            h("a_MVL24[%i] = new GenericMuscleCell()"%i)
            h("access a_MVL24[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MVL24[0].position(-80., 420., -80.) }")

        h("proc initialiseV_MVL24() { for i = 0, n_MVL24-1 { a_MVL24[i].set_initial_v() } }")
        h("objref fih_MVL24")
        h('{fih_MVL24 = new FInitializeHandler(0, "initialiseV_MVL24()")}')

        h("proc initialiseIons_MVL24() { for i = 0, n_MVL24-1 { a_MVL24[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MVL24")
        h('{fih_ion_MVL24 = new FInitializeHandler(1, "initialiseIons_MVL24()")}')

        # ######################   Population: MDL01
        print("Population MDL01 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MDL01 = []
        h("{ n_MDL01 = 1 }")
        h("objectvar a_MDL01[n_MDL01]")
        for i in range(int(h.n_MDL01)):
            h("a_MDL01[%i] = new GenericMuscleCell()"%i)
            h("access a_MDL01[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MDL01[0].position(80., -270., -80.) }")

        h("proc initialiseV_MDL01() { for i = 0, n_MDL01-1 { a_MDL01[i].set_initial_v() } }")
        h("objref fih_MDL01")
        h('{fih_MDL01 = new FInitializeHandler(0, "initialiseV_MDL01()")}')

        h("proc initialiseIons_MDL01() { for i = 0, n_MDL01-1 { a_MDL01[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MDL01")
        h('{fih_ion_MDL01 = new FInitializeHandler(1, "initialiseIons_MDL01()")}')

        # ######################   Population: MDL02
        print("Population MDL02 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MDL02 = []
        h("{ n_MDL02 = 1 }")
        h("objectvar a_MDL02[n_MDL02]")
        for i in range(int(h.n_MDL02)):
            h("a_MDL02[%i] = new GenericMuscleCell()"%i)
            h("access a_MDL02[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MDL02[0].position(80., -240., -80.) }")

        h("proc initialiseV_MDL02() { for i = 0, n_MDL02-1 { a_MDL02[i].set_initial_v() } }")
        h("objref fih_MDL02")
        h('{fih_MDL02 = new FInitializeHandler(0, "initialiseV_MDL02()")}')

        h("proc initialiseIons_MDL02() { for i = 0, n_MDL02-1 { a_MDL02[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MDL02")
        h('{fih_ion_MDL02 = new FInitializeHandler(1, "initialiseIons_MDL02()")}')

        # ######################   Population: MDL03
        print("Population MDL03 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MDL03 = []
        h("{ n_MDL03 = 1 }")
        h("objectvar a_MDL03[n_MDL03]")
        for i in range(int(h.n_MDL03)):
            h("a_MDL03[%i] = new GenericMuscleCell()"%i)
            h("access a_MDL03[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MDL03[0].position(80., -210., -80.) }")

        h("proc initialiseV_MDL03() { for i = 0, n_MDL03-1 { a_MDL03[i].set_initial_v() } }")
        h("objref fih_MDL03")
        h('{fih_MDL03 = new FInitializeHandler(0, "initialiseV_MDL03()")}')

        h("proc initialiseIons_MDL03() { for i = 0, n_MDL03-1 { a_MDL03[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MDL03")
        h('{fih_ion_MDL03 = new FInitializeHandler(1, "initialiseIons_MDL03()")}')

        # ######################   Population: MDL04
        print("Population MDL04 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MDL04 = []
        h("{ n_MDL04 = 1 }")
        h("objectvar a_MDL04[n_MDL04]")
        for i in range(int(h.n_MDL04)):
            h("a_MDL04[%i] = new GenericMuscleCell()"%i)
            h("access a_MDL04[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MDL04[0].position(80., -180., -80.) }")

        h("proc initialiseV_MDL04() { for i = 0, n_MDL04-1 { a_MDL04[i].set_initial_v() } }")
        h("objref fih_MDL04")
        h('{fih_MDL04 = new FInitializeHandler(0, "initialiseV_MDL04()")}')

        h("proc initialiseIons_MDL04() { for i = 0, n_MDL04-1 { a_MDL04[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MDL04")
        h('{fih_ion_MDL04 = new FInitializeHandler(1, "initialiseIons_MDL04()")}')

        # ######################   Population: MDL05
        print("Population MDL05 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MDL05 = []
        h("{ n_MDL05 = 1 }")
        h("objectvar a_MDL05[n_MDL05]")
        for i in range(int(h.n_MDL05)):
            h("a_MDL05[%i] = new GenericMuscleCell()"%i)
            h("access a_MDL05[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MDL05[0].position(80., -150., -80.) }")

        h("proc initialiseV_MDL05() { for i = 0, n_MDL05-1 { a_MDL05[i].set_initial_v() } }")
        h("objref fih_MDL05")
        h('{fih_MDL05 = new FInitializeHandler(0, "initialiseV_MDL05()")}')

        h("proc initialiseIons_MDL05() { for i = 0, n_MDL05-1 { a_MDL05[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MDL05")
        h('{fih_ion_MDL05 = new FInitializeHandler(1, "initialiseIons_MDL05()")}')

        # ######################   Population: MDL06
        print("Population MDL06 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MDL06 = []
        h("{ n_MDL06 = 1 }")
        h("objectvar a_MDL06[n_MDL06]")
        for i in range(int(h.n_MDL06)):
            h("a_MDL06[%i] = new GenericMuscleCell()"%i)
            h("access a_MDL06[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MDL06[0].position(80., -120., -80.) }")

        h("proc initialiseV_MDL06() { for i = 0, n_MDL06-1 { a_MDL06[i].set_initial_v() } }")
        h("objref fih_MDL06")
        h('{fih_MDL06 = new FInitializeHandler(0, "initialiseV_MDL06()")}')

        h("proc initialiseIons_MDL06() { for i = 0, n_MDL06-1 { a_MDL06[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MDL06")
        h('{fih_ion_MDL06 = new FInitializeHandler(1, "initialiseIons_MDL06()")}')

        # ######################   Population: MDL07
        print("Population MDL07 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MDL07 = []
        h("{ n_MDL07 = 1 }")
        h("objectvar a_MDL07[n_MDL07]")
        for i in range(int(h.n_MDL07)):
            h("a_MDL07[%i] = new GenericMuscleCell()"%i)
            h("access a_MDL07[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MDL07[0].position(80., -90., -80.) }")

        h("proc initialiseV_MDL07() { for i = 0, n_MDL07-1 { a_MDL07[i].set_initial_v() } }")
        h("objref fih_MDL07")
        h('{fih_MDL07 = new FInitializeHandler(0, "initialiseV_MDL07()")}')

        h("proc initialiseIons_MDL07() { for i = 0, n_MDL07-1 { a_MDL07[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MDL07")
        h('{fih_ion_MDL07 = new FInitializeHandler(1, "initialiseIons_MDL07()")}')

        # ######################   Population: MDL08
        print("Population MDL08 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MDL08 = []
        h("{ n_MDL08 = 1 }")
        h("objectvar a_MDL08[n_MDL08]")
        for i in range(int(h.n_MDL08)):
            h("a_MDL08[%i] = new GenericMuscleCell()"%i)
            h("access a_MDL08[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MDL08[0].position(80., -60., -80.) }")

        h("proc initialiseV_MDL08() { for i = 0, n_MDL08-1 { a_MDL08[i].set_initial_v() } }")
        h("objref fih_MDL08")
        h('{fih_MDL08 = new FInitializeHandler(0, "initialiseV_MDL08()")}')

        h("proc initialiseIons_MDL08() { for i = 0, n_MDL08-1 { a_MDL08[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MDL08")
        h('{fih_ion_MDL08 = new FInitializeHandler(1, "initialiseIons_MDL08()")}')

        # ######################   Population: MDL09
        print("Population MDL09 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MDL09 = []
        h("{ n_MDL09 = 1 }")
        h("objectvar a_MDL09[n_MDL09]")
        for i in range(int(h.n_MDL09)):
            h("a_MDL09[%i] = new GenericMuscleCell()"%i)
            h("access a_MDL09[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MDL09[0].position(80., -30., -80.) }")

        h("proc initialiseV_MDL09() { for i = 0, n_MDL09-1 { a_MDL09[i].set_initial_v() } }")
        h("objref fih_MDL09")
        h('{fih_MDL09 = new FInitializeHandler(0, "initialiseV_MDL09()")}')

        h("proc initialiseIons_MDL09() { for i = 0, n_MDL09-1 { a_MDL09[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MDL09")
        h('{fih_ion_MDL09 = new FInitializeHandler(1, "initialiseIons_MDL09()")}')

        # ######################   Population: MDL10
        print("Population MDL10 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MDL10 = []
        h("{ n_MDL10 = 1 }")
        h("objectvar a_MDL10[n_MDL10]")
        for i in range(int(h.n_MDL10)):
            h("a_MDL10[%i] = new GenericMuscleCell()"%i)
            h("access a_MDL10[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MDL10[0].position(80., 0., -80.) }")

        h("proc initialiseV_MDL10() { for i = 0, n_MDL10-1 { a_MDL10[i].set_initial_v() } }")
        h("objref fih_MDL10")
        h('{fih_MDL10 = new FInitializeHandler(0, "initialiseV_MDL10()")}')

        h("proc initialiseIons_MDL10() { for i = 0, n_MDL10-1 { a_MDL10[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MDL10")
        h('{fih_ion_MDL10 = new FInitializeHandler(1, "initialiseIons_MDL10()")}')

        # ######################   Population: MDL11
        print("Population MDL11 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MDL11 = []
        h("{ n_MDL11 = 1 }")
        h("objectvar a_MDL11[n_MDL11]")
        for i in range(int(h.n_MDL11)):
            h("a_MDL11[%i] = new GenericMuscleCell()"%i)
            h("access a_MDL11[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MDL11[0].position(80., 30., -80.) }")

        h("proc initialiseV_MDL11() { for i = 0, n_MDL11-1 { a_MDL11[i].set_initial_v() } }")
        h("objref fih_MDL11")
        h('{fih_MDL11 = new FInitializeHandler(0, "initialiseV_MDL11()")}')

        h("proc initialiseIons_MDL11() { for i = 0, n_MDL11-1 { a_MDL11[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MDL11")
        h('{fih_ion_MDL11 = new FInitializeHandler(1, "initialiseIons_MDL11()")}')

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

        # ######################   Population: MDL13
        print("Population MDL13 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MDL13 = []
        h("{ n_MDL13 = 1 }")
        h("objectvar a_MDL13[n_MDL13]")
        for i in range(int(h.n_MDL13)):
            h("a_MDL13[%i] = new GenericMuscleCell()"%i)
            h("access a_MDL13[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MDL13[0].position(80., 90., -80.) }")

        h("proc initialiseV_MDL13() { for i = 0, n_MDL13-1 { a_MDL13[i].set_initial_v() } }")
        h("objref fih_MDL13")
        h('{fih_MDL13 = new FInitializeHandler(0, "initialiseV_MDL13()")}')

        h("proc initialiseIons_MDL13() { for i = 0, n_MDL13-1 { a_MDL13[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MDL13")
        h('{fih_ion_MDL13 = new FInitializeHandler(1, "initialiseIons_MDL13()")}')

        # ######################   Population: MDL14
        print("Population MDL14 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MDL14 = []
        h("{ n_MDL14 = 1 }")
        h("objectvar a_MDL14[n_MDL14]")
        for i in range(int(h.n_MDL14)):
            h("a_MDL14[%i] = new GenericMuscleCell()"%i)
            h("access a_MDL14[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MDL14[0].position(80., 120., -80.) }")

        h("proc initialiseV_MDL14() { for i = 0, n_MDL14-1 { a_MDL14[i].set_initial_v() } }")
        h("objref fih_MDL14")
        h('{fih_MDL14 = new FInitializeHandler(0, "initialiseV_MDL14()")}')

        h("proc initialiseIons_MDL14() { for i = 0, n_MDL14-1 { a_MDL14[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MDL14")
        h('{fih_ion_MDL14 = new FInitializeHandler(1, "initialiseIons_MDL14()")}')

        # ######################   Population: MDL15
        print("Population MDL15 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MDL15 = []
        h("{ n_MDL15 = 1 }")
        h("objectvar a_MDL15[n_MDL15]")
        for i in range(int(h.n_MDL15)):
            h("a_MDL15[%i] = new GenericMuscleCell()"%i)
            h("access a_MDL15[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MDL15[0].position(80., 150., -80.) }")

        h("proc initialiseV_MDL15() { for i = 0, n_MDL15-1 { a_MDL15[i].set_initial_v() } }")
        h("objref fih_MDL15")
        h('{fih_MDL15 = new FInitializeHandler(0, "initialiseV_MDL15()")}')

        h("proc initialiseIons_MDL15() { for i = 0, n_MDL15-1 { a_MDL15[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MDL15")
        h('{fih_ion_MDL15 = new FInitializeHandler(1, "initialiseIons_MDL15()")}')

        # ######################   Population: MDL16
        print("Population MDL16 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MDL16 = []
        h("{ n_MDL16 = 1 }")
        h("objectvar a_MDL16[n_MDL16]")
        for i in range(int(h.n_MDL16)):
            h("a_MDL16[%i] = new GenericMuscleCell()"%i)
            h("access a_MDL16[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MDL16[0].position(80., 180., -80.) }")

        h("proc initialiseV_MDL16() { for i = 0, n_MDL16-1 { a_MDL16[i].set_initial_v() } }")
        h("objref fih_MDL16")
        h('{fih_MDL16 = new FInitializeHandler(0, "initialiseV_MDL16()")}')

        h("proc initialiseIons_MDL16() { for i = 0, n_MDL16-1 { a_MDL16[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MDL16")
        h('{fih_ion_MDL16 = new FInitializeHandler(1, "initialiseIons_MDL16()")}')

        # ######################   Population: MDL17
        print("Population MDL17 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MDL17 = []
        h("{ n_MDL17 = 1 }")
        h("objectvar a_MDL17[n_MDL17]")
        for i in range(int(h.n_MDL17)):
            h("a_MDL17[%i] = new GenericMuscleCell()"%i)
            h("access a_MDL17[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MDL17[0].position(80., 210., -80.) }")

        h("proc initialiseV_MDL17() { for i = 0, n_MDL17-1 { a_MDL17[i].set_initial_v() } }")
        h("objref fih_MDL17")
        h('{fih_MDL17 = new FInitializeHandler(0, "initialiseV_MDL17()")}')

        h("proc initialiseIons_MDL17() { for i = 0, n_MDL17-1 { a_MDL17[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MDL17")
        h('{fih_ion_MDL17 = new FInitializeHandler(1, "initialiseIons_MDL17()")}')

        # ######################   Population: MDL18
        print("Population MDL18 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MDL18 = []
        h("{ n_MDL18 = 1 }")
        h("objectvar a_MDL18[n_MDL18]")
        for i in range(int(h.n_MDL18)):
            h("a_MDL18[%i] = new GenericMuscleCell()"%i)
            h("access a_MDL18[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MDL18[0].position(80., 240., -80.) }")

        h("proc initialiseV_MDL18() { for i = 0, n_MDL18-1 { a_MDL18[i].set_initial_v() } }")
        h("objref fih_MDL18")
        h('{fih_MDL18 = new FInitializeHandler(0, "initialiseV_MDL18()")}')

        h("proc initialiseIons_MDL18() { for i = 0, n_MDL18-1 { a_MDL18[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MDL18")
        h('{fih_ion_MDL18 = new FInitializeHandler(1, "initialiseIons_MDL18()")}')

        # ######################   Population: MDL19
        print("Population MDL19 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MDL19 = []
        h("{ n_MDL19 = 1 }")
        h("objectvar a_MDL19[n_MDL19]")
        for i in range(int(h.n_MDL19)):
            h("a_MDL19[%i] = new GenericMuscleCell()"%i)
            h("access a_MDL19[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MDL19[0].position(80., 270., -80.) }")

        h("proc initialiseV_MDL19() { for i = 0, n_MDL19-1 { a_MDL19[i].set_initial_v() } }")
        h("objref fih_MDL19")
        h('{fih_MDL19 = new FInitializeHandler(0, "initialiseV_MDL19()")}')

        h("proc initialiseIons_MDL19() { for i = 0, n_MDL19-1 { a_MDL19[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MDL19")
        h('{fih_ion_MDL19 = new FInitializeHandler(1, "initialiseIons_MDL19()")}')

        # ######################   Population: MDL20
        print("Population MDL20 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MDL20 = []
        h("{ n_MDL20 = 1 }")
        h("objectvar a_MDL20[n_MDL20]")
        for i in range(int(h.n_MDL20)):
            h("a_MDL20[%i] = new GenericMuscleCell()"%i)
            h("access a_MDL20[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MDL20[0].position(80., 300., -80.) }")

        h("proc initialiseV_MDL20() { for i = 0, n_MDL20-1 { a_MDL20[i].set_initial_v() } }")
        h("objref fih_MDL20")
        h('{fih_MDL20 = new FInitializeHandler(0, "initialiseV_MDL20()")}')

        h("proc initialiseIons_MDL20() { for i = 0, n_MDL20-1 { a_MDL20[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MDL20")
        h('{fih_ion_MDL20 = new FInitializeHandler(1, "initialiseIons_MDL20()")}')

        # ######################   Population: MDL21
        print("Population MDL21 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MDL21 = []
        h("{ n_MDL21 = 1 }")
        h("objectvar a_MDL21[n_MDL21]")
        for i in range(int(h.n_MDL21)):
            h("a_MDL21[%i] = new GenericMuscleCell()"%i)
            h("access a_MDL21[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MDL21[0].position(80., 330., -80.) }")

        h("proc initialiseV_MDL21() { for i = 0, n_MDL21-1 { a_MDL21[i].set_initial_v() } }")
        h("objref fih_MDL21")
        h('{fih_MDL21 = new FInitializeHandler(0, "initialiseV_MDL21()")}')

        h("proc initialiseIons_MDL21() { for i = 0, n_MDL21-1 { a_MDL21[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MDL21")
        h('{fih_ion_MDL21 = new FInitializeHandler(1, "initialiseIons_MDL21()")}')

        # ######################   Population: MDL22
        print("Population MDL22 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MDL22 = []
        h("{ n_MDL22 = 1 }")
        h("objectvar a_MDL22[n_MDL22]")
        for i in range(int(h.n_MDL22)):
            h("a_MDL22[%i] = new GenericMuscleCell()"%i)
            h("access a_MDL22[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MDL22[0].position(80., 360., -80.) }")

        h("proc initialiseV_MDL22() { for i = 0, n_MDL22-1 { a_MDL22[i].set_initial_v() } }")
        h("objref fih_MDL22")
        h('{fih_MDL22 = new FInitializeHandler(0, "initialiseV_MDL22()")}')

        h("proc initialiseIons_MDL22() { for i = 0, n_MDL22-1 { a_MDL22[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MDL22")
        h('{fih_ion_MDL22 = new FInitializeHandler(1, "initialiseIons_MDL22()")}')

        # ######################   Population: MDL23
        print("Population MDL23 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MDL23 = []
        h("{ n_MDL23 = 1 }")
        h("objectvar a_MDL23[n_MDL23]")
        for i in range(int(h.n_MDL23)):
            h("a_MDL23[%i] = new GenericMuscleCell()"%i)
            h("access a_MDL23[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MDL23[0].position(80., 390., -80.) }")

        h("proc initialiseV_MDL23() { for i = 0, n_MDL23-1 { a_MDL23[i].set_initial_v() } }")
        h("objref fih_MDL23")
        h('{fih_MDL23 = new FInitializeHandler(0, "initialiseV_MDL23()")}')

        h("proc initialiseIons_MDL23() { for i = 0, n_MDL23-1 { a_MDL23[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MDL23")
        h('{fih_ion_MDL23 = new FInitializeHandler(1, "initialiseIons_MDL23()")}')

        # ######################   Population: MDL24
        print("Population MDL24 contains 1 instance(s) of component: GenericMuscleCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericMuscleCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericMuscleCell.hoc")
        a_MDL24 = []
        h("{ n_MDL24 = 1 }")
        h("objectvar a_MDL24[n_MDL24]")
        for i in range(int(h.n_MDL24)):
            h("a_MDL24[%i] = new GenericMuscleCell()"%i)
            h("access a_MDL24[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_MDL24[0].position(80., 420., -80.) }")

        h("proc initialiseV_MDL24() { for i = 0, n_MDL24-1 { a_MDL24[i].set_initial_v() } }")
        h("objref fih_MDL24")
        h('{fih_MDL24 = new FInitializeHandler(0, "initialiseV_MDL24()")}')

        h("proc initialiseIons_MDL24() { for i = 0, n_MDL24-1 { a_MDL24[i].set_initial_ion_properties() } }")
        h("objref fih_ion_MDL24")
        h('{fih_ion_MDL24 = new FInitializeHandler(1, "initialiseIons_MDL24()")}')

        # ######################   Electrical Projection: NC_AVBL_AVBR_Generic_GJ
        print("Adding electrical projection: NC_AVBL_AVBR_Generic_GJ from AVBL to AVBR, with 1 connection(s)")

        #h("objectvar syn_NC_AVBL_AVBR_Generic_GJ_neuron_to_neuron_elec_syn_17conns_A[1]")
        h("objectvar syn_NC_AVBL_AVBR_Generic_GJ_neuron_to_neuron_elec_syn_17conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVBL[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVBR[0].soma], weight: 1.0
        #h("a_AVBL[0].soma { syn_NC_AVBL_AVBR_Generic_GJ_neuron_to_neuron_elec_syn_17conns_A[0] = new neuron_to_neuron_elec_syn_17conns(0.5) }")
        h("a_AVBR[0].soma { syn_NC_AVBL_AVBR_Generic_GJ_neuron_to_neuron_elec_syn_17conns_B[0] = new neuron_to_neuron_elec_syn_17conns(0.5) }")
        #h("setpointer syn_NC_AVBL_AVBR_Generic_GJ_neuron_to_neuron_elec_syn_17conns_A[0].vpeer, a_AVBR[0].soma.v(0.5)")
        h("setpointer syn_NC_AVBL_AVBR_Generic_GJ_neuron_to_neuron_elec_syn_17conns_B[0].vpeer, a_AVBL[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_AVBL_DB2_Generic_GJ
        print("Adding electrical projection: NC_AVBL_DB2_Generic_GJ from AVBL to DB2, with 1 connection(s)")

        #h("objectvar syn_NC_AVBL_DB2_Generic_GJ_AVBL_to_DB2_elec_syn_4conns_A[1]")
        h("objectvar syn_NC_AVBL_DB2_Generic_GJ_AVBL_to_DB2_elec_syn_4conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVBL[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DB2[0].soma], weight: 1.0
        #h("a_AVBL[0].soma { syn_NC_AVBL_DB2_Generic_GJ_AVBL_to_DB2_elec_syn_4conns_A[0] = new AVBL_to_DB2_elec_syn_4conns(0.5) }")
        h("a_DB2[0].soma { syn_NC_AVBL_DB2_Generic_GJ_AVBL_to_DB2_elec_syn_4conns_B[0] = new AVBL_to_DB2_elec_syn_4conns(0.5) }")
        #h("setpointer syn_NC_AVBL_DB2_Generic_GJ_AVBL_to_DB2_elec_syn_4conns_A[0].vpeer, a_DB2[0].soma.v(0.5)")
        h("setpointer syn_NC_AVBL_DB2_Generic_GJ_AVBL_to_DB2_elec_syn_4conns_B[0].vpeer, a_AVBL[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_AVBL_DB3_Generic_GJ
        print("Adding electrical projection: NC_AVBL_DB3_Generic_GJ from AVBL to DB3, with 1 connection(s)")

        #h("objectvar syn_NC_AVBL_DB3_Generic_GJ_AVBL_to_DB3_elec_syn_9conns_A[1]")
        h("objectvar syn_NC_AVBL_DB3_Generic_GJ_AVBL_to_DB3_elec_syn_9conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVBL[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DB3[0].soma], weight: 1.0
        #h("a_AVBL[0].soma { syn_NC_AVBL_DB3_Generic_GJ_AVBL_to_DB3_elec_syn_9conns_A[0] = new AVBL_to_DB3_elec_syn_9conns(0.5) }")
        h("a_DB3[0].soma { syn_NC_AVBL_DB3_Generic_GJ_AVBL_to_DB3_elec_syn_9conns_B[0] = new AVBL_to_DB3_elec_syn_9conns(0.5) }")
        #h("setpointer syn_NC_AVBL_DB3_Generic_GJ_AVBL_to_DB3_elec_syn_9conns_A[0].vpeer, a_DB3[0].soma.v(0.5)")
        h("setpointer syn_NC_AVBL_DB3_Generic_GJ_AVBL_to_DB3_elec_syn_9conns_B[0].vpeer, a_AVBL[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_AVBL_DB4_Generic_GJ
        print("Adding electrical projection: NC_AVBL_DB4_Generic_GJ from AVBL to DB4, with 1 connection(s)")

        #h("objectvar syn_NC_AVBL_DB4_Generic_GJ_AVBL_to_DB4_elec_syn_4conns_A[1]")
        h("objectvar syn_NC_AVBL_DB4_Generic_GJ_AVBL_to_DB4_elec_syn_4conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVBL[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DB4[0].soma], weight: 1.0
        #h("a_AVBL[0].soma { syn_NC_AVBL_DB4_Generic_GJ_AVBL_to_DB4_elec_syn_4conns_A[0] = new AVBL_to_DB4_elec_syn_4conns(0.5) }")
        h("a_DB4[0].soma { syn_NC_AVBL_DB4_Generic_GJ_AVBL_to_DB4_elec_syn_4conns_B[0] = new AVBL_to_DB4_elec_syn_4conns(0.5) }")
        #h("setpointer syn_NC_AVBL_DB4_Generic_GJ_AVBL_to_DB4_elec_syn_4conns_A[0].vpeer, a_DB4[0].soma.v(0.5)")
        h("setpointer syn_NC_AVBL_DB4_Generic_GJ_AVBL_to_DB4_elec_syn_4conns_B[0].vpeer, a_AVBL[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_AVBL_DB5_Generic_GJ
        print("Adding electrical projection: NC_AVBL_DB5_Generic_GJ from AVBL to DB5, with 1 connection(s)")

        #h("objectvar syn_NC_AVBL_DB5_Generic_GJ_AVBL_to_DB5_elec_syn_3conns_A[1]")
        h("objectvar syn_NC_AVBL_DB5_Generic_GJ_AVBL_to_DB5_elec_syn_3conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVBL[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DB5[0].soma], weight: 1.0
        #h("a_AVBL[0].soma { syn_NC_AVBL_DB5_Generic_GJ_AVBL_to_DB5_elec_syn_3conns_A[0] = new AVBL_to_DB5_elec_syn_3conns(0.5) }")
        h("a_DB5[0].soma { syn_NC_AVBL_DB5_Generic_GJ_AVBL_to_DB5_elec_syn_3conns_B[0] = new AVBL_to_DB5_elec_syn_3conns(0.5) }")
        #h("setpointer syn_NC_AVBL_DB5_Generic_GJ_AVBL_to_DB5_elec_syn_3conns_A[0].vpeer, a_DB5[0].soma.v(0.5)")
        h("setpointer syn_NC_AVBL_DB5_Generic_GJ_AVBL_to_DB5_elec_syn_3conns_B[0].vpeer, a_AVBL[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_AVBL_DB6_Generic_GJ
        print("Adding electrical projection: NC_AVBL_DB6_Generic_GJ from AVBL to DB6, with 1 connection(s)")

        #h("objectvar syn_NC_AVBL_DB6_Generic_GJ_AVBL_to_DB6_elec_syn_4conns_A[1]")
        h("objectvar syn_NC_AVBL_DB6_Generic_GJ_AVBL_to_DB6_elec_syn_4conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVBL[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DB6[0].soma], weight: 1.0
        #h("a_AVBL[0].soma { syn_NC_AVBL_DB6_Generic_GJ_AVBL_to_DB6_elec_syn_4conns_A[0] = new AVBL_to_DB6_elec_syn_4conns(0.5) }")
        h("a_DB6[0].soma { syn_NC_AVBL_DB6_Generic_GJ_AVBL_to_DB6_elec_syn_4conns_B[0] = new AVBL_to_DB6_elec_syn_4conns(0.5) }")
        #h("setpointer syn_NC_AVBL_DB6_Generic_GJ_AVBL_to_DB6_elec_syn_4conns_A[0].vpeer, a_DB6[0].soma.v(0.5)")
        h("setpointer syn_NC_AVBL_DB6_Generic_GJ_AVBL_to_DB6_elec_syn_4conns_B[0].vpeer, a_AVBL[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_AVBL_DB7_Generic_GJ
        print("Adding electrical projection: NC_AVBL_DB7_Generic_GJ from AVBL to DB7, with 1 connection(s)")

        #h("objectvar syn_NC_AVBL_DB7_Generic_GJ_AVBL_to_DB7_elec_syn_13conns_A[1]")
        h("objectvar syn_NC_AVBL_DB7_Generic_GJ_AVBL_to_DB7_elec_syn_13conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVBL[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DB7[0].soma], weight: 1.0
        #h("a_AVBL[0].soma { syn_NC_AVBL_DB7_Generic_GJ_AVBL_to_DB7_elec_syn_13conns_A[0] = new AVBL_to_DB7_elec_syn_13conns(0.5) }")
        h("a_DB7[0].soma { syn_NC_AVBL_DB7_Generic_GJ_AVBL_to_DB7_elec_syn_13conns_B[0] = new AVBL_to_DB7_elec_syn_13conns(0.5) }")
        #h("setpointer syn_NC_AVBL_DB7_Generic_GJ_AVBL_to_DB7_elec_syn_13conns_A[0].vpeer, a_DB7[0].soma.v(0.5)")
        h("setpointer syn_NC_AVBL_DB7_Generic_GJ_AVBL_to_DB7_elec_syn_13conns_B[0].vpeer, a_AVBL[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_AVBR_AVBL_Generic_GJ
        print("Adding electrical projection: NC_AVBR_AVBL_Generic_GJ from AVBR to AVBL, with 1 connection(s)")

        #h("objectvar syn_NC_AVBR_AVBL_Generic_GJ_neuron_to_neuron_elec_syn_17conns_A[1]")
        h("objectvar syn_NC_AVBR_AVBL_Generic_GJ_neuron_to_neuron_elec_syn_17conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVBR[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVBL[0].soma], weight: 1.0
        #h("a_AVBR[0].soma { syn_NC_AVBR_AVBL_Generic_GJ_neuron_to_neuron_elec_syn_17conns_A[0] = new neuron_to_neuron_elec_syn_17conns(0.5) }")
        h("a_AVBL[0].soma { syn_NC_AVBR_AVBL_Generic_GJ_neuron_to_neuron_elec_syn_17conns_B[0] = new neuron_to_neuron_elec_syn_17conns(0.5) }")
        #h("setpointer syn_NC_AVBR_AVBL_Generic_GJ_neuron_to_neuron_elec_syn_17conns_A[0].vpeer, a_AVBL[0].soma.v(0.5)")
        h("setpointer syn_NC_AVBR_AVBL_Generic_GJ_neuron_to_neuron_elec_syn_17conns_B[0].vpeer, a_AVBR[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_AVBR_DB1_Generic_GJ
        print("Adding electrical projection: NC_AVBR_DB1_Generic_GJ from AVBR to DB1, with 1 connection(s)")

        #h("objectvar syn_NC_AVBR_DB1_Generic_GJ_AVBR_to_DB1_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_AVBR_DB1_Generic_GJ_AVBR_to_DB1_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVBR[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DB1[0].soma], weight: 1.0
        #h("a_AVBR[0].soma { syn_NC_AVBR_DB1_Generic_GJ_AVBR_to_DB1_elec_syn_15conns_A[0] = new AVBR_to_DB1_elec_syn_15conns(0.5) }")
        h("a_DB1[0].soma { syn_NC_AVBR_DB1_Generic_GJ_AVBR_to_DB1_elec_syn_15conns_B[0] = new AVBR_to_DB1_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_AVBR_DB1_Generic_GJ_AVBR_to_DB1_elec_syn_15conns_A[0].vpeer, a_DB1[0].soma.v(0.5)")
        h("setpointer syn_NC_AVBR_DB1_Generic_GJ_AVBR_to_DB1_elec_syn_15conns_B[0].vpeer, a_AVBR[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_AVBR_DB2_Generic_GJ
        print("Adding electrical projection: NC_AVBR_DB2_Generic_GJ from AVBR to DB2, with 1 connection(s)")

        #h("objectvar syn_NC_AVBR_DB2_Generic_GJ_AVBR_to_DB2_elec_syn_3conns_A[1]")
        h("objectvar syn_NC_AVBR_DB2_Generic_GJ_AVBR_to_DB2_elec_syn_3conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVBR[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DB2[0].soma], weight: 1.0
        #h("a_AVBR[0].soma { syn_NC_AVBR_DB2_Generic_GJ_AVBR_to_DB2_elec_syn_3conns_A[0] = new AVBR_to_DB2_elec_syn_3conns(0.5) }")
        h("a_DB2[0].soma { syn_NC_AVBR_DB2_Generic_GJ_AVBR_to_DB2_elec_syn_3conns_B[0] = new AVBR_to_DB2_elec_syn_3conns(0.5) }")
        #h("setpointer syn_NC_AVBR_DB2_Generic_GJ_AVBR_to_DB2_elec_syn_3conns_A[0].vpeer, a_DB2[0].soma.v(0.5)")
        h("setpointer syn_NC_AVBR_DB2_Generic_GJ_AVBR_to_DB2_elec_syn_3conns_B[0].vpeer, a_AVBR[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_AVBR_DB3_Generic_GJ
        print("Adding electrical projection: NC_AVBR_DB3_Generic_GJ from AVBR to DB3, with 1 connection(s)")

        #h("objectvar syn_NC_AVBR_DB3_Generic_GJ_AVBR_to_DB3_elec_syn_2conns_A[1]")
        h("objectvar syn_NC_AVBR_DB3_Generic_GJ_AVBR_to_DB3_elec_syn_2conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVBR[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DB3[0].soma], weight: 1.0
        #h("a_AVBR[0].soma { syn_NC_AVBR_DB3_Generic_GJ_AVBR_to_DB3_elec_syn_2conns_A[0] = new AVBR_to_DB3_elec_syn_2conns(0.5) }")
        h("a_DB3[0].soma { syn_NC_AVBR_DB3_Generic_GJ_AVBR_to_DB3_elec_syn_2conns_B[0] = new AVBR_to_DB3_elec_syn_2conns(0.5) }")
        #h("setpointer syn_NC_AVBR_DB3_Generic_GJ_AVBR_to_DB3_elec_syn_2conns_A[0].vpeer, a_DB3[0].soma.v(0.5)")
        h("setpointer syn_NC_AVBR_DB3_Generic_GJ_AVBR_to_DB3_elec_syn_2conns_B[0].vpeer, a_AVBR[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_AVBR_DB4_Generic_GJ
        print("Adding electrical projection: NC_AVBR_DB4_Generic_GJ from AVBR to DB4, with 1 connection(s)")

        #h("objectvar syn_NC_AVBR_DB4_Generic_GJ_AVBR_to_DB4_elec_syn_5conns_A[1]")
        h("objectvar syn_NC_AVBR_DB4_Generic_GJ_AVBR_to_DB4_elec_syn_5conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVBR[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DB4[0].soma], weight: 1.0
        #h("a_AVBR[0].soma { syn_NC_AVBR_DB4_Generic_GJ_AVBR_to_DB4_elec_syn_5conns_A[0] = new AVBR_to_DB4_elec_syn_5conns(0.5) }")
        h("a_DB4[0].soma { syn_NC_AVBR_DB4_Generic_GJ_AVBR_to_DB4_elec_syn_5conns_B[0] = new AVBR_to_DB4_elec_syn_5conns(0.5) }")
        #h("setpointer syn_NC_AVBR_DB4_Generic_GJ_AVBR_to_DB4_elec_syn_5conns_A[0].vpeer, a_DB4[0].soma.v(0.5)")
        h("setpointer syn_NC_AVBR_DB4_Generic_GJ_AVBR_to_DB4_elec_syn_5conns_B[0].vpeer, a_AVBR[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_AVBR_DB5_Generic_GJ
        print("Adding electrical projection: NC_AVBR_DB5_Generic_GJ from AVBR to DB5, with 1 connection(s)")

        #h("objectvar syn_NC_AVBR_DB5_Generic_GJ_AVBR_to_DB5_elec_syn_4conns_A[1]")
        h("objectvar syn_NC_AVBR_DB5_Generic_GJ_AVBR_to_DB5_elec_syn_4conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVBR[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DB5[0].soma], weight: 1.0
        #h("a_AVBR[0].soma { syn_NC_AVBR_DB5_Generic_GJ_AVBR_to_DB5_elec_syn_4conns_A[0] = new AVBR_to_DB5_elec_syn_4conns(0.5) }")
        h("a_DB5[0].soma { syn_NC_AVBR_DB5_Generic_GJ_AVBR_to_DB5_elec_syn_4conns_B[0] = new AVBR_to_DB5_elec_syn_4conns(0.5) }")
        #h("setpointer syn_NC_AVBR_DB5_Generic_GJ_AVBR_to_DB5_elec_syn_4conns_A[0].vpeer, a_DB5[0].soma.v(0.5)")
        h("setpointer syn_NC_AVBR_DB5_Generic_GJ_AVBR_to_DB5_elec_syn_4conns_B[0].vpeer, a_AVBR[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_AVBR_DB6_Generic_GJ
        print("Adding electrical projection: NC_AVBR_DB6_Generic_GJ from AVBR to DB6, with 1 connection(s)")

        #h("objectvar syn_NC_AVBR_DB6_Generic_GJ_AVBR_to_DB6_elec_syn_3conns_A[1]")
        h("objectvar syn_NC_AVBR_DB6_Generic_GJ_AVBR_to_DB6_elec_syn_3conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVBR[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DB6[0].soma], weight: 1.0
        #h("a_AVBR[0].soma { syn_NC_AVBR_DB6_Generic_GJ_AVBR_to_DB6_elec_syn_3conns_A[0] = new AVBR_to_DB6_elec_syn_3conns(0.5) }")
        h("a_DB6[0].soma { syn_NC_AVBR_DB6_Generic_GJ_AVBR_to_DB6_elec_syn_3conns_B[0] = new AVBR_to_DB6_elec_syn_3conns(0.5) }")
        #h("setpointer syn_NC_AVBR_DB6_Generic_GJ_AVBR_to_DB6_elec_syn_3conns_A[0].vpeer, a_DB6[0].soma.v(0.5)")
        h("setpointer syn_NC_AVBR_DB6_Generic_GJ_AVBR_to_DB6_elec_syn_3conns_B[0].vpeer, a_AVBR[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_AVBR_DB7_Generic_GJ
        print("Adding electrical projection: NC_AVBR_DB7_Generic_GJ from AVBR to DB7, with 1 connection(s)")

        #h("objectvar syn_NC_AVBR_DB7_Generic_GJ_AVBR_to_DB7_elec_syn_3conns_A[1]")
        h("objectvar syn_NC_AVBR_DB7_Generic_GJ_AVBR_to_DB7_elec_syn_3conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVBR[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DB7[0].soma], weight: 1.0
        #h("a_AVBR[0].soma { syn_NC_AVBR_DB7_Generic_GJ_AVBR_to_DB7_elec_syn_3conns_A[0] = new AVBR_to_DB7_elec_syn_3conns(0.5) }")
        h("a_DB7[0].soma { syn_NC_AVBR_DB7_Generic_GJ_AVBR_to_DB7_elec_syn_3conns_B[0] = new AVBR_to_DB7_elec_syn_3conns(0.5) }")
        #h("setpointer syn_NC_AVBR_DB7_Generic_GJ_AVBR_to_DB7_elec_syn_3conns_A[0].vpeer, a_DB7[0].soma.v(0.5)")
        h("setpointer syn_NC_AVBR_DB7_Generic_GJ_AVBR_to_DB7_elec_syn_3conns_B[0].vpeer, a_AVBR[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_DB1_AVBR_Generic_GJ
        print("Adding electrical projection: NC_DB1_AVBR_Generic_GJ from DB1 to AVBR, with 1 connection(s)")

        #h("objectvar syn_NC_DB1_AVBR_Generic_GJ_DB1_to_AVBR_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_DB1_AVBR_Generic_GJ_DB1_to_AVBR_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB1[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVBR[0].soma], weight: 1.0
        #h("a_DB1[0].soma { syn_NC_DB1_AVBR_Generic_GJ_DB1_to_AVBR_elec_syn_15conns_A[0] = new DB1_to_AVBR_elec_syn_15conns(0.5) }")
        h("a_AVBR[0].soma { syn_NC_DB1_AVBR_Generic_GJ_DB1_to_AVBR_elec_syn_15conns_B[0] = new DB1_to_AVBR_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_DB1_AVBR_Generic_GJ_DB1_to_AVBR_elec_syn_15conns_A[0].vpeer, a_AVBR[0].soma.v(0.5)")
        h("setpointer syn_NC_DB1_AVBR_Generic_GJ_DB1_to_AVBR_elec_syn_15conns_B[0].vpeer, a_DB1[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_DB1_DB2_Generic_GJ
        print("Adding electrical projection: NC_DB1_DB2_Generic_GJ from DB1 to DB2, with 1 connection(s)")

        #h("objectvar syn_NC_DB1_DB2_Generic_GJ_DB1_to_DB2_elec_syn_5conns_A[1]")
        h("objectvar syn_NC_DB1_DB2_Generic_GJ_DB1_to_DB2_elec_syn_5conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB1[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DB2[0].soma], weight: 1.0
        #h("a_DB1[0].soma { syn_NC_DB1_DB2_Generic_GJ_DB1_to_DB2_elec_syn_5conns_A[0] = new DB1_to_DB2_elec_syn_5conns(0.5) }")
        h("a_DB2[0].soma { syn_NC_DB1_DB2_Generic_GJ_DB1_to_DB2_elec_syn_5conns_B[0] = new DB1_to_DB2_elec_syn_5conns(0.5) }")
        #h("setpointer syn_NC_DB1_DB2_Generic_GJ_DB1_to_DB2_elec_syn_5conns_A[0].vpeer, a_DB2[0].soma.v(0.5)")
        h("setpointer syn_NC_DB1_DB2_Generic_GJ_DB1_to_DB2_elec_syn_5conns_B[0].vpeer, a_DB1[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_DB2_AVBL_Generic_GJ
        print("Adding electrical projection: NC_DB2_AVBL_Generic_GJ from DB2 to AVBL, with 1 connection(s)")

        #h("objectvar syn_NC_DB2_AVBL_Generic_GJ_DB2_to_AVBL_elec_syn_4conns_A[1]")
        h("objectvar syn_NC_DB2_AVBL_Generic_GJ_DB2_to_AVBL_elec_syn_4conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB2[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVBL[0].soma], weight: 1.0
        #h("a_DB2[0].soma { syn_NC_DB2_AVBL_Generic_GJ_DB2_to_AVBL_elec_syn_4conns_A[0] = new DB2_to_AVBL_elec_syn_4conns(0.5) }")
        h("a_AVBL[0].soma { syn_NC_DB2_AVBL_Generic_GJ_DB2_to_AVBL_elec_syn_4conns_B[0] = new DB2_to_AVBL_elec_syn_4conns(0.5) }")
        #h("setpointer syn_NC_DB2_AVBL_Generic_GJ_DB2_to_AVBL_elec_syn_4conns_A[0].vpeer, a_AVBL[0].soma.v(0.5)")
        h("setpointer syn_NC_DB2_AVBL_Generic_GJ_DB2_to_AVBL_elec_syn_4conns_B[0].vpeer, a_DB2[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_DB2_AVBR_Generic_GJ
        print("Adding electrical projection: NC_DB2_AVBR_Generic_GJ from DB2 to AVBR, with 1 connection(s)")

        #h("objectvar syn_NC_DB2_AVBR_Generic_GJ_DB2_to_AVBR_elec_syn_3conns_A[1]")
        h("objectvar syn_NC_DB2_AVBR_Generic_GJ_DB2_to_AVBR_elec_syn_3conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB2[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVBR[0].soma], weight: 1.0
        #h("a_DB2[0].soma { syn_NC_DB2_AVBR_Generic_GJ_DB2_to_AVBR_elec_syn_3conns_A[0] = new DB2_to_AVBR_elec_syn_3conns(0.5) }")
        h("a_AVBR[0].soma { syn_NC_DB2_AVBR_Generic_GJ_DB2_to_AVBR_elec_syn_3conns_B[0] = new DB2_to_AVBR_elec_syn_3conns(0.5) }")
        #h("setpointer syn_NC_DB2_AVBR_Generic_GJ_DB2_to_AVBR_elec_syn_3conns_A[0].vpeer, a_AVBR[0].soma.v(0.5)")
        h("setpointer syn_NC_DB2_AVBR_Generic_GJ_DB2_to_AVBR_elec_syn_3conns_B[0].vpeer, a_DB2[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_DB2_DB1_Generic_GJ
        print("Adding electrical projection: NC_DB2_DB1_Generic_GJ from DB2 to DB1, with 1 connection(s)")

        #h("objectvar syn_NC_DB2_DB1_Generic_GJ_DB2_to_DB1_elec_syn_5conns_A[1]")
        h("objectvar syn_NC_DB2_DB1_Generic_GJ_DB2_to_DB1_elec_syn_5conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB2[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DB1[0].soma], weight: 1.0
        #h("a_DB2[0].soma { syn_NC_DB2_DB1_Generic_GJ_DB2_to_DB1_elec_syn_5conns_A[0] = new DB2_to_DB1_elec_syn_5conns(0.5) }")
        h("a_DB1[0].soma { syn_NC_DB2_DB1_Generic_GJ_DB2_to_DB1_elec_syn_5conns_B[0] = new DB2_to_DB1_elec_syn_5conns(0.5) }")
        #h("setpointer syn_NC_DB2_DB1_Generic_GJ_DB2_to_DB1_elec_syn_5conns_A[0].vpeer, a_DB1[0].soma.v(0.5)")
        h("setpointer syn_NC_DB2_DB1_Generic_GJ_DB2_to_DB1_elec_syn_5conns_B[0].vpeer, a_DB2[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_DB2_DB3_Generic_GJ
        print("Adding electrical projection: NC_DB2_DB3_Generic_GJ from DB2 to DB3, with 1 connection(s)")

        #h("objectvar syn_NC_DB2_DB3_Generic_GJ_DB2_to_DB3_elec_syn_14conns_A[1]")
        h("objectvar syn_NC_DB2_DB3_Generic_GJ_DB2_to_DB3_elec_syn_14conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB2[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DB3[0].soma], weight: 1.0
        #h("a_DB2[0].soma { syn_NC_DB2_DB3_Generic_GJ_DB2_to_DB3_elec_syn_14conns_A[0] = new DB2_to_DB3_elec_syn_14conns(0.5) }")
        h("a_DB3[0].soma { syn_NC_DB2_DB3_Generic_GJ_DB2_to_DB3_elec_syn_14conns_B[0] = new DB2_to_DB3_elec_syn_14conns(0.5) }")
        #h("setpointer syn_NC_DB2_DB3_Generic_GJ_DB2_to_DB3_elec_syn_14conns_A[0].vpeer, a_DB3[0].soma.v(0.5)")
        h("setpointer syn_NC_DB2_DB3_Generic_GJ_DB2_to_DB3_elec_syn_14conns_B[0].vpeer, a_DB2[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_DB3_AVBL_Generic_GJ
        print("Adding electrical projection: NC_DB3_AVBL_Generic_GJ from DB3 to AVBL, with 1 connection(s)")

        #h("objectvar syn_NC_DB3_AVBL_Generic_GJ_DB3_to_AVBL_elec_syn_9conns_A[1]")
        h("objectvar syn_NC_DB3_AVBL_Generic_GJ_DB3_to_AVBL_elec_syn_9conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB3[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVBL[0].soma], weight: 1.0
        #h("a_DB3[0].soma { syn_NC_DB3_AVBL_Generic_GJ_DB3_to_AVBL_elec_syn_9conns_A[0] = new DB3_to_AVBL_elec_syn_9conns(0.5) }")
        h("a_AVBL[0].soma { syn_NC_DB3_AVBL_Generic_GJ_DB3_to_AVBL_elec_syn_9conns_B[0] = new DB3_to_AVBL_elec_syn_9conns(0.5) }")
        #h("setpointer syn_NC_DB3_AVBL_Generic_GJ_DB3_to_AVBL_elec_syn_9conns_A[0].vpeer, a_AVBL[0].soma.v(0.5)")
        h("setpointer syn_NC_DB3_AVBL_Generic_GJ_DB3_to_AVBL_elec_syn_9conns_B[0].vpeer, a_DB3[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_DB3_AVBR_Generic_GJ
        print("Adding electrical projection: NC_DB3_AVBR_Generic_GJ from DB3 to AVBR, with 1 connection(s)")

        #h("objectvar syn_NC_DB3_AVBR_Generic_GJ_DB3_to_AVBR_elec_syn_2conns_A[1]")
        h("objectvar syn_NC_DB3_AVBR_Generic_GJ_DB3_to_AVBR_elec_syn_2conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB3[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVBR[0].soma], weight: 1.0
        #h("a_DB3[0].soma { syn_NC_DB3_AVBR_Generic_GJ_DB3_to_AVBR_elec_syn_2conns_A[0] = new DB3_to_AVBR_elec_syn_2conns(0.5) }")
        h("a_AVBR[0].soma { syn_NC_DB3_AVBR_Generic_GJ_DB3_to_AVBR_elec_syn_2conns_B[0] = new DB3_to_AVBR_elec_syn_2conns(0.5) }")
        #h("setpointer syn_NC_DB3_AVBR_Generic_GJ_DB3_to_AVBR_elec_syn_2conns_A[0].vpeer, a_AVBR[0].soma.v(0.5)")
        h("setpointer syn_NC_DB3_AVBR_Generic_GJ_DB3_to_AVBR_elec_syn_2conns_B[0].vpeer, a_DB3[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_DB3_DB2_Generic_GJ
        print("Adding electrical projection: NC_DB3_DB2_Generic_GJ from DB3 to DB2, with 1 connection(s)")

        #h("objectvar syn_NC_DB3_DB2_Generic_GJ_DB3_to_DB2_elec_syn_14conns_A[1]")
        h("objectvar syn_NC_DB3_DB2_Generic_GJ_DB3_to_DB2_elec_syn_14conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB3[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DB2[0].soma], weight: 1.0
        #h("a_DB3[0].soma { syn_NC_DB3_DB2_Generic_GJ_DB3_to_DB2_elec_syn_14conns_A[0] = new DB3_to_DB2_elec_syn_14conns(0.5) }")
        h("a_DB2[0].soma { syn_NC_DB3_DB2_Generic_GJ_DB3_to_DB2_elec_syn_14conns_B[0] = new DB3_to_DB2_elec_syn_14conns(0.5) }")
        #h("setpointer syn_NC_DB3_DB2_Generic_GJ_DB3_to_DB2_elec_syn_14conns_A[0].vpeer, a_DB2[0].soma.v(0.5)")
        h("setpointer syn_NC_DB3_DB2_Generic_GJ_DB3_to_DB2_elec_syn_14conns_B[0].vpeer, a_DB3[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_DB3_DB4_Generic_GJ
        print("Adding electrical projection: NC_DB3_DB4_Generic_GJ from DB3 to DB4, with 1 connection(s)")

        #h("objectvar syn_NC_DB3_DB4_Generic_GJ_DB3_to_DB4_elec_syn_1conns_A[1]")
        h("objectvar syn_NC_DB3_DB4_Generic_GJ_DB3_to_DB4_elec_syn_1conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB3[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DB4[0].soma], weight: 1.0
        #h("a_DB3[0].soma { syn_NC_DB3_DB4_Generic_GJ_DB3_to_DB4_elec_syn_1conns_A[0] = new DB3_to_DB4_elec_syn_1conns(0.5) }")
        h("a_DB4[0].soma { syn_NC_DB3_DB4_Generic_GJ_DB3_to_DB4_elec_syn_1conns_B[0] = new DB3_to_DB4_elec_syn_1conns(0.5) }")
        #h("setpointer syn_NC_DB3_DB4_Generic_GJ_DB3_to_DB4_elec_syn_1conns_A[0].vpeer, a_DB4[0].soma.v(0.5)")
        h("setpointer syn_NC_DB3_DB4_Generic_GJ_DB3_to_DB4_elec_syn_1conns_B[0].vpeer, a_DB3[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_DB4_AVBL_Generic_GJ
        print("Adding electrical projection: NC_DB4_AVBL_Generic_GJ from DB4 to AVBL, with 1 connection(s)")

        #h("objectvar syn_NC_DB4_AVBL_Generic_GJ_DB4_to_AVBL_elec_syn_4conns_A[1]")
        h("objectvar syn_NC_DB4_AVBL_Generic_GJ_DB4_to_AVBL_elec_syn_4conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB4[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVBL[0].soma], weight: 1.0
        #h("a_DB4[0].soma { syn_NC_DB4_AVBL_Generic_GJ_DB4_to_AVBL_elec_syn_4conns_A[0] = new DB4_to_AVBL_elec_syn_4conns(0.5) }")
        h("a_AVBL[0].soma { syn_NC_DB4_AVBL_Generic_GJ_DB4_to_AVBL_elec_syn_4conns_B[0] = new DB4_to_AVBL_elec_syn_4conns(0.5) }")
        #h("setpointer syn_NC_DB4_AVBL_Generic_GJ_DB4_to_AVBL_elec_syn_4conns_A[0].vpeer, a_AVBL[0].soma.v(0.5)")
        h("setpointer syn_NC_DB4_AVBL_Generic_GJ_DB4_to_AVBL_elec_syn_4conns_B[0].vpeer, a_DB4[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_DB4_AVBR_Generic_GJ
        print("Adding electrical projection: NC_DB4_AVBR_Generic_GJ from DB4 to AVBR, with 1 connection(s)")

        #h("objectvar syn_NC_DB4_AVBR_Generic_GJ_DB4_to_AVBR_elec_syn_5conns_A[1]")
        h("objectvar syn_NC_DB4_AVBR_Generic_GJ_DB4_to_AVBR_elec_syn_5conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB4[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVBR[0].soma], weight: 1.0
        #h("a_DB4[0].soma { syn_NC_DB4_AVBR_Generic_GJ_DB4_to_AVBR_elec_syn_5conns_A[0] = new DB4_to_AVBR_elec_syn_5conns(0.5) }")
        h("a_AVBR[0].soma { syn_NC_DB4_AVBR_Generic_GJ_DB4_to_AVBR_elec_syn_5conns_B[0] = new DB4_to_AVBR_elec_syn_5conns(0.5) }")
        #h("setpointer syn_NC_DB4_AVBR_Generic_GJ_DB4_to_AVBR_elec_syn_5conns_A[0].vpeer, a_AVBR[0].soma.v(0.5)")
        h("setpointer syn_NC_DB4_AVBR_Generic_GJ_DB4_to_AVBR_elec_syn_5conns_B[0].vpeer, a_DB4[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_DB4_DB3_Generic_GJ
        print("Adding electrical projection: NC_DB4_DB3_Generic_GJ from DB4 to DB3, with 1 connection(s)")

        #h("objectvar syn_NC_DB4_DB3_Generic_GJ_DB4_to_DB3_elec_syn_1conns_A[1]")
        h("objectvar syn_NC_DB4_DB3_Generic_GJ_DB4_to_DB3_elec_syn_1conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB4[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DB3[0].soma], weight: 1.0
        #h("a_DB4[0].soma { syn_NC_DB4_DB3_Generic_GJ_DB4_to_DB3_elec_syn_1conns_A[0] = new DB4_to_DB3_elec_syn_1conns(0.5) }")
        h("a_DB3[0].soma { syn_NC_DB4_DB3_Generic_GJ_DB4_to_DB3_elec_syn_1conns_B[0] = new DB4_to_DB3_elec_syn_1conns(0.5) }")
        #h("setpointer syn_NC_DB4_DB3_Generic_GJ_DB4_to_DB3_elec_syn_1conns_A[0].vpeer, a_DB3[0].soma.v(0.5)")
        h("setpointer syn_NC_DB4_DB3_Generic_GJ_DB4_to_DB3_elec_syn_1conns_B[0].vpeer, a_DB4[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_DB4_DB5_Generic_GJ
        print("Adding electrical projection: NC_DB4_DB5_Generic_GJ from DB4 to DB5, with 1 connection(s)")

        #h("objectvar syn_NC_DB4_DB5_Generic_GJ_DB4_to_DB5_elec_syn_5conns_A[1]")
        h("objectvar syn_NC_DB4_DB5_Generic_GJ_DB4_to_DB5_elec_syn_5conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB4[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DB5[0].soma], weight: 1.0
        #h("a_DB4[0].soma { syn_NC_DB4_DB5_Generic_GJ_DB4_to_DB5_elec_syn_5conns_A[0] = new DB4_to_DB5_elec_syn_5conns(0.5) }")
        h("a_DB5[0].soma { syn_NC_DB4_DB5_Generic_GJ_DB4_to_DB5_elec_syn_5conns_B[0] = new DB4_to_DB5_elec_syn_5conns(0.5) }")
        #h("setpointer syn_NC_DB4_DB5_Generic_GJ_DB4_to_DB5_elec_syn_5conns_A[0].vpeer, a_DB5[0].soma.v(0.5)")
        h("setpointer syn_NC_DB4_DB5_Generic_GJ_DB4_to_DB5_elec_syn_5conns_B[0].vpeer, a_DB4[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_DB5_AVBL_Generic_GJ
        print("Adding electrical projection: NC_DB5_AVBL_Generic_GJ from DB5 to AVBL, with 1 connection(s)")

        #h("objectvar syn_NC_DB5_AVBL_Generic_GJ_DB5_to_AVBL_elec_syn_3conns_A[1]")
        h("objectvar syn_NC_DB5_AVBL_Generic_GJ_DB5_to_AVBL_elec_syn_3conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB5[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVBL[0].soma], weight: 1.0
        #h("a_DB5[0].soma { syn_NC_DB5_AVBL_Generic_GJ_DB5_to_AVBL_elec_syn_3conns_A[0] = new DB5_to_AVBL_elec_syn_3conns(0.5) }")
        h("a_AVBL[0].soma { syn_NC_DB5_AVBL_Generic_GJ_DB5_to_AVBL_elec_syn_3conns_B[0] = new DB5_to_AVBL_elec_syn_3conns(0.5) }")
        #h("setpointer syn_NC_DB5_AVBL_Generic_GJ_DB5_to_AVBL_elec_syn_3conns_A[0].vpeer, a_AVBL[0].soma.v(0.5)")
        h("setpointer syn_NC_DB5_AVBL_Generic_GJ_DB5_to_AVBL_elec_syn_3conns_B[0].vpeer, a_DB5[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_DB5_AVBR_Generic_GJ
        print("Adding electrical projection: NC_DB5_AVBR_Generic_GJ from DB5 to AVBR, with 1 connection(s)")

        #h("objectvar syn_NC_DB5_AVBR_Generic_GJ_DB5_to_AVBR_elec_syn_4conns_A[1]")
        h("objectvar syn_NC_DB5_AVBR_Generic_GJ_DB5_to_AVBR_elec_syn_4conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB5[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVBR[0].soma], weight: 1.0
        #h("a_DB5[0].soma { syn_NC_DB5_AVBR_Generic_GJ_DB5_to_AVBR_elec_syn_4conns_A[0] = new DB5_to_AVBR_elec_syn_4conns(0.5) }")
        h("a_AVBR[0].soma { syn_NC_DB5_AVBR_Generic_GJ_DB5_to_AVBR_elec_syn_4conns_B[0] = new DB5_to_AVBR_elec_syn_4conns(0.5) }")
        #h("setpointer syn_NC_DB5_AVBR_Generic_GJ_DB5_to_AVBR_elec_syn_4conns_A[0].vpeer, a_AVBR[0].soma.v(0.5)")
        h("setpointer syn_NC_DB5_AVBR_Generic_GJ_DB5_to_AVBR_elec_syn_4conns_B[0].vpeer, a_DB5[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_DB5_DB4_Generic_GJ
        print("Adding electrical projection: NC_DB5_DB4_Generic_GJ from DB5 to DB4, with 1 connection(s)")

        #h("objectvar syn_NC_DB5_DB4_Generic_GJ_DB5_to_DB4_elec_syn_5conns_A[1]")
        h("objectvar syn_NC_DB5_DB4_Generic_GJ_DB5_to_DB4_elec_syn_5conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB5[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DB4[0].soma], weight: 1.0
        #h("a_DB5[0].soma { syn_NC_DB5_DB4_Generic_GJ_DB5_to_DB4_elec_syn_5conns_A[0] = new DB5_to_DB4_elec_syn_5conns(0.5) }")
        h("a_DB4[0].soma { syn_NC_DB5_DB4_Generic_GJ_DB5_to_DB4_elec_syn_5conns_B[0] = new DB5_to_DB4_elec_syn_5conns(0.5) }")
        #h("setpointer syn_NC_DB5_DB4_Generic_GJ_DB5_to_DB4_elec_syn_5conns_A[0].vpeer, a_DB4[0].soma.v(0.5)")
        h("setpointer syn_NC_DB5_DB4_Generic_GJ_DB5_to_DB4_elec_syn_5conns_B[0].vpeer, a_DB5[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_DB5_DB6_Generic_GJ
        print("Adding electrical projection: NC_DB5_DB6_Generic_GJ from DB5 to DB6, with 1 connection(s)")

        #h("objectvar syn_NC_DB5_DB6_Generic_GJ_DB5_to_DB6_elec_syn_5conns_A[1]")
        h("objectvar syn_NC_DB5_DB6_Generic_GJ_DB5_to_DB6_elec_syn_5conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB5[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DB6[0].soma], weight: 1.0
        #h("a_DB5[0].soma { syn_NC_DB5_DB6_Generic_GJ_DB5_to_DB6_elec_syn_5conns_A[0] = new DB5_to_DB6_elec_syn_5conns(0.5) }")
        h("a_DB6[0].soma { syn_NC_DB5_DB6_Generic_GJ_DB5_to_DB6_elec_syn_5conns_B[0] = new DB5_to_DB6_elec_syn_5conns(0.5) }")
        #h("setpointer syn_NC_DB5_DB6_Generic_GJ_DB5_to_DB6_elec_syn_5conns_A[0].vpeer, a_DB6[0].soma.v(0.5)")
        h("setpointer syn_NC_DB5_DB6_Generic_GJ_DB5_to_DB6_elec_syn_5conns_B[0].vpeer, a_DB5[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_DB6_AVBL_Generic_GJ
        print("Adding electrical projection: NC_DB6_AVBL_Generic_GJ from DB6 to AVBL, with 1 connection(s)")

        #h("objectvar syn_NC_DB6_AVBL_Generic_GJ_DB6_to_AVBL_elec_syn_3conns_A[1]")
        h("objectvar syn_NC_DB6_AVBL_Generic_GJ_DB6_to_AVBL_elec_syn_3conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB6[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVBL[0].soma], weight: 1.0
        #h("a_DB6[0].soma { syn_NC_DB6_AVBL_Generic_GJ_DB6_to_AVBL_elec_syn_3conns_A[0] = new DB6_to_AVBL_elec_syn_3conns(0.5) }")
        h("a_AVBL[0].soma { syn_NC_DB6_AVBL_Generic_GJ_DB6_to_AVBL_elec_syn_3conns_B[0] = new DB6_to_AVBL_elec_syn_3conns(0.5) }")
        #h("setpointer syn_NC_DB6_AVBL_Generic_GJ_DB6_to_AVBL_elec_syn_3conns_A[0].vpeer, a_AVBL[0].soma.v(0.5)")
        h("setpointer syn_NC_DB6_AVBL_Generic_GJ_DB6_to_AVBL_elec_syn_3conns_B[0].vpeer, a_DB6[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_DB6_AVBR_Generic_GJ
        print("Adding electrical projection: NC_DB6_AVBR_Generic_GJ from DB6 to AVBR, with 1 connection(s)")

        #h("objectvar syn_NC_DB6_AVBR_Generic_GJ_DB6_to_AVBR_elec_syn_4conns_A[1]")
        h("objectvar syn_NC_DB6_AVBR_Generic_GJ_DB6_to_AVBR_elec_syn_4conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB6[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVBR[0].soma], weight: 1.0
        #h("a_DB6[0].soma { syn_NC_DB6_AVBR_Generic_GJ_DB6_to_AVBR_elec_syn_4conns_A[0] = new DB6_to_AVBR_elec_syn_4conns(0.5) }")
        h("a_AVBR[0].soma { syn_NC_DB6_AVBR_Generic_GJ_DB6_to_AVBR_elec_syn_4conns_B[0] = new DB6_to_AVBR_elec_syn_4conns(0.5) }")
        #h("setpointer syn_NC_DB6_AVBR_Generic_GJ_DB6_to_AVBR_elec_syn_4conns_A[0].vpeer, a_AVBR[0].soma.v(0.5)")
        h("setpointer syn_NC_DB6_AVBR_Generic_GJ_DB6_to_AVBR_elec_syn_4conns_B[0].vpeer, a_DB6[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_DB6_DB5_Generic_GJ
        print("Adding electrical projection: NC_DB6_DB5_Generic_GJ from DB6 to DB5, with 1 connection(s)")

        #h("objectvar syn_NC_DB6_DB5_Generic_GJ_DB6_to_DB5_elec_syn_5conns_A[1]")
        h("objectvar syn_NC_DB6_DB5_Generic_GJ_DB6_to_DB5_elec_syn_5conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB6[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DB5[0].soma], weight: 1.0
        #h("a_DB6[0].soma { syn_NC_DB6_DB5_Generic_GJ_DB6_to_DB5_elec_syn_5conns_A[0] = new DB6_to_DB5_elec_syn_5conns(0.5) }")
        h("a_DB5[0].soma { syn_NC_DB6_DB5_Generic_GJ_DB6_to_DB5_elec_syn_5conns_B[0] = new DB6_to_DB5_elec_syn_5conns(0.5) }")
        #h("setpointer syn_NC_DB6_DB5_Generic_GJ_DB6_to_DB5_elec_syn_5conns_A[0].vpeer, a_DB5[0].soma.v(0.5)")
        h("setpointer syn_NC_DB6_DB5_Generic_GJ_DB6_to_DB5_elec_syn_5conns_B[0].vpeer, a_DB6[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_DB6_DB7_Generic_GJ
        print("Adding electrical projection: NC_DB6_DB7_Generic_GJ from DB6 to DB7, with 1 connection(s)")

        #h("objectvar syn_NC_DB6_DB7_Generic_GJ_DB6_to_DB7_elec_syn_5conns_A[1]")
        h("objectvar syn_NC_DB6_DB7_Generic_GJ_DB6_to_DB7_elec_syn_5conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB6[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DB7[0].soma], weight: 1.0
        #h("a_DB6[0].soma { syn_NC_DB6_DB7_Generic_GJ_DB6_to_DB7_elec_syn_5conns_A[0] = new DB6_to_DB7_elec_syn_5conns(0.5) }")
        h("a_DB7[0].soma { syn_NC_DB6_DB7_Generic_GJ_DB6_to_DB7_elec_syn_5conns_B[0] = new DB6_to_DB7_elec_syn_5conns(0.5) }")
        #h("setpointer syn_NC_DB6_DB7_Generic_GJ_DB6_to_DB7_elec_syn_5conns_A[0].vpeer, a_DB7[0].soma.v(0.5)")
        h("setpointer syn_NC_DB6_DB7_Generic_GJ_DB6_to_DB7_elec_syn_5conns_B[0].vpeer, a_DB6[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_DB7_AVBL_Generic_GJ
        print("Adding electrical projection: NC_DB7_AVBL_Generic_GJ from DB7 to AVBL, with 1 connection(s)")

        #h("objectvar syn_NC_DB7_AVBL_Generic_GJ_DB7_to_AVBL_elec_syn_13conns_A[1]")
        h("objectvar syn_NC_DB7_AVBL_Generic_GJ_DB7_to_AVBL_elec_syn_13conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB7[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVBL[0].soma], weight: 1.0
        #h("a_DB7[0].soma { syn_NC_DB7_AVBL_Generic_GJ_DB7_to_AVBL_elec_syn_13conns_A[0] = new DB7_to_AVBL_elec_syn_13conns(0.5) }")
        h("a_AVBL[0].soma { syn_NC_DB7_AVBL_Generic_GJ_DB7_to_AVBL_elec_syn_13conns_B[0] = new DB7_to_AVBL_elec_syn_13conns(0.5) }")
        #h("setpointer syn_NC_DB7_AVBL_Generic_GJ_DB7_to_AVBL_elec_syn_13conns_A[0].vpeer, a_AVBL[0].soma.v(0.5)")
        h("setpointer syn_NC_DB7_AVBL_Generic_GJ_DB7_to_AVBL_elec_syn_13conns_B[0].vpeer, a_DB7[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_DB7_AVBR_Generic_GJ
        print("Adding electrical projection: NC_DB7_AVBR_Generic_GJ from DB7 to AVBR, with 1 connection(s)")

        #h("objectvar syn_NC_DB7_AVBR_Generic_GJ_DB7_to_AVBR_elec_syn_3conns_A[1]")
        h("objectvar syn_NC_DB7_AVBR_Generic_GJ_DB7_to_AVBR_elec_syn_3conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB7[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVBR[0].soma], weight: 1.0
        #h("a_DB7[0].soma { syn_NC_DB7_AVBR_Generic_GJ_DB7_to_AVBR_elec_syn_3conns_A[0] = new DB7_to_AVBR_elec_syn_3conns(0.5) }")
        h("a_AVBR[0].soma { syn_NC_DB7_AVBR_Generic_GJ_DB7_to_AVBR_elec_syn_3conns_B[0] = new DB7_to_AVBR_elec_syn_3conns(0.5) }")
        #h("setpointer syn_NC_DB7_AVBR_Generic_GJ_DB7_to_AVBR_elec_syn_3conns_A[0].vpeer, a_AVBR[0].soma.v(0.5)")
        h("setpointer syn_NC_DB7_AVBR_Generic_GJ_DB7_to_AVBR_elec_syn_3conns_B[0].vpeer, a_DB7[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_DB7_DB6_Generic_GJ
        print("Adding electrical projection: NC_DB7_DB6_Generic_GJ from DB7 to DB6, with 1 connection(s)")

        #h("objectvar syn_NC_DB7_DB6_Generic_GJ_DB7_to_DB6_elec_syn_5conns_A[1]")
        h("objectvar syn_NC_DB7_DB6_Generic_GJ_DB7_to_DB6_elec_syn_5conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB7[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DB6[0].soma], weight: 1.0
        #h("a_DB7[0].soma { syn_NC_DB7_DB6_Generic_GJ_DB7_to_DB6_elec_syn_5conns_A[0] = new DB7_to_DB6_elec_syn_5conns(0.5) }")
        h("a_DB6[0].soma { syn_NC_DB7_DB6_Generic_GJ_DB7_to_DB6_elec_syn_5conns_B[0] = new DB7_to_DB6_elec_syn_5conns(0.5) }")
        #h("setpointer syn_NC_DB7_DB6_Generic_GJ_DB7_to_DB6_elec_syn_5conns_A[0].vpeer, a_DB6[0].soma.v(0.5)")
        h("setpointer syn_NC_DB7_DB6_Generic_GJ_DB7_to_DB6_elec_syn_5conns_B[0].vpeer, a_DB7[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDL01_MDL02_Generic_GJ
        print("Adding electrical projection: NC_MDL01_MDL02_Generic_GJ from MDL01 to MDL02, with 1 connection(s)")

        #h("objectvar syn_NC_MDL01_MDL02_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDL01_MDL02_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDL01[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL02[0].soma], weight: 1.0
        #h("a_MDL01[0].soma { syn_NC_MDL01_MDL02_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDL02[0].soma { syn_NC_MDL01_MDL02_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDL01_MDL02_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDL02[0].soma.v(0.5)")
        h("setpointer syn_NC_MDL01_MDL02_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDL01[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDL01_MDL03_Generic_GJ
        print("Adding electrical projection: NC_MDL01_MDL03_Generic_GJ from MDL01 to MDL03, with 1 connection(s)")

        #h("objectvar syn_NC_MDL01_MDL03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDL01_MDL03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDL01[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL03[0].soma], weight: 1.0
        #h("a_MDL01[0].soma { syn_NC_MDL01_MDL03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDL03[0].soma { syn_NC_MDL01_MDL03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDL01_MDL03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDL03[0].soma.v(0.5)")
        h("setpointer syn_NC_MDL01_MDL03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDL01[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDL02_MDL01_Generic_GJ
        print("Adding electrical projection: NC_MDL02_MDL01_Generic_GJ from MDL02 to MDL01, with 1 connection(s)")

        #h("objectvar syn_NC_MDL02_MDL01_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDL02_MDL01_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDL02[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL01[0].soma], weight: 1.0
        #h("a_MDL02[0].soma { syn_NC_MDL02_MDL01_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDL01[0].soma { syn_NC_MDL02_MDL01_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDL02_MDL01_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDL01[0].soma.v(0.5)")
        h("setpointer syn_NC_MDL02_MDL01_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDL02[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDL02_MDL03_Generic_GJ
        print("Adding electrical projection: NC_MDL02_MDL03_Generic_GJ from MDL02 to MDL03, with 1 connection(s)")

        #h("objectvar syn_NC_MDL02_MDL03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDL02_MDL03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDL02[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL03[0].soma], weight: 1.0
        #h("a_MDL02[0].soma { syn_NC_MDL02_MDL03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDL03[0].soma { syn_NC_MDL02_MDL03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDL02_MDL03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDL03[0].soma.v(0.5)")
        h("setpointer syn_NC_MDL02_MDL03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDL02[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDL03_MDL01_Generic_GJ
        print("Adding electrical projection: NC_MDL03_MDL01_Generic_GJ from MDL03 to MDL01, with 1 connection(s)")

        #h("objectvar syn_NC_MDL03_MDL01_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDL03_MDL01_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDL03[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL01[0].soma], weight: 1.0
        #h("a_MDL03[0].soma { syn_NC_MDL03_MDL01_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDL01[0].soma { syn_NC_MDL03_MDL01_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDL03_MDL01_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDL01[0].soma.v(0.5)")
        h("setpointer syn_NC_MDL03_MDL01_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDL03[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDL03_MDL02_Generic_GJ
        print("Adding electrical projection: NC_MDL03_MDL02_Generic_GJ from MDL03 to MDL02, with 1 connection(s)")

        #h("objectvar syn_NC_MDL03_MDL02_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDL03_MDL02_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDL03[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL02[0].soma], weight: 1.0
        #h("a_MDL03[0].soma { syn_NC_MDL03_MDL02_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDL02[0].soma { syn_NC_MDL03_MDL02_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDL03_MDL02_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDL02[0].soma.v(0.5)")
        h("setpointer syn_NC_MDL03_MDL02_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDL03[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDL03_MDL04_Generic_GJ
        print("Adding electrical projection: NC_MDL03_MDL04_Generic_GJ from MDL03 to MDL04, with 1 connection(s)")

        #h("objectvar syn_NC_MDL03_MDL04_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDL03_MDL04_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDL03[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL04[0].soma], weight: 1.0
        #h("a_MDL03[0].soma { syn_NC_MDL03_MDL04_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDL04[0].soma { syn_NC_MDL03_MDL04_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDL03_MDL04_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDL04[0].soma.v(0.5)")
        h("setpointer syn_NC_MDL03_MDL04_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDL03[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDL04_MDL03_Generic_GJ
        print("Adding electrical projection: NC_MDL04_MDL03_Generic_GJ from MDL04 to MDL03, with 1 connection(s)")

        #h("objectvar syn_NC_MDL04_MDL03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDL04_MDL03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDL04[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL03[0].soma], weight: 1.0
        #h("a_MDL04[0].soma { syn_NC_MDL04_MDL03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDL03[0].soma { syn_NC_MDL04_MDL03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDL04_MDL03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDL03[0].soma.v(0.5)")
        h("setpointer syn_NC_MDL04_MDL03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDL04[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDL04_MDL05_Generic_GJ
        print("Adding electrical projection: NC_MDL04_MDL05_Generic_GJ from MDL04 to MDL05, with 1 connection(s)")

        #h("objectvar syn_NC_MDL04_MDL05_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDL04_MDL05_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDL04[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL05[0].soma], weight: 1.0
        #h("a_MDL04[0].soma { syn_NC_MDL04_MDL05_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDL05[0].soma { syn_NC_MDL04_MDL05_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDL04_MDL05_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDL05[0].soma.v(0.5)")
        h("setpointer syn_NC_MDL04_MDL05_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDL04[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDL05_MDL04_Generic_GJ
        print("Adding electrical projection: NC_MDL05_MDL04_Generic_GJ from MDL05 to MDL04, with 1 connection(s)")

        #h("objectvar syn_NC_MDL05_MDL04_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDL05_MDL04_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDL05[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL04[0].soma], weight: 1.0
        #h("a_MDL05[0].soma { syn_NC_MDL05_MDL04_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDL04[0].soma { syn_NC_MDL05_MDL04_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDL05_MDL04_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDL04[0].soma.v(0.5)")
        h("setpointer syn_NC_MDL05_MDL04_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDL05[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDL05_MDL06_Generic_GJ
        print("Adding electrical projection: NC_MDL05_MDL06_Generic_GJ from MDL05 to MDL06, with 1 connection(s)")

        #h("objectvar syn_NC_MDL05_MDL06_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDL05_MDL06_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDL05[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL06[0].soma], weight: 1.0
        #h("a_MDL05[0].soma { syn_NC_MDL05_MDL06_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDL06[0].soma { syn_NC_MDL05_MDL06_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDL05_MDL06_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDL06[0].soma.v(0.5)")
        h("setpointer syn_NC_MDL05_MDL06_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDL05[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDL06_MDL05_Generic_GJ
        print("Adding electrical projection: NC_MDL06_MDL05_Generic_GJ from MDL06 to MDL05, with 1 connection(s)")

        #h("objectvar syn_NC_MDL06_MDL05_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDL06_MDL05_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDL06[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL05[0].soma], weight: 1.0
        #h("a_MDL06[0].soma { syn_NC_MDL06_MDL05_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDL05[0].soma { syn_NC_MDL06_MDL05_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDL06_MDL05_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDL05[0].soma.v(0.5)")
        h("setpointer syn_NC_MDL06_MDL05_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDL06[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDL06_MDL07_Generic_GJ
        print("Adding electrical projection: NC_MDL06_MDL07_Generic_GJ from MDL06 to MDL07, with 1 connection(s)")

        #h("objectvar syn_NC_MDL06_MDL07_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDL06_MDL07_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDL06[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL07[0].soma], weight: 1.0
        #h("a_MDL06[0].soma { syn_NC_MDL06_MDL07_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDL07[0].soma { syn_NC_MDL06_MDL07_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDL06_MDL07_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDL07[0].soma.v(0.5)")
        h("setpointer syn_NC_MDL06_MDL07_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDL06[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDL07_MDL06_Generic_GJ
        print("Adding electrical projection: NC_MDL07_MDL06_Generic_GJ from MDL07 to MDL06, with 1 connection(s)")

        #h("objectvar syn_NC_MDL07_MDL06_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDL07_MDL06_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDL07[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL06[0].soma], weight: 1.0
        #h("a_MDL07[0].soma { syn_NC_MDL07_MDL06_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDL06[0].soma { syn_NC_MDL07_MDL06_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDL07_MDL06_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDL06[0].soma.v(0.5)")
        h("setpointer syn_NC_MDL07_MDL06_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDL07[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDL07_MDL08_Generic_GJ
        print("Adding electrical projection: NC_MDL07_MDL08_Generic_GJ from MDL07 to MDL08, with 1 connection(s)")

        #h("objectvar syn_NC_MDL07_MDL08_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDL07_MDL08_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDL07[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL08[0].soma], weight: 1.0
        #h("a_MDL07[0].soma { syn_NC_MDL07_MDL08_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDL08[0].soma { syn_NC_MDL07_MDL08_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDL07_MDL08_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDL08[0].soma.v(0.5)")
        h("setpointer syn_NC_MDL07_MDL08_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDL07[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDL08_MDL07_Generic_GJ
        print("Adding electrical projection: NC_MDL08_MDL07_Generic_GJ from MDL08 to MDL07, with 1 connection(s)")

        #h("objectvar syn_NC_MDL08_MDL07_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDL08_MDL07_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDL08[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL07[0].soma], weight: 1.0
        #h("a_MDL08[0].soma { syn_NC_MDL08_MDL07_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDL07[0].soma { syn_NC_MDL08_MDL07_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDL08_MDL07_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDL07[0].soma.v(0.5)")
        h("setpointer syn_NC_MDL08_MDL07_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDL08[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDL08_MDL09_Generic_GJ
        print("Adding electrical projection: NC_MDL08_MDL09_Generic_GJ from MDL08 to MDL09, with 1 connection(s)")

        #h("objectvar syn_NC_MDL08_MDL09_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDL08_MDL09_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDL08[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL09[0].soma], weight: 1.0
        #h("a_MDL08[0].soma { syn_NC_MDL08_MDL09_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDL09[0].soma { syn_NC_MDL08_MDL09_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDL08_MDL09_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDL09[0].soma.v(0.5)")
        h("setpointer syn_NC_MDL08_MDL09_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDL08[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDL09_MDL08_Generic_GJ
        print("Adding electrical projection: NC_MDL09_MDL08_Generic_GJ from MDL09 to MDL08, with 1 connection(s)")

        #h("objectvar syn_NC_MDL09_MDL08_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDL09_MDL08_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDL09[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL08[0].soma], weight: 1.0
        #h("a_MDL09[0].soma { syn_NC_MDL09_MDL08_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDL08[0].soma { syn_NC_MDL09_MDL08_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDL09_MDL08_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDL08[0].soma.v(0.5)")
        h("setpointer syn_NC_MDL09_MDL08_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDL09[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDL09_MDL10_Generic_GJ
        print("Adding electrical projection: NC_MDL09_MDL10_Generic_GJ from MDL09 to MDL10, with 1 connection(s)")

        #h("objectvar syn_NC_MDL09_MDL10_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDL09_MDL10_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDL09[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL10[0].soma], weight: 1.0
        #h("a_MDL09[0].soma { syn_NC_MDL09_MDL10_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDL10[0].soma { syn_NC_MDL09_MDL10_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDL09_MDL10_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDL10[0].soma.v(0.5)")
        h("setpointer syn_NC_MDL09_MDL10_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDL09[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDL10_MDL09_Generic_GJ
        print("Adding electrical projection: NC_MDL10_MDL09_Generic_GJ from MDL10 to MDL09, with 1 connection(s)")

        #h("objectvar syn_NC_MDL10_MDL09_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDL10_MDL09_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDL10[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL09[0].soma], weight: 1.0
        #h("a_MDL10[0].soma { syn_NC_MDL10_MDL09_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDL09[0].soma { syn_NC_MDL10_MDL09_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDL10_MDL09_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDL09[0].soma.v(0.5)")
        h("setpointer syn_NC_MDL10_MDL09_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDL10[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDL10_MDL11_Generic_GJ
        print("Adding electrical projection: NC_MDL10_MDL11_Generic_GJ from MDL10 to MDL11, with 1 connection(s)")

        #h("objectvar syn_NC_MDL10_MDL11_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDL10_MDL11_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDL10[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL11[0].soma], weight: 1.0
        #h("a_MDL10[0].soma { syn_NC_MDL10_MDL11_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDL11[0].soma { syn_NC_MDL10_MDL11_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDL10_MDL11_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDL11[0].soma.v(0.5)")
        h("setpointer syn_NC_MDL10_MDL11_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDL10[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDL11_MDL10_Generic_GJ
        print("Adding electrical projection: NC_MDL11_MDL10_Generic_GJ from MDL11 to MDL10, with 1 connection(s)")

        #h("objectvar syn_NC_MDL11_MDL10_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDL11_MDL10_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDL11[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL10[0].soma], weight: 1.0
        #h("a_MDL11[0].soma { syn_NC_MDL11_MDL10_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDL10[0].soma { syn_NC_MDL11_MDL10_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDL11_MDL10_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDL10[0].soma.v(0.5)")
        h("setpointer syn_NC_MDL11_MDL10_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDL11[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDL11_MDL12_Generic_GJ
        print("Adding electrical projection: NC_MDL11_MDL12_Generic_GJ from MDL11 to MDL12, with 1 connection(s)")

        #h("objectvar syn_NC_MDL11_MDL12_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDL11_MDL12_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDL11[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL12[0].soma], weight: 1.0
        #h("a_MDL11[0].soma { syn_NC_MDL11_MDL12_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDL12[0].soma { syn_NC_MDL11_MDL12_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDL11_MDL12_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDL12[0].soma.v(0.5)")
        h("setpointer syn_NC_MDL11_MDL12_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDL11[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDL12_MDL11_Generic_GJ
        print("Adding electrical projection: NC_MDL12_MDL11_Generic_GJ from MDL12 to MDL11, with 1 connection(s)")

        #h("objectvar syn_NC_MDL12_MDL11_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDL12_MDL11_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDL12[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL11[0].soma], weight: 1.0
        #h("a_MDL12[0].soma { syn_NC_MDL12_MDL11_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDL11[0].soma { syn_NC_MDL12_MDL11_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDL12_MDL11_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDL11[0].soma.v(0.5)")
        h("setpointer syn_NC_MDL12_MDL11_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDL12[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDL12_MDL13_Generic_GJ
        print("Adding electrical projection: NC_MDL12_MDL13_Generic_GJ from MDL12 to MDL13, with 1 connection(s)")

        #h("objectvar syn_NC_MDL12_MDL13_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDL12_MDL13_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDL12[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL13[0].soma], weight: 1.0
        #h("a_MDL12[0].soma { syn_NC_MDL12_MDL13_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDL13[0].soma { syn_NC_MDL12_MDL13_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDL12_MDL13_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDL13[0].soma.v(0.5)")
        h("setpointer syn_NC_MDL12_MDL13_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDL12[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDL13_MDL12_Generic_GJ
        print("Adding electrical projection: NC_MDL13_MDL12_Generic_GJ from MDL13 to MDL12, with 1 connection(s)")

        #h("objectvar syn_NC_MDL13_MDL12_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDL13_MDL12_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDL13[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL12[0].soma], weight: 1.0
        #h("a_MDL13[0].soma { syn_NC_MDL13_MDL12_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDL12[0].soma { syn_NC_MDL13_MDL12_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDL13_MDL12_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDL12[0].soma.v(0.5)")
        h("setpointer syn_NC_MDL13_MDL12_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDL13[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDL13_MDL14_Generic_GJ
        print("Adding electrical projection: NC_MDL13_MDL14_Generic_GJ from MDL13 to MDL14, with 1 connection(s)")

        #h("objectvar syn_NC_MDL13_MDL14_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDL13_MDL14_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDL13[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL14[0].soma], weight: 1.0
        #h("a_MDL13[0].soma { syn_NC_MDL13_MDL14_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDL14[0].soma { syn_NC_MDL13_MDL14_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDL13_MDL14_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDL14[0].soma.v(0.5)")
        h("setpointer syn_NC_MDL13_MDL14_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDL13[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDL14_MDL13_Generic_GJ
        print("Adding electrical projection: NC_MDL14_MDL13_Generic_GJ from MDL14 to MDL13, with 1 connection(s)")

        #h("objectvar syn_NC_MDL14_MDL13_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDL14_MDL13_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDL14[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL13[0].soma], weight: 1.0
        #h("a_MDL14[0].soma { syn_NC_MDL14_MDL13_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDL13[0].soma { syn_NC_MDL14_MDL13_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDL14_MDL13_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDL13[0].soma.v(0.5)")
        h("setpointer syn_NC_MDL14_MDL13_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDL14[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDL14_MDL15_Generic_GJ
        print("Adding electrical projection: NC_MDL14_MDL15_Generic_GJ from MDL14 to MDL15, with 1 connection(s)")

        #h("objectvar syn_NC_MDL14_MDL15_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDL14_MDL15_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDL14[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL15[0].soma], weight: 1.0
        #h("a_MDL14[0].soma { syn_NC_MDL14_MDL15_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDL15[0].soma { syn_NC_MDL14_MDL15_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDL14_MDL15_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDL15[0].soma.v(0.5)")
        h("setpointer syn_NC_MDL14_MDL15_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDL14[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDL15_MDL14_Generic_GJ
        print("Adding electrical projection: NC_MDL15_MDL14_Generic_GJ from MDL15 to MDL14, with 1 connection(s)")

        #h("objectvar syn_NC_MDL15_MDL14_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDL15_MDL14_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDL15[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL14[0].soma], weight: 1.0
        #h("a_MDL15[0].soma { syn_NC_MDL15_MDL14_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDL14[0].soma { syn_NC_MDL15_MDL14_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDL15_MDL14_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDL14[0].soma.v(0.5)")
        h("setpointer syn_NC_MDL15_MDL14_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDL15[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDL15_MDL16_Generic_GJ
        print("Adding electrical projection: NC_MDL15_MDL16_Generic_GJ from MDL15 to MDL16, with 1 connection(s)")

        #h("objectvar syn_NC_MDL15_MDL16_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDL15_MDL16_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDL15[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL16[0].soma], weight: 1.0
        #h("a_MDL15[0].soma { syn_NC_MDL15_MDL16_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDL16[0].soma { syn_NC_MDL15_MDL16_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDL15_MDL16_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDL16[0].soma.v(0.5)")
        h("setpointer syn_NC_MDL15_MDL16_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDL15[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDL16_MDL15_Generic_GJ
        print("Adding electrical projection: NC_MDL16_MDL15_Generic_GJ from MDL16 to MDL15, with 1 connection(s)")

        #h("objectvar syn_NC_MDL16_MDL15_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDL16_MDL15_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDL16[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL15[0].soma], weight: 1.0
        #h("a_MDL16[0].soma { syn_NC_MDL16_MDL15_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDL15[0].soma { syn_NC_MDL16_MDL15_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDL16_MDL15_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDL15[0].soma.v(0.5)")
        h("setpointer syn_NC_MDL16_MDL15_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDL16[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDL16_MDL17_Generic_GJ
        print("Adding electrical projection: NC_MDL16_MDL17_Generic_GJ from MDL16 to MDL17, with 1 connection(s)")

        #h("objectvar syn_NC_MDL16_MDL17_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDL16_MDL17_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDL16[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL17[0].soma], weight: 1.0
        #h("a_MDL16[0].soma { syn_NC_MDL16_MDL17_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDL17[0].soma { syn_NC_MDL16_MDL17_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDL16_MDL17_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDL17[0].soma.v(0.5)")
        h("setpointer syn_NC_MDL16_MDL17_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDL16[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDL17_MDL16_Generic_GJ
        print("Adding electrical projection: NC_MDL17_MDL16_Generic_GJ from MDL17 to MDL16, with 1 connection(s)")

        #h("objectvar syn_NC_MDL17_MDL16_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDL17_MDL16_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDL17[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL16[0].soma], weight: 1.0
        #h("a_MDL17[0].soma { syn_NC_MDL17_MDL16_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDL16[0].soma { syn_NC_MDL17_MDL16_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDL17_MDL16_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDL16[0].soma.v(0.5)")
        h("setpointer syn_NC_MDL17_MDL16_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDL17[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDL17_MDL18_Generic_GJ
        print("Adding electrical projection: NC_MDL17_MDL18_Generic_GJ from MDL17 to MDL18, with 1 connection(s)")

        #h("objectvar syn_NC_MDL17_MDL18_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDL17_MDL18_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDL17[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL18[0].soma], weight: 1.0
        #h("a_MDL17[0].soma { syn_NC_MDL17_MDL18_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDL18[0].soma { syn_NC_MDL17_MDL18_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDL17_MDL18_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDL18[0].soma.v(0.5)")
        h("setpointer syn_NC_MDL17_MDL18_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDL17[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDL18_MDL17_Generic_GJ
        print("Adding electrical projection: NC_MDL18_MDL17_Generic_GJ from MDL18 to MDL17, with 1 connection(s)")

        #h("objectvar syn_NC_MDL18_MDL17_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDL18_MDL17_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDL18[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL17[0].soma], weight: 1.0
        #h("a_MDL18[0].soma { syn_NC_MDL18_MDL17_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDL17[0].soma { syn_NC_MDL18_MDL17_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDL18_MDL17_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDL17[0].soma.v(0.5)")
        h("setpointer syn_NC_MDL18_MDL17_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDL18[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDL18_MDL19_Generic_GJ
        print("Adding electrical projection: NC_MDL18_MDL19_Generic_GJ from MDL18 to MDL19, with 1 connection(s)")

        #h("objectvar syn_NC_MDL18_MDL19_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDL18_MDL19_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDL18[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL19[0].soma], weight: 1.0
        #h("a_MDL18[0].soma { syn_NC_MDL18_MDL19_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDL19[0].soma { syn_NC_MDL18_MDL19_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDL18_MDL19_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDL19[0].soma.v(0.5)")
        h("setpointer syn_NC_MDL18_MDL19_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDL18[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDL19_MDL18_Generic_GJ
        print("Adding electrical projection: NC_MDL19_MDL18_Generic_GJ from MDL19 to MDL18, with 1 connection(s)")

        #h("objectvar syn_NC_MDL19_MDL18_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDL19_MDL18_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDL19[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL18[0].soma], weight: 1.0
        #h("a_MDL19[0].soma { syn_NC_MDL19_MDL18_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDL18[0].soma { syn_NC_MDL19_MDL18_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDL19_MDL18_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDL18[0].soma.v(0.5)")
        h("setpointer syn_NC_MDL19_MDL18_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDL19[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDL19_MDL20_Generic_GJ
        print("Adding electrical projection: NC_MDL19_MDL20_Generic_GJ from MDL19 to MDL20, with 1 connection(s)")

        #h("objectvar syn_NC_MDL19_MDL20_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDL19_MDL20_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDL19[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL20[0].soma], weight: 1.0
        #h("a_MDL19[0].soma { syn_NC_MDL19_MDL20_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDL20[0].soma { syn_NC_MDL19_MDL20_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDL19_MDL20_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDL20[0].soma.v(0.5)")
        h("setpointer syn_NC_MDL19_MDL20_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDL19[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDL20_MDL19_Generic_GJ
        print("Adding electrical projection: NC_MDL20_MDL19_Generic_GJ from MDL20 to MDL19, with 1 connection(s)")

        #h("objectvar syn_NC_MDL20_MDL19_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDL20_MDL19_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDL20[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL19[0].soma], weight: 1.0
        #h("a_MDL20[0].soma { syn_NC_MDL20_MDL19_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDL19[0].soma { syn_NC_MDL20_MDL19_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDL20_MDL19_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDL19[0].soma.v(0.5)")
        h("setpointer syn_NC_MDL20_MDL19_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDL20[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDL20_MDL21_Generic_GJ
        print("Adding electrical projection: NC_MDL20_MDL21_Generic_GJ from MDL20 to MDL21, with 1 connection(s)")

        #h("objectvar syn_NC_MDL20_MDL21_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDL20_MDL21_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDL20[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL21[0].soma], weight: 1.0
        #h("a_MDL20[0].soma { syn_NC_MDL20_MDL21_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDL21[0].soma { syn_NC_MDL20_MDL21_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDL20_MDL21_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDL21[0].soma.v(0.5)")
        h("setpointer syn_NC_MDL20_MDL21_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDL20[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDL21_MDL20_Generic_GJ
        print("Adding electrical projection: NC_MDL21_MDL20_Generic_GJ from MDL21 to MDL20, with 1 connection(s)")

        #h("objectvar syn_NC_MDL21_MDL20_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDL21_MDL20_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDL21[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL20[0].soma], weight: 1.0
        #h("a_MDL21[0].soma { syn_NC_MDL21_MDL20_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDL20[0].soma { syn_NC_MDL21_MDL20_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDL21_MDL20_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDL20[0].soma.v(0.5)")
        h("setpointer syn_NC_MDL21_MDL20_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDL21[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDL21_MDL22_Generic_GJ
        print("Adding electrical projection: NC_MDL21_MDL22_Generic_GJ from MDL21 to MDL22, with 1 connection(s)")

        #h("objectvar syn_NC_MDL21_MDL22_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDL21_MDL22_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDL21[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL22[0].soma], weight: 1.0
        #h("a_MDL21[0].soma { syn_NC_MDL21_MDL22_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDL22[0].soma { syn_NC_MDL21_MDL22_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDL21_MDL22_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDL22[0].soma.v(0.5)")
        h("setpointer syn_NC_MDL21_MDL22_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDL21[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDL22_MDL21_Generic_GJ
        print("Adding electrical projection: NC_MDL22_MDL21_Generic_GJ from MDL22 to MDL21, with 1 connection(s)")

        #h("objectvar syn_NC_MDL22_MDL21_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDL22_MDL21_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDL22[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL21[0].soma], weight: 1.0
        #h("a_MDL22[0].soma { syn_NC_MDL22_MDL21_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDL21[0].soma { syn_NC_MDL22_MDL21_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDL22_MDL21_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDL21[0].soma.v(0.5)")
        h("setpointer syn_NC_MDL22_MDL21_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDL22[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDL22_MDL23_Generic_GJ
        print("Adding electrical projection: NC_MDL22_MDL23_Generic_GJ from MDL22 to MDL23, with 1 connection(s)")

        #h("objectvar syn_NC_MDL22_MDL23_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDL22_MDL23_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDL22[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL23[0].soma], weight: 1.0
        #h("a_MDL22[0].soma { syn_NC_MDL22_MDL23_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDL23[0].soma { syn_NC_MDL22_MDL23_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDL22_MDL23_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDL23[0].soma.v(0.5)")
        h("setpointer syn_NC_MDL22_MDL23_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDL22[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDL23_MDL22_Generic_GJ
        print("Adding electrical projection: NC_MDL23_MDL22_Generic_GJ from MDL23 to MDL22, with 1 connection(s)")

        #h("objectvar syn_NC_MDL23_MDL22_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDL23_MDL22_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDL23[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL22[0].soma], weight: 1.0
        #h("a_MDL23[0].soma { syn_NC_MDL23_MDL22_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDL22[0].soma { syn_NC_MDL23_MDL22_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDL23_MDL22_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDL22[0].soma.v(0.5)")
        h("setpointer syn_NC_MDL23_MDL22_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDL23[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDL23_MDL24_Generic_GJ
        print("Adding electrical projection: NC_MDL23_MDL24_Generic_GJ from MDL23 to MDL24, with 1 connection(s)")

        #h("objectvar syn_NC_MDL23_MDL24_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDL23_MDL24_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDL23[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL24[0].soma], weight: 1.0
        #h("a_MDL23[0].soma { syn_NC_MDL23_MDL24_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDL24[0].soma { syn_NC_MDL23_MDL24_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDL23_MDL24_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDL24[0].soma.v(0.5)")
        h("setpointer syn_NC_MDL23_MDL24_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDL23[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDL24_MDL23_Generic_GJ
        print("Adding electrical projection: NC_MDL24_MDL23_Generic_GJ from MDL24 to MDL23, with 1 connection(s)")

        #h("objectvar syn_NC_MDL24_MDL23_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDL24_MDL23_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDL24[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL23[0].soma], weight: 1.0
        #h("a_MDL24[0].soma { syn_NC_MDL24_MDL23_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDL23[0].soma { syn_NC_MDL24_MDL23_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDL24_MDL23_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDL23[0].soma.v(0.5)")
        h("setpointer syn_NC_MDL24_MDL23_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDL24[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDR01_MDR02_Generic_GJ
        print("Adding electrical projection: NC_MDR01_MDR02_Generic_GJ from MDR01 to MDR02, with 1 connection(s)")

        #h("objectvar syn_NC_MDR01_MDR02_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDR01_MDR02_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDR01[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR02[0].soma], weight: 1.0
        #h("a_MDR01[0].soma { syn_NC_MDR01_MDR02_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDR02[0].soma { syn_NC_MDR01_MDR02_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDR01_MDR02_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDR02[0].soma.v(0.5)")
        h("setpointer syn_NC_MDR01_MDR02_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDR01[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDR01_MDR03_Generic_GJ
        print("Adding electrical projection: NC_MDR01_MDR03_Generic_GJ from MDR01 to MDR03, with 1 connection(s)")

        #h("objectvar syn_NC_MDR01_MDR03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDR01_MDR03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDR01[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR03[0].soma], weight: 1.0
        #h("a_MDR01[0].soma { syn_NC_MDR01_MDR03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDR03[0].soma { syn_NC_MDR01_MDR03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDR01_MDR03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDR03[0].soma.v(0.5)")
        h("setpointer syn_NC_MDR01_MDR03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDR01[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDR02_MDR01_Generic_GJ
        print("Adding electrical projection: NC_MDR02_MDR01_Generic_GJ from MDR02 to MDR01, with 1 connection(s)")

        #h("objectvar syn_NC_MDR02_MDR01_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDR02_MDR01_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDR02[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR01[0].soma], weight: 1.0
        #h("a_MDR02[0].soma { syn_NC_MDR02_MDR01_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDR01[0].soma { syn_NC_MDR02_MDR01_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDR02_MDR01_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDR01[0].soma.v(0.5)")
        h("setpointer syn_NC_MDR02_MDR01_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDR02[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDR02_MDR03_Generic_GJ
        print("Adding electrical projection: NC_MDR02_MDR03_Generic_GJ from MDR02 to MDR03, with 1 connection(s)")

        #h("objectvar syn_NC_MDR02_MDR03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDR02_MDR03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDR02[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR03[0].soma], weight: 1.0
        #h("a_MDR02[0].soma { syn_NC_MDR02_MDR03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDR03[0].soma { syn_NC_MDR02_MDR03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDR02_MDR03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDR03[0].soma.v(0.5)")
        h("setpointer syn_NC_MDR02_MDR03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDR02[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDR03_MDR01_Generic_GJ
        print("Adding electrical projection: NC_MDR03_MDR01_Generic_GJ from MDR03 to MDR01, with 1 connection(s)")

        #h("objectvar syn_NC_MDR03_MDR01_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDR03_MDR01_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDR03[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR01[0].soma], weight: 1.0
        #h("a_MDR03[0].soma { syn_NC_MDR03_MDR01_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDR01[0].soma { syn_NC_MDR03_MDR01_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDR03_MDR01_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDR01[0].soma.v(0.5)")
        h("setpointer syn_NC_MDR03_MDR01_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDR03[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDR03_MDR02_Generic_GJ
        print("Adding electrical projection: NC_MDR03_MDR02_Generic_GJ from MDR03 to MDR02, with 1 connection(s)")

        #h("objectvar syn_NC_MDR03_MDR02_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDR03_MDR02_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDR03[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR02[0].soma], weight: 1.0
        #h("a_MDR03[0].soma { syn_NC_MDR03_MDR02_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDR02[0].soma { syn_NC_MDR03_MDR02_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDR03_MDR02_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDR02[0].soma.v(0.5)")
        h("setpointer syn_NC_MDR03_MDR02_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDR03[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDR03_MDR04_Generic_GJ
        print("Adding electrical projection: NC_MDR03_MDR04_Generic_GJ from MDR03 to MDR04, with 1 connection(s)")

        #h("objectvar syn_NC_MDR03_MDR04_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDR03_MDR04_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDR03[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR04[0].soma], weight: 1.0
        #h("a_MDR03[0].soma { syn_NC_MDR03_MDR04_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDR04[0].soma { syn_NC_MDR03_MDR04_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDR03_MDR04_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDR04[0].soma.v(0.5)")
        h("setpointer syn_NC_MDR03_MDR04_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDR03[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDR04_MDR03_Generic_GJ
        print("Adding electrical projection: NC_MDR04_MDR03_Generic_GJ from MDR04 to MDR03, with 1 connection(s)")

        #h("objectvar syn_NC_MDR04_MDR03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDR04_MDR03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDR04[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR03[0].soma], weight: 1.0
        #h("a_MDR04[0].soma { syn_NC_MDR04_MDR03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDR03[0].soma { syn_NC_MDR04_MDR03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDR04_MDR03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDR03[0].soma.v(0.5)")
        h("setpointer syn_NC_MDR04_MDR03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDR04[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDR04_MDR05_Generic_GJ
        print("Adding electrical projection: NC_MDR04_MDR05_Generic_GJ from MDR04 to MDR05, with 1 connection(s)")

        #h("objectvar syn_NC_MDR04_MDR05_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDR04_MDR05_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDR04[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR05[0].soma], weight: 1.0
        #h("a_MDR04[0].soma { syn_NC_MDR04_MDR05_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDR05[0].soma { syn_NC_MDR04_MDR05_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDR04_MDR05_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDR05[0].soma.v(0.5)")
        h("setpointer syn_NC_MDR04_MDR05_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDR04[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDR05_MDR04_Generic_GJ
        print("Adding electrical projection: NC_MDR05_MDR04_Generic_GJ from MDR05 to MDR04, with 1 connection(s)")

        #h("objectvar syn_NC_MDR05_MDR04_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDR05_MDR04_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDR05[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR04[0].soma], weight: 1.0
        #h("a_MDR05[0].soma { syn_NC_MDR05_MDR04_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDR04[0].soma { syn_NC_MDR05_MDR04_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDR05_MDR04_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDR04[0].soma.v(0.5)")
        h("setpointer syn_NC_MDR05_MDR04_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDR05[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDR05_MDR06_Generic_GJ
        print("Adding electrical projection: NC_MDR05_MDR06_Generic_GJ from MDR05 to MDR06, with 1 connection(s)")

        #h("objectvar syn_NC_MDR05_MDR06_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDR05_MDR06_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDR05[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR06[0].soma], weight: 1.0
        #h("a_MDR05[0].soma { syn_NC_MDR05_MDR06_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDR06[0].soma { syn_NC_MDR05_MDR06_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDR05_MDR06_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDR06[0].soma.v(0.5)")
        h("setpointer syn_NC_MDR05_MDR06_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDR05[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDR06_MDR05_Generic_GJ
        print("Adding electrical projection: NC_MDR06_MDR05_Generic_GJ from MDR06 to MDR05, with 1 connection(s)")

        #h("objectvar syn_NC_MDR06_MDR05_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDR06_MDR05_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDR06[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR05[0].soma], weight: 1.0
        #h("a_MDR06[0].soma { syn_NC_MDR06_MDR05_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDR05[0].soma { syn_NC_MDR06_MDR05_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDR06_MDR05_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDR05[0].soma.v(0.5)")
        h("setpointer syn_NC_MDR06_MDR05_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDR06[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDR06_MDR07_Generic_GJ
        print("Adding electrical projection: NC_MDR06_MDR07_Generic_GJ from MDR06 to MDR07, with 1 connection(s)")

        #h("objectvar syn_NC_MDR06_MDR07_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDR06_MDR07_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDR06[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR07[0].soma], weight: 1.0
        #h("a_MDR06[0].soma { syn_NC_MDR06_MDR07_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDR07[0].soma { syn_NC_MDR06_MDR07_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDR06_MDR07_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDR07[0].soma.v(0.5)")
        h("setpointer syn_NC_MDR06_MDR07_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDR06[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDR07_MDR06_Generic_GJ
        print("Adding electrical projection: NC_MDR07_MDR06_Generic_GJ from MDR07 to MDR06, with 1 connection(s)")

        #h("objectvar syn_NC_MDR07_MDR06_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDR07_MDR06_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDR07[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR06[0].soma], weight: 1.0
        #h("a_MDR07[0].soma { syn_NC_MDR07_MDR06_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDR06[0].soma { syn_NC_MDR07_MDR06_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDR07_MDR06_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDR06[0].soma.v(0.5)")
        h("setpointer syn_NC_MDR07_MDR06_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDR07[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDR07_MDR08_Generic_GJ
        print("Adding electrical projection: NC_MDR07_MDR08_Generic_GJ from MDR07 to MDR08, with 1 connection(s)")

        #h("objectvar syn_NC_MDR07_MDR08_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDR07_MDR08_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDR07[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR08[0].soma], weight: 1.0
        #h("a_MDR07[0].soma { syn_NC_MDR07_MDR08_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDR08[0].soma { syn_NC_MDR07_MDR08_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDR07_MDR08_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDR08[0].soma.v(0.5)")
        h("setpointer syn_NC_MDR07_MDR08_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDR07[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDR08_MDR07_Generic_GJ
        print("Adding electrical projection: NC_MDR08_MDR07_Generic_GJ from MDR08 to MDR07, with 1 connection(s)")

        #h("objectvar syn_NC_MDR08_MDR07_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDR08_MDR07_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDR08[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR07[0].soma], weight: 1.0
        #h("a_MDR08[0].soma { syn_NC_MDR08_MDR07_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDR07[0].soma { syn_NC_MDR08_MDR07_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDR08_MDR07_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDR07[0].soma.v(0.5)")
        h("setpointer syn_NC_MDR08_MDR07_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDR08[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDR08_MDR09_Generic_GJ
        print("Adding electrical projection: NC_MDR08_MDR09_Generic_GJ from MDR08 to MDR09, with 1 connection(s)")

        #h("objectvar syn_NC_MDR08_MDR09_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDR08_MDR09_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDR08[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR09[0].soma], weight: 1.0
        #h("a_MDR08[0].soma { syn_NC_MDR08_MDR09_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDR09[0].soma { syn_NC_MDR08_MDR09_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDR08_MDR09_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDR09[0].soma.v(0.5)")
        h("setpointer syn_NC_MDR08_MDR09_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDR08[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDR09_MDR08_Generic_GJ
        print("Adding electrical projection: NC_MDR09_MDR08_Generic_GJ from MDR09 to MDR08, with 1 connection(s)")

        #h("objectvar syn_NC_MDR09_MDR08_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDR09_MDR08_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDR09[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR08[0].soma], weight: 1.0
        #h("a_MDR09[0].soma { syn_NC_MDR09_MDR08_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDR08[0].soma { syn_NC_MDR09_MDR08_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDR09_MDR08_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDR08[0].soma.v(0.5)")
        h("setpointer syn_NC_MDR09_MDR08_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDR09[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDR09_MDR10_Generic_GJ
        print("Adding electrical projection: NC_MDR09_MDR10_Generic_GJ from MDR09 to MDR10, with 1 connection(s)")

        #h("objectvar syn_NC_MDR09_MDR10_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDR09_MDR10_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDR09[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR10[0].soma], weight: 1.0
        #h("a_MDR09[0].soma { syn_NC_MDR09_MDR10_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDR10[0].soma { syn_NC_MDR09_MDR10_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDR09_MDR10_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDR10[0].soma.v(0.5)")
        h("setpointer syn_NC_MDR09_MDR10_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDR09[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDR10_MDR09_Generic_GJ
        print("Adding electrical projection: NC_MDR10_MDR09_Generic_GJ from MDR10 to MDR09, with 1 connection(s)")

        #h("objectvar syn_NC_MDR10_MDR09_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDR10_MDR09_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDR10[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR09[0].soma], weight: 1.0
        #h("a_MDR10[0].soma { syn_NC_MDR10_MDR09_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDR09[0].soma { syn_NC_MDR10_MDR09_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDR10_MDR09_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDR09[0].soma.v(0.5)")
        h("setpointer syn_NC_MDR10_MDR09_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDR10[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDR10_MDR11_Generic_GJ
        print("Adding electrical projection: NC_MDR10_MDR11_Generic_GJ from MDR10 to MDR11, with 1 connection(s)")

        #h("objectvar syn_NC_MDR10_MDR11_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDR10_MDR11_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDR10[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR11[0].soma], weight: 1.0
        #h("a_MDR10[0].soma { syn_NC_MDR10_MDR11_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDR11[0].soma { syn_NC_MDR10_MDR11_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDR10_MDR11_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDR11[0].soma.v(0.5)")
        h("setpointer syn_NC_MDR10_MDR11_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDR10[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDR11_MDR10_Generic_GJ
        print("Adding electrical projection: NC_MDR11_MDR10_Generic_GJ from MDR11 to MDR10, with 1 connection(s)")

        #h("objectvar syn_NC_MDR11_MDR10_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDR11_MDR10_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDR11[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR10[0].soma], weight: 1.0
        #h("a_MDR11[0].soma { syn_NC_MDR11_MDR10_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDR10[0].soma { syn_NC_MDR11_MDR10_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDR11_MDR10_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDR10[0].soma.v(0.5)")
        h("setpointer syn_NC_MDR11_MDR10_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDR11[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDR11_MDR12_Generic_GJ
        print("Adding electrical projection: NC_MDR11_MDR12_Generic_GJ from MDR11 to MDR12, with 1 connection(s)")

        #h("objectvar syn_NC_MDR11_MDR12_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDR11_MDR12_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDR11[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR12[0].soma], weight: 1.0
        #h("a_MDR11[0].soma { syn_NC_MDR11_MDR12_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDR12[0].soma { syn_NC_MDR11_MDR12_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDR11_MDR12_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDR12[0].soma.v(0.5)")
        h("setpointer syn_NC_MDR11_MDR12_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDR11[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDR12_MDR11_Generic_GJ
        print("Adding electrical projection: NC_MDR12_MDR11_Generic_GJ from MDR12 to MDR11, with 1 connection(s)")

        #h("objectvar syn_NC_MDR12_MDR11_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDR12_MDR11_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDR12[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR11[0].soma], weight: 1.0
        #h("a_MDR12[0].soma { syn_NC_MDR12_MDR11_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDR11[0].soma { syn_NC_MDR12_MDR11_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDR12_MDR11_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDR11[0].soma.v(0.5)")
        h("setpointer syn_NC_MDR12_MDR11_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDR12[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDR12_MDR13_Generic_GJ
        print("Adding electrical projection: NC_MDR12_MDR13_Generic_GJ from MDR12 to MDR13, with 1 connection(s)")

        #h("objectvar syn_NC_MDR12_MDR13_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDR12_MDR13_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDR12[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR13[0].soma], weight: 1.0
        #h("a_MDR12[0].soma { syn_NC_MDR12_MDR13_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDR13[0].soma { syn_NC_MDR12_MDR13_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDR12_MDR13_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDR13[0].soma.v(0.5)")
        h("setpointer syn_NC_MDR12_MDR13_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDR12[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDR13_MDR12_Generic_GJ
        print("Adding electrical projection: NC_MDR13_MDR12_Generic_GJ from MDR13 to MDR12, with 1 connection(s)")

        #h("objectvar syn_NC_MDR13_MDR12_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDR13_MDR12_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDR13[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR12[0].soma], weight: 1.0
        #h("a_MDR13[0].soma { syn_NC_MDR13_MDR12_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDR12[0].soma { syn_NC_MDR13_MDR12_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDR13_MDR12_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDR12[0].soma.v(0.5)")
        h("setpointer syn_NC_MDR13_MDR12_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDR13[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDR13_MDR14_Generic_GJ
        print("Adding electrical projection: NC_MDR13_MDR14_Generic_GJ from MDR13 to MDR14, with 1 connection(s)")

        #h("objectvar syn_NC_MDR13_MDR14_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDR13_MDR14_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDR13[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR14[0].soma], weight: 1.0
        #h("a_MDR13[0].soma { syn_NC_MDR13_MDR14_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDR14[0].soma { syn_NC_MDR13_MDR14_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDR13_MDR14_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDR14[0].soma.v(0.5)")
        h("setpointer syn_NC_MDR13_MDR14_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDR13[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDR14_MDR13_Generic_GJ
        print("Adding electrical projection: NC_MDR14_MDR13_Generic_GJ from MDR14 to MDR13, with 1 connection(s)")

        #h("objectvar syn_NC_MDR14_MDR13_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDR14_MDR13_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDR14[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR13[0].soma], weight: 1.0
        #h("a_MDR14[0].soma { syn_NC_MDR14_MDR13_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDR13[0].soma { syn_NC_MDR14_MDR13_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDR14_MDR13_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDR13[0].soma.v(0.5)")
        h("setpointer syn_NC_MDR14_MDR13_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDR14[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDR14_MDR15_Generic_GJ
        print("Adding electrical projection: NC_MDR14_MDR15_Generic_GJ from MDR14 to MDR15, with 1 connection(s)")

        #h("objectvar syn_NC_MDR14_MDR15_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDR14_MDR15_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDR14[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR15[0].soma], weight: 1.0
        #h("a_MDR14[0].soma { syn_NC_MDR14_MDR15_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDR15[0].soma { syn_NC_MDR14_MDR15_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDR14_MDR15_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDR15[0].soma.v(0.5)")
        h("setpointer syn_NC_MDR14_MDR15_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDR14[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDR15_MDR14_Generic_GJ
        print("Adding electrical projection: NC_MDR15_MDR14_Generic_GJ from MDR15 to MDR14, with 1 connection(s)")

        #h("objectvar syn_NC_MDR15_MDR14_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDR15_MDR14_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDR15[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR14[0].soma], weight: 1.0
        #h("a_MDR15[0].soma { syn_NC_MDR15_MDR14_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDR14[0].soma { syn_NC_MDR15_MDR14_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDR15_MDR14_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDR14[0].soma.v(0.5)")
        h("setpointer syn_NC_MDR15_MDR14_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDR15[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDR15_MDR16_Generic_GJ
        print("Adding electrical projection: NC_MDR15_MDR16_Generic_GJ from MDR15 to MDR16, with 1 connection(s)")

        #h("objectvar syn_NC_MDR15_MDR16_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDR15_MDR16_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDR15[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR16[0].soma], weight: 1.0
        #h("a_MDR15[0].soma { syn_NC_MDR15_MDR16_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDR16[0].soma { syn_NC_MDR15_MDR16_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDR15_MDR16_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDR16[0].soma.v(0.5)")
        h("setpointer syn_NC_MDR15_MDR16_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDR15[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDR16_MDR15_Generic_GJ
        print("Adding electrical projection: NC_MDR16_MDR15_Generic_GJ from MDR16 to MDR15, with 1 connection(s)")

        #h("objectvar syn_NC_MDR16_MDR15_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDR16_MDR15_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDR16[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR15[0].soma], weight: 1.0
        #h("a_MDR16[0].soma { syn_NC_MDR16_MDR15_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDR15[0].soma { syn_NC_MDR16_MDR15_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDR16_MDR15_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDR15[0].soma.v(0.5)")
        h("setpointer syn_NC_MDR16_MDR15_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDR16[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDR16_MDR17_Generic_GJ
        print("Adding electrical projection: NC_MDR16_MDR17_Generic_GJ from MDR16 to MDR17, with 1 connection(s)")

        #h("objectvar syn_NC_MDR16_MDR17_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDR16_MDR17_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDR16[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR17[0].soma], weight: 1.0
        #h("a_MDR16[0].soma { syn_NC_MDR16_MDR17_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDR17[0].soma { syn_NC_MDR16_MDR17_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDR16_MDR17_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDR17[0].soma.v(0.5)")
        h("setpointer syn_NC_MDR16_MDR17_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDR16[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDR17_MDR16_Generic_GJ
        print("Adding electrical projection: NC_MDR17_MDR16_Generic_GJ from MDR17 to MDR16, with 1 connection(s)")

        #h("objectvar syn_NC_MDR17_MDR16_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDR17_MDR16_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDR17[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR16[0].soma], weight: 1.0
        #h("a_MDR17[0].soma { syn_NC_MDR17_MDR16_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDR16[0].soma { syn_NC_MDR17_MDR16_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDR17_MDR16_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDR16[0].soma.v(0.5)")
        h("setpointer syn_NC_MDR17_MDR16_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDR17[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDR17_MDR18_Generic_GJ
        print("Adding electrical projection: NC_MDR17_MDR18_Generic_GJ from MDR17 to MDR18, with 1 connection(s)")

        #h("objectvar syn_NC_MDR17_MDR18_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDR17_MDR18_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDR17[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR18[0].soma], weight: 1.0
        #h("a_MDR17[0].soma { syn_NC_MDR17_MDR18_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDR18[0].soma { syn_NC_MDR17_MDR18_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDR17_MDR18_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDR18[0].soma.v(0.5)")
        h("setpointer syn_NC_MDR17_MDR18_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDR17[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDR18_MDR17_Generic_GJ
        print("Adding electrical projection: NC_MDR18_MDR17_Generic_GJ from MDR18 to MDR17, with 1 connection(s)")

        #h("objectvar syn_NC_MDR18_MDR17_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDR18_MDR17_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDR18[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR17[0].soma], weight: 1.0
        #h("a_MDR18[0].soma { syn_NC_MDR18_MDR17_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDR17[0].soma { syn_NC_MDR18_MDR17_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDR18_MDR17_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDR17[0].soma.v(0.5)")
        h("setpointer syn_NC_MDR18_MDR17_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDR18[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDR18_MDR19_Generic_GJ
        print("Adding electrical projection: NC_MDR18_MDR19_Generic_GJ from MDR18 to MDR19, with 1 connection(s)")

        #h("objectvar syn_NC_MDR18_MDR19_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDR18_MDR19_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDR18[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR19[0].soma], weight: 1.0
        #h("a_MDR18[0].soma { syn_NC_MDR18_MDR19_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDR19[0].soma { syn_NC_MDR18_MDR19_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDR18_MDR19_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDR19[0].soma.v(0.5)")
        h("setpointer syn_NC_MDR18_MDR19_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDR18[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDR19_MDR18_Generic_GJ
        print("Adding electrical projection: NC_MDR19_MDR18_Generic_GJ from MDR19 to MDR18, with 1 connection(s)")

        #h("objectvar syn_NC_MDR19_MDR18_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDR19_MDR18_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDR19[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR18[0].soma], weight: 1.0
        #h("a_MDR19[0].soma { syn_NC_MDR19_MDR18_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDR18[0].soma { syn_NC_MDR19_MDR18_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDR19_MDR18_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDR18[0].soma.v(0.5)")
        h("setpointer syn_NC_MDR19_MDR18_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDR19[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDR19_MDR20_Generic_GJ
        print("Adding electrical projection: NC_MDR19_MDR20_Generic_GJ from MDR19 to MDR20, with 1 connection(s)")

        #h("objectvar syn_NC_MDR19_MDR20_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDR19_MDR20_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDR19[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR20[0].soma], weight: 1.0
        #h("a_MDR19[0].soma { syn_NC_MDR19_MDR20_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDR20[0].soma { syn_NC_MDR19_MDR20_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDR19_MDR20_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDR20[0].soma.v(0.5)")
        h("setpointer syn_NC_MDR19_MDR20_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDR19[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDR20_MDR19_Generic_GJ
        print("Adding electrical projection: NC_MDR20_MDR19_Generic_GJ from MDR20 to MDR19, with 1 connection(s)")

        #h("objectvar syn_NC_MDR20_MDR19_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDR20_MDR19_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDR20[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR19[0].soma], weight: 1.0
        #h("a_MDR20[0].soma { syn_NC_MDR20_MDR19_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDR19[0].soma { syn_NC_MDR20_MDR19_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDR20_MDR19_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDR19[0].soma.v(0.5)")
        h("setpointer syn_NC_MDR20_MDR19_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDR20[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDR20_MDR21_Generic_GJ
        print("Adding electrical projection: NC_MDR20_MDR21_Generic_GJ from MDR20 to MDR21, with 1 connection(s)")

        #h("objectvar syn_NC_MDR20_MDR21_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDR20_MDR21_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDR20[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR21[0].soma], weight: 1.0
        #h("a_MDR20[0].soma { syn_NC_MDR20_MDR21_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDR21[0].soma { syn_NC_MDR20_MDR21_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDR20_MDR21_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDR21[0].soma.v(0.5)")
        h("setpointer syn_NC_MDR20_MDR21_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDR20[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDR21_MDR20_Generic_GJ
        print("Adding electrical projection: NC_MDR21_MDR20_Generic_GJ from MDR21 to MDR20, with 1 connection(s)")

        #h("objectvar syn_NC_MDR21_MDR20_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDR21_MDR20_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDR21[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR20[0].soma], weight: 1.0
        #h("a_MDR21[0].soma { syn_NC_MDR21_MDR20_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDR20[0].soma { syn_NC_MDR21_MDR20_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDR21_MDR20_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDR20[0].soma.v(0.5)")
        h("setpointer syn_NC_MDR21_MDR20_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDR21[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDR21_MDR22_Generic_GJ
        print("Adding electrical projection: NC_MDR21_MDR22_Generic_GJ from MDR21 to MDR22, with 1 connection(s)")

        #h("objectvar syn_NC_MDR21_MDR22_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDR21_MDR22_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDR21[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR22[0].soma], weight: 1.0
        #h("a_MDR21[0].soma { syn_NC_MDR21_MDR22_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDR22[0].soma { syn_NC_MDR21_MDR22_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDR21_MDR22_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDR22[0].soma.v(0.5)")
        h("setpointer syn_NC_MDR21_MDR22_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDR21[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDR22_MDR21_Generic_GJ
        print("Adding electrical projection: NC_MDR22_MDR21_Generic_GJ from MDR22 to MDR21, with 1 connection(s)")

        #h("objectvar syn_NC_MDR22_MDR21_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDR22_MDR21_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDR22[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR21[0].soma], weight: 1.0
        #h("a_MDR22[0].soma { syn_NC_MDR22_MDR21_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDR21[0].soma { syn_NC_MDR22_MDR21_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDR22_MDR21_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDR21[0].soma.v(0.5)")
        h("setpointer syn_NC_MDR22_MDR21_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDR22[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDR22_MDR23_Generic_GJ
        print("Adding electrical projection: NC_MDR22_MDR23_Generic_GJ from MDR22 to MDR23, with 1 connection(s)")

        #h("objectvar syn_NC_MDR22_MDR23_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDR22_MDR23_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDR22[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR23[0].soma], weight: 1.0
        #h("a_MDR22[0].soma { syn_NC_MDR22_MDR23_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDR23[0].soma { syn_NC_MDR22_MDR23_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDR22_MDR23_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDR23[0].soma.v(0.5)")
        h("setpointer syn_NC_MDR22_MDR23_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDR22[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDR23_MDR22_Generic_GJ
        print("Adding electrical projection: NC_MDR23_MDR22_Generic_GJ from MDR23 to MDR22, with 1 connection(s)")

        #h("objectvar syn_NC_MDR23_MDR22_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDR23_MDR22_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDR23[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR22[0].soma], weight: 1.0
        #h("a_MDR23[0].soma { syn_NC_MDR23_MDR22_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDR22[0].soma { syn_NC_MDR23_MDR22_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDR23_MDR22_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDR22[0].soma.v(0.5)")
        h("setpointer syn_NC_MDR23_MDR22_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDR23[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDR23_MDR24_Generic_GJ
        print("Adding electrical projection: NC_MDR23_MDR24_Generic_GJ from MDR23 to MDR24, with 1 connection(s)")

        #h("objectvar syn_NC_MDR23_MDR24_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDR23_MDR24_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDR23[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR24[0].soma], weight: 1.0
        #h("a_MDR23[0].soma { syn_NC_MDR23_MDR24_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDR24[0].soma { syn_NC_MDR23_MDR24_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDR23_MDR24_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDR24[0].soma.v(0.5)")
        h("setpointer syn_NC_MDR23_MDR24_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDR23[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MDR24_MDR23_Generic_GJ
        print("Adding electrical projection: NC_MDR24_MDR23_Generic_GJ from MDR24 to MDR23, with 1 connection(s)")

        #h("objectvar syn_NC_MDR24_MDR23_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MDR24_MDR23_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MDR24[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR23[0].soma], weight: 1.0
        #h("a_MDR24[0].soma { syn_NC_MDR24_MDR23_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MDR23[0].soma { syn_NC_MDR24_MDR23_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MDR24_MDR23_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MDR23[0].soma.v(0.5)")
        h("setpointer syn_NC_MDR24_MDR23_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MDR24[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVL01_MVL02_Generic_GJ
        print("Adding electrical projection: NC_MVL01_MVL02_Generic_GJ from MVL01 to MVL02, with 1 connection(s)")

        #h("objectvar syn_NC_MVL01_MVL02_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVL01_MVL02_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVL01[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVL02[0].soma], weight: 1.0
        #h("a_MVL01[0].soma { syn_NC_MVL01_MVL02_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVL02[0].soma { syn_NC_MVL01_MVL02_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVL01_MVL02_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVL02[0].soma.v(0.5)")
        h("setpointer syn_NC_MVL01_MVL02_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVL01[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVL01_MVL03_Generic_GJ
        print("Adding electrical projection: NC_MVL01_MVL03_Generic_GJ from MVL01 to MVL03, with 1 connection(s)")

        #h("objectvar syn_NC_MVL01_MVL03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVL01_MVL03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVL01[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVL03[0].soma], weight: 1.0
        #h("a_MVL01[0].soma { syn_NC_MVL01_MVL03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVL03[0].soma { syn_NC_MVL01_MVL03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVL01_MVL03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVL03[0].soma.v(0.5)")
        h("setpointer syn_NC_MVL01_MVL03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVL01[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVL02_MVL01_Generic_GJ
        print("Adding electrical projection: NC_MVL02_MVL01_Generic_GJ from MVL02 to MVL01, with 1 connection(s)")

        #h("objectvar syn_NC_MVL02_MVL01_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVL02_MVL01_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVL02[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVL01[0].soma], weight: 1.0
        #h("a_MVL02[0].soma { syn_NC_MVL02_MVL01_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVL01[0].soma { syn_NC_MVL02_MVL01_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVL02_MVL01_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVL01[0].soma.v(0.5)")
        h("setpointer syn_NC_MVL02_MVL01_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVL02[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVL02_MVL03_Generic_GJ
        print("Adding electrical projection: NC_MVL02_MVL03_Generic_GJ from MVL02 to MVL03, with 1 connection(s)")

        #h("objectvar syn_NC_MVL02_MVL03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVL02_MVL03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVL02[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVL03[0].soma], weight: 1.0
        #h("a_MVL02[0].soma { syn_NC_MVL02_MVL03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVL03[0].soma { syn_NC_MVL02_MVL03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVL02_MVL03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVL03[0].soma.v(0.5)")
        h("setpointer syn_NC_MVL02_MVL03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVL02[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVL03_MVL01_Generic_GJ
        print("Adding electrical projection: NC_MVL03_MVL01_Generic_GJ from MVL03 to MVL01, with 1 connection(s)")

        #h("objectvar syn_NC_MVL03_MVL01_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVL03_MVL01_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVL03[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVL01[0].soma], weight: 1.0
        #h("a_MVL03[0].soma { syn_NC_MVL03_MVL01_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVL01[0].soma { syn_NC_MVL03_MVL01_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVL03_MVL01_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVL01[0].soma.v(0.5)")
        h("setpointer syn_NC_MVL03_MVL01_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVL03[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVL03_MVL02_Generic_GJ
        print("Adding electrical projection: NC_MVL03_MVL02_Generic_GJ from MVL03 to MVL02, with 1 connection(s)")

        #h("objectvar syn_NC_MVL03_MVL02_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVL03_MVL02_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVL03[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVL02[0].soma], weight: 1.0
        #h("a_MVL03[0].soma { syn_NC_MVL03_MVL02_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVL02[0].soma { syn_NC_MVL03_MVL02_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVL03_MVL02_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVL02[0].soma.v(0.5)")
        h("setpointer syn_NC_MVL03_MVL02_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVL03[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVL03_MVL04_Generic_GJ
        print("Adding electrical projection: NC_MVL03_MVL04_Generic_GJ from MVL03 to MVL04, with 1 connection(s)")

        #h("objectvar syn_NC_MVL03_MVL04_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVL03_MVL04_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVL03[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVL04[0].soma], weight: 1.0
        #h("a_MVL03[0].soma { syn_NC_MVL03_MVL04_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVL04[0].soma { syn_NC_MVL03_MVL04_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVL03_MVL04_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVL04[0].soma.v(0.5)")
        h("setpointer syn_NC_MVL03_MVL04_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVL03[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVL04_MVL03_Generic_GJ
        print("Adding electrical projection: NC_MVL04_MVL03_Generic_GJ from MVL04 to MVL03, with 1 connection(s)")

        #h("objectvar syn_NC_MVL04_MVL03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVL04_MVL03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVL04[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVL03[0].soma], weight: 1.0
        #h("a_MVL04[0].soma { syn_NC_MVL04_MVL03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVL03[0].soma { syn_NC_MVL04_MVL03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVL04_MVL03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVL03[0].soma.v(0.5)")
        h("setpointer syn_NC_MVL04_MVL03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVL04[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVL04_MVL05_Generic_GJ
        print("Adding electrical projection: NC_MVL04_MVL05_Generic_GJ from MVL04 to MVL05, with 1 connection(s)")

        #h("objectvar syn_NC_MVL04_MVL05_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVL04_MVL05_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVL04[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVL05[0].soma], weight: 1.0
        #h("a_MVL04[0].soma { syn_NC_MVL04_MVL05_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVL05[0].soma { syn_NC_MVL04_MVL05_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVL04_MVL05_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVL05[0].soma.v(0.5)")
        h("setpointer syn_NC_MVL04_MVL05_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVL04[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVL05_MVL04_Generic_GJ
        print("Adding electrical projection: NC_MVL05_MVL04_Generic_GJ from MVL05 to MVL04, with 1 connection(s)")

        #h("objectvar syn_NC_MVL05_MVL04_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVL05_MVL04_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVL05[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVL04[0].soma], weight: 1.0
        #h("a_MVL05[0].soma { syn_NC_MVL05_MVL04_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVL04[0].soma { syn_NC_MVL05_MVL04_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVL05_MVL04_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVL04[0].soma.v(0.5)")
        h("setpointer syn_NC_MVL05_MVL04_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVL05[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVL05_MVL06_Generic_GJ
        print("Adding electrical projection: NC_MVL05_MVL06_Generic_GJ from MVL05 to MVL06, with 1 connection(s)")

        #h("objectvar syn_NC_MVL05_MVL06_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVL05_MVL06_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVL05[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVL06[0].soma], weight: 1.0
        #h("a_MVL05[0].soma { syn_NC_MVL05_MVL06_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVL06[0].soma { syn_NC_MVL05_MVL06_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVL05_MVL06_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVL06[0].soma.v(0.5)")
        h("setpointer syn_NC_MVL05_MVL06_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVL05[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVL06_MVL05_Generic_GJ
        print("Adding electrical projection: NC_MVL06_MVL05_Generic_GJ from MVL06 to MVL05, with 1 connection(s)")

        #h("objectvar syn_NC_MVL06_MVL05_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVL06_MVL05_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVL06[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVL05[0].soma], weight: 1.0
        #h("a_MVL06[0].soma { syn_NC_MVL06_MVL05_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVL05[0].soma { syn_NC_MVL06_MVL05_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVL06_MVL05_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVL05[0].soma.v(0.5)")
        h("setpointer syn_NC_MVL06_MVL05_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVL06[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVL06_MVL07_Generic_GJ
        print("Adding electrical projection: NC_MVL06_MVL07_Generic_GJ from MVL06 to MVL07, with 1 connection(s)")

        #h("objectvar syn_NC_MVL06_MVL07_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVL06_MVL07_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVL06[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVL07[0].soma], weight: 1.0
        #h("a_MVL06[0].soma { syn_NC_MVL06_MVL07_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVL07[0].soma { syn_NC_MVL06_MVL07_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVL06_MVL07_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVL07[0].soma.v(0.5)")
        h("setpointer syn_NC_MVL06_MVL07_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVL06[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVL07_MVL06_Generic_GJ
        print("Adding electrical projection: NC_MVL07_MVL06_Generic_GJ from MVL07 to MVL06, with 1 connection(s)")

        #h("objectvar syn_NC_MVL07_MVL06_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVL07_MVL06_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVL07[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVL06[0].soma], weight: 1.0
        #h("a_MVL07[0].soma { syn_NC_MVL07_MVL06_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVL06[0].soma { syn_NC_MVL07_MVL06_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVL07_MVL06_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVL06[0].soma.v(0.5)")
        h("setpointer syn_NC_MVL07_MVL06_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVL07[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVL07_MVL08_Generic_GJ
        print("Adding electrical projection: NC_MVL07_MVL08_Generic_GJ from MVL07 to MVL08, with 1 connection(s)")

        #h("objectvar syn_NC_MVL07_MVL08_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVL07_MVL08_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVL07[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVL08[0].soma], weight: 1.0
        #h("a_MVL07[0].soma { syn_NC_MVL07_MVL08_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVL08[0].soma { syn_NC_MVL07_MVL08_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVL07_MVL08_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVL08[0].soma.v(0.5)")
        h("setpointer syn_NC_MVL07_MVL08_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVL07[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVL08_MVL07_Generic_GJ
        print("Adding electrical projection: NC_MVL08_MVL07_Generic_GJ from MVL08 to MVL07, with 1 connection(s)")

        #h("objectvar syn_NC_MVL08_MVL07_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVL08_MVL07_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVL08[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVL07[0].soma], weight: 1.0
        #h("a_MVL08[0].soma { syn_NC_MVL08_MVL07_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVL07[0].soma { syn_NC_MVL08_MVL07_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVL08_MVL07_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVL07[0].soma.v(0.5)")
        h("setpointer syn_NC_MVL08_MVL07_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVL08[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVL08_MVL09_Generic_GJ
        print("Adding electrical projection: NC_MVL08_MVL09_Generic_GJ from MVL08 to MVL09, with 1 connection(s)")

        #h("objectvar syn_NC_MVL08_MVL09_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVL08_MVL09_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVL08[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVL09[0].soma], weight: 1.0
        #h("a_MVL08[0].soma { syn_NC_MVL08_MVL09_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVL09[0].soma { syn_NC_MVL08_MVL09_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVL08_MVL09_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVL09[0].soma.v(0.5)")
        h("setpointer syn_NC_MVL08_MVL09_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVL08[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVL09_MVL08_Generic_GJ
        print("Adding electrical projection: NC_MVL09_MVL08_Generic_GJ from MVL09 to MVL08, with 1 connection(s)")

        #h("objectvar syn_NC_MVL09_MVL08_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVL09_MVL08_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVL09[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVL08[0].soma], weight: 1.0
        #h("a_MVL09[0].soma { syn_NC_MVL09_MVL08_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVL08[0].soma { syn_NC_MVL09_MVL08_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVL09_MVL08_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVL08[0].soma.v(0.5)")
        h("setpointer syn_NC_MVL09_MVL08_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVL09[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVL09_MVL10_Generic_GJ
        print("Adding electrical projection: NC_MVL09_MVL10_Generic_GJ from MVL09 to MVL10, with 1 connection(s)")

        #h("objectvar syn_NC_MVL09_MVL10_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVL09_MVL10_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVL09[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVL10[0].soma], weight: 1.0
        #h("a_MVL09[0].soma { syn_NC_MVL09_MVL10_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVL10[0].soma { syn_NC_MVL09_MVL10_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVL09_MVL10_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVL10[0].soma.v(0.5)")
        h("setpointer syn_NC_MVL09_MVL10_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVL09[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVL09_MVR08_Generic_GJ
        print("Adding electrical projection: NC_MVL09_MVR08_Generic_GJ from MVL09 to MVR08, with 1 connection(s)")

        #h("objectvar syn_NC_MVL09_MVR08_Generic_GJ_muscle_to_muscle_elec_syn_2conns_A[1]")
        h("objectvar syn_NC_MVL09_MVR08_Generic_GJ_muscle_to_muscle_elec_syn_2conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVL09[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVR08[0].soma], weight: 1.0
        #h("a_MVL09[0].soma { syn_NC_MVL09_MVR08_Generic_GJ_muscle_to_muscle_elec_syn_2conns_A[0] = new muscle_to_muscle_elec_syn_2conns(0.5) }")
        h("a_MVR08[0].soma { syn_NC_MVL09_MVR08_Generic_GJ_muscle_to_muscle_elec_syn_2conns_B[0] = new muscle_to_muscle_elec_syn_2conns(0.5) }")
        #h("setpointer syn_NC_MVL09_MVR08_Generic_GJ_muscle_to_muscle_elec_syn_2conns_A[0].vpeer, a_MVR08[0].soma.v(0.5)")
        h("setpointer syn_NC_MVL09_MVR08_Generic_GJ_muscle_to_muscle_elec_syn_2conns_B[0].vpeer, a_MVL09[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVL10_MVL09_Generic_GJ
        print("Adding electrical projection: NC_MVL10_MVL09_Generic_GJ from MVL10 to MVL09, with 1 connection(s)")

        #h("objectvar syn_NC_MVL10_MVL09_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVL10_MVL09_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVL10[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVL09[0].soma], weight: 1.0
        #h("a_MVL10[0].soma { syn_NC_MVL10_MVL09_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVL09[0].soma { syn_NC_MVL10_MVL09_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVL10_MVL09_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVL09[0].soma.v(0.5)")
        h("setpointer syn_NC_MVL10_MVL09_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVL10[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVL10_MVL11_Generic_GJ
        print("Adding electrical projection: NC_MVL10_MVL11_Generic_GJ from MVL10 to MVL11, with 1 connection(s)")

        #h("objectvar syn_NC_MVL10_MVL11_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVL10_MVL11_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVL10[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVL11[0].soma], weight: 1.0
        #h("a_MVL10[0].soma { syn_NC_MVL10_MVL11_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVL11[0].soma { syn_NC_MVL10_MVL11_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVL10_MVL11_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVL11[0].soma.v(0.5)")
        h("setpointer syn_NC_MVL10_MVL11_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVL10[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVL11_MVL10_Generic_GJ
        print("Adding electrical projection: NC_MVL11_MVL10_Generic_GJ from MVL11 to MVL10, with 1 connection(s)")

        #h("objectvar syn_NC_MVL11_MVL10_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVL11_MVL10_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVL11[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVL10[0].soma], weight: 1.0
        #h("a_MVL11[0].soma { syn_NC_MVL11_MVL10_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVL10[0].soma { syn_NC_MVL11_MVL10_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVL11_MVL10_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVL10[0].soma.v(0.5)")
        h("setpointer syn_NC_MVL11_MVL10_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVL11[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVL11_MVL12_Generic_GJ
        print("Adding electrical projection: NC_MVL11_MVL12_Generic_GJ from MVL11 to MVL12, with 1 connection(s)")

        #h("objectvar syn_NC_MVL11_MVL12_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVL11_MVL12_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVL11[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVL12[0].soma], weight: 1.0
        #h("a_MVL11[0].soma { syn_NC_MVL11_MVL12_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVL12[0].soma { syn_NC_MVL11_MVL12_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVL11_MVL12_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVL12[0].soma.v(0.5)")
        h("setpointer syn_NC_MVL11_MVL12_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVL11[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVL12_MVL11_Generic_GJ
        print("Adding electrical projection: NC_MVL12_MVL11_Generic_GJ from MVL12 to MVL11, with 1 connection(s)")

        #h("objectvar syn_NC_MVL12_MVL11_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVL12_MVL11_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVL12[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVL11[0].soma], weight: 1.0
        #h("a_MVL12[0].soma { syn_NC_MVL12_MVL11_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVL11[0].soma { syn_NC_MVL12_MVL11_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVL12_MVL11_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVL11[0].soma.v(0.5)")
        h("setpointer syn_NC_MVL12_MVL11_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVL12[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVL12_MVL13_Generic_GJ
        print("Adding electrical projection: NC_MVL12_MVL13_Generic_GJ from MVL12 to MVL13, with 1 connection(s)")

        #h("objectvar syn_NC_MVL12_MVL13_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVL12_MVL13_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVL12[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVL13[0].soma], weight: 1.0
        #h("a_MVL12[0].soma { syn_NC_MVL12_MVL13_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVL13[0].soma { syn_NC_MVL12_MVL13_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVL12_MVL13_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVL13[0].soma.v(0.5)")
        h("setpointer syn_NC_MVL12_MVL13_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVL12[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVL13_MVL12_Generic_GJ
        print("Adding electrical projection: NC_MVL13_MVL12_Generic_GJ from MVL13 to MVL12, with 1 connection(s)")

        #h("objectvar syn_NC_MVL13_MVL12_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVL13_MVL12_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVL13[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVL12[0].soma], weight: 1.0
        #h("a_MVL13[0].soma { syn_NC_MVL13_MVL12_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVL12[0].soma { syn_NC_MVL13_MVL12_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVL13_MVL12_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVL12[0].soma.v(0.5)")
        h("setpointer syn_NC_MVL13_MVL12_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVL13[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVL13_MVL14_Generic_GJ
        print("Adding electrical projection: NC_MVL13_MVL14_Generic_GJ from MVL13 to MVL14, with 1 connection(s)")

        #h("objectvar syn_NC_MVL13_MVL14_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVL13_MVL14_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVL13[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVL14[0].soma], weight: 1.0
        #h("a_MVL13[0].soma { syn_NC_MVL13_MVL14_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVL14[0].soma { syn_NC_MVL13_MVL14_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVL13_MVL14_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVL14[0].soma.v(0.5)")
        h("setpointer syn_NC_MVL13_MVL14_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVL13[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVL14_MVL13_Generic_GJ
        print("Adding electrical projection: NC_MVL14_MVL13_Generic_GJ from MVL14 to MVL13, with 1 connection(s)")

        #h("objectvar syn_NC_MVL14_MVL13_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVL14_MVL13_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVL14[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVL13[0].soma], weight: 1.0
        #h("a_MVL14[0].soma { syn_NC_MVL14_MVL13_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVL13[0].soma { syn_NC_MVL14_MVL13_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVL14_MVL13_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVL13[0].soma.v(0.5)")
        h("setpointer syn_NC_MVL14_MVL13_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVL14[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVL14_MVL15_Generic_GJ
        print("Adding electrical projection: NC_MVL14_MVL15_Generic_GJ from MVL14 to MVL15, with 1 connection(s)")

        #h("objectvar syn_NC_MVL14_MVL15_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVL14_MVL15_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVL14[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVL15[0].soma], weight: 1.0
        #h("a_MVL14[0].soma { syn_NC_MVL14_MVL15_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVL15[0].soma { syn_NC_MVL14_MVL15_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVL14_MVL15_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVL15[0].soma.v(0.5)")
        h("setpointer syn_NC_MVL14_MVL15_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVL14[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVL15_MVL14_Generic_GJ
        print("Adding electrical projection: NC_MVL15_MVL14_Generic_GJ from MVL15 to MVL14, with 1 connection(s)")

        #h("objectvar syn_NC_MVL15_MVL14_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVL15_MVL14_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVL15[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVL14[0].soma], weight: 1.0
        #h("a_MVL15[0].soma { syn_NC_MVL15_MVL14_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVL14[0].soma { syn_NC_MVL15_MVL14_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVL15_MVL14_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVL14[0].soma.v(0.5)")
        h("setpointer syn_NC_MVL15_MVL14_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVL15[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVL15_MVL16_Generic_GJ
        print("Adding electrical projection: NC_MVL15_MVL16_Generic_GJ from MVL15 to MVL16, with 1 connection(s)")

        #h("objectvar syn_NC_MVL15_MVL16_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVL15_MVL16_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVL15[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVL16[0].soma], weight: 1.0
        #h("a_MVL15[0].soma { syn_NC_MVL15_MVL16_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVL16[0].soma { syn_NC_MVL15_MVL16_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVL15_MVL16_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVL16[0].soma.v(0.5)")
        h("setpointer syn_NC_MVL15_MVL16_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVL15[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVL16_MVL15_Generic_GJ
        print("Adding electrical projection: NC_MVL16_MVL15_Generic_GJ from MVL16 to MVL15, with 1 connection(s)")

        #h("objectvar syn_NC_MVL16_MVL15_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVL16_MVL15_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVL16[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVL15[0].soma], weight: 1.0
        #h("a_MVL16[0].soma { syn_NC_MVL16_MVL15_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVL15[0].soma { syn_NC_MVL16_MVL15_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVL16_MVL15_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVL15[0].soma.v(0.5)")
        h("setpointer syn_NC_MVL16_MVL15_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVL16[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVL16_MVL17_Generic_GJ
        print("Adding electrical projection: NC_MVL16_MVL17_Generic_GJ from MVL16 to MVL17, with 1 connection(s)")

        #h("objectvar syn_NC_MVL16_MVL17_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVL16_MVL17_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVL16[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVL17[0].soma], weight: 1.0
        #h("a_MVL16[0].soma { syn_NC_MVL16_MVL17_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVL17[0].soma { syn_NC_MVL16_MVL17_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVL16_MVL17_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVL17[0].soma.v(0.5)")
        h("setpointer syn_NC_MVL16_MVL17_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVL16[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVL17_MVL16_Generic_GJ
        print("Adding electrical projection: NC_MVL17_MVL16_Generic_GJ from MVL17 to MVL16, with 1 connection(s)")

        #h("objectvar syn_NC_MVL17_MVL16_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVL17_MVL16_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVL17[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVL16[0].soma], weight: 1.0
        #h("a_MVL17[0].soma { syn_NC_MVL17_MVL16_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVL16[0].soma { syn_NC_MVL17_MVL16_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVL17_MVL16_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVL16[0].soma.v(0.5)")
        h("setpointer syn_NC_MVL17_MVL16_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVL17[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVL17_MVL18_Generic_GJ
        print("Adding electrical projection: NC_MVL17_MVL18_Generic_GJ from MVL17 to MVL18, with 1 connection(s)")

        #h("objectvar syn_NC_MVL17_MVL18_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVL17_MVL18_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVL17[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVL18[0].soma], weight: 1.0
        #h("a_MVL17[0].soma { syn_NC_MVL17_MVL18_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVL18[0].soma { syn_NC_MVL17_MVL18_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVL17_MVL18_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVL18[0].soma.v(0.5)")
        h("setpointer syn_NC_MVL17_MVL18_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVL17[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVL18_MVL17_Generic_GJ
        print("Adding electrical projection: NC_MVL18_MVL17_Generic_GJ from MVL18 to MVL17, with 1 connection(s)")

        #h("objectvar syn_NC_MVL18_MVL17_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVL18_MVL17_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVL18[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVL17[0].soma], weight: 1.0
        #h("a_MVL18[0].soma { syn_NC_MVL18_MVL17_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVL17[0].soma { syn_NC_MVL18_MVL17_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVL18_MVL17_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVL17[0].soma.v(0.5)")
        h("setpointer syn_NC_MVL18_MVL17_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVL18[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVL18_MVL19_Generic_GJ
        print("Adding electrical projection: NC_MVL18_MVL19_Generic_GJ from MVL18 to MVL19, with 1 connection(s)")

        #h("objectvar syn_NC_MVL18_MVL19_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVL18_MVL19_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVL18[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVL19[0].soma], weight: 1.0
        #h("a_MVL18[0].soma { syn_NC_MVL18_MVL19_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVL19[0].soma { syn_NC_MVL18_MVL19_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVL18_MVL19_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVL19[0].soma.v(0.5)")
        h("setpointer syn_NC_MVL18_MVL19_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVL18[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVL19_MVL18_Generic_GJ
        print("Adding electrical projection: NC_MVL19_MVL18_Generic_GJ from MVL19 to MVL18, with 1 connection(s)")

        #h("objectvar syn_NC_MVL19_MVL18_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVL19_MVL18_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVL19[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVL18[0].soma], weight: 1.0
        #h("a_MVL19[0].soma { syn_NC_MVL19_MVL18_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVL18[0].soma { syn_NC_MVL19_MVL18_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVL19_MVL18_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVL18[0].soma.v(0.5)")
        h("setpointer syn_NC_MVL19_MVL18_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVL19[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVL19_MVL20_Generic_GJ
        print("Adding electrical projection: NC_MVL19_MVL20_Generic_GJ from MVL19 to MVL20, with 1 connection(s)")

        #h("objectvar syn_NC_MVL19_MVL20_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVL19_MVL20_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVL19[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVL20[0].soma], weight: 1.0
        #h("a_MVL19[0].soma { syn_NC_MVL19_MVL20_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVL20[0].soma { syn_NC_MVL19_MVL20_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVL19_MVL20_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVL20[0].soma.v(0.5)")
        h("setpointer syn_NC_MVL19_MVL20_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVL19[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVL20_MVL19_Generic_GJ
        print("Adding electrical projection: NC_MVL20_MVL19_Generic_GJ from MVL20 to MVL19, with 1 connection(s)")

        #h("objectvar syn_NC_MVL20_MVL19_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVL20_MVL19_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVL20[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVL19[0].soma], weight: 1.0
        #h("a_MVL20[0].soma { syn_NC_MVL20_MVL19_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVL19[0].soma { syn_NC_MVL20_MVL19_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVL20_MVL19_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVL19[0].soma.v(0.5)")
        h("setpointer syn_NC_MVL20_MVL19_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVL20[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVL20_MVL21_Generic_GJ
        print("Adding electrical projection: NC_MVL20_MVL21_Generic_GJ from MVL20 to MVL21, with 1 connection(s)")

        #h("objectvar syn_NC_MVL20_MVL21_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVL20_MVL21_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVL20[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVL21[0].soma], weight: 1.0
        #h("a_MVL20[0].soma { syn_NC_MVL20_MVL21_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVL21[0].soma { syn_NC_MVL20_MVL21_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVL20_MVL21_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVL21[0].soma.v(0.5)")
        h("setpointer syn_NC_MVL20_MVL21_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVL20[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVL21_MVL20_Generic_GJ
        print("Adding electrical projection: NC_MVL21_MVL20_Generic_GJ from MVL21 to MVL20, with 1 connection(s)")

        #h("objectvar syn_NC_MVL21_MVL20_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVL21_MVL20_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVL21[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVL20[0].soma], weight: 1.0
        #h("a_MVL21[0].soma { syn_NC_MVL21_MVL20_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVL20[0].soma { syn_NC_MVL21_MVL20_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVL21_MVL20_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVL20[0].soma.v(0.5)")
        h("setpointer syn_NC_MVL21_MVL20_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVL21[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVL21_MVL22_Generic_GJ
        print("Adding electrical projection: NC_MVL21_MVL22_Generic_GJ from MVL21 to MVL22, with 1 connection(s)")

        #h("objectvar syn_NC_MVL21_MVL22_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVL21_MVL22_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVL21[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVL22[0].soma], weight: 1.0
        #h("a_MVL21[0].soma { syn_NC_MVL21_MVL22_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVL22[0].soma { syn_NC_MVL21_MVL22_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVL21_MVL22_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVL22[0].soma.v(0.5)")
        h("setpointer syn_NC_MVL21_MVL22_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVL21[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVL22_MVL21_Generic_GJ
        print("Adding electrical projection: NC_MVL22_MVL21_Generic_GJ from MVL22 to MVL21, with 1 connection(s)")

        #h("objectvar syn_NC_MVL22_MVL21_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVL22_MVL21_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVL22[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVL21[0].soma], weight: 1.0
        #h("a_MVL22[0].soma { syn_NC_MVL22_MVL21_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVL21[0].soma { syn_NC_MVL22_MVL21_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVL22_MVL21_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVL21[0].soma.v(0.5)")
        h("setpointer syn_NC_MVL22_MVL21_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVL22[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVL22_MVL23_Generic_GJ
        print("Adding electrical projection: NC_MVL22_MVL23_Generic_GJ from MVL22 to MVL23, with 1 connection(s)")

        #h("objectvar syn_NC_MVL22_MVL23_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVL22_MVL23_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVL22[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVL23[0].soma], weight: 1.0
        #h("a_MVL22[0].soma { syn_NC_MVL22_MVL23_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVL23[0].soma { syn_NC_MVL22_MVL23_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVL22_MVL23_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVL23[0].soma.v(0.5)")
        h("setpointer syn_NC_MVL22_MVL23_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVL22[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVL23_MVL22_Generic_GJ
        print("Adding electrical projection: NC_MVL23_MVL22_Generic_GJ from MVL23 to MVL22, with 1 connection(s)")

        #h("objectvar syn_NC_MVL23_MVL22_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVL23_MVL22_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVL23[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVL22[0].soma], weight: 1.0
        #h("a_MVL23[0].soma { syn_NC_MVL23_MVL22_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVL22[0].soma { syn_NC_MVL23_MVL22_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVL23_MVL22_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVL22[0].soma.v(0.5)")
        h("setpointer syn_NC_MVL23_MVL22_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVL23[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVR01_MVR02_Generic_GJ
        print("Adding electrical projection: NC_MVR01_MVR02_Generic_GJ from MVR01 to MVR02, with 1 connection(s)")

        #h("objectvar syn_NC_MVR01_MVR02_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVR01_MVR02_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVR01[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVR02[0].soma], weight: 1.0
        #h("a_MVR01[0].soma { syn_NC_MVR01_MVR02_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVR02[0].soma { syn_NC_MVR01_MVR02_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVR01_MVR02_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVR02[0].soma.v(0.5)")
        h("setpointer syn_NC_MVR01_MVR02_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVR01[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVR01_MVR03_Generic_GJ
        print("Adding electrical projection: NC_MVR01_MVR03_Generic_GJ from MVR01 to MVR03, with 1 connection(s)")

        #h("objectvar syn_NC_MVR01_MVR03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVR01_MVR03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVR01[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVR03[0].soma], weight: 1.0
        #h("a_MVR01[0].soma { syn_NC_MVR01_MVR03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVR03[0].soma { syn_NC_MVR01_MVR03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVR01_MVR03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVR03[0].soma.v(0.5)")
        h("setpointer syn_NC_MVR01_MVR03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVR01[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVR02_MVR01_Generic_GJ
        print("Adding electrical projection: NC_MVR02_MVR01_Generic_GJ from MVR02 to MVR01, with 1 connection(s)")

        #h("objectvar syn_NC_MVR02_MVR01_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVR02_MVR01_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVR02[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVR01[0].soma], weight: 1.0
        #h("a_MVR02[0].soma { syn_NC_MVR02_MVR01_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVR01[0].soma { syn_NC_MVR02_MVR01_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVR02_MVR01_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVR01[0].soma.v(0.5)")
        h("setpointer syn_NC_MVR02_MVR01_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVR02[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVR02_MVR03_Generic_GJ
        print("Adding electrical projection: NC_MVR02_MVR03_Generic_GJ from MVR02 to MVR03, with 1 connection(s)")

        #h("objectvar syn_NC_MVR02_MVR03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVR02_MVR03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVR02[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVR03[0].soma], weight: 1.0
        #h("a_MVR02[0].soma { syn_NC_MVR02_MVR03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVR03[0].soma { syn_NC_MVR02_MVR03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVR02_MVR03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVR03[0].soma.v(0.5)")
        h("setpointer syn_NC_MVR02_MVR03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVR02[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVR03_MVR01_Generic_GJ
        print("Adding electrical projection: NC_MVR03_MVR01_Generic_GJ from MVR03 to MVR01, with 1 connection(s)")

        #h("objectvar syn_NC_MVR03_MVR01_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVR03_MVR01_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVR03[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVR01[0].soma], weight: 1.0
        #h("a_MVR03[0].soma { syn_NC_MVR03_MVR01_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVR01[0].soma { syn_NC_MVR03_MVR01_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVR03_MVR01_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVR01[0].soma.v(0.5)")
        h("setpointer syn_NC_MVR03_MVR01_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVR03[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVR03_MVR02_Generic_GJ
        print("Adding electrical projection: NC_MVR03_MVR02_Generic_GJ from MVR03 to MVR02, with 1 connection(s)")

        #h("objectvar syn_NC_MVR03_MVR02_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVR03_MVR02_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVR03[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVR02[0].soma], weight: 1.0
        #h("a_MVR03[0].soma { syn_NC_MVR03_MVR02_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVR02[0].soma { syn_NC_MVR03_MVR02_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVR03_MVR02_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVR02[0].soma.v(0.5)")
        h("setpointer syn_NC_MVR03_MVR02_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVR03[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVR03_MVR04_Generic_GJ
        print("Adding electrical projection: NC_MVR03_MVR04_Generic_GJ from MVR03 to MVR04, with 1 connection(s)")

        #h("objectvar syn_NC_MVR03_MVR04_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVR03_MVR04_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVR03[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVR04[0].soma], weight: 1.0
        #h("a_MVR03[0].soma { syn_NC_MVR03_MVR04_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVR04[0].soma { syn_NC_MVR03_MVR04_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVR03_MVR04_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVR04[0].soma.v(0.5)")
        h("setpointer syn_NC_MVR03_MVR04_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVR03[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVR04_MVR03_Generic_GJ
        print("Adding electrical projection: NC_MVR04_MVR03_Generic_GJ from MVR04 to MVR03, with 1 connection(s)")

        #h("objectvar syn_NC_MVR04_MVR03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVR04_MVR03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVR04[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVR03[0].soma], weight: 1.0
        #h("a_MVR04[0].soma { syn_NC_MVR04_MVR03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVR03[0].soma { syn_NC_MVR04_MVR03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVR04_MVR03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVR03[0].soma.v(0.5)")
        h("setpointer syn_NC_MVR04_MVR03_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVR04[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVR04_MVR05_Generic_GJ
        print("Adding electrical projection: NC_MVR04_MVR05_Generic_GJ from MVR04 to MVR05, with 1 connection(s)")

        #h("objectvar syn_NC_MVR04_MVR05_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVR04_MVR05_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVR04[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVR05[0].soma], weight: 1.0
        #h("a_MVR04[0].soma { syn_NC_MVR04_MVR05_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVR05[0].soma { syn_NC_MVR04_MVR05_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVR04_MVR05_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVR05[0].soma.v(0.5)")
        h("setpointer syn_NC_MVR04_MVR05_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVR04[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVR05_MVR04_Generic_GJ
        print("Adding electrical projection: NC_MVR05_MVR04_Generic_GJ from MVR05 to MVR04, with 1 connection(s)")

        #h("objectvar syn_NC_MVR05_MVR04_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVR05_MVR04_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVR05[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVR04[0].soma], weight: 1.0
        #h("a_MVR05[0].soma { syn_NC_MVR05_MVR04_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVR04[0].soma { syn_NC_MVR05_MVR04_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVR05_MVR04_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVR04[0].soma.v(0.5)")
        h("setpointer syn_NC_MVR05_MVR04_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVR05[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVR05_MVR06_Generic_GJ
        print("Adding electrical projection: NC_MVR05_MVR06_Generic_GJ from MVR05 to MVR06, with 1 connection(s)")

        #h("objectvar syn_NC_MVR05_MVR06_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVR05_MVR06_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVR05[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVR06[0].soma], weight: 1.0
        #h("a_MVR05[0].soma { syn_NC_MVR05_MVR06_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVR06[0].soma { syn_NC_MVR05_MVR06_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVR05_MVR06_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVR06[0].soma.v(0.5)")
        h("setpointer syn_NC_MVR05_MVR06_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVR05[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVR06_MVR05_Generic_GJ
        print("Adding electrical projection: NC_MVR06_MVR05_Generic_GJ from MVR06 to MVR05, with 1 connection(s)")

        #h("objectvar syn_NC_MVR06_MVR05_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVR06_MVR05_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVR06[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVR05[0].soma], weight: 1.0
        #h("a_MVR06[0].soma { syn_NC_MVR06_MVR05_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVR05[0].soma { syn_NC_MVR06_MVR05_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVR06_MVR05_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVR05[0].soma.v(0.5)")
        h("setpointer syn_NC_MVR06_MVR05_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVR06[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVR06_MVR07_Generic_GJ
        print("Adding electrical projection: NC_MVR06_MVR07_Generic_GJ from MVR06 to MVR07, with 1 connection(s)")

        #h("objectvar syn_NC_MVR06_MVR07_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVR06_MVR07_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVR06[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVR07[0].soma], weight: 1.0
        #h("a_MVR06[0].soma { syn_NC_MVR06_MVR07_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVR07[0].soma { syn_NC_MVR06_MVR07_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVR06_MVR07_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVR07[0].soma.v(0.5)")
        h("setpointer syn_NC_MVR06_MVR07_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVR06[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVR07_MVR06_Generic_GJ
        print("Adding electrical projection: NC_MVR07_MVR06_Generic_GJ from MVR07 to MVR06, with 1 connection(s)")

        #h("objectvar syn_NC_MVR07_MVR06_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVR07_MVR06_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVR07[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVR06[0].soma], weight: 1.0
        #h("a_MVR07[0].soma { syn_NC_MVR07_MVR06_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVR06[0].soma { syn_NC_MVR07_MVR06_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVR07_MVR06_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVR06[0].soma.v(0.5)")
        h("setpointer syn_NC_MVR07_MVR06_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVR07[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVR07_MVR08_Generic_GJ
        print("Adding electrical projection: NC_MVR07_MVR08_Generic_GJ from MVR07 to MVR08, with 1 connection(s)")

        #h("objectvar syn_NC_MVR07_MVR08_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVR07_MVR08_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVR07[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVR08[0].soma], weight: 1.0
        #h("a_MVR07[0].soma { syn_NC_MVR07_MVR08_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVR08[0].soma { syn_NC_MVR07_MVR08_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVR07_MVR08_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVR08[0].soma.v(0.5)")
        h("setpointer syn_NC_MVR07_MVR08_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVR07[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVR08_MVL09_Generic_GJ
        print("Adding electrical projection: NC_MVR08_MVL09_Generic_GJ from MVR08 to MVL09, with 1 connection(s)")

        #h("objectvar syn_NC_MVR08_MVL09_Generic_GJ_muscle_to_muscle_elec_syn_2conns_A[1]")
        h("objectvar syn_NC_MVR08_MVL09_Generic_GJ_muscle_to_muscle_elec_syn_2conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVR08[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVL09[0].soma], weight: 1.0
        #h("a_MVR08[0].soma { syn_NC_MVR08_MVL09_Generic_GJ_muscle_to_muscle_elec_syn_2conns_A[0] = new muscle_to_muscle_elec_syn_2conns(0.5) }")
        h("a_MVL09[0].soma { syn_NC_MVR08_MVL09_Generic_GJ_muscle_to_muscle_elec_syn_2conns_B[0] = new muscle_to_muscle_elec_syn_2conns(0.5) }")
        #h("setpointer syn_NC_MVR08_MVL09_Generic_GJ_muscle_to_muscle_elec_syn_2conns_A[0].vpeer, a_MVL09[0].soma.v(0.5)")
        h("setpointer syn_NC_MVR08_MVL09_Generic_GJ_muscle_to_muscle_elec_syn_2conns_B[0].vpeer, a_MVR08[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVR08_MVR07_Generic_GJ
        print("Adding electrical projection: NC_MVR08_MVR07_Generic_GJ from MVR08 to MVR07, with 1 connection(s)")

        #h("objectvar syn_NC_MVR08_MVR07_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVR08_MVR07_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVR08[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVR07[0].soma], weight: 1.0
        #h("a_MVR08[0].soma { syn_NC_MVR08_MVR07_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVR07[0].soma { syn_NC_MVR08_MVR07_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVR08_MVR07_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVR07[0].soma.v(0.5)")
        h("setpointer syn_NC_MVR08_MVR07_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVR08[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVR08_MVR09_Generic_GJ
        print("Adding electrical projection: NC_MVR08_MVR09_Generic_GJ from MVR08 to MVR09, with 1 connection(s)")

        #h("objectvar syn_NC_MVR08_MVR09_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVR08_MVR09_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVR08[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVR09[0].soma], weight: 1.0
        #h("a_MVR08[0].soma { syn_NC_MVR08_MVR09_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVR09[0].soma { syn_NC_MVR08_MVR09_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVR08_MVR09_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVR09[0].soma.v(0.5)")
        h("setpointer syn_NC_MVR08_MVR09_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVR08[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVR09_MVR08_Generic_GJ
        print("Adding electrical projection: NC_MVR09_MVR08_Generic_GJ from MVR09 to MVR08, with 1 connection(s)")

        #h("objectvar syn_NC_MVR09_MVR08_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVR09_MVR08_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVR09[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVR08[0].soma], weight: 1.0
        #h("a_MVR09[0].soma { syn_NC_MVR09_MVR08_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVR08[0].soma { syn_NC_MVR09_MVR08_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVR09_MVR08_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVR08[0].soma.v(0.5)")
        h("setpointer syn_NC_MVR09_MVR08_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVR09[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVR09_MVR10_Generic_GJ
        print("Adding electrical projection: NC_MVR09_MVR10_Generic_GJ from MVR09 to MVR10, with 1 connection(s)")

        #h("objectvar syn_NC_MVR09_MVR10_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVR09_MVR10_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVR09[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVR10[0].soma], weight: 1.0
        #h("a_MVR09[0].soma { syn_NC_MVR09_MVR10_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVR10[0].soma { syn_NC_MVR09_MVR10_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVR09_MVR10_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVR10[0].soma.v(0.5)")
        h("setpointer syn_NC_MVR09_MVR10_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVR09[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVR10_MVR09_Generic_GJ
        print("Adding electrical projection: NC_MVR10_MVR09_Generic_GJ from MVR10 to MVR09, with 1 connection(s)")

        #h("objectvar syn_NC_MVR10_MVR09_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVR10_MVR09_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVR10[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVR09[0].soma], weight: 1.0
        #h("a_MVR10[0].soma { syn_NC_MVR10_MVR09_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVR09[0].soma { syn_NC_MVR10_MVR09_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVR10_MVR09_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVR09[0].soma.v(0.5)")
        h("setpointer syn_NC_MVR10_MVR09_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVR10[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVR10_MVR11_Generic_GJ
        print("Adding electrical projection: NC_MVR10_MVR11_Generic_GJ from MVR10 to MVR11, with 1 connection(s)")

        #h("objectvar syn_NC_MVR10_MVR11_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVR10_MVR11_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVR10[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVR11[0].soma], weight: 1.0
        #h("a_MVR10[0].soma { syn_NC_MVR10_MVR11_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVR11[0].soma { syn_NC_MVR10_MVR11_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVR10_MVR11_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVR11[0].soma.v(0.5)")
        h("setpointer syn_NC_MVR10_MVR11_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVR10[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVR11_MVR10_Generic_GJ
        print("Adding electrical projection: NC_MVR11_MVR10_Generic_GJ from MVR11 to MVR10, with 1 connection(s)")

        #h("objectvar syn_NC_MVR11_MVR10_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVR11_MVR10_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVR11[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVR10[0].soma], weight: 1.0
        #h("a_MVR11[0].soma { syn_NC_MVR11_MVR10_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVR10[0].soma { syn_NC_MVR11_MVR10_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVR11_MVR10_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVR10[0].soma.v(0.5)")
        h("setpointer syn_NC_MVR11_MVR10_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVR11[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVR11_MVR12_Generic_GJ
        print("Adding electrical projection: NC_MVR11_MVR12_Generic_GJ from MVR11 to MVR12, with 1 connection(s)")

        #h("objectvar syn_NC_MVR11_MVR12_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVR11_MVR12_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVR11[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVR12[0].soma], weight: 1.0
        #h("a_MVR11[0].soma { syn_NC_MVR11_MVR12_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVR12[0].soma { syn_NC_MVR11_MVR12_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVR11_MVR12_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVR12[0].soma.v(0.5)")
        h("setpointer syn_NC_MVR11_MVR12_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVR11[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVR12_MVR11_Generic_GJ
        print("Adding electrical projection: NC_MVR12_MVR11_Generic_GJ from MVR12 to MVR11, with 1 connection(s)")

        #h("objectvar syn_NC_MVR12_MVR11_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVR12_MVR11_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVR12[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVR11[0].soma], weight: 1.0
        #h("a_MVR12[0].soma { syn_NC_MVR12_MVR11_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVR11[0].soma { syn_NC_MVR12_MVR11_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVR12_MVR11_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVR11[0].soma.v(0.5)")
        h("setpointer syn_NC_MVR12_MVR11_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVR12[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVR12_MVR13_Generic_GJ
        print("Adding electrical projection: NC_MVR12_MVR13_Generic_GJ from MVR12 to MVR13, with 1 connection(s)")

        #h("objectvar syn_NC_MVR12_MVR13_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVR12_MVR13_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVR12[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVR13[0].soma], weight: 1.0
        #h("a_MVR12[0].soma { syn_NC_MVR12_MVR13_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVR13[0].soma { syn_NC_MVR12_MVR13_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVR12_MVR13_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVR13[0].soma.v(0.5)")
        h("setpointer syn_NC_MVR12_MVR13_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVR12[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVR13_MVR12_Generic_GJ
        print("Adding electrical projection: NC_MVR13_MVR12_Generic_GJ from MVR13 to MVR12, with 1 connection(s)")

        #h("objectvar syn_NC_MVR13_MVR12_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVR13_MVR12_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVR13[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVR12[0].soma], weight: 1.0
        #h("a_MVR13[0].soma { syn_NC_MVR13_MVR12_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVR12[0].soma { syn_NC_MVR13_MVR12_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVR13_MVR12_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVR12[0].soma.v(0.5)")
        h("setpointer syn_NC_MVR13_MVR12_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVR13[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVR13_MVR14_Generic_GJ
        print("Adding electrical projection: NC_MVR13_MVR14_Generic_GJ from MVR13 to MVR14, with 1 connection(s)")

        #h("objectvar syn_NC_MVR13_MVR14_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVR13_MVR14_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVR13[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVR14[0].soma], weight: 1.0
        #h("a_MVR13[0].soma { syn_NC_MVR13_MVR14_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVR14[0].soma { syn_NC_MVR13_MVR14_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVR13_MVR14_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVR14[0].soma.v(0.5)")
        h("setpointer syn_NC_MVR13_MVR14_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVR13[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVR14_MVR13_Generic_GJ
        print("Adding electrical projection: NC_MVR14_MVR13_Generic_GJ from MVR14 to MVR13, with 1 connection(s)")

        #h("objectvar syn_NC_MVR14_MVR13_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVR14_MVR13_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVR14[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVR13[0].soma], weight: 1.0
        #h("a_MVR14[0].soma { syn_NC_MVR14_MVR13_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVR13[0].soma { syn_NC_MVR14_MVR13_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVR14_MVR13_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVR13[0].soma.v(0.5)")
        h("setpointer syn_NC_MVR14_MVR13_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVR14[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVR14_MVR15_Generic_GJ
        print("Adding electrical projection: NC_MVR14_MVR15_Generic_GJ from MVR14 to MVR15, with 1 connection(s)")

        #h("objectvar syn_NC_MVR14_MVR15_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVR14_MVR15_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVR14[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVR15[0].soma], weight: 1.0
        #h("a_MVR14[0].soma { syn_NC_MVR14_MVR15_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVR15[0].soma { syn_NC_MVR14_MVR15_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVR14_MVR15_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVR15[0].soma.v(0.5)")
        h("setpointer syn_NC_MVR14_MVR15_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVR14[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVR15_MVR14_Generic_GJ
        print("Adding electrical projection: NC_MVR15_MVR14_Generic_GJ from MVR15 to MVR14, with 1 connection(s)")

        #h("objectvar syn_NC_MVR15_MVR14_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVR15_MVR14_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVR15[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVR14[0].soma], weight: 1.0
        #h("a_MVR15[0].soma { syn_NC_MVR15_MVR14_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVR14[0].soma { syn_NC_MVR15_MVR14_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVR15_MVR14_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVR14[0].soma.v(0.5)")
        h("setpointer syn_NC_MVR15_MVR14_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVR15[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVR15_MVR16_Generic_GJ
        print("Adding electrical projection: NC_MVR15_MVR16_Generic_GJ from MVR15 to MVR16, with 1 connection(s)")

        #h("objectvar syn_NC_MVR15_MVR16_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVR15_MVR16_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVR15[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVR16[0].soma], weight: 1.0
        #h("a_MVR15[0].soma { syn_NC_MVR15_MVR16_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVR16[0].soma { syn_NC_MVR15_MVR16_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVR15_MVR16_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVR16[0].soma.v(0.5)")
        h("setpointer syn_NC_MVR15_MVR16_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVR15[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVR16_MVR15_Generic_GJ
        print("Adding electrical projection: NC_MVR16_MVR15_Generic_GJ from MVR16 to MVR15, with 1 connection(s)")

        #h("objectvar syn_NC_MVR16_MVR15_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVR16_MVR15_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVR16[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVR15[0].soma], weight: 1.0
        #h("a_MVR16[0].soma { syn_NC_MVR16_MVR15_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVR15[0].soma { syn_NC_MVR16_MVR15_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVR16_MVR15_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVR15[0].soma.v(0.5)")
        h("setpointer syn_NC_MVR16_MVR15_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVR16[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVR16_MVR17_Generic_GJ
        print("Adding electrical projection: NC_MVR16_MVR17_Generic_GJ from MVR16 to MVR17, with 1 connection(s)")

        #h("objectvar syn_NC_MVR16_MVR17_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVR16_MVR17_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVR16[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVR17[0].soma], weight: 1.0
        #h("a_MVR16[0].soma { syn_NC_MVR16_MVR17_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVR17[0].soma { syn_NC_MVR16_MVR17_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVR16_MVR17_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVR17[0].soma.v(0.5)")
        h("setpointer syn_NC_MVR16_MVR17_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVR16[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVR17_MVR16_Generic_GJ
        print("Adding electrical projection: NC_MVR17_MVR16_Generic_GJ from MVR17 to MVR16, with 1 connection(s)")

        #h("objectvar syn_NC_MVR17_MVR16_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVR17_MVR16_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVR17[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVR16[0].soma], weight: 1.0
        #h("a_MVR17[0].soma { syn_NC_MVR17_MVR16_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVR16[0].soma { syn_NC_MVR17_MVR16_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVR17_MVR16_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVR16[0].soma.v(0.5)")
        h("setpointer syn_NC_MVR17_MVR16_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVR17[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVR17_MVR18_Generic_GJ
        print("Adding electrical projection: NC_MVR17_MVR18_Generic_GJ from MVR17 to MVR18, with 1 connection(s)")

        #h("objectvar syn_NC_MVR17_MVR18_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVR17_MVR18_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVR17[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVR18[0].soma], weight: 1.0
        #h("a_MVR17[0].soma { syn_NC_MVR17_MVR18_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVR18[0].soma { syn_NC_MVR17_MVR18_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVR17_MVR18_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVR18[0].soma.v(0.5)")
        h("setpointer syn_NC_MVR17_MVR18_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVR17[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVR18_MVR17_Generic_GJ
        print("Adding electrical projection: NC_MVR18_MVR17_Generic_GJ from MVR18 to MVR17, with 1 connection(s)")

        #h("objectvar syn_NC_MVR18_MVR17_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVR18_MVR17_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVR18[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVR17[0].soma], weight: 1.0
        #h("a_MVR18[0].soma { syn_NC_MVR18_MVR17_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVR17[0].soma { syn_NC_MVR18_MVR17_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVR18_MVR17_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVR17[0].soma.v(0.5)")
        h("setpointer syn_NC_MVR18_MVR17_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVR18[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVR18_MVR19_Generic_GJ
        print("Adding electrical projection: NC_MVR18_MVR19_Generic_GJ from MVR18 to MVR19, with 1 connection(s)")

        #h("objectvar syn_NC_MVR18_MVR19_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVR18_MVR19_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVR18[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVR19[0].soma], weight: 1.0
        #h("a_MVR18[0].soma { syn_NC_MVR18_MVR19_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVR19[0].soma { syn_NC_MVR18_MVR19_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVR18_MVR19_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVR19[0].soma.v(0.5)")
        h("setpointer syn_NC_MVR18_MVR19_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVR18[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVR19_MVR18_Generic_GJ
        print("Adding electrical projection: NC_MVR19_MVR18_Generic_GJ from MVR19 to MVR18, with 1 connection(s)")

        #h("objectvar syn_NC_MVR19_MVR18_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVR19_MVR18_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVR19[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVR18[0].soma], weight: 1.0
        #h("a_MVR19[0].soma { syn_NC_MVR19_MVR18_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVR18[0].soma { syn_NC_MVR19_MVR18_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVR19_MVR18_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVR18[0].soma.v(0.5)")
        h("setpointer syn_NC_MVR19_MVR18_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVR19[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVR19_MVR20_Generic_GJ
        print("Adding electrical projection: NC_MVR19_MVR20_Generic_GJ from MVR19 to MVR20, with 1 connection(s)")

        #h("objectvar syn_NC_MVR19_MVR20_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVR19_MVR20_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVR19[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVR20[0].soma], weight: 1.0
        #h("a_MVR19[0].soma { syn_NC_MVR19_MVR20_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVR20[0].soma { syn_NC_MVR19_MVR20_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVR19_MVR20_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVR20[0].soma.v(0.5)")
        h("setpointer syn_NC_MVR19_MVR20_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVR19[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVR20_MVR19_Generic_GJ
        print("Adding electrical projection: NC_MVR20_MVR19_Generic_GJ from MVR20 to MVR19, with 1 connection(s)")

        #h("objectvar syn_NC_MVR20_MVR19_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVR20_MVR19_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVR20[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVR19[0].soma], weight: 1.0
        #h("a_MVR20[0].soma { syn_NC_MVR20_MVR19_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVR19[0].soma { syn_NC_MVR20_MVR19_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVR20_MVR19_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVR19[0].soma.v(0.5)")
        h("setpointer syn_NC_MVR20_MVR19_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVR20[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVR20_MVR21_Generic_GJ
        print("Adding electrical projection: NC_MVR20_MVR21_Generic_GJ from MVR20 to MVR21, with 1 connection(s)")

        #h("objectvar syn_NC_MVR20_MVR21_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVR20_MVR21_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVR20[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVR21[0].soma], weight: 1.0
        #h("a_MVR20[0].soma { syn_NC_MVR20_MVR21_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVR21[0].soma { syn_NC_MVR20_MVR21_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVR20_MVR21_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVR21[0].soma.v(0.5)")
        h("setpointer syn_NC_MVR20_MVR21_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVR20[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVR21_MVR20_Generic_GJ
        print("Adding electrical projection: NC_MVR21_MVR20_Generic_GJ from MVR21 to MVR20, with 1 connection(s)")

        #h("objectvar syn_NC_MVR21_MVR20_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVR21_MVR20_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVR21[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVR20[0].soma], weight: 1.0
        #h("a_MVR21[0].soma { syn_NC_MVR21_MVR20_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVR20[0].soma { syn_NC_MVR21_MVR20_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVR21_MVR20_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVR20[0].soma.v(0.5)")
        h("setpointer syn_NC_MVR21_MVR20_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVR21[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVR21_MVR22_Generic_GJ
        print("Adding electrical projection: NC_MVR21_MVR22_Generic_GJ from MVR21 to MVR22, with 1 connection(s)")

        #h("objectvar syn_NC_MVR21_MVR22_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVR21_MVR22_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVR21[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVR22[0].soma], weight: 1.0
        #h("a_MVR21[0].soma { syn_NC_MVR21_MVR22_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVR22[0].soma { syn_NC_MVR21_MVR22_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVR21_MVR22_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVR22[0].soma.v(0.5)")
        h("setpointer syn_NC_MVR21_MVR22_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVR21[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVR22_MVR21_Generic_GJ
        print("Adding electrical projection: NC_MVR22_MVR21_Generic_GJ from MVR22 to MVR21, with 1 connection(s)")

        #h("objectvar syn_NC_MVR22_MVR21_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVR22_MVR21_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVR22[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVR21[0].soma], weight: 1.0
        #h("a_MVR22[0].soma { syn_NC_MVR22_MVR21_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVR21[0].soma { syn_NC_MVR22_MVR21_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVR22_MVR21_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVR21[0].soma.v(0.5)")
        h("setpointer syn_NC_MVR22_MVR21_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVR22[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVR22_MVR23_Generic_GJ
        print("Adding electrical projection: NC_MVR22_MVR23_Generic_GJ from MVR22 to MVR23, with 1 connection(s)")

        #h("objectvar syn_NC_MVR22_MVR23_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVR22_MVR23_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVR22[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVR23[0].soma], weight: 1.0
        #h("a_MVR22[0].soma { syn_NC_MVR22_MVR23_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVR23[0].soma { syn_NC_MVR22_MVR23_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVR22_MVR23_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVR23[0].soma.v(0.5)")
        h("setpointer syn_NC_MVR22_MVR23_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVR22[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_MVR23_MVR22_Generic_GJ
        print("Adding electrical projection: NC_MVR23_MVR22_Generic_GJ from MVR23 to MVR22, with 1 connection(s)")

        #h("objectvar syn_NC_MVR23_MVR22_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[1]")
        h("objectvar syn_NC_MVR23_MVR22_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_MVR23[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVR22[0].soma], weight: 1.0
        #h("a_MVR23[0].soma { syn_NC_MVR23_MVR22_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        h("a_MVR22[0].soma { syn_NC_MVR23_MVR22_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0] = new muscle_to_muscle_elec_syn_15conns(0.5) }")
        #h("setpointer syn_NC_MVR23_MVR22_Generic_GJ_muscle_to_muscle_elec_syn_15conns_A[0].vpeer, a_MVR22[0].soma.v(0.5)")
        h("setpointer syn_NC_MVR23_MVR22_Generic_GJ_muscle_to_muscle_elec_syn_15conns_B[0].vpeer, a_MVR23[0].soma.v(0.5)")

        # ######################   Continuous Projection: NC_AVBL_AVBR_Acetylcholine
        print("Adding continuous projection: NC_AVBL_AVBR_Acetylcholine from AVBL to AVBR, with 1 connection(s)")

        h("objectvar syn_NC_AVBL_AVBR_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_AVBL_AVBR_Acetylcholine_neuron_to_neuron_exc_syn_6conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVBL[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVBR[0].soma], weight: 1.0
        h("a_AVBL[0].soma { syn_NC_AVBL_AVBR_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_AVBR[0].soma { syn_NC_AVBL_AVBR_Acetylcholine_neuron_to_neuron_exc_syn_6conns_post[0] = new neuron_to_neuron_exc_syn_6conns(0.500000) }")
        h("setpointer syn_NC_AVBL_AVBR_Acetylcholine_silent_pre[0].vpeer, a_AVBR[0].soma.v(0.500000)")
        h("setpointer syn_NC_AVBL_AVBR_Acetylcholine_neuron_to_neuron_exc_syn_6conns_post[0].vpeer, a_AVBL[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_AVBR_AVBL_Acetylcholine
        print("Adding continuous projection: NC_AVBR_AVBL_Acetylcholine from AVBR to AVBL, with 1 connection(s)")

        h("objectvar syn_NC_AVBR_AVBL_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_AVBR_AVBL_Acetylcholine_neuron_to_neuron_exc_syn_2conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVBR[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVBL[0].soma], weight: 1.0
        h("a_AVBR[0].soma { syn_NC_AVBR_AVBL_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_AVBL[0].soma { syn_NC_AVBR_AVBL_Acetylcholine_neuron_to_neuron_exc_syn_2conns_post[0] = new neuron_to_neuron_exc_syn_2conns(0.500000) }")
        h("setpointer syn_NC_AVBR_AVBL_Acetylcholine_silent_pre[0].vpeer, a_AVBL[0].soma.v(0.500000)")
        h("setpointer syn_NC_AVBR_AVBL_Acetylcholine_neuron_to_neuron_exc_syn_2conns_post[0].vpeer, a_AVBR[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_AVBR_DB4_Acetylcholine
        print("Adding continuous projection: NC_AVBR_DB4_Acetylcholine from AVBR to DB4, with 1 connection(s)")

        h("objectvar syn_NC_AVBR_DB4_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_AVBR_DB4_Acetylcholine_neuron_to_neuron_exc_syn_1conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVBR[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DB4[0].soma], weight: 1.0
        h("a_AVBR[0].soma { syn_NC_AVBR_DB4_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_DB4[0].soma { syn_NC_AVBR_DB4_Acetylcholine_neuron_to_neuron_exc_syn_1conns_post[0] = new neuron_to_neuron_exc_syn_1conns(0.500000) }")
        h("setpointer syn_NC_AVBR_DB4_Acetylcholine_silent_pre[0].vpeer, a_DB4[0].soma.v(0.500000)")
        h("setpointer syn_NC_AVBR_DB4_Acetylcholine_neuron_to_neuron_exc_syn_1conns_post[0].vpeer, a_AVBR[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_AVBR_MVL16_Acetylcholine
        print("Adding continuous projection: NC_AVBR_MVL16_Acetylcholine from AVBR to MVL16, with 1 connection(s)")

        h("objectvar syn_NC_AVBR_MVL16_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_AVBR_MVL16_Acetylcholine_neuron_to_muscle_exc_syn_1conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVBR[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MVL16[0].soma], weight: 1.0
        h("a_AVBR[0].soma { syn_NC_AVBR_MVL16_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MVL16[0].soma { syn_NC_AVBR_MVL16_Acetylcholine_neuron_to_muscle_exc_syn_1conns_post[0] = new neuron_to_muscle_exc_syn_1conns(0.500000) }")
        h("setpointer syn_NC_AVBR_MVL16_Acetylcholine_silent_pre[0].vpeer, a_MVL16[0].soma.v(0.500000)")
        h("setpointer syn_NC_AVBR_MVL16_Acetylcholine_neuron_to_muscle_exc_syn_1conns_post[0].vpeer, a_AVBR[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB1_MDL06_Acetylcholine
        print("Adding continuous projection: NC_DB1_MDL06_Acetylcholine from DB1 to MDL06, with 1 connection(s)")

        h("objectvar syn_NC_DB1_MDL06_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB1_MDL06_Acetylcholine_DB1_to_MDL06_exc_syn_3conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB1[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL06[0].soma], weight: 1.0
        h("a_DB1[0].soma { syn_NC_DB1_MDL06_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDL06[0].soma { syn_NC_DB1_MDL06_Acetylcholine_DB1_to_MDL06_exc_syn_3conns_post[0] = new DB1_to_MDL06_exc_syn_3conns(0.500000) }")
        h("setpointer syn_NC_DB1_MDL06_Acetylcholine_silent_pre[0].vpeer, a_MDL06[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB1_MDL06_Acetylcholine_DB1_to_MDL06_exc_syn_3conns_post[0].vpeer, a_DB1[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB1_MDL08_Acetylcholine
        print("Adding continuous projection: NC_DB1_MDL08_Acetylcholine from DB1 to MDL08, with 1 connection(s)")

        h("objectvar syn_NC_DB1_MDL08_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB1_MDL08_Acetylcholine_DB1_to_MDL08_exc_syn_3conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB1[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL08[0].soma], weight: 1.0
        h("a_DB1[0].soma { syn_NC_DB1_MDL08_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDL08[0].soma { syn_NC_DB1_MDL08_Acetylcholine_DB1_to_MDL08_exc_syn_3conns_post[0] = new DB1_to_MDL08_exc_syn_3conns(0.500000) }")
        h("setpointer syn_NC_DB1_MDL08_Acetylcholine_silent_pre[0].vpeer, a_MDL08[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB1_MDL08_Acetylcholine_DB1_to_MDL08_exc_syn_3conns_post[0].vpeer, a_DB1[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB1_MDL09_Acetylcholine
        print("Adding continuous projection: NC_DB1_MDL09_Acetylcholine from DB1 to MDL09, with 1 connection(s)")

        h("objectvar syn_NC_DB1_MDL09_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB1_MDL09_Acetylcholine_DB1_to_MDL09_exc_syn_6conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB1[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL09[0].soma], weight: 1.0
        h("a_DB1[0].soma { syn_NC_DB1_MDL09_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDL09[0].soma { syn_NC_DB1_MDL09_Acetylcholine_DB1_to_MDL09_exc_syn_6conns_post[0] = new DB1_to_MDL09_exc_syn_6conns(0.500000) }")
        h("setpointer syn_NC_DB1_MDL09_Acetylcholine_silent_pre[0].vpeer, a_MDL09[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB1_MDL09_Acetylcholine_DB1_to_MDL09_exc_syn_6conns_post[0].vpeer, a_DB1[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB1_MDR08_Acetylcholine
        print("Adding continuous projection: NC_DB1_MDR08_Acetylcholine from DB1 to MDR08, with 1 connection(s)")

        h("objectvar syn_NC_DB1_MDR08_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB1_MDR08_Acetylcholine_DB1_to_MDR08_exc_syn_6conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB1[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR08[0].soma], weight: 1.0
        h("a_DB1[0].soma { syn_NC_DB1_MDR08_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDR08[0].soma { syn_NC_DB1_MDR08_Acetylcholine_DB1_to_MDR08_exc_syn_6conns_post[0] = new DB1_to_MDR08_exc_syn_6conns(0.500000) }")
        h("setpointer syn_NC_DB1_MDR08_Acetylcholine_silent_pre[0].vpeer, a_MDR08[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB1_MDR08_Acetylcholine_DB1_to_MDR08_exc_syn_6conns_post[0].vpeer, a_DB1[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB1_MDR09_Acetylcholine
        print("Adding continuous projection: NC_DB1_MDR09_Acetylcholine from DB1 to MDR09, with 1 connection(s)")

        h("objectvar syn_NC_DB1_MDR09_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB1_MDR09_Acetylcholine_DB1_to_MDR09_exc_syn_2conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB1[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR09[0].soma], weight: 1.0
        h("a_DB1[0].soma { syn_NC_DB1_MDR09_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDR09[0].soma { syn_NC_DB1_MDR09_Acetylcholine_DB1_to_MDR09_exc_syn_2conns_post[0] = new DB1_to_MDR09_exc_syn_2conns(0.500000) }")
        h("setpointer syn_NC_DB1_MDR09_Acetylcholine_silent_pre[0].vpeer, a_MDR09[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB1_MDR09_Acetylcholine_DB1_to_MDR09_exc_syn_2conns_post[0].vpeer, a_DB1[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB2_MDL09_Acetylcholine
        print("Adding continuous projection: NC_DB2_MDL09_Acetylcholine from DB2 to MDL09, with 1 connection(s)")

        h("objectvar syn_NC_DB2_MDL09_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB2_MDL09_Acetylcholine_DB2_to_MDL09_exc_syn_2conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB2[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL09[0].soma], weight: 1.0
        h("a_DB2[0].soma { syn_NC_DB2_MDL09_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDL09[0].soma { syn_NC_DB2_MDL09_Acetylcholine_DB2_to_MDL09_exc_syn_2conns_post[0] = new DB2_to_MDL09_exc_syn_2conns(0.500000) }")
        h("setpointer syn_NC_DB2_MDL09_Acetylcholine_silent_pre[0].vpeer, a_MDL09[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB2_MDL09_Acetylcholine_DB2_to_MDL09_exc_syn_2conns_post[0].vpeer, a_DB2[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB2_MDL10_Acetylcholine
        print("Adding continuous projection: NC_DB2_MDL10_Acetylcholine from DB2 to MDL10, with 1 connection(s)")

        h("objectvar syn_NC_DB2_MDL10_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB2_MDL10_Acetylcholine_DB2_to_MDL10_exc_syn_4conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB2[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL10[0].soma], weight: 1.0
        h("a_DB2[0].soma { syn_NC_DB2_MDL10_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDL10[0].soma { syn_NC_DB2_MDL10_Acetylcholine_DB2_to_MDL10_exc_syn_4conns_post[0] = new DB2_to_MDL10_exc_syn_4conns(0.500000) }")
        h("setpointer syn_NC_DB2_MDL10_Acetylcholine_silent_pre[0].vpeer, a_MDL10[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB2_MDL10_Acetylcholine_DB2_to_MDL10_exc_syn_4conns_post[0].vpeer, a_DB2[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB2_MDL11_Acetylcholine
        print("Adding continuous projection: NC_DB2_MDL11_Acetylcholine from DB2 to MDL11, with 1 connection(s)")

        h("objectvar syn_NC_DB2_MDL11_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB2_MDL11_Acetylcholine_DB2_to_MDL11_exc_syn_5conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB2[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL11[0].soma], weight: 1.0
        h("a_DB2[0].soma { syn_NC_DB2_MDL11_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDL11[0].soma { syn_NC_DB2_MDL11_Acetylcholine_DB2_to_MDL11_exc_syn_5conns_post[0] = new DB2_to_MDL11_exc_syn_5conns(0.500000) }")
        h("setpointer syn_NC_DB2_MDL11_Acetylcholine_silent_pre[0].vpeer, a_MDL11[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB2_MDL11_Acetylcholine_DB2_to_MDL11_exc_syn_5conns_post[0].vpeer, a_DB2[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB2_MDL12_Acetylcholine
        print("Adding continuous projection: NC_DB2_MDL12_Acetylcholine from DB2 to MDL12, with 1 connection(s)")

        h("objectvar syn_NC_DB2_MDL12_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB2_MDL12_Acetylcholine_DB2_to_MDL12_exc_syn_1conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB2[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL12[0].soma], weight: 1.0
        h("a_DB2[0].soma { syn_NC_DB2_MDL12_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDL12[0].soma { syn_NC_DB2_MDL12_Acetylcholine_DB2_to_MDL12_exc_syn_1conns_post[0] = new DB2_to_MDL12_exc_syn_1conns(0.500000) }")
        h("setpointer syn_NC_DB2_MDL12_Acetylcholine_silent_pre[0].vpeer, a_MDL12[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB2_MDL12_Acetylcholine_DB2_to_MDL12_exc_syn_1conns_post[0].vpeer, a_DB2[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB2_MDR09_Acetylcholine
        print("Adding continuous projection: NC_DB2_MDR09_Acetylcholine from DB2 to MDR09, with 1 connection(s)")

        h("objectvar syn_NC_DB2_MDR09_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB2_MDR09_Acetylcholine_DB2_to_MDR09_exc_syn_1conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB2[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR09[0].soma], weight: 1.0
        h("a_DB2[0].soma { syn_NC_DB2_MDR09_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDR09[0].soma { syn_NC_DB2_MDR09_Acetylcholine_DB2_to_MDR09_exc_syn_1conns_post[0] = new DB2_to_MDR09_exc_syn_1conns(0.500000) }")
        h("setpointer syn_NC_DB2_MDR09_Acetylcholine_silent_pre[0].vpeer, a_MDR09[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB2_MDR09_Acetylcholine_DB2_to_MDR09_exc_syn_1conns_post[0].vpeer, a_DB2[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB2_MDR10_Acetylcholine
        print("Adding continuous projection: NC_DB2_MDR10_Acetylcholine from DB2 to MDR10, with 1 connection(s)")

        h("objectvar syn_NC_DB2_MDR10_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB2_MDR10_Acetylcholine_DB2_to_MDR10_exc_syn_6conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB2[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR10[0].soma], weight: 1.0
        h("a_DB2[0].soma { syn_NC_DB2_MDR10_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDR10[0].soma { syn_NC_DB2_MDR10_Acetylcholine_DB2_to_MDR10_exc_syn_6conns_post[0] = new DB2_to_MDR10_exc_syn_6conns(0.500000) }")
        h("setpointer syn_NC_DB2_MDR10_Acetylcholine_silent_pre[0].vpeer, a_MDR10[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB2_MDR10_Acetylcholine_DB2_to_MDR10_exc_syn_6conns_post[0].vpeer, a_DB2[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB2_MDR11_Acetylcholine
        print("Adding continuous projection: NC_DB2_MDR11_Acetylcholine from DB2 to MDR11, with 1 connection(s)")

        h("objectvar syn_NC_DB2_MDR11_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB2_MDR11_Acetylcholine_DB2_to_MDR11_exc_syn_8conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB2[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR11[0].soma], weight: 1.0
        h("a_DB2[0].soma { syn_NC_DB2_MDR11_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDR11[0].soma { syn_NC_DB2_MDR11_Acetylcholine_DB2_to_MDR11_exc_syn_8conns_post[0] = new DB2_to_MDR11_exc_syn_8conns(0.500000) }")
        h("setpointer syn_NC_DB2_MDR11_Acetylcholine_silent_pre[0].vpeer, a_MDR11[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB2_MDR11_Acetylcholine_DB2_to_MDR11_exc_syn_8conns_post[0].vpeer, a_DB2[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB3_MDL11_Acetylcholine
        print("Adding continuous projection: NC_DB3_MDL11_Acetylcholine from DB3 to MDL11, with 1 connection(s)")

        h("objectvar syn_NC_DB3_MDL11_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB3_MDL11_Acetylcholine_DB3_to_MDL11_exc_syn_6conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB3[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL11[0].soma], weight: 1.0
        h("a_DB3[0].soma { syn_NC_DB3_MDL11_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDL11[0].soma { syn_NC_DB3_MDL11_Acetylcholine_DB3_to_MDL11_exc_syn_6conns_post[0] = new DB3_to_MDL11_exc_syn_6conns(0.500000) }")
        h("setpointer syn_NC_DB3_MDL11_Acetylcholine_silent_pre[0].vpeer, a_MDL11[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB3_MDL11_Acetylcholine_DB3_to_MDL11_exc_syn_6conns_post[0].vpeer, a_DB3[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB3_MDL12_Acetylcholine
        print("Adding continuous projection: NC_DB3_MDL12_Acetylcholine from DB3 to MDL12, with 1 connection(s)")

        h("objectvar syn_NC_DB3_MDL12_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB3_MDL12_Acetylcholine_neuron_to_muscle_exc_syn_1conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB3[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL12[0].soma], weight: 1.0
        h("a_DB3[0].soma { syn_NC_DB3_MDL12_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDL12[0].soma { syn_NC_DB3_MDL12_Acetylcholine_neuron_to_muscle_exc_syn_1conns_post[0] = new neuron_to_muscle_exc_syn_1conns(0.500000) }")
        h("setpointer syn_NC_DB3_MDL12_Acetylcholine_silent_pre[0].vpeer, a_MDL12[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB3_MDL12_Acetylcholine_neuron_to_muscle_exc_syn_1conns_post[0].vpeer, a_DB3[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB3_MDL13_Acetylcholine
        print("Adding continuous projection: NC_DB3_MDL13_Acetylcholine from DB3 to MDL13, with 1 connection(s)")

        h("objectvar syn_NC_DB3_MDL13_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB3_MDL13_Acetylcholine_DB3_to_MDL13_exc_syn_3conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB3[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL13[0].soma], weight: 1.0
        h("a_DB3[0].soma { syn_NC_DB3_MDL13_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDL13[0].soma { syn_NC_DB3_MDL13_Acetylcholine_DB3_to_MDL13_exc_syn_3conns_post[0] = new DB3_to_MDL13_exc_syn_3conns(0.500000) }")
        h("setpointer syn_NC_DB3_MDL13_Acetylcholine_silent_pre[0].vpeer, a_MDL13[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB3_MDL13_Acetylcholine_DB3_to_MDL13_exc_syn_3conns_post[0].vpeer, a_DB3[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB3_MDL14_Acetylcholine
        print("Adding continuous projection: NC_DB3_MDL14_Acetylcholine from DB3 to MDL14, with 1 connection(s)")

        h("objectvar syn_NC_DB3_MDL14_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB3_MDL14_Acetylcholine_DB3_to_MDL14_exc_syn_1conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB3[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL14[0].soma], weight: 1.0
        h("a_DB3[0].soma { syn_NC_DB3_MDL14_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDL14[0].soma { syn_NC_DB3_MDL14_Acetylcholine_DB3_to_MDL14_exc_syn_1conns_post[0] = new DB3_to_MDL14_exc_syn_1conns(0.500000) }")
        h("setpointer syn_NC_DB3_MDL14_Acetylcholine_silent_pre[0].vpeer, a_MDL14[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB3_MDL14_Acetylcholine_DB3_to_MDL14_exc_syn_1conns_post[0].vpeer, a_DB3[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB3_MDR11_Acetylcholine
        print("Adding continuous projection: NC_DB3_MDR11_Acetylcholine from DB3 to MDR11, with 1 connection(s)")

        h("objectvar syn_NC_DB3_MDR11_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB3_MDR11_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB3[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR11[0].soma], weight: 1.0
        h("a_DB3[0].soma { syn_NC_DB3_MDR11_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDR11[0].soma { syn_NC_DB3_MDR11_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[0] = new neuron_to_muscle_exc_syn_2conns(0.500000) }")
        h("setpointer syn_NC_DB3_MDR11_Acetylcholine_silent_pre[0].vpeer, a_MDR11[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB3_MDR11_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[0].vpeer, a_DB3[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB3_MDR12_Acetylcholine
        print("Adding continuous projection: NC_DB3_MDR12_Acetylcholine from DB3 to MDR12, with 1 connection(s)")

        h("objectvar syn_NC_DB3_MDR12_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB3_MDR12_Acetylcholine_neuron_to_muscle_exc_syn_13conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB3[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR12[0].soma], weight: 1.0
        h("a_DB3[0].soma { syn_NC_DB3_MDR12_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDR12[0].soma { syn_NC_DB3_MDR12_Acetylcholine_neuron_to_muscle_exc_syn_13conns_post[0] = new neuron_to_muscle_exc_syn_13conns(0.500000) }")
        h("setpointer syn_NC_DB3_MDR12_Acetylcholine_silent_pre[0].vpeer, a_MDR12[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB3_MDR12_Acetylcholine_neuron_to_muscle_exc_syn_13conns_post[0].vpeer, a_DB3[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB3_MDR13_Acetylcholine
        print("Adding continuous projection: NC_DB3_MDR13_Acetylcholine from DB3 to MDR13, with 1 connection(s)")

        h("objectvar syn_NC_DB3_MDR13_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB3_MDR13_Acetylcholine_neuron_to_muscle_exc_syn_1conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB3[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR13[0].soma], weight: 1.0
        h("a_DB3[0].soma { syn_NC_DB3_MDR13_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDR13[0].soma { syn_NC_DB3_MDR13_Acetylcholine_neuron_to_muscle_exc_syn_1conns_post[0] = new neuron_to_muscle_exc_syn_1conns(0.500000) }")
        h("setpointer syn_NC_DB3_MDR13_Acetylcholine_silent_pre[0].vpeer, a_MDR13[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB3_MDR13_Acetylcholine_neuron_to_muscle_exc_syn_1conns_post[0].vpeer, a_DB3[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB4_MDL13_Acetylcholine
        print("Adding continuous projection: NC_DB4_MDL13_Acetylcholine from DB4 to MDL13, with 1 connection(s)")

        h("objectvar syn_NC_DB4_MDL13_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB4_MDL13_Acetylcholine_DB4_to_MDL13_exc_syn_4conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB4[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL13[0].soma], weight: 1.0
        h("a_DB4[0].soma { syn_NC_DB4_MDL13_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDL13[0].soma { syn_NC_DB4_MDL13_Acetylcholine_DB4_to_MDL13_exc_syn_4conns_post[0] = new DB4_to_MDL13_exc_syn_4conns(0.500000) }")
        h("setpointer syn_NC_DB4_MDL13_Acetylcholine_silent_pre[0].vpeer, a_MDL13[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB4_MDL13_Acetylcholine_DB4_to_MDL13_exc_syn_4conns_post[0].vpeer, a_DB4[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB4_MDL14_Acetylcholine
        print("Adding continuous projection: NC_DB4_MDL14_Acetylcholine from DB4 to MDL14, with 1 connection(s)")

        h("objectvar syn_NC_DB4_MDL14_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB4_MDL14_Acetylcholine_DB4_to_MDL14_exc_syn_1conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB4[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL14[0].soma], weight: 1.0
        h("a_DB4[0].soma { syn_NC_DB4_MDL14_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDL14[0].soma { syn_NC_DB4_MDL14_Acetylcholine_DB4_to_MDL14_exc_syn_1conns_post[0] = new DB4_to_MDL14_exc_syn_1conns(0.500000) }")
        h("setpointer syn_NC_DB4_MDL14_Acetylcholine_silent_pre[0].vpeer, a_MDL14[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB4_MDL14_Acetylcholine_DB4_to_MDL14_exc_syn_1conns_post[0].vpeer, a_DB4[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB4_MDL15_Acetylcholine
        print("Adding continuous projection: NC_DB4_MDL15_Acetylcholine from DB4 to MDL15, with 1 connection(s)")

        h("objectvar syn_NC_DB4_MDL15_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB4_MDL15_Acetylcholine_DB4_to_MDL15_exc_syn_3conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB4[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL15[0].soma], weight: 1.0
        h("a_DB4[0].soma { syn_NC_DB4_MDL15_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDL15[0].soma { syn_NC_DB4_MDL15_Acetylcholine_DB4_to_MDL15_exc_syn_3conns_post[0] = new DB4_to_MDL15_exc_syn_3conns(0.500000) }")
        h("setpointer syn_NC_DB4_MDL15_Acetylcholine_silent_pre[0].vpeer, a_MDL15[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB4_MDL15_Acetylcholine_DB4_to_MDL15_exc_syn_3conns_post[0].vpeer, a_DB4[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB4_MDL16_Acetylcholine
        print("Adding continuous projection: NC_DB4_MDL16_Acetylcholine from DB4 to MDL16, with 1 connection(s)")

        h("objectvar syn_NC_DB4_MDL16_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB4_MDL16_Acetylcholine_DB4_to_MDL16_exc_syn_3conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB4[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL16[0].soma], weight: 1.0
        h("a_DB4[0].soma { syn_NC_DB4_MDL16_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDL16[0].soma { syn_NC_DB4_MDL16_Acetylcholine_DB4_to_MDL16_exc_syn_3conns_post[0] = new DB4_to_MDL16_exc_syn_3conns(0.500000) }")
        h("setpointer syn_NC_DB4_MDL16_Acetylcholine_silent_pre[0].vpeer, a_MDL16[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB4_MDL16_Acetylcholine_DB4_to_MDL16_exc_syn_3conns_post[0].vpeer, a_DB4[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB4_MDR13_Acetylcholine
        print("Adding continuous projection: NC_DB4_MDR13_Acetylcholine from DB4 to MDR13, with 1 connection(s)")

        h("objectvar syn_NC_DB4_MDR13_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB4_MDR13_Acetylcholine_neuron_to_muscle_exc_syn_3conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB4[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR13[0].soma], weight: 1.0
        h("a_DB4[0].soma { syn_NC_DB4_MDR13_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDR13[0].soma { syn_NC_DB4_MDR13_Acetylcholine_neuron_to_muscle_exc_syn_3conns_post[0] = new neuron_to_muscle_exc_syn_3conns(0.500000) }")
        h("setpointer syn_NC_DB4_MDR13_Acetylcholine_silent_pre[0].vpeer, a_MDR13[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB4_MDR13_Acetylcholine_neuron_to_muscle_exc_syn_3conns_post[0].vpeer, a_DB4[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB4_MDR14_Acetylcholine
        print("Adding continuous projection: NC_DB4_MDR14_Acetylcholine from DB4 to MDR14, with 1 connection(s)")

        h("objectvar syn_NC_DB4_MDR14_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB4_MDR14_Acetylcholine_neuron_to_muscle_exc_syn_5conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB4[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR14[0].soma], weight: 1.0
        h("a_DB4[0].soma { syn_NC_DB4_MDR14_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDR14[0].soma { syn_NC_DB4_MDR14_Acetylcholine_neuron_to_muscle_exc_syn_5conns_post[0] = new neuron_to_muscle_exc_syn_5conns(0.500000) }")
        h("setpointer syn_NC_DB4_MDR14_Acetylcholine_silent_pre[0].vpeer, a_MDR14[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB4_MDR14_Acetylcholine_neuron_to_muscle_exc_syn_5conns_post[0].vpeer, a_DB4[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB4_MDR15_Acetylcholine
        print("Adding continuous projection: NC_DB4_MDR15_Acetylcholine from DB4 to MDR15, with 1 connection(s)")

        h("objectvar syn_NC_DB4_MDR15_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB4_MDR15_Acetylcholine_neuron_to_muscle_exc_syn_3conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB4[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR15[0].soma], weight: 1.0
        h("a_DB4[0].soma { syn_NC_DB4_MDR15_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDR15[0].soma { syn_NC_DB4_MDR15_Acetylcholine_neuron_to_muscle_exc_syn_3conns_post[0] = new neuron_to_muscle_exc_syn_3conns(0.500000) }")
        h("setpointer syn_NC_DB4_MDR15_Acetylcholine_silent_pre[0].vpeer, a_MDR15[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB4_MDR15_Acetylcholine_neuron_to_muscle_exc_syn_3conns_post[0].vpeer, a_DB4[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB4_MDR16_Acetylcholine
        print("Adding continuous projection: NC_DB4_MDR16_Acetylcholine from DB4 to MDR16, with 1 connection(s)")

        h("objectvar syn_NC_DB4_MDR16_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB4_MDR16_Acetylcholine_neuron_to_muscle_exc_syn_3conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB4[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR16[0].soma], weight: 1.0
        h("a_DB4[0].soma { syn_NC_DB4_MDR16_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDR16[0].soma { syn_NC_DB4_MDR16_Acetylcholine_neuron_to_muscle_exc_syn_3conns_post[0] = new neuron_to_muscle_exc_syn_3conns(0.500000) }")
        h("setpointer syn_NC_DB4_MDR16_Acetylcholine_silent_pre[0].vpeer, a_MDR16[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB4_MDR16_Acetylcholine_neuron_to_muscle_exc_syn_3conns_post[0].vpeer, a_DB4[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB5_MDL14_Acetylcholine
        print("Adding continuous projection: NC_DB5_MDL14_Acetylcholine from DB5 to MDL14, with 1 connection(s)")

        h("objectvar syn_NC_DB5_MDL14_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB5_MDL14_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB5[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL14[0].soma], weight: 1.0
        h("a_DB5[0].soma { syn_NC_DB5_MDL14_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDL14[0].soma { syn_NC_DB5_MDL14_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[0] = new neuron_to_muscle_exc_syn_2conns(0.500000) }")
        h("setpointer syn_NC_DB5_MDL14_Acetylcholine_silent_pre[0].vpeer, a_MDL14[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB5_MDL14_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[0].vpeer, a_DB5[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB5_MDL15_Acetylcholine
        print("Adding continuous projection: NC_DB5_MDL15_Acetylcholine from DB5 to MDL15, with 1 connection(s)")

        h("objectvar syn_NC_DB5_MDL15_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB5_MDL15_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB5[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL15[0].soma], weight: 1.0
        h("a_DB5[0].soma { syn_NC_DB5_MDL15_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDL15[0].soma { syn_NC_DB5_MDL15_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[0] = new neuron_to_muscle_exc_syn_2conns(0.500000) }")
        h("setpointer syn_NC_DB5_MDL15_Acetylcholine_silent_pre[0].vpeer, a_MDL15[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB5_MDL15_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[0].vpeer, a_DB5[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB5_MDL16_Acetylcholine
        print("Adding continuous projection: NC_DB5_MDL16_Acetylcholine from DB5 to MDL16, with 1 connection(s)")

        h("objectvar syn_NC_DB5_MDL16_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB5_MDL16_Acetylcholine_DB5_to_MDL16_exc_syn_2conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB5[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL16[0].soma], weight: 1.0
        h("a_DB5[0].soma { syn_NC_DB5_MDL16_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDL16[0].soma { syn_NC_DB5_MDL16_Acetylcholine_DB5_to_MDL16_exc_syn_2conns_post[0] = new DB5_to_MDL16_exc_syn_2conns(0.500000) }")
        h("setpointer syn_NC_DB5_MDL16_Acetylcholine_silent_pre[0].vpeer, a_MDL16[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB5_MDL16_Acetylcholine_DB5_to_MDL16_exc_syn_2conns_post[0].vpeer, a_DB5[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB5_MDL17_Acetylcholine
        print("Adding continuous projection: NC_DB5_MDL17_Acetylcholine from DB5 to MDL17, with 1 connection(s)")

        h("objectvar syn_NC_DB5_MDL17_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB5_MDL17_Acetylcholine_DB5_to_MDL17_exc_syn_2conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB5[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL17[0].soma], weight: 1.0
        h("a_DB5[0].soma { syn_NC_DB5_MDL17_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDL17[0].soma { syn_NC_DB5_MDL17_Acetylcholine_DB5_to_MDL17_exc_syn_2conns_post[0] = new DB5_to_MDL17_exc_syn_2conns(0.500000) }")
        h("setpointer syn_NC_DB5_MDL17_Acetylcholine_silent_pre[0].vpeer, a_MDL17[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB5_MDL17_Acetylcholine_DB5_to_MDL17_exc_syn_2conns_post[0].vpeer, a_DB5[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB5_MDL18_Acetylcholine
        print("Adding continuous projection: NC_DB5_MDL18_Acetylcholine from DB5 to MDL18, with 1 connection(s)")

        h("objectvar syn_NC_DB5_MDL18_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB5_MDL18_Acetylcholine_DB5_to_MDL18_exc_syn_2conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB5[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL18[0].soma], weight: 1.0
        h("a_DB5[0].soma { syn_NC_DB5_MDL18_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDL18[0].soma { syn_NC_DB5_MDL18_Acetylcholine_DB5_to_MDL18_exc_syn_2conns_post[0] = new DB5_to_MDL18_exc_syn_2conns(0.500000) }")
        h("setpointer syn_NC_DB5_MDL18_Acetylcholine_silent_pre[0].vpeer, a_MDL18[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB5_MDL18_Acetylcholine_DB5_to_MDL18_exc_syn_2conns_post[0].vpeer, a_DB5[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB5_MDL19_Acetylcholine
        print("Adding continuous projection: NC_DB5_MDL19_Acetylcholine from DB5 to MDL19, with 1 connection(s)")

        h("objectvar syn_NC_DB5_MDL19_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB5_MDL19_Acetylcholine_DB5_to_MDL19_exc_syn_2conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB5[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL19[0].soma], weight: 1.0
        h("a_DB5[0].soma { syn_NC_DB5_MDL19_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDL19[0].soma { syn_NC_DB5_MDL19_Acetylcholine_DB5_to_MDL19_exc_syn_2conns_post[0] = new DB5_to_MDL19_exc_syn_2conns(0.500000) }")
        h("setpointer syn_NC_DB5_MDL19_Acetylcholine_silent_pre[0].vpeer, a_MDL19[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB5_MDL19_Acetylcholine_DB5_to_MDL19_exc_syn_2conns_post[0].vpeer, a_DB5[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB5_MDR14_Acetylcholine
        print("Adding continuous projection: NC_DB5_MDR14_Acetylcholine from DB5 to MDR14, with 1 connection(s)")

        h("objectvar syn_NC_DB5_MDR14_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB5_MDR14_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB5[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR14[0].soma], weight: 1.0
        h("a_DB5[0].soma { syn_NC_DB5_MDR14_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDR14[0].soma { syn_NC_DB5_MDR14_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[0] = new neuron_to_muscle_exc_syn_2conns(0.500000) }")
        h("setpointer syn_NC_DB5_MDR14_Acetylcholine_silent_pre[0].vpeer, a_MDR14[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB5_MDR14_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[0].vpeer, a_DB5[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB5_MDR15_Acetylcholine
        print("Adding continuous projection: NC_DB5_MDR15_Acetylcholine from DB5 to MDR15, with 1 connection(s)")

        h("objectvar syn_NC_DB5_MDR15_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB5_MDR15_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB5[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR15[0].soma], weight: 1.0
        h("a_DB5[0].soma { syn_NC_DB5_MDR15_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDR15[0].soma { syn_NC_DB5_MDR15_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[0] = new neuron_to_muscle_exc_syn_2conns(0.500000) }")
        h("setpointer syn_NC_DB5_MDR15_Acetylcholine_silent_pre[0].vpeer, a_MDR15[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB5_MDR15_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[0].vpeer, a_DB5[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB5_MDR16_Acetylcholine
        print("Adding continuous projection: NC_DB5_MDR16_Acetylcholine from DB5 to MDR16, with 1 connection(s)")

        h("objectvar syn_NC_DB5_MDR16_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB5_MDR16_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB5[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR16[0].soma], weight: 1.0
        h("a_DB5[0].soma { syn_NC_DB5_MDR16_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDR16[0].soma { syn_NC_DB5_MDR16_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[0] = new neuron_to_muscle_exc_syn_2conns(0.500000) }")
        h("setpointer syn_NC_DB5_MDR16_Acetylcholine_silent_pre[0].vpeer, a_MDR16[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB5_MDR16_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[0].vpeer, a_DB5[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB5_MDR17_Acetylcholine
        print("Adding continuous projection: NC_DB5_MDR17_Acetylcholine from DB5 to MDR17, with 1 connection(s)")

        h("objectvar syn_NC_DB5_MDR17_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB5_MDR17_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB5[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR17[0].soma], weight: 1.0
        h("a_DB5[0].soma { syn_NC_DB5_MDR17_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDR17[0].soma { syn_NC_DB5_MDR17_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[0] = new neuron_to_muscle_exc_syn_2conns(0.500000) }")
        h("setpointer syn_NC_DB5_MDR17_Acetylcholine_silent_pre[0].vpeer, a_MDR17[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB5_MDR17_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[0].vpeer, a_DB5[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB5_MDR18_Acetylcholine
        print("Adding continuous projection: NC_DB5_MDR18_Acetylcholine from DB5 to MDR18, with 1 connection(s)")

        h("objectvar syn_NC_DB5_MDR18_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB5_MDR18_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB5[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR18[0].soma], weight: 1.0
        h("a_DB5[0].soma { syn_NC_DB5_MDR18_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDR18[0].soma { syn_NC_DB5_MDR18_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[0] = new neuron_to_muscle_exc_syn_2conns(0.500000) }")
        h("setpointer syn_NC_DB5_MDR18_Acetylcholine_silent_pre[0].vpeer, a_MDR18[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB5_MDR18_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[0].vpeer, a_DB5[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB5_MDR19_Acetylcholine
        print("Adding continuous projection: NC_DB5_MDR19_Acetylcholine from DB5 to MDR19, with 1 connection(s)")

        h("objectvar syn_NC_DB5_MDR19_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB5_MDR19_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB5[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR19[0].soma], weight: 1.0
        h("a_DB5[0].soma { syn_NC_DB5_MDR19_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDR19[0].soma { syn_NC_DB5_MDR19_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[0] = new neuron_to_muscle_exc_syn_2conns(0.500000) }")
        h("setpointer syn_NC_DB5_MDR19_Acetylcholine_silent_pre[0].vpeer, a_MDR19[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB5_MDR19_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[0].vpeer, a_DB5[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB6_MDL16_Acetylcholine
        print("Adding continuous projection: NC_DB6_MDL16_Acetylcholine from DB6 to MDL16, with 1 connection(s)")

        h("objectvar syn_NC_DB6_MDL16_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB6_MDL16_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB6[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL16[0].soma], weight: 1.0
        h("a_DB6[0].soma { syn_NC_DB6_MDL16_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDL16[0].soma { syn_NC_DB6_MDL16_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[0] = new neuron_to_muscle_exc_syn_2conns(0.500000) }")
        h("setpointer syn_NC_DB6_MDL16_Acetylcholine_silent_pre[0].vpeer, a_MDL16[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB6_MDL16_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[0].vpeer, a_DB6[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB6_MDL17_Acetylcholine
        print("Adding continuous projection: NC_DB6_MDL17_Acetylcholine from DB6 to MDL17, with 1 connection(s)")

        h("objectvar syn_NC_DB6_MDL17_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB6_MDL17_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB6[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL17[0].soma], weight: 1.0
        h("a_DB6[0].soma { syn_NC_DB6_MDL17_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDL17[0].soma { syn_NC_DB6_MDL17_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[0] = new neuron_to_muscle_exc_syn_2conns(0.500000) }")
        h("setpointer syn_NC_DB6_MDL17_Acetylcholine_silent_pre[0].vpeer, a_MDL17[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB6_MDL17_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[0].vpeer, a_DB6[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB6_MDL18_Acetylcholine
        print("Adding continuous projection: NC_DB6_MDL18_Acetylcholine from DB6 to MDL18, with 1 connection(s)")

        h("objectvar syn_NC_DB6_MDL18_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB6_MDL18_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB6[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL18[0].soma], weight: 1.0
        h("a_DB6[0].soma { syn_NC_DB6_MDL18_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDL18[0].soma { syn_NC_DB6_MDL18_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[0] = new neuron_to_muscle_exc_syn_2conns(0.500000) }")
        h("setpointer syn_NC_DB6_MDL18_Acetylcholine_silent_pre[0].vpeer, a_MDL18[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB6_MDL18_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[0].vpeer, a_DB6[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB6_MDL19_Acetylcholine
        print("Adding continuous projection: NC_DB6_MDL19_Acetylcholine from DB6 to MDL19, with 1 connection(s)")

        h("objectvar syn_NC_DB6_MDL19_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB6_MDL19_Acetylcholine_DB6_to_MDL19_exc_syn_2conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB6[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL19[0].soma], weight: 1.0
        h("a_DB6[0].soma { syn_NC_DB6_MDL19_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDL19[0].soma { syn_NC_DB6_MDL19_Acetylcholine_DB6_to_MDL19_exc_syn_2conns_post[0] = new DB6_to_MDL19_exc_syn_2conns(0.500000) }")
        h("setpointer syn_NC_DB6_MDL19_Acetylcholine_silent_pre[0].vpeer, a_MDL19[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB6_MDL19_Acetylcholine_DB6_to_MDL19_exc_syn_2conns_post[0].vpeer, a_DB6[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB6_MDL20_Acetylcholine
        print("Adding continuous projection: NC_DB6_MDL20_Acetylcholine from DB6 to MDL20, with 1 connection(s)")

        h("objectvar syn_NC_DB6_MDL20_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB6_MDL20_Acetylcholine_DB6_to_MDL20_exc_syn_2conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB6[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL20[0].soma], weight: 1.0
        h("a_DB6[0].soma { syn_NC_DB6_MDL20_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDL20[0].soma { syn_NC_DB6_MDL20_Acetylcholine_DB6_to_MDL20_exc_syn_2conns_post[0] = new DB6_to_MDL20_exc_syn_2conns(0.500000) }")
        h("setpointer syn_NC_DB6_MDL20_Acetylcholine_silent_pre[0].vpeer, a_MDL20[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB6_MDL20_Acetylcholine_DB6_to_MDL20_exc_syn_2conns_post[0].vpeer, a_DB6[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB6_MDL21_Acetylcholine
        print("Adding continuous projection: NC_DB6_MDL21_Acetylcholine from DB6 to MDL21, with 1 connection(s)")

        h("objectvar syn_NC_DB6_MDL21_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB6_MDL21_Acetylcholine_DB6_to_MDL21_exc_syn_2conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB6[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL21[0].soma], weight: 1.0
        h("a_DB6[0].soma { syn_NC_DB6_MDL21_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDL21[0].soma { syn_NC_DB6_MDL21_Acetylcholine_DB6_to_MDL21_exc_syn_2conns_post[0] = new DB6_to_MDL21_exc_syn_2conns(0.500000) }")
        h("setpointer syn_NC_DB6_MDL21_Acetylcholine_silent_pre[0].vpeer, a_MDL21[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB6_MDL21_Acetylcholine_DB6_to_MDL21_exc_syn_2conns_post[0].vpeer, a_DB6[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB6_MDR16_Acetylcholine
        print("Adding continuous projection: NC_DB6_MDR16_Acetylcholine from DB6 to MDR16, with 1 connection(s)")

        h("objectvar syn_NC_DB6_MDR16_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB6_MDR16_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB6[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR16[0].soma], weight: 1.0
        h("a_DB6[0].soma { syn_NC_DB6_MDR16_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDR16[0].soma { syn_NC_DB6_MDR16_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[0] = new neuron_to_muscle_exc_syn_2conns(0.500000) }")
        h("setpointer syn_NC_DB6_MDR16_Acetylcholine_silent_pre[0].vpeer, a_MDR16[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB6_MDR16_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[0].vpeer, a_DB6[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB6_MDR17_Acetylcholine
        print("Adding continuous projection: NC_DB6_MDR17_Acetylcholine from DB6 to MDR17, with 1 connection(s)")

        h("objectvar syn_NC_DB6_MDR17_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB6_MDR17_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB6[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR17[0].soma], weight: 1.0
        h("a_DB6[0].soma { syn_NC_DB6_MDR17_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDR17[0].soma { syn_NC_DB6_MDR17_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[0] = new neuron_to_muscle_exc_syn_2conns(0.500000) }")
        h("setpointer syn_NC_DB6_MDR17_Acetylcholine_silent_pre[0].vpeer, a_MDR17[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB6_MDR17_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[0].vpeer, a_DB6[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB6_MDR18_Acetylcholine
        print("Adding continuous projection: NC_DB6_MDR18_Acetylcholine from DB6 to MDR18, with 1 connection(s)")

        h("objectvar syn_NC_DB6_MDR18_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB6_MDR18_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB6[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR18[0].soma], weight: 1.0
        h("a_DB6[0].soma { syn_NC_DB6_MDR18_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDR18[0].soma { syn_NC_DB6_MDR18_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[0] = new neuron_to_muscle_exc_syn_2conns(0.500000) }")
        h("setpointer syn_NC_DB6_MDR18_Acetylcholine_silent_pre[0].vpeer, a_MDR18[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB6_MDR18_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[0].vpeer, a_DB6[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB6_MDR19_Acetylcholine
        print("Adding continuous projection: NC_DB6_MDR19_Acetylcholine from DB6 to MDR19, with 1 connection(s)")

        h("objectvar syn_NC_DB6_MDR19_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB6_MDR19_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB6[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR19[0].soma], weight: 1.0
        h("a_DB6[0].soma { syn_NC_DB6_MDR19_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDR19[0].soma { syn_NC_DB6_MDR19_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[0] = new neuron_to_muscle_exc_syn_2conns(0.500000) }")
        h("setpointer syn_NC_DB6_MDR19_Acetylcholine_silent_pre[0].vpeer, a_MDR19[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB6_MDR19_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[0].vpeer, a_DB6[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB6_MDR20_Acetylcholine
        print("Adding continuous projection: NC_DB6_MDR20_Acetylcholine from DB6 to MDR20, with 1 connection(s)")

        h("objectvar syn_NC_DB6_MDR20_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB6_MDR20_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB6[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR20[0].soma], weight: 1.0
        h("a_DB6[0].soma { syn_NC_DB6_MDR20_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDR20[0].soma { syn_NC_DB6_MDR20_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[0] = new neuron_to_muscle_exc_syn_2conns(0.500000) }")
        h("setpointer syn_NC_DB6_MDR20_Acetylcholine_silent_pre[0].vpeer, a_MDR20[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB6_MDR20_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[0].vpeer, a_DB6[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB6_MDR21_Acetylcholine
        print("Adding continuous projection: NC_DB6_MDR21_Acetylcholine from DB6 to MDR21, with 1 connection(s)")

        h("objectvar syn_NC_DB6_MDR21_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB6_MDR21_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB6[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR21[0].soma], weight: 1.0
        h("a_DB6[0].soma { syn_NC_DB6_MDR21_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDR21[0].soma { syn_NC_DB6_MDR21_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[0] = new neuron_to_muscle_exc_syn_2conns(0.500000) }")
        h("setpointer syn_NC_DB6_MDR21_Acetylcholine_silent_pre[0].vpeer, a_MDR21[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB6_MDR21_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[0].vpeer, a_DB6[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB7_MDL19_Acetylcholine
        print("Adding continuous projection: NC_DB7_MDL19_Acetylcholine from DB7 to MDL19, with 1 connection(s)")

        h("objectvar syn_NC_DB7_MDL19_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB7_MDL19_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB7[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL19[0].soma], weight: 1.0
        h("a_DB7[0].soma { syn_NC_DB7_MDL19_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDL19[0].soma { syn_NC_DB7_MDL19_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[0] = new neuron_to_muscle_exc_syn_2conns(0.500000) }")
        h("setpointer syn_NC_DB7_MDL19_Acetylcholine_silent_pre[0].vpeer, a_MDL19[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB7_MDL19_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[0].vpeer, a_DB7[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB7_MDL20_Acetylcholine
        print("Adding continuous projection: NC_DB7_MDL20_Acetylcholine from DB7 to MDL20, with 1 connection(s)")

        h("objectvar syn_NC_DB7_MDL20_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB7_MDL20_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB7[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL20[0].soma], weight: 1.0
        h("a_DB7[0].soma { syn_NC_DB7_MDL20_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDL20[0].soma { syn_NC_DB7_MDL20_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[0] = new neuron_to_muscle_exc_syn_2conns(0.500000) }")
        h("setpointer syn_NC_DB7_MDL20_Acetylcholine_silent_pre[0].vpeer, a_MDL20[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB7_MDL20_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[0].vpeer, a_DB7[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB7_MDL21_Acetylcholine
        print("Adding continuous projection: NC_DB7_MDL21_Acetylcholine from DB7 to MDL21, with 1 connection(s)")

        h("objectvar syn_NC_DB7_MDL21_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB7_MDL21_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB7[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL21[0].soma], weight: 1.0
        h("a_DB7[0].soma { syn_NC_DB7_MDL21_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDL21[0].soma { syn_NC_DB7_MDL21_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[0] = new neuron_to_muscle_exc_syn_2conns(0.500000) }")
        h("setpointer syn_NC_DB7_MDL21_Acetylcholine_silent_pre[0].vpeer, a_MDL21[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB7_MDL21_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[0].vpeer, a_DB7[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB7_MDL22_Acetylcholine
        print("Adding continuous projection: NC_DB7_MDL22_Acetylcholine from DB7 to MDL22, with 1 connection(s)")

        h("objectvar syn_NC_DB7_MDL22_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB7_MDL22_Acetylcholine_DB7_to_MDL22_exc_syn_2conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB7[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL22[0].soma], weight: 1.0
        h("a_DB7[0].soma { syn_NC_DB7_MDL22_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDL22[0].soma { syn_NC_DB7_MDL22_Acetylcholine_DB7_to_MDL22_exc_syn_2conns_post[0] = new DB7_to_MDL22_exc_syn_2conns(0.500000) }")
        h("setpointer syn_NC_DB7_MDL22_Acetylcholine_silent_pre[0].vpeer, a_MDL22[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB7_MDL22_Acetylcholine_DB7_to_MDL22_exc_syn_2conns_post[0].vpeer, a_DB7[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB7_MDL23_Acetylcholine
        print("Adding continuous projection: NC_DB7_MDL23_Acetylcholine from DB7 to MDL23, with 1 connection(s)")

        h("objectvar syn_NC_DB7_MDL23_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB7_MDL23_Acetylcholine_DB7_to_MDL23_exc_syn_2conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB7[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL23[0].soma], weight: 1.0
        h("a_DB7[0].soma { syn_NC_DB7_MDL23_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDL23[0].soma { syn_NC_DB7_MDL23_Acetylcholine_DB7_to_MDL23_exc_syn_2conns_post[0] = new DB7_to_MDL23_exc_syn_2conns(0.500000) }")
        h("setpointer syn_NC_DB7_MDL23_Acetylcholine_silent_pre[0].vpeer, a_MDL23[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB7_MDL23_Acetylcholine_DB7_to_MDL23_exc_syn_2conns_post[0].vpeer, a_DB7[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB7_MDL24_Acetylcholine
        print("Adding continuous projection: NC_DB7_MDL24_Acetylcholine from DB7 to MDL24, with 1 connection(s)")

        h("objectvar syn_NC_DB7_MDL24_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB7_MDL24_Acetylcholine_DB7_to_MDL24_exc_syn_2conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB7[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDL24[0].soma], weight: 1.0
        h("a_DB7[0].soma { syn_NC_DB7_MDL24_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDL24[0].soma { syn_NC_DB7_MDL24_Acetylcholine_DB7_to_MDL24_exc_syn_2conns_post[0] = new DB7_to_MDL24_exc_syn_2conns(0.500000) }")
        h("setpointer syn_NC_DB7_MDL24_Acetylcholine_silent_pre[0].vpeer, a_MDL24[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB7_MDL24_Acetylcholine_DB7_to_MDL24_exc_syn_2conns_post[0].vpeer, a_DB7[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB7_MDR19_Acetylcholine
        print("Adding continuous projection: NC_DB7_MDR19_Acetylcholine from DB7 to MDR19, with 1 connection(s)")

        h("objectvar syn_NC_DB7_MDR19_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB7_MDR19_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB7[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR19[0].soma], weight: 1.0
        h("a_DB7[0].soma { syn_NC_DB7_MDR19_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDR19[0].soma { syn_NC_DB7_MDR19_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[0] = new neuron_to_muscle_exc_syn_2conns(0.500000) }")
        h("setpointer syn_NC_DB7_MDR19_Acetylcholine_silent_pre[0].vpeer, a_MDR19[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB7_MDR19_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[0].vpeer, a_DB7[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB7_MDR20_Acetylcholine
        print("Adding continuous projection: NC_DB7_MDR20_Acetylcholine from DB7 to MDR20, with 1 connection(s)")

        h("objectvar syn_NC_DB7_MDR20_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB7_MDR20_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB7[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR20[0].soma], weight: 1.0
        h("a_DB7[0].soma { syn_NC_DB7_MDR20_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDR20[0].soma { syn_NC_DB7_MDR20_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[0] = new neuron_to_muscle_exc_syn_2conns(0.500000) }")
        h("setpointer syn_NC_DB7_MDR20_Acetylcholine_silent_pre[0].vpeer, a_MDR20[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB7_MDR20_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[0].vpeer, a_DB7[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB7_MDR21_Acetylcholine
        print("Adding continuous projection: NC_DB7_MDR21_Acetylcholine from DB7 to MDR21, with 1 connection(s)")

        h("objectvar syn_NC_DB7_MDR21_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB7_MDR21_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB7[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR21[0].soma], weight: 1.0
        h("a_DB7[0].soma { syn_NC_DB7_MDR21_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDR21[0].soma { syn_NC_DB7_MDR21_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[0] = new neuron_to_muscle_exc_syn_2conns(0.500000) }")
        h("setpointer syn_NC_DB7_MDR21_Acetylcholine_silent_pre[0].vpeer, a_MDR21[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB7_MDR21_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[0].vpeer, a_DB7[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB7_MDR22_Acetylcholine
        print("Adding continuous projection: NC_DB7_MDR22_Acetylcholine from DB7 to MDR22, with 1 connection(s)")

        h("objectvar syn_NC_DB7_MDR22_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB7_MDR22_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB7[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR22[0].soma], weight: 1.0
        h("a_DB7[0].soma { syn_NC_DB7_MDR22_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDR22[0].soma { syn_NC_DB7_MDR22_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[0] = new neuron_to_muscle_exc_syn_2conns(0.500000) }")
        h("setpointer syn_NC_DB7_MDR22_Acetylcholine_silent_pre[0].vpeer, a_MDR22[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB7_MDR22_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[0].vpeer, a_DB7[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB7_MDR23_Acetylcholine
        print("Adding continuous projection: NC_DB7_MDR23_Acetylcholine from DB7 to MDR23, with 1 connection(s)")

        h("objectvar syn_NC_DB7_MDR23_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB7_MDR23_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB7[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR23[0].soma], weight: 1.0
        h("a_DB7[0].soma { syn_NC_DB7_MDR23_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDR23[0].soma { syn_NC_DB7_MDR23_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[0] = new neuron_to_muscle_exc_syn_2conns(0.500000) }")
        h("setpointer syn_NC_DB7_MDR23_Acetylcholine_silent_pre[0].vpeer, a_MDR23[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB7_MDR23_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[0].vpeer, a_DB7[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB7_MDR24_Acetylcholine
        print("Adding continuous projection: NC_DB7_MDR24_Acetylcholine from DB7 to MDR24, with 1 connection(s)")

        h("objectvar syn_NC_DB7_MDR24_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB7_MDR24_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB7[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_MDR24[0].soma], weight: 1.0
        h("a_DB7[0].soma { syn_NC_DB7_MDR24_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_MDR24[0].soma { syn_NC_DB7_MDR24_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[0] = new neuron_to_muscle_exc_syn_2conns(0.500000) }")
        h("setpointer syn_NC_DB7_MDR24_Acetylcholine_silent_pre[0].vpeer, a_MDR24[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB7_MDR24_Acetylcholine_neuron_to_muscle_exc_syn_2conns_post[0].vpeer, a_DB7[0].soma.v(0.500000)")

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

        trec = h.Vector()
        trec.record(h._ref_t)

        h.tstop = tstop

        h.dt = dt

        h.steps_per_ms = 1/h.dt



        # ######################   File to save: c302_C2_AVB_DB.activity.dat (neurons_activity)
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
        # Column: DB1/0/GenericNeuronCell/caConc
        h(' objectvar v_DB1_v_neurons_activity ')
        h(' { v_DB1_v_neurons_activity = new Vector() } ')
        h(' { v_DB1_v_neurons_activity.record(&a_DB1[0].soma.cai(0.5)) } ')
        h.v_DB1_v_neurons_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: DB2/0/GenericNeuronCell/caConc
        h(' objectvar v_DB2_v_neurons_activity ')
        h(' { v_DB2_v_neurons_activity = new Vector() } ')
        h(' { v_DB2_v_neurons_activity.record(&a_DB2[0].soma.cai(0.5)) } ')
        h.v_DB2_v_neurons_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: DB3/0/GenericNeuronCell/caConc
        h(' objectvar v_DB3_v_neurons_activity ')
        h(' { v_DB3_v_neurons_activity = new Vector() } ')
        h(' { v_DB3_v_neurons_activity.record(&a_DB3[0].soma.cai(0.5)) } ')
        h.v_DB3_v_neurons_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: DB4/0/GenericNeuronCell/caConc
        h(' objectvar v_DB4_v_neurons_activity ')
        h(' { v_DB4_v_neurons_activity = new Vector() } ')
        h(' { v_DB4_v_neurons_activity.record(&a_DB4[0].soma.cai(0.5)) } ')
        h.v_DB4_v_neurons_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: DB5/0/GenericNeuronCell/caConc
        h(' objectvar v_DB5_v_neurons_activity ')
        h(' { v_DB5_v_neurons_activity = new Vector() } ')
        h(' { v_DB5_v_neurons_activity.record(&a_DB5[0].soma.cai(0.5)) } ')
        h.v_DB5_v_neurons_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: DB6/0/GenericNeuronCell/caConc
        h(' objectvar v_DB6_v_neurons_activity ')
        h(' { v_DB6_v_neurons_activity = new Vector() } ')
        h(' { v_DB6_v_neurons_activity.record(&a_DB6[0].soma.cai(0.5)) } ')
        h.v_DB6_v_neurons_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: DB7/0/GenericNeuronCell/caConc
        h(' objectvar v_DB7_v_neurons_activity ')
        h(' { v_DB7_v_neurons_activity = new Vector() } ')
        h(' { v_DB7_v_neurons_activity.record(&a_DB7[0].soma.cai(0.5)) } ')
        h.v_DB7_v_neurons_activity.resize((h.tstop * h.steps_per_ms) + 1)

        # ######################   File to save: c302_C2_AVB_DB.muscles.dat (muscles_v)
        # Column: MDR01/0/GenericMuscleCell/v
        h(' objectvar v_MDR01_v_muscles_v ')
        h(' { v_MDR01_v_muscles_v = new Vector() } ')
        h(' { v_MDR01_v_muscles_v.record(&a_MDR01[0].soma.v(0.5)) } ')
        h.v_MDR01_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDR02/0/GenericMuscleCell/v
        h(' objectvar v_MDR02_v_muscles_v ')
        h(' { v_MDR02_v_muscles_v = new Vector() } ')
        h(' { v_MDR02_v_muscles_v.record(&a_MDR02[0].soma.v(0.5)) } ')
        h.v_MDR02_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDR03/0/GenericMuscleCell/v
        h(' objectvar v_MDR03_v_muscles_v ')
        h(' { v_MDR03_v_muscles_v = new Vector() } ')
        h(' { v_MDR03_v_muscles_v.record(&a_MDR03[0].soma.v(0.5)) } ')
        h.v_MDR03_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDR04/0/GenericMuscleCell/v
        h(' objectvar v_MDR04_v_muscles_v ')
        h(' { v_MDR04_v_muscles_v = new Vector() } ')
        h(' { v_MDR04_v_muscles_v.record(&a_MDR04[0].soma.v(0.5)) } ')
        h.v_MDR04_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDR05/0/GenericMuscleCell/v
        h(' objectvar v_MDR05_v_muscles_v ')
        h(' { v_MDR05_v_muscles_v = new Vector() } ')
        h(' { v_MDR05_v_muscles_v.record(&a_MDR05[0].soma.v(0.5)) } ')
        h.v_MDR05_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDR06/0/GenericMuscleCell/v
        h(' objectvar v_MDR06_v_muscles_v ')
        h(' { v_MDR06_v_muscles_v = new Vector() } ')
        h(' { v_MDR06_v_muscles_v.record(&a_MDR06[0].soma.v(0.5)) } ')
        h.v_MDR06_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDR07/0/GenericMuscleCell/v
        h(' objectvar v_MDR07_v_muscles_v ')
        h(' { v_MDR07_v_muscles_v = new Vector() } ')
        h(' { v_MDR07_v_muscles_v.record(&a_MDR07[0].soma.v(0.5)) } ')
        h.v_MDR07_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDR08/0/GenericMuscleCell/v
        h(' objectvar v_MDR08_v_muscles_v ')
        h(' { v_MDR08_v_muscles_v = new Vector() } ')
        h(' { v_MDR08_v_muscles_v.record(&a_MDR08[0].soma.v(0.5)) } ')
        h.v_MDR08_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDR09/0/GenericMuscleCell/v
        h(' objectvar v_MDR09_v_muscles_v ')
        h(' { v_MDR09_v_muscles_v = new Vector() } ')
        h(' { v_MDR09_v_muscles_v.record(&a_MDR09[0].soma.v(0.5)) } ')
        h.v_MDR09_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDR10/0/GenericMuscleCell/v
        h(' objectvar v_MDR10_v_muscles_v ')
        h(' { v_MDR10_v_muscles_v = new Vector() } ')
        h(' { v_MDR10_v_muscles_v.record(&a_MDR10[0].soma.v(0.5)) } ')
        h.v_MDR10_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDR11/0/GenericMuscleCell/v
        h(' objectvar v_MDR11_v_muscles_v ')
        h(' { v_MDR11_v_muscles_v = new Vector() } ')
        h(' { v_MDR11_v_muscles_v.record(&a_MDR11[0].soma.v(0.5)) } ')
        h.v_MDR11_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDR12/0/GenericMuscleCell/v
        h(' objectvar v_MDR12_v_muscles_v ')
        h(' { v_MDR12_v_muscles_v = new Vector() } ')
        h(' { v_MDR12_v_muscles_v.record(&a_MDR12[0].soma.v(0.5)) } ')
        h.v_MDR12_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDR13/0/GenericMuscleCell/v
        h(' objectvar v_MDR13_v_muscles_v ')
        h(' { v_MDR13_v_muscles_v = new Vector() } ')
        h(' { v_MDR13_v_muscles_v.record(&a_MDR13[0].soma.v(0.5)) } ')
        h.v_MDR13_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDR14/0/GenericMuscleCell/v
        h(' objectvar v_MDR14_v_muscles_v ')
        h(' { v_MDR14_v_muscles_v = new Vector() } ')
        h(' { v_MDR14_v_muscles_v.record(&a_MDR14[0].soma.v(0.5)) } ')
        h.v_MDR14_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDR15/0/GenericMuscleCell/v
        h(' objectvar v_MDR15_v_muscles_v ')
        h(' { v_MDR15_v_muscles_v = new Vector() } ')
        h(' { v_MDR15_v_muscles_v.record(&a_MDR15[0].soma.v(0.5)) } ')
        h.v_MDR15_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDR16/0/GenericMuscleCell/v
        h(' objectvar v_MDR16_v_muscles_v ')
        h(' { v_MDR16_v_muscles_v = new Vector() } ')
        h(' { v_MDR16_v_muscles_v.record(&a_MDR16[0].soma.v(0.5)) } ')
        h.v_MDR16_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDR17/0/GenericMuscleCell/v
        h(' objectvar v_MDR17_v_muscles_v ')
        h(' { v_MDR17_v_muscles_v = new Vector() } ')
        h(' { v_MDR17_v_muscles_v.record(&a_MDR17[0].soma.v(0.5)) } ')
        h.v_MDR17_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDR18/0/GenericMuscleCell/v
        h(' objectvar v_MDR18_v_muscles_v ')
        h(' { v_MDR18_v_muscles_v = new Vector() } ')
        h(' { v_MDR18_v_muscles_v.record(&a_MDR18[0].soma.v(0.5)) } ')
        h.v_MDR18_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDR19/0/GenericMuscleCell/v
        h(' objectvar v_MDR19_v_muscles_v ')
        h(' { v_MDR19_v_muscles_v = new Vector() } ')
        h(' { v_MDR19_v_muscles_v.record(&a_MDR19[0].soma.v(0.5)) } ')
        h.v_MDR19_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDR20/0/GenericMuscleCell/v
        h(' objectvar v_MDR20_v_muscles_v ')
        h(' { v_MDR20_v_muscles_v = new Vector() } ')
        h(' { v_MDR20_v_muscles_v.record(&a_MDR20[0].soma.v(0.5)) } ')
        h.v_MDR20_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDR21/0/GenericMuscleCell/v
        h(' objectvar v_MDR21_v_muscles_v ')
        h(' { v_MDR21_v_muscles_v = new Vector() } ')
        h(' { v_MDR21_v_muscles_v.record(&a_MDR21[0].soma.v(0.5)) } ')
        h.v_MDR21_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDR22/0/GenericMuscleCell/v
        h(' objectvar v_MDR22_v_muscles_v ')
        h(' { v_MDR22_v_muscles_v = new Vector() } ')
        h(' { v_MDR22_v_muscles_v.record(&a_MDR22[0].soma.v(0.5)) } ')
        h.v_MDR22_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDR23/0/GenericMuscleCell/v
        h(' objectvar v_MDR23_v_muscles_v ')
        h(' { v_MDR23_v_muscles_v = new Vector() } ')
        h(' { v_MDR23_v_muscles_v.record(&a_MDR23[0].soma.v(0.5)) } ')
        h.v_MDR23_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDR24/0/GenericMuscleCell/v
        h(' objectvar v_MDR24_v_muscles_v ')
        h(' { v_MDR24_v_muscles_v = new Vector() } ')
        h(' { v_MDR24_v_muscles_v.record(&a_MDR24[0].soma.v(0.5)) } ')
        h.v_MDR24_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVR01/0/GenericMuscleCell/v
        h(' objectvar v_MVR01_v_muscles_v ')
        h(' { v_MVR01_v_muscles_v = new Vector() } ')
        h(' { v_MVR01_v_muscles_v.record(&a_MVR01[0].soma.v(0.5)) } ')
        h.v_MVR01_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVR02/0/GenericMuscleCell/v
        h(' objectvar v_MVR02_v_muscles_v ')
        h(' { v_MVR02_v_muscles_v = new Vector() } ')
        h(' { v_MVR02_v_muscles_v.record(&a_MVR02[0].soma.v(0.5)) } ')
        h.v_MVR02_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVR03/0/GenericMuscleCell/v
        h(' objectvar v_MVR03_v_muscles_v ')
        h(' { v_MVR03_v_muscles_v = new Vector() } ')
        h(' { v_MVR03_v_muscles_v.record(&a_MVR03[0].soma.v(0.5)) } ')
        h.v_MVR03_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVR04/0/GenericMuscleCell/v
        h(' objectvar v_MVR04_v_muscles_v ')
        h(' { v_MVR04_v_muscles_v = new Vector() } ')
        h(' { v_MVR04_v_muscles_v.record(&a_MVR04[0].soma.v(0.5)) } ')
        h.v_MVR04_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVR05/0/GenericMuscleCell/v
        h(' objectvar v_MVR05_v_muscles_v ')
        h(' { v_MVR05_v_muscles_v = new Vector() } ')
        h(' { v_MVR05_v_muscles_v.record(&a_MVR05[0].soma.v(0.5)) } ')
        h.v_MVR05_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVR06/0/GenericMuscleCell/v
        h(' objectvar v_MVR06_v_muscles_v ')
        h(' { v_MVR06_v_muscles_v = new Vector() } ')
        h(' { v_MVR06_v_muscles_v.record(&a_MVR06[0].soma.v(0.5)) } ')
        h.v_MVR06_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVR07/0/GenericMuscleCell/v
        h(' objectvar v_MVR07_v_muscles_v ')
        h(' { v_MVR07_v_muscles_v = new Vector() } ')
        h(' { v_MVR07_v_muscles_v.record(&a_MVR07[0].soma.v(0.5)) } ')
        h.v_MVR07_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVR08/0/GenericMuscleCell/v
        h(' objectvar v_MVR08_v_muscles_v ')
        h(' { v_MVR08_v_muscles_v = new Vector() } ')
        h(' { v_MVR08_v_muscles_v.record(&a_MVR08[0].soma.v(0.5)) } ')
        h.v_MVR08_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVR09/0/GenericMuscleCell/v
        h(' objectvar v_MVR09_v_muscles_v ')
        h(' { v_MVR09_v_muscles_v = new Vector() } ')
        h(' { v_MVR09_v_muscles_v.record(&a_MVR09[0].soma.v(0.5)) } ')
        h.v_MVR09_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVR10/0/GenericMuscleCell/v
        h(' objectvar v_MVR10_v_muscles_v ')
        h(' { v_MVR10_v_muscles_v = new Vector() } ')
        h(' { v_MVR10_v_muscles_v.record(&a_MVR10[0].soma.v(0.5)) } ')
        h.v_MVR10_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVR11/0/GenericMuscleCell/v
        h(' objectvar v_MVR11_v_muscles_v ')
        h(' { v_MVR11_v_muscles_v = new Vector() } ')
        h(' { v_MVR11_v_muscles_v.record(&a_MVR11[0].soma.v(0.5)) } ')
        h.v_MVR11_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVR12/0/GenericMuscleCell/v
        h(' objectvar v_MVR12_v_muscles_v ')
        h(' { v_MVR12_v_muscles_v = new Vector() } ')
        h(' { v_MVR12_v_muscles_v.record(&a_MVR12[0].soma.v(0.5)) } ')
        h.v_MVR12_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVR13/0/GenericMuscleCell/v
        h(' objectvar v_MVR13_v_muscles_v ')
        h(' { v_MVR13_v_muscles_v = new Vector() } ')
        h(' { v_MVR13_v_muscles_v.record(&a_MVR13[0].soma.v(0.5)) } ')
        h.v_MVR13_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVR14/0/GenericMuscleCell/v
        h(' objectvar v_MVR14_v_muscles_v ')
        h(' { v_MVR14_v_muscles_v = new Vector() } ')
        h(' { v_MVR14_v_muscles_v.record(&a_MVR14[0].soma.v(0.5)) } ')
        h.v_MVR14_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVR15/0/GenericMuscleCell/v
        h(' objectvar v_MVR15_v_muscles_v ')
        h(' { v_MVR15_v_muscles_v = new Vector() } ')
        h(' { v_MVR15_v_muscles_v.record(&a_MVR15[0].soma.v(0.5)) } ')
        h.v_MVR15_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVR16/0/GenericMuscleCell/v
        h(' objectvar v_MVR16_v_muscles_v ')
        h(' { v_MVR16_v_muscles_v = new Vector() } ')
        h(' { v_MVR16_v_muscles_v.record(&a_MVR16[0].soma.v(0.5)) } ')
        h.v_MVR16_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVR17/0/GenericMuscleCell/v
        h(' objectvar v_MVR17_v_muscles_v ')
        h(' { v_MVR17_v_muscles_v = new Vector() } ')
        h(' { v_MVR17_v_muscles_v.record(&a_MVR17[0].soma.v(0.5)) } ')
        h.v_MVR17_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVR18/0/GenericMuscleCell/v
        h(' objectvar v_MVR18_v_muscles_v ')
        h(' { v_MVR18_v_muscles_v = new Vector() } ')
        h(' { v_MVR18_v_muscles_v.record(&a_MVR18[0].soma.v(0.5)) } ')
        h.v_MVR18_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVR19/0/GenericMuscleCell/v
        h(' objectvar v_MVR19_v_muscles_v ')
        h(' { v_MVR19_v_muscles_v = new Vector() } ')
        h(' { v_MVR19_v_muscles_v.record(&a_MVR19[0].soma.v(0.5)) } ')
        h.v_MVR19_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVR20/0/GenericMuscleCell/v
        h(' objectvar v_MVR20_v_muscles_v ')
        h(' { v_MVR20_v_muscles_v = new Vector() } ')
        h(' { v_MVR20_v_muscles_v.record(&a_MVR20[0].soma.v(0.5)) } ')
        h.v_MVR20_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVR21/0/GenericMuscleCell/v
        h(' objectvar v_MVR21_v_muscles_v ')
        h(' { v_MVR21_v_muscles_v = new Vector() } ')
        h(' { v_MVR21_v_muscles_v.record(&a_MVR21[0].soma.v(0.5)) } ')
        h.v_MVR21_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVR22/0/GenericMuscleCell/v
        h(' objectvar v_MVR22_v_muscles_v ')
        h(' { v_MVR22_v_muscles_v = new Vector() } ')
        h(' { v_MVR22_v_muscles_v.record(&a_MVR22[0].soma.v(0.5)) } ')
        h.v_MVR22_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVR23/0/GenericMuscleCell/v
        h(' objectvar v_MVR23_v_muscles_v ')
        h(' { v_MVR23_v_muscles_v = new Vector() } ')
        h(' { v_MVR23_v_muscles_v.record(&a_MVR23[0].soma.v(0.5)) } ')
        h.v_MVR23_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVL01/0/GenericMuscleCell/v
        h(' objectvar v_MVL01_v_muscles_v ')
        h(' { v_MVL01_v_muscles_v = new Vector() } ')
        h(' { v_MVL01_v_muscles_v.record(&a_MVL01[0].soma.v(0.5)) } ')
        h.v_MVL01_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVL02/0/GenericMuscleCell/v
        h(' objectvar v_MVL02_v_muscles_v ')
        h(' { v_MVL02_v_muscles_v = new Vector() } ')
        h(' { v_MVL02_v_muscles_v.record(&a_MVL02[0].soma.v(0.5)) } ')
        h.v_MVL02_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVL03/0/GenericMuscleCell/v
        h(' objectvar v_MVL03_v_muscles_v ')
        h(' { v_MVL03_v_muscles_v = new Vector() } ')
        h(' { v_MVL03_v_muscles_v.record(&a_MVL03[0].soma.v(0.5)) } ')
        h.v_MVL03_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVL04/0/GenericMuscleCell/v
        h(' objectvar v_MVL04_v_muscles_v ')
        h(' { v_MVL04_v_muscles_v = new Vector() } ')
        h(' { v_MVL04_v_muscles_v.record(&a_MVL04[0].soma.v(0.5)) } ')
        h.v_MVL04_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVL05/0/GenericMuscleCell/v
        h(' objectvar v_MVL05_v_muscles_v ')
        h(' { v_MVL05_v_muscles_v = new Vector() } ')
        h(' { v_MVL05_v_muscles_v.record(&a_MVL05[0].soma.v(0.5)) } ')
        h.v_MVL05_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVL06/0/GenericMuscleCell/v
        h(' objectvar v_MVL06_v_muscles_v ')
        h(' { v_MVL06_v_muscles_v = new Vector() } ')
        h(' { v_MVL06_v_muscles_v.record(&a_MVL06[0].soma.v(0.5)) } ')
        h.v_MVL06_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVL07/0/GenericMuscleCell/v
        h(' objectvar v_MVL07_v_muscles_v ')
        h(' { v_MVL07_v_muscles_v = new Vector() } ')
        h(' { v_MVL07_v_muscles_v.record(&a_MVL07[0].soma.v(0.5)) } ')
        h.v_MVL07_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVL08/0/GenericMuscleCell/v
        h(' objectvar v_MVL08_v_muscles_v ')
        h(' { v_MVL08_v_muscles_v = new Vector() } ')
        h(' { v_MVL08_v_muscles_v.record(&a_MVL08[0].soma.v(0.5)) } ')
        h.v_MVL08_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVL09/0/GenericMuscleCell/v
        h(' objectvar v_MVL09_v_muscles_v ')
        h(' { v_MVL09_v_muscles_v = new Vector() } ')
        h(' { v_MVL09_v_muscles_v.record(&a_MVL09[0].soma.v(0.5)) } ')
        h.v_MVL09_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVL10/0/GenericMuscleCell/v
        h(' objectvar v_MVL10_v_muscles_v ')
        h(' { v_MVL10_v_muscles_v = new Vector() } ')
        h(' { v_MVL10_v_muscles_v.record(&a_MVL10[0].soma.v(0.5)) } ')
        h.v_MVL10_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVL11/0/GenericMuscleCell/v
        h(' objectvar v_MVL11_v_muscles_v ')
        h(' { v_MVL11_v_muscles_v = new Vector() } ')
        h(' { v_MVL11_v_muscles_v.record(&a_MVL11[0].soma.v(0.5)) } ')
        h.v_MVL11_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVL12/0/GenericMuscleCell/v
        h(' objectvar v_MVL12_v_muscles_v ')
        h(' { v_MVL12_v_muscles_v = new Vector() } ')
        h(' { v_MVL12_v_muscles_v.record(&a_MVL12[0].soma.v(0.5)) } ')
        h.v_MVL12_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVL13/0/GenericMuscleCell/v
        h(' objectvar v_MVL13_v_muscles_v ')
        h(' { v_MVL13_v_muscles_v = new Vector() } ')
        h(' { v_MVL13_v_muscles_v.record(&a_MVL13[0].soma.v(0.5)) } ')
        h.v_MVL13_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVL14/0/GenericMuscleCell/v
        h(' objectvar v_MVL14_v_muscles_v ')
        h(' { v_MVL14_v_muscles_v = new Vector() } ')
        h(' { v_MVL14_v_muscles_v.record(&a_MVL14[0].soma.v(0.5)) } ')
        h.v_MVL14_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVL15/0/GenericMuscleCell/v
        h(' objectvar v_MVL15_v_muscles_v ')
        h(' { v_MVL15_v_muscles_v = new Vector() } ')
        h(' { v_MVL15_v_muscles_v.record(&a_MVL15[0].soma.v(0.5)) } ')
        h.v_MVL15_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVL16/0/GenericMuscleCell/v
        h(' objectvar v_MVL16_v_muscles_v ')
        h(' { v_MVL16_v_muscles_v = new Vector() } ')
        h(' { v_MVL16_v_muscles_v.record(&a_MVL16[0].soma.v(0.5)) } ')
        h.v_MVL16_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVL17/0/GenericMuscleCell/v
        h(' objectvar v_MVL17_v_muscles_v ')
        h(' { v_MVL17_v_muscles_v = new Vector() } ')
        h(' { v_MVL17_v_muscles_v.record(&a_MVL17[0].soma.v(0.5)) } ')
        h.v_MVL17_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVL18/0/GenericMuscleCell/v
        h(' objectvar v_MVL18_v_muscles_v ')
        h(' { v_MVL18_v_muscles_v = new Vector() } ')
        h(' { v_MVL18_v_muscles_v.record(&a_MVL18[0].soma.v(0.5)) } ')
        h.v_MVL18_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVL19/0/GenericMuscleCell/v
        h(' objectvar v_MVL19_v_muscles_v ')
        h(' { v_MVL19_v_muscles_v = new Vector() } ')
        h(' { v_MVL19_v_muscles_v.record(&a_MVL19[0].soma.v(0.5)) } ')
        h.v_MVL19_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVL20/0/GenericMuscleCell/v
        h(' objectvar v_MVL20_v_muscles_v ')
        h(' { v_MVL20_v_muscles_v = new Vector() } ')
        h(' { v_MVL20_v_muscles_v.record(&a_MVL20[0].soma.v(0.5)) } ')
        h.v_MVL20_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVL21/0/GenericMuscleCell/v
        h(' objectvar v_MVL21_v_muscles_v ')
        h(' { v_MVL21_v_muscles_v = new Vector() } ')
        h(' { v_MVL21_v_muscles_v.record(&a_MVL21[0].soma.v(0.5)) } ')
        h.v_MVL21_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVL22/0/GenericMuscleCell/v
        h(' objectvar v_MVL22_v_muscles_v ')
        h(' { v_MVL22_v_muscles_v = new Vector() } ')
        h(' { v_MVL22_v_muscles_v.record(&a_MVL22[0].soma.v(0.5)) } ')
        h.v_MVL22_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVL23/0/GenericMuscleCell/v
        h(' objectvar v_MVL23_v_muscles_v ')
        h(' { v_MVL23_v_muscles_v = new Vector() } ')
        h(' { v_MVL23_v_muscles_v.record(&a_MVL23[0].soma.v(0.5)) } ')
        h.v_MVL23_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVL24/0/GenericMuscleCell/v
        h(' objectvar v_MVL24_v_muscles_v ')
        h(' { v_MVL24_v_muscles_v = new Vector() } ')
        h(' { v_MVL24_v_muscles_v.record(&a_MVL24[0].soma.v(0.5)) } ')
        h.v_MVL24_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDL01/0/GenericMuscleCell/v
        h(' objectvar v_MDL01_v_muscles_v ')
        h(' { v_MDL01_v_muscles_v = new Vector() } ')
        h(' { v_MDL01_v_muscles_v.record(&a_MDL01[0].soma.v(0.5)) } ')
        h.v_MDL01_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDL02/0/GenericMuscleCell/v
        h(' objectvar v_MDL02_v_muscles_v ')
        h(' { v_MDL02_v_muscles_v = new Vector() } ')
        h(' { v_MDL02_v_muscles_v.record(&a_MDL02[0].soma.v(0.5)) } ')
        h.v_MDL02_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDL03/0/GenericMuscleCell/v
        h(' objectvar v_MDL03_v_muscles_v ')
        h(' { v_MDL03_v_muscles_v = new Vector() } ')
        h(' { v_MDL03_v_muscles_v.record(&a_MDL03[0].soma.v(0.5)) } ')
        h.v_MDL03_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDL04/0/GenericMuscleCell/v
        h(' objectvar v_MDL04_v_muscles_v ')
        h(' { v_MDL04_v_muscles_v = new Vector() } ')
        h(' { v_MDL04_v_muscles_v.record(&a_MDL04[0].soma.v(0.5)) } ')
        h.v_MDL04_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDL05/0/GenericMuscleCell/v
        h(' objectvar v_MDL05_v_muscles_v ')
        h(' { v_MDL05_v_muscles_v = new Vector() } ')
        h(' { v_MDL05_v_muscles_v.record(&a_MDL05[0].soma.v(0.5)) } ')
        h.v_MDL05_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDL06/0/GenericMuscleCell/v
        h(' objectvar v_MDL06_v_muscles_v ')
        h(' { v_MDL06_v_muscles_v = new Vector() } ')
        h(' { v_MDL06_v_muscles_v.record(&a_MDL06[0].soma.v(0.5)) } ')
        h.v_MDL06_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDL07/0/GenericMuscleCell/v
        h(' objectvar v_MDL07_v_muscles_v ')
        h(' { v_MDL07_v_muscles_v = new Vector() } ')
        h(' { v_MDL07_v_muscles_v.record(&a_MDL07[0].soma.v(0.5)) } ')
        h.v_MDL07_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDL08/0/GenericMuscleCell/v
        h(' objectvar v_MDL08_v_muscles_v ')
        h(' { v_MDL08_v_muscles_v = new Vector() } ')
        h(' { v_MDL08_v_muscles_v.record(&a_MDL08[0].soma.v(0.5)) } ')
        h.v_MDL08_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDL09/0/GenericMuscleCell/v
        h(' objectvar v_MDL09_v_muscles_v ')
        h(' { v_MDL09_v_muscles_v = new Vector() } ')
        h(' { v_MDL09_v_muscles_v.record(&a_MDL09[0].soma.v(0.5)) } ')
        h.v_MDL09_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDL10/0/GenericMuscleCell/v
        h(' objectvar v_MDL10_v_muscles_v ')
        h(' { v_MDL10_v_muscles_v = new Vector() } ')
        h(' { v_MDL10_v_muscles_v.record(&a_MDL10[0].soma.v(0.5)) } ')
        h.v_MDL10_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDL11/0/GenericMuscleCell/v
        h(' objectvar v_MDL11_v_muscles_v ')
        h(' { v_MDL11_v_muscles_v = new Vector() } ')
        h(' { v_MDL11_v_muscles_v.record(&a_MDL11[0].soma.v(0.5)) } ')
        h.v_MDL11_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDL12/0/GenericMuscleCell/v
        h(' objectvar v_MDL12_v_muscles_v ')
        h(' { v_MDL12_v_muscles_v = new Vector() } ')
        h(' { v_MDL12_v_muscles_v.record(&a_MDL12[0].soma.v(0.5)) } ')
        h.v_MDL12_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDL13/0/GenericMuscleCell/v
        h(' objectvar v_MDL13_v_muscles_v ')
        h(' { v_MDL13_v_muscles_v = new Vector() } ')
        h(' { v_MDL13_v_muscles_v.record(&a_MDL13[0].soma.v(0.5)) } ')
        h.v_MDL13_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDL14/0/GenericMuscleCell/v
        h(' objectvar v_MDL14_v_muscles_v ')
        h(' { v_MDL14_v_muscles_v = new Vector() } ')
        h(' { v_MDL14_v_muscles_v.record(&a_MDL14[0].soma.v(0.5)) } ')
        h.v_MDL14_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDL15/0/GenericMuscleCell/v
        h(' objectvar v_MDL15_v_muscles_v ')
        h(' { v_MDL15_v_muscles_v = new Vector() } ')
        h(' { v_MDL15_v_muscles_v.record(&a_MDL15[0].soma.v(0.5)) } ')
        h.v_MDL15_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDL16/0/GenericMuscleCell/v
        h(' objectvar v_MDL16_v_muscles_v ')
        h(' { v_MDL16_v_muscles_v = new Vector() } ')
        h(' { v_MDL16_v_muscles_v.record(&a_MDL16[0].soma.v(0.5)) } ')
        h.v_MDL16_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDL17/0/GenericMuscleCell/v
        h(' objectvar v_MDL17_v_muscles_v ')
        h(' { v_MDL17_v_muscles_v = new Vector() } ')
        h(' { v_MDL17_v_muscles_v.record(&a_MDL17[0].soma.v(0.5)) } ')
        h.v_MDL17_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDL18/0/GenericMuscleCell/v
        h(' objectvar v_MDL18_v_muscles_v ')
        h(' { v_MDL18_v_muscles_v = new Vector() } ')
        h(' { v_MDL18_v_muscles_v.record(&a_MDL18[0].soma.v(0.5)) } ')
        h.v_MDL18_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDL19/0/GenericMuscleCell/v
        h(' objectvar v_MDL19_v_muscles_v ')
        h(' { v_MDL19_v_muscles_v = new Vector() } ')
        h(' { v_MDL19_v_muscles_v.record(&a_MDL19[0].soma.v(0.5)) } ')
        h.v_MDL19_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDL20/0/GenericMuscleCell/v
        h(' objectvar v_MDL20_v_muscles_v ')
        h(' { v_MDL20_v_muscles_v = new Vector() } ')
        h(' { v_MDL20_v_muscles_v.record(&a_MDL20[0].soma.v(0.5)) } ')
        h.v_MDL20_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDL21/0/GenericMuscleCell/v
        h(' objectvar v_MDL21_v_muscles_v ')
        h(' { v_MDL21_v_muscles_v = new Vector() } ')
        h(' { v_MDL21_v_muscles_v.record(&a_MDL21[0].soma.v(0.5)) } ')
        h.v_MDL21_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDL22/0/GenericMuscleCell/v
        h(' objectvar v_MDL22_v_muscles_v ')
        h(' { v_MDL22_v_muscles_v = new Vector() } ')
        h(' { v_MDL22_v_muscles_v.record(&a_MDL22[0].soma.v(0.5)) } ')
        h.v_MDL22_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDL23/0/GenericMuscleCell/v
        h(' objectvar v_MDL23_v_muscles_v ')
        h(' { v_MDL23_v_muscles_v = new Vector() } ')
        h(' { v_MDL23_v_muscles_v.record(&a_MDL23[0].soma.v(0.5)) } ')
        h.v_MDL23_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDL24/0/GenericMuscleCell/v
        h(' objectvar v_MDL24_v_muscles_v ')
        h(' { v_MDL24_v_muscles_v = new Vector() } ')
        h(' { v_MDL24_v_muscles_v.record(&a_MDL24[0].soma.v(0.5)) } ')
        h.v_MDL24_v_muscles_v.resize((h.tstop * h.steps_per_ms) + 1)

        # ######################   File to save: c302_C2_AVB_DB.muscles.activity.dat (muscles_activity)
        # Column: MDR01/0/GenericMuscleCell/caConc
        h(' objectvar v_MDR01_v_muscles_activity ')
        h(' { v_MDR01_v_muscles_activity = new Vector() } ')
        h(' { v_MDR01_v_muscles_activity.record(&a_MDR01[0].soma.cai(0.5)) } ')
        h.v_MDR01_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDR02/0/GenericMuscleCell/caConc
        h(' objectvar v_MDR02_v_muscles_activity ')
        h(' { v_MDR02_v_muscles_activity = new Vector() } ')
        h(' { v_MDR02_v_muscles_activity.record(&a_MDR02[0].soma.cai(0.5)) } ')
        h.v_MDR02_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDR03/0/GenericMuscleCell/caConc
        h(' objectvar v_MDR03_v_muscles_activity ')
        h(' { v_MDR03_v_muscles_activity = new Vector() } ')
        h(' { v_MDR03_v_muscles_activity.record(&a_MDR03[0].soma.cai(0.5)) } ')
        h.v_MDR03_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDR04/0/GenericMuscleCell/caConc
        h(' objectvar v_MDR04_v_muscles_activity ')
        h(' { v_MDR04_v_muscles_activity = new Vector() } ')
        h(' { v_MDR04_v_muscles_activity.record(&a_MDR04[0].soma.cai(0.5)) } ')
        h.v_MDR04_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDR05/0/GenericMuscleCell/caConc
        h(' objectvar v_MDR05_v_muscles_activity ')
        h(' { v_MDR05_v_muscles_activity = new Vector() } ')
        h(' { v_MDR05_v_muscles_activity.record(&a_MDR05[0].soma.cai(0.5)) } ')
        h.v_MDR05_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDR06/0/GenericMuscleCell/caConc
        h(' objectvar v_MDR06_v_muscles_activity ')
        h(' { v_MDR06_v_muscles_activity = new Vector() } ')
        h(' { v_MDR06_v_muscles_activity.record(&a_MDR06[0].soma.cai(0.5)) } ')
        h.v_MDR06_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDR07/0/GenericMuscleCell/caConc
        h(' objectvar v_MDR07_v_muscles_activity ')
        h(' { v_MDR07_v_muscles_activity = new Vector() } ')
        h(' { v_MDR07_v_muscles_activity.record(&a_MDR07[0].soma.cai(0.5)) } ')
        h.v_MDR07_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDR08/0/GenericMuscleCell/caConc
        h(' objectvar v_MDR08_v_muscles_activity ')
        h(' { v_MDR08_v_muscles_activity = new Vector() } ')
        h(' { v_MDR08_v_muscles_activity.record(&a_MDR08[0].soma.cai(0.5)) } ')
        h.v_MDR08_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDR09/0/GenericMuscleCell/caConc
        h(' objectvar v_MDR09_v_muscles_activity ')
        h(' { v_MDR09_v_muscles_activity = new Vector() } ')
        h(' { v_MDR09_v_muscles_activity.record(&a_MDR09[0].soma.cai(0.5)) } ')
        h.v_MDR09_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDR10/0/GenericMuscleCell/caConc
        h(' objectvar v_MDR10_v_muscles_activity ')
        h(' { v_MDR10_v_muscles_activity = new Vector() } ')
        h(' { v_MDR10_v_muscles_activity.record(&a_MDR10[0].soma.cai(0.5)) } ')
        h.v_MDR10_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDR11/0/GenericMuscleCell/caConc
        h(' objectvar v_MDR11_v_muscles_activity ')
        h(' { v_MDR11_v_muscles_activity = new Vector() } ')
        h(' { v_MDR11_v_muscles_activity.record(&a_MDR11[0].soma.cai(0.5)) } ')
        h.v_MDR11_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDR12/0/GenericMuscleCell/caConc
        h(' objectvar v_MDR12_v_muscles_activity ')
        h(' { v_MDR12_v_muscles_activity = new Vector() } ')
        h(' { v_MDR12_v_muscles_activity.record(&a_MDR12[0].soma.cai(0.5)) } ')
        h.v_MDR12_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDR13/0/GenericMuscleCell/caConc
        h(' objectvar v_MDR13_v_muscles_activity ')
        h(' { v_MDR13_v_muscles_activity = new Vector() } ')
        h(' { v_MDR13_v_muscles_activity.record(&a_MDR13[0].soma.cai(0.5)) } ')
        h.v_MDR13_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDR14/0/GenericMuscleCell/caConc
        h(' objectvar v_MDR14_v_muscles_activity ')
        h(' { v_MDR14_v_muscles_activity = new Vector() } ')
        h(' { v_MDR14_v_muscles_activity.record(&a_MDR14[0].soma.cai(0.5)) } ')
        h.v_MDR14_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDR15/0/GenericMuscleCell/caConc
        h(' objectvar v_MDR15_v_muscles_activity ')
        h(' { v_MDR15_v_muscles_activity = new Vector() } ')
        h(' { v_MDR15_v_muscles_activity.record(&a_MDR15[0].soma.cai(0.5)) } ')
        h.v_MDR15_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDR16/0/GenericMuscleCell/caConc
        h(' objectvar v_MDR16_v_muscles_activity ')
        h(' { v_MDR16_v_muscles_activity = new Vector() } ')
        h(' { v_MDR16_v_muscles_activity.record(&a_MDR16[0].soma.cai(0.5)) } ')
        h.v_MDR16_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDR17/0/GenericMuscleCell/caConc
        h(' objectvar v_MDR17_v_muscles_activity ')
        h(' { v_MDR17_v_muscles_activity = new Vector() } ')
        h(' { v_MDR17_v_muscles_activity.record(&a_MDR17[0].soma.cai(0.5)) } ')
        h.v_MDR17_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDR18/0/GenericMuscleCell/caConc
        h(' objectvar v_MDR18_v_muscles_activity ')
        h(' { v_MDR18_v_muscles_activity = new Vector() } ')
        h(' { v_MDR18_v_muscles_activity.record(&a_MDR18[0].soma.cai(0.5)) } ')
        h.v_MDR18_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDR19/0/GenericMuscleCell/caConc
        h(' objectvar v_MDR19_v_muscles_activity ')
        h(' { v_MDR19_v_muscles_activity = new Vector() } ')
        h(' { v_MDR19_v_muscles_activity.record(&a_MDR19[0].soma.cai(0.5)) } ')
        h.v_MDR19_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDR20/0/GenericMuscleCell/caConc
        h(' objectvar v_MDR20_v_muscles_activity ')
        h(' { v_MDR20_v_muscles_activity = new Vector() } ')
        h(' { v_MDR20_v_muscles_activity.record(&a_MDR20[0].soma.cai(0.5)) } ')
        h.v_MDR20_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDR21/0/GenericMuscleCell/caConc
        h(' objectvar v_MDR21_v_muscles_activity ')
        h(' { v_MDR21_v_muscles_activity = new Vector() } ')
        h(' { v_MDR21_v_muscles_activity.record(&a_MDR21[0].soma.cai(0.5)) } ')
        h.v_MDR21_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDR22/0/GenericMuscleCell/caConc
        h(' objectvar v_MDR22_v_muscles_activity ')
        h(' { v_MDR22_v_muscles_activity = new Vector() } ')
        h(' { v_MDR22_v_muscles_activity.record(&a_MDR22[0].soma.cai(0.5)) } ')
        h.v_MDR22_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDR23/0/GenericMuscleCell/caConc
        h(' objectvar v_MDR23_v_muscles_activity ')
        h(' { v_MDR23_v_muscles_activity = new Vector() } ')
        h(' { v_MDR23_v_muscles_activity.record(&a_MDR23[0].soma.cai(0.5)) } ')
        h.v_MDR23_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDR24/0/GenericMuscleCell/caConc
        h(' objectvar v_MDR24_v_muscles_activity ')
        h(' { v_MDR24_v_muscles_activity = new Vector() } ')
        h(' { v_MDR24_v_muscles_activity.record(&a_MDR24[0].soma.cai(0.5)) } ')
        h.v_MDR24_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVR01/0/GenericMuscleCell/caConc
        h(' objectvar v_MVR01_v_muscles_activity ')
        h(' { v_MVR01_v_muscles_activity = new Vector() } ')
        h(' { v_MVR01_v_muscles_activity.record(&a_MVR01[0].soma.cai(0.5)) } ')
        h.v_MVR01_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVR02/0/GenericMuscleCell/caConc
        h(' objectvar v_MVR02_v_muscles_activity ')
        h(' { v_MVR02_v_muscles_activity = new Vector() } ')
        h(' { v_MVR02_v_muscles_activity.record(&a_MVR02[0].soma.cai(0.5)) } ')
        h.v_MVR02_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVR03/0/GenericMuscleCell/caConc
        h(' objectvar v_MVR03_v_muscles_activity ')
        h(' { v_MVR03_v_muscles_activity = new Vector() } ')
        h(' { v_MVR03_v_muscles_activity.record(&a_MVR03[0].soma.cai(0.5)) } ')
        h.v_MVR03_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVR04/0/GenericMuscleCell/caConc
        h(' objectvar v_MVR04_v_muscles_activity ')
        h(' { v_MVR04_v_muscles_activity = new Vector() } ')
        h(' { v_MVR04_v_muscles_activity.record(&a_MVR04[0].soma.cai(0.5)) } ')
        h.v_MVR04_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVR05/0/GenericMuscleCell/caConc
        h(' objectvar v_MVR05_v_muscles_activity ')
        h(' { v_MVR05_v_muscles_activity = new Vector() } ')
        h(' { v_MVR05_v_muscles_activity.record(&a_MVR05[0].soma.cai(0.5)) } ')
        h.v_MVR05_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVR06/0/GenericMuscleCell/caConc
        h(' objectvar v_MVR06_v_muscles_activity ')
        h(' { v_MVR06_v_muscles_activity = new Vector() } ')
        h(' { v_MVR06_v_muscles_activity.record(&a_MVR06[0].soma.cai(0.5)) } ')
        h.v_MVR06_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVR07/0/GenericMuscleCell/caConc
        h(' objectvar v_MVR07_v_muscles_activity ')
        h(' { v_MVR07_v_muscles_activity = new Vector() } ')
        h(' { v_MVR07_v_muscles_activity.record(&a_MVR07[0].soma.cai(0.5)) } ')
        h.v_MVR07_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVR08/0/GenericMuscleCell/caConc
        h(' objectvar v_MVR08_v_muscles_activity ')
        h(' { v_MVR08_v_muscles_activity = new Vector() } ')
        h(' { v_MVR08_v_muscles_activity.record(&a_MVR08[0].soma.cai(0.5)) } ')
        h.v_MVR08_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVR09/0/GenericMuscleCell/caConc
        h(' objectvar v_MVR09_v_muscles_activity ')
        h(' { v_MVR09_v_muscles_activity = new Vector() } ')
        h(' { v_MVR09_v_muscles_activity.record(&a_MVR09[0].soma.cai(0.5)) } ')
        h.v_MVR09_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVR10/0/GenericMuscleCell/caConc
        h(' objectvar v_MVR10_v_muscles_activity ')
        h(' { v_MVR10_v_muscles_activity = new Vector() } ')
        h(' { v_MVR10_v_muscles_activity.record(&a_MVR10[0].soma.cai(0.5)) } ')
        h.v_MVR10_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVR11/0/GenericMuscleCell/caConc
        h(' objectvar v_MVR11_v_muscles_activity ')
        h(' { v_MVR11_v_muscles_activity = new Vector() } ')
        h(' { v_MVR11_v_muscles_activity.record(&a_MVR11[0].soma.cai(0.5)) } ')
        h.v_MVR11_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVR12/0/GenericMuscleCell/caConc
        h(' objectvar v_MVR12_v_muscles_activity ')
        h(' { v_MVR12_v_muscles_activity = new Vector() } ')
        h(' { v_MVR12_v_muscles_activity.record(&a_MVR12[0].soma.cai(0.5)) } ')
        h.v_MVR12_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVR13/0/GenericMuscleCell/caConc
        h(' objectvar v_MVR13_v_muscles_activity ')
        h(' { v_MVR13_v_muscles_activity = new Vector() } ')
        h(' { v_MVR13_v_muscles_activity.record(&a_MVR13[0].soma.cai(0.5)) } ')
        h.v_MVR13_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVR14/0/GenericMuscleCell/caConc
        h(' objectvar v_MVR14_v_muscles_activity ')
        h(' { v_MVR14_v_muscles_activity = new Vector() } ')
        h(' { v_MVR14_v_muscles_activity.record(&a_MVR14[0].soma.cai(0.5)) } ')
        h.v_MVR14_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVR15/0/GenericMuscleCell/caConc
        h(' objectvar v_MVR15_v_muscles_activity ')
        h(' { v_MVR15_v_muscles_activity = new Vector() } ')
        h(' { v_MVR15_v_muscles_activity.record(&a_MVR15[0].soma.cai(0.5)) } ')
        h.v_MVR15_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVR16/0/GenericMuscleCell/caConc
        h(' objectvar v_MVR16_v_muscles_activity ')
        h(' { v_MVR16_v_muscles_activity = new Vector() } ')
        h(' { v_MVR16_v_muscles_activity.record(&a_MVR16[0].soma.cai(0.5)) } ')
        h.v_MVR16_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVR17/0/GenericMuscleCell/caConc
        h(' objectvar v_MVR17_v_muscles_activity ')
        h(' { v_MVR17_v_muscles_activity = new Vector() } ')
        h(' { v_MVR17_v_muscles_activity.record(&a_MVR17[0].soma.cai(0.5)) } ')
        h.v_MVR17_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVR18/0/GenericMuscleCell/caConc
        h(' objectvar v_MVR18_v_muscles_activity ')
        h(' { v_MVR18_v_muscles_activity = new Vector() } ')
        h(' { v_MVR18_v_muscles_activity.record(&a_MVR18[0].soma.cai(0.5)) } ')
        h.v_MVR18_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVR19/0/GenericMuscleCell/caConc
        h(' objectvar v_MVR19_v_muscles_activity ')
        h(' { v_MVR19_v_muscles_activity = new Vector() } ')
        h(' { v_MVR19_v_muscles_activity.record(&a_MVR19[0].soma.cai(0.5)) } ')
        h.v_MVR19_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVR20/0/GenericMuscleCell/caConc
        h(' objectvar v_MVR20_v_muscles_activity ')
        h(' { v_MVR20_v_muscles_activity = new Vector() } ')
        h(' { v_MVR20_v_muscles_activity.record(&a_MVR20[0].soma.cai(0.5)) } ')
        h.v_MVR20_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVR21/0/GenericMuscleCell/caConc
        h(' objectvar v_MVR21_v_muscles_activity ')
        h(' { v_MVR21_v_muscles_activity = new Vector() } ')
        h(' { v_MVR21_v_muscles_activity.record(&a_MVR21[0].soma.cai(0.5)) } ')
        h.v_MVR21_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVR22/0/GenericMuscleCell/caConc
        h(' objectvar v_MVR22_v_muscles_activity ')
        h(' { v_MVR22_v_muscles_activity = new Vector() } ')
        h(' { v_MVR22_v_muscles_activity.record(&a_MVR22[0].soma.cai(0.5)) } ')
        h.v_MVR22_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVR23/0/GenericMuscleCell/caConc
        h(' objectvar v_MVR23_v_muscles_activity ')
        h(' { v_MVR23_v_muscles_activity = new Vector() } ')
        h(' { v_MVR23_v_muscles_activity.record(&a_MVR23[0].soma.cai(0.5)) } ')
        h.v_MVR23_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVL01/0/GenericMuscleCell/caConc
        h(' objectvar v_MVL01_v_muscles_activity ')
        h(' { v_MVL01_v_muscles_activity = new Vector() } ')
        h(' { v_MVL01_v_muscles_activity.record(&a_MVL01[0].soma.cai(0.5)) } ')
        h.v_MVL01_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVL02/0/GenericMuscleCell/caConc
        h(' objectvar v_MVL02_v_muscles_activity ')
        h(' { v_MVL02_v_muscles_activity = new Vector() } ')
        h(' { v_MVL02_v_muscles_activity.record(&a_MVL02[0].soma.cai(0.5)) } ')
        h.v_MVL02_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVL03/0/GenericMuscleCell/caConc
        h(' objectvar v_MVL03_v_muscles_activity ')
        h(' { v_MVL03_v_muscles_activity = new Vector() } ')
        h(' { v_MVL03_v_muscles_activity.record(&a_MVL03[0].soma.cai(0.5)) } ')
        h.v_MVL03_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVL04/0/GenericMuscleCell/caConc
        h(' objectvar v_MVL04_v_muscles_activity ')
        h(' { v_MVL04_v_muscles_activity = new Vector() } ')
        h(' { v_MVL04_v_muscles_activity.record(&a_MVL04[0].soma.cai(0.5)) } ')
        h.v_MVL04_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVL05/0/GenericMuscleCell/caConc
        h(' objectvar v_MVL05_v_muscles_activity ')
        h(' { v_MVL05_v_muscles_activity = new Vector() } ')
        h(' { v_MVL05_v_muscles_activity.record(&a_MVL05[0].soma.cai(0.5)) } ')
        h.v_MVL05_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVL06/0/GenericMuscleCell/caConc
        h(' objectvar v_MVL06_v_muscles_activity ')
        h(' { v_MVL06_v_muscles_activity = new Vector() } ')
        h(' { v_MVL06_v_muscles_activity.record(&a_MVL06[0].soma.cai(0.5)) } ')
        h.v_MVL06_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVL07/0/GenericMuscleCell/caConc
        h(' objectvar v_MVL07_v_muscles_activity ')
        h(' { v_MVL07_v_muscles_activity = new Vector() } ')
        h(' { v_MVL07_v_muscles_activity.record(&a_MVL07[0].soma.cai(0.5)) } ')
        h.v_MVL07_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVL08/0/GenericMuscleCell/caConc
        h(' objectvar v_MVL08_v_muscles_activity ')
        h(' { v_MVL08_v_muscles_activity = new Vector() } ')
        h(' { v_MVL08_v_muscles_activity.record(&a_MVL08[0].soma.cai(0.5)) } ')
        h.v_MVL08_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVL09/0/GenericMuscleCell/caConc
        h(' objectvar v_MVL09_v_muscles_activity ')
        h(' { v_MVL09_v_muscles_activity = new Vector() } ')
        h(' { v_MVL09_v_muscles_activity.record(&a_MVL09[0].soma.cai(0.5)) } ')
        h.v_MVL09_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVL10/0/GenericMuscleCell/caConc
        h(' objectvar v_MVL10_v_muscles_activity ')
        h(' { v_MVL10_v_muscles_activity = new Vector() } ')
        h(' { v_MVL10_v_muscles_activity.record(&a_MVL10[0].soma.cai(0.5)) } ')
        h.v_MVL10_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVL11/0/GenericMuscleCell/caConc
        h(' objectvar v_MVL11_v_muscles_activity ')
        h(' { v_MVL11_v_muscles_activity = new Vector() } ')
        h(' { v_MVL11_v_muscles_activity.record(&a_MVL11[0].soma.cai(0.5)) } ')
        h.v_MVL11_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVL12/0/GenericMuscleCell/caConc
        h(' objectvar v_MVL12_v_muscles_activity ')
        h(' { v_MVL12_v_muscles_activity = new Vector() } ')
        h(' { v_MVL12_v_muscles_activity.record(&a_MVL12[0].soma.cai(0.5)) } ')
        h.v_MVL12_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVL13/0/GenericMuscleCell/caConc
        h(' objectvar v_MVL13_v_muscles_activity ')
        h(' { v_MVL13_v_muscles_activity = new Vector() } ')
        h(' { v_MVL13_v_muscles_activity.record(&a_MVL13[0].soma.cai(0.5)) } ')
        h.v_MVL13_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVL14/0/GenericMuscleCell/caConc
        h(' objectvar v_MVL14_v_muscles_activity ')
        h(' { v_MVL14_v_muscles_activity = new Vector() } ')
        h(' { v_MVL14_v_muscles_activity.record(&a_MVL14[0].soma.cai(0.5)) } ')
        h.v_MVL14_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVL15/0/GenericMuscleCell/caConc
        h(' objectvar v_MVL15_v_muscles_activity ')
        h(' { v_MVL15_v_muscles_activity = new Vector() } ')
        h(' { v_MVL15_v_muscles_activity.record(&a_MVL15[0].soma.cai(0.5)) } ')
        h.v_MVL15_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVL16/0/GenericMuscleCell/caConc
        h(' objectvar v_MVL16_v_muscles_activity ')
        h(' { v_MVL16_v_muscles_activity = new Vector() } ')
        h(' { v_MVL16_v_muscles_activity.record(&a_MVL16[0].soma.cai(0.5)) } ')
        h.v_MVL16_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVL17/0/GenericMuscleCell/caConc
        h(' objectvar v_MVL17_v_muscles_activity ')
        h(' { v_MVL17_v_muscles_activity = new Vector() } ')
        h(' { v_MVL17_v_muscles_activity.record(&a_MVL17[0].soma.cai(0.5)) } ')
        h.v_MVL17_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVL18/0/GenericMuscleCell/caConc
        h(' objectvar v_MVL18_v_muscles_activity ')
        h(' { v_MVL18_v_muscles_activity = new Vector() } ')
        h(' { v_MVL18_v_muscles_activity.record(&a_MVL18[0].soma.cai(0.5)) } ')
        h.v_MVL18_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVL19/0/GenericMuscleCell/caConc
        h(' objectvar v_MVL19_v_muscles_activity ')
        h(' { v_MVL19_v_muscles_activity = new Vector() } ')
        h(' { v_MVL19_v_muscles_activity.record(&a_MVL19[0].soma.cai(0.5)) } ')
        h.v_MVL19_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVL20/0/GenericMuscleCell/caConc
        h(' objectvar v_MVL20_v_muscles_activity ')
        h(' { v_MVL20_v_muscles_activity = new Vector() } ')
        h(' { v_MVL20_v_muscles_activity.record(&a_MVL20[0].soma.cai(0.5)) } ')
        h.v_MVL20_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVL21/0/GenericMuscleCell/caConc
        h(' objectvar v_MVL21_v_muscles_activity ')
        h(' { v_MVL21_v_muscles_activity = new Vector() } ')
        h(' { v_MVL21_v_muscles_activity.record(&a_MVL21[0].soma.cai(0.5)) } ')
        h.v_MVL21_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVL22/0/GenericMuscleCell/caConc
        h(' objectvar v_MVL22_v_muscles_activity ')
        h(' { v_MVL22_v_muscles_activity = new Vector() } ')
        h(' { v_MVL22_v_muscles_activity.record(&a_MVL22[0].soma.cai(0.5)) } ')
        h.v_MVL22_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVL23/0/GenericMuscleCell/caConc
        h(' objectvar v_MVL23_v_muscles_activity ')
        h(' { v_MVL23_v_muscles_activity = new Vector() } ')
        h(' { v_MVL23_v_muscles_activity.record(&a_MVL23[0].soma.cai(0.5)) } ')
        h.v_MVL23_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MVL24/0/GenericMuscleCell/caConc
        h(' objectvar v_MVL24_v_muscles_activity ')
        h(' { v_MVL24_v_muscles_activity = new Vector() } ')
        h(' { v_MVL24_v_muscles_activity.record(&a_MVL24[0].soma.cai(0.5)) } ')
        h.v_MVL24_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDL01/0/GenericMuscleCell/caConc
        h(' objectvar v_MDL01_v_muscles_activity ')
        h(' { v_MDL01_v_muscles_activity = new Vector() } ')
        h(' { v_MDL01_v_muscles_activity.record(&a_MDL01[0].soma.cai(0.5)) } ')
        h.v_MDL01_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDL02/0/GenericMuscleCell/caConc
        h(' objectvar v_MDL02_v_muscles_activity ')
        h(' { v_MDL02_v_muscles_activity = new Vector() } ')
        h(' { v_MDL02_v_muscles_activity.record(&a_MDL02[0].soma.cai(0.5)) } ')
        h.v_MDL02_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDL03/0/GenericMuscleCell/caConc
        h(' objectvar v_MDL03_v_muscles_activity ')
        h(' { v_MDL03_v_muscles_activity = new Vector() } ')
        h(' { v_MDL03_v_muscles_activity.record(&a_MDL03[0].soma.cai(0.5)) } ')
        h.v_MDL03_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDL04/0/GenericMuscleCell/caConc
        h(' objectvar v_MDL04_v_muscles_activity ')
        h(' { v_MDL04_v_muscles_activity = new Vector() } ')
        h(' { v_MDL04_v_muscles_activity.record(&a_MDL04[0].soma.cai(0.5)) } ')
        h.v_MDL04_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDL05/0/GenericMuscleCell/caConc
        h(' objectvar v_MDL05_v_muscles_activity ')
        h(' { v_MDL05_v_muscles_activity = new Vector() } ')
        h(' { v_MDL05_v_muscles_activity.record(&a_MDL05[0].soma.cai(0.5)) } ')
        h.v_MDL05_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDL06/0/GenericMuscleCell/caConc
        h(' objectvar v_MDL06_v_muscles_activity ')
        h(' { v_MDL06_v_muscles_activity = new Vector() } ')
        h(' { v_MDL06_v_muscles_activity.record(&a_MDL06[0].soma.cai(0.5)) } ')
        h.v_MDL06_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDL07/0/GenericMuscleCell/caConc
        h(' objectvar v_MDL07_v_muscles_activity ')
        h(' { v_MDL07_v_muscles_activity = new Vector() } ')
        h(' { v_MDL07_v_muscles_activity.record(&a_MDL07[0].soma.cai(0.5)) } ')
        h.v_MDL07_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDL08/0/GenericMuscleCell/caConc
        h(' objectvar v_MDL08_v_muscles_activity ')
        h(' { v_MDL08_v_muscles_activity = new Vector() } ')
        h(' { v_MDL08_v_muscles_activity.record(&a_MDL08[0].soma.cai(0.5)) } ')
        h.v_MDL08_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDL09/0/GenericMuscleCell/caConc
        h(' objectvar v_MDL09_v_muscles_activity ')
        h(' { v_MDL09_v_muscles_activity = new Vector() } ')
        h(' { v_MDL09_v_muscles_activity.record(&a_MDL09[0].soma.cai(0.5)) } ')
        h.v_MDL09_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDL10/0/GenericMuscleCell/caConc
        h(' objectvar v_MDL10_v_muscles_activity ')
        h(' { v_MDL10_v_muscles_activity = new Vector() } ')
        h(' { v_MDL10_v_muscles_activity.record(&a_MDL10[0].soma.cai(0.5)) } ')
        h.v_MDL10_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDL11/0/GenericMuscleCell/caConc
        h(' objectvar v_MDL11_v_muscles_activity ')
        h(' { v_MDL11_v_muscles_activity = new Vector() } ')
        h(' { v_MDL11_v_muscles_activity.record(&a_MDL11[0].soma.cai(0.5)) } ')
        h.v_MDL11_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDL12/0/GenericMuscleCell/caConc
        h(' objectvar v_MDL12_v_muscles_activity ')
        h(' { v_MDL12_v_muscles_activity = new Vector() } ')
        h(' { v_MDL12_v_muscles_activity.record(&a_MDL12[0].soma.cai(0.5)) } ')
        h.v_MDL12_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDL13/0/GenericMuscleCell/caConc
        h(' objectvar v_MDL13_v_muscles_activity ')
        h(' { v_MDL13_v_muscles_activity = new Vector() } ')
        h(' { v_MDL13_v_muscles_activity.record(&a_MDL13[0].soma.cai(0.5)) } ')
        h.v_MDL13_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDL14/0/GenericMuscleCell/caConc
        h(' objectvar v_MDL14_v_muscles_activity ')
        h(' { v_MDL14_v_muscles_activity = new Vector() } ')
        h(' { v_MDL14_v_muscles_activity.record(&a_MDL14[0].soma.cai(0.5)) } ')
        h.v_MDL14_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDL15/0/GenericMuscleCell/caConc
        h(' objectvar v_MDL15_v_muscles_activity ')
        h(' { v_MDL15_v_muscles_activity = new Vector() } ')
        h(' { v_MDL15_v_muscles_activity.record(&a_MDL15[0].soma.cai(0.5)) } ')
        h.v_MDL15_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDL16/0/GenericMuscleCell/caConc
        h(' objectvar v_MDL16_v_muscles_activity ')
        h(' { v_MDL16_v_muscles_activity = new Vector() } ')
        h(' { v_MDL16_v_muscles_activity.record(&a_MDL16[0].soma.cai(0.5)) } ')
        h.v_MDL16_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDL17/0/GenericMuscleCell/caConc
        h(' objectvar v_MDL17_v_muscles_activity ')
        h(' { v_MDL17_v_muscles_activity = new Vector() } ')
        h(' { v_MDL17_v_muscles_activity.record(&a_MDL17[0].soma.cai(0.5)) } ')
        h.v_MDL17_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDL18/0/GenericMuscleCell/caConc
        h(' objectvar v_MDL18_v_muscles_activity ')
        h(' { v_MDL18_v_muscles_activity = new Vector() } ')
        h(' { v_MDL18_v_muscles_activity.record(&a_MDL18[0].soma.cai(0.5)) } ')
        h.v_MDL18_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDL19/0/GenericMuscleCell/caConc
        h(' objectvar v_MDL19_v_muscles_activity ')
        h(' { v_MDL19_v_muscles_activity = new Vector() } ')
        h(' { v_MDL19_v_muscles_activity.record(&a_MDL19[0].soma.cai(0.5)) } ')
        h.v_MDL19_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDL20/0/GenericMuscleCell/caConc
        h(' objectvar v_MDL20_v_muscles_activity ')
        h(' { v_MDL20_v_muscles_activity = new Vector() } ')
        h(' { v_MDL20_v_muscles_activity.record(&a_MDL20[0].soma.cai(0.5)) } ')
        h.v_MDL20_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDL21/0/GenericMuscleCell/caConc
        h(' objectvar v_MDL21_v_muscles_activity ')
        h(' { v_MDL21_v_muscles_activity = new Vector() } ')
        h(' { v_MDL21_v_muscles_activity.record(&a_MDL21[0].soma.cai(0.5)) } ')
        h.v_MDL21_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDL22/0/GenericMuscleCell/caConc
        h(' objectvar v_MDL22_v_muscles_activity ')
        h(' { v_MDL22_v_muscles_activity = new Vector() } ')
        h(' { v_MDL22_v_muscles_activity.record(&a_MDL22[0].soma.cai(0.5)) } ')
        h.v_MDL22_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDL23/0/GenericMuscleCell/caConc
        h(' objectvar v_MDL23_v_muscles_activity ')
        h(' { v_MDL23_v_muscles_activity = new Vector() } ')
        h(' { v_MDL23_v_muscles_activity.record(&a_MDL23[0].soma.cai(0.5)) } ')
        h.v_MDL23_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: MDL24/0/GenericMuscleCell/caConc
        h(' objectvar v_MDL24_v_muscles_activity ')
        h(' { v_MDL24_v_muscles_activity = new Vector() } ')
        h(' { v_MDL24_v_muscles_activity.record(&a_MDL24[0].soma.cai(0.5)) } ')
        h.v_MDL24_v_muscles_activity.resize((h.tstop * h.steps_per_ms) + 1)

        # ######################   File to save: c302_C2_AVB_DB.dat (neurons_v)
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
        # Column: DB1/0/GenericNeuronCell/v
        h(' objectvar v_DB1_v_neurons_v ')
        h(' { v_DB1_v_neurons_v = new Vector() } ')
        h(' { v_DB1_v_neurons_v.record(&a_DB1[0].soma.v(0.5)) } ')
        h.v_DB1_v_neurons_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: DB2/0/GenericNeuronCell/v
        h(' objectvar v_DB2_v_neurons_v ')
        h(' { v_DB2_v_neurons_v = new Vector() } ')
        h(' { v_DB2_v_neurons_v.record(&a_DB2[0].soma.v(0.5)) } ')
        h.v_DB2_v_neurons_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: DB3/0/GenericNeuronCell/v
        h(' objectvar v_DB3_v_neurons_v ')
        h(' { v_DB3_v_neurons_v = new Vector() } ')
        h(' { v_DB3_v_neurons_v.record(&a_DB3[0].soma.v(0.5)) } ')
        h.v_DB3_v_neurons_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: DB4/0/GenericNeuronCell/v
        h(' objectvar v_DB4_v_neurons_v ')
        h(' { v_DB4_v_neurons_v = new Vector() } ')
        h(' { v_DB4_v_neurons_v.record(&a_DB4[0].soma.v(0.5)) } ')
        h.v_DB4_v_neurons_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: DB5/0/GenericNeuronCell/v
        h(' objectvar v_DB5_v_neurons_v ')
        h(' { v_DB5_v_neurons_v = new Vector() } ')
        h(' { v_DB5_v_neurons_v.record(&a_DB5[0].soma.v(0.5)) } ')
        h.v_DB5_v_neurons_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: DB6/0/GenericNeuronCell/v
        h(' objectvar v_DB6_v_neurons_v ')
        h(' { v_DB6_v_neurons_v = new Vector() } ')
        h(' { v_DB6_v_neurons_v.record(&a_DB6[0].soma.v(0.5)) } ')
        h.v_DB6_v_neurons_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: DB7/0/GenericNeuronCell/v
        h(' objectvar v_DB7_v_neurons_v ')
        h(' { v_DB7_v_neurons_v = new Vector() } ')
        h(' { v_DB7_v_neurons_v.record(&a_DB7[0].soma.v(0.5)) } ')
        h.v_DB7_v_neurons_v.resize((h.tstop * h.steps_per_ms) + 1)

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

        # ######################   File to save: c302_C2_AVB_DB.activity.dat (neurons_activity)
        py_v_AVBL_v_neurons_activity = [ float(x ) for x in h.v_AVBL_v_neurons_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_AVBR_v_neurons_activity = [ float(x ) for x in h.v_AVBR_v_neurons_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_DB1_v_neurons_activity = [ float(x ) for x in h.v_DB1_v_neurons_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_DB2_v_neurons_activity = [ float(x ) for x in h.v_DB2_v_neurons_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_DB3_v_neurons_activity = [ float(x ) for x in h.v_DB3_v_neurons_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_DB4_v_neurons_activity = [ float(x ) for x in h.v_DB4_v_neurons_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_DB5_v_neurons_activity = [ float(x ) for x in h.v_DB5_v_neurons_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_DB6_v_neurons_activity = [ float(x ) for x in h.v_DB6_v_neurons_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_DB7_v_neurons_activity = [ float(x ) for x in h.v_DB7_v_neurons_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration

        f_neurons_activity_f2 = open('c302_C2_AVB_DB.activity.dat', 'w')
        num_points = len(py_v_time)  # Simulation may have been stopped before tstop...

        for i in range(num_points):
            f_neurons_activity_f2.write('%e\t'% py_v_time[i]  + '%e\t'%(py_v_AVBL_v_neurons_activity[i])  + '%e\t'%(py_v_AVBR_v_neurons_activity[i])  + '%e\t'%(py_v_DB1_v_neurons_activity[i])  + '%e\t'%(py_v_DB2_v_neurons_activity[i])  + '%e\t'%(py_v_DB3_v_neurons_activity[i])  + '%e\t'%(py_v_DB4_v_neurons_activity[i])  + '%e\t'%(py_v_DB5_v_neurons_activity[i])  + '%e\t'%(py_v_DB6_v_neurons_activity[i])  + '%e\t'%(py_v_DB7_v_neurons_activity[i]) + '\n')
        f_neurons_activity_f2.close()
        print("Saved data to: c302_C2_AVB_DB.activity.dat")

        # ######################   File to save: c302_C2_AVB_DB.muscles.dat (muscles_v)
        py_v_MDR01_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MDR01_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MDR02_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MDR02_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MDR03_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MDR03_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MDR04_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MDR04_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MDR05_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MDR05_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MDR06_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MDR06_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MDR07_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MDR07_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MDR08_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MDR08_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MDR09_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MDR09_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MDR10_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MDR10_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MDR11_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MDR11_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MDR12_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MDR12_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MDR13_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MDR13_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MDR14_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MDR14_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MDR15_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MDR15_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MDR16_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MDR16_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MDR17_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MDR17_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MDR18_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MDR18_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MDR19_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MDR19_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MDR20_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MDR20_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MDR21_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MDR21_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MDR22_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MDR22_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MDR23_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MDR23_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MDR24_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MDR24_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MVR01_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MVR01_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MVR02_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MVR02_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MVR03_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MVR03_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MVR04_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MVR04_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MVR05_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MVR05_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MVR06_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MVR06_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MVR07_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MVR07_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MVR08_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MVR08_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MVR09_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MVR09_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MVR10_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MVR10_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MVR11_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MVR11_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MVR12_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MVR12_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MVR13_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MVR13_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MVR14_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MVR14_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MVR15_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MVR15_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MVR16_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MVR16_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MVR17_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MVR17_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MVR18_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MVR18_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MVR19_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MVR19_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MVR20_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MVR20_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MVR21_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MVR21_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MVR22_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MVR22_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MVR23_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MVR23_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MVL01_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MVL01_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MVL02_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MVL02_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MVL03_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MVL03_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MVL04_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MVL04_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MVL05_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MVL05_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MVL06_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MVL06_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MVL07_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MVL07_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MVL08_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MVL08_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MVL09_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MVL09_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MVL10_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MVL10_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MVL11_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MVL11_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MVL12_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MVL12_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MVL13_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MVL13_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MVL14_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MVL14_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MVL15_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MVL15_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MVL16_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MVL16_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MVL17_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MVL17_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MVL18_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MVL18_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MVL19_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MVL19_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MVL20_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MVL20_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MVL21_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MVL21_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MVL22_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MVL22_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MVL23_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MVL23_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MVL24_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MVL24_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MDL01_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MDL01_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MDL02_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MDL02_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MDL03_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MDL03_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MDL04_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MDL04_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MDL05_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MDL05_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MDL06_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MDL06_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MDL07_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MDL07_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MDL08_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MDL08_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MDL09_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MDL09_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MDL10_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MDL10_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MDL11_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MDL11_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MDL12_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MDL12_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MDL13_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MDL13_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MDL14_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MDL14_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MDL15_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MDL15_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MDL16_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MDL16_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MDL17_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MDL17_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MDL18_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MDL18_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MDL19_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MDL19_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MDL20_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MDL20_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MDL21_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MDL21_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MDL22_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MDL22_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MDL23_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MDL23_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_MDL24_v_muscles_v = [ float(x  / 1000.0) for x in h.v_MDL24_v_muscles_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage

        f_muscles_v_f2 = open('c302_C2_AVB_DB.muscles.dat', 'w')
        num_points = len(py_v_time)  # Simulation may have been stopped before tstop...

        for i in range(num_points):
            f_muscles_v_f2.write('%e\t'% py_v_time[i]  + '%e\t'%(py_v_MDR01_v_muscles_v[i])  + '%e\t'%(py_v_MDR02_v_muscles_v[i])  + '%e\t'%(py_v_MDR03_v_muscles_v[i])  + '%e\t'%(py_v_MDR04_v_muscles_v[i])  + '%e\t'%(py_v_MDR05_v_muscles_v[i])  + '%e\t'%(py_v_MDR06_v_muscles_v[i])  + '%e\t'%(py_v_MDR07_v_muscles_v[i])  + '%e\t'%(py_v_MDR08_v_muscles_v[i])  + '%e\t'%(py_v_MDR09_v_muscles_v[i])  + '%e\t'%(py_v_MDR10_v_muscles_v[i])  + '%e\t'%(py_v_MDR11_v_muscles_v[i])  + '%e\t'%(py_v_MDR12_v_muscles_v[i])  + '%e\t'%(py_v_MDR13_v_muscles_v[i])  + '%e\t'%(py_v_MDR14_v_muscles_v[i])  + '%e\t'%(py_v_MDR15_v_muscles_v[i])  + '%e\t'%(py_v_MDR16_v_muscles_v[i])  + '%e\t'%(py_v_MDR17_v_muscles_v[i])  + '%e\t'%(py_v_MDR18_v_muscles_v[i])  + '%e\t'%(py_v_MDR19_v_muscles_v[i])  + '%e\t'%(py_v_MDR20_v_muscles_v[i])  + '%e\t'%(py_v_MDR21_v_muscles_v[i])  + '%e\t'%(py_v_MDR22_v_muscles_v[i])  + '%e\t'%(py_v_MDR23_v_muscles_v[i])  + '%e\t'%(py_v_MDR24_v_muscles_v[i])  + '%e\t'%(py_v_MVR01_v_muscles_v[i])  + '%e\t'%(py_v_MVR02_v_muscles_v[i])  + '%e\t'%(py_v_MVR03_v_muscles_v[i])  + '%e\t'%(py_v_MVR04_v_muscles_v[i])  + '%e\t'%(py_v_MVR05_v_muscles_v[i])  + '%e\t'%(py_v_MVR06_v_muscles_v[i])  + '%e\t'%(py_v_MVR07_v_muscles_v[i])  + '%e\t'%(py_v_MVR08_v_muscles_v[i])  + '%e\t'%(py_v_MVR09_v_muscles_v[i])  + '%e\t'%(py_v_MVR10_v_muscles_v[i])  + '%e\t'%(py_v_MVR11_v_muscles_v[i])  + '%e\t'%(py_v_MVR12_v_muscles_v[i])  + '%e\t'%(py_v_MVR13_v_muscles_v[i])  + '%e\t'%(py_v_MVR14_v_muscles_v[i])  + '%e\t'%(py_v_MVR15_v_muscles_v[i])  + '%e\t'%(py_v_MVR16_v_muscles_v[i])  + '%e\t'%(py_v_MVR17_v_muscles_v[i])  + '%e\t'%(py_v_MVR18_v_muscles_v[i])  + '%e\t'%(py_v_MVR19_v_muscles_v[i])  + '%e\t'%(py_v_MVR20_v_muscles_v[i])  + '%e\t'%(py_v_MVR21_v_muscles_v[i])  + '%e\t'%(py_v_MVR22_v_muscles_v[i])  + '%e\t'%(py_v_MVR23_v_muscles_v[i])  + '%e\t'%(py_v_MVL01_v_muscles_v[i])  + '%e\t'%(py_v_MVL02_v_muscles_v[i])  + '%e\t'%(py_v_MVL03_v_muscles_v[i])  + '%e\t'%(py_v_MVL04_v_muscles_v[i])  + '%e\t'%(py_v_MVL05_v_muscles_v[i])  + '%e\t'%(py_v_MVL06_v_muscles_v[i])  + '%e\t'%(py_v_MVL07_v_muscles_v[i])  + '%e\t'%(py_v_MVL08_v_muscles_v[i])  + '%e\t'%(py_v_MVL09_v_muscles_v[i])  + '%e\t'%(py_v_MVL10_v_muscles_v[i])  + '%e\t'%(py_v_MVL11_v_muscles_v[i])  + '%e\t'%(py_v_MVL12_v_muscles_v[i])  + '%e\t'%(py_v_MVL13_v_muscles_v[i])  + '%e\t'%(py_v_MVL14_v_muscles_v[i])  + '%e\t'%(py_v_MVL15_v_muscles_v[i])  + '%e\t'%(py_v_MVL16_v_muscles_v[i])  + '%e\t'%(py_v_MVL17_v_muscles_v[i])  + '%e\t'%(py_v_MVL18_v_muscles_v[i])  + '%e\t'%(py_v_MVL19_v_muscles_v[i])  + '%e\t'%(py_v_MVL20_v_muscles_v[i])  + '%e\t'%(py_v_MVL21_v_muscles_v[i])  + '%e\t'%(py_v_MVL22_v_muscles_v[i])  + '%e\t'%(py_v_MVL23_v_muscles_v[i])  + '%e\t'%(py_v_MVL24_v_muscles_v[i])  + '%e\t'%(py_v_MDL01_v_muscles_v[i])  + '%e\t'%(py_v_MDL02_v_muscles_v[i])  + '%e\t'%(py_v_MDL03_v_muscles_v[i])  + '%e\t'%(py_v_MDL04_v_muscles_v[i])  + '%e\t'%(py_v_MDL05_v_muscles_v[i])  + '%e\t'%(py_v_MDL06_v_muscles_v[i])  + '%e\t'%(py_v_MDL07_v_muscles_v[i])  + '%e\t'%(py_v_MDL08_v_muscles_v[i])  + '%e\t'%(py_v_MDL09_v_muscles_v[i])  + '%e\t'%(py_v_MDL10_v_muscles_v[i])  + '%e\t'%(py_v_MDL11_v_muscles_v[i])  + '%e\t'%(py_v_MDL12_v_muscles_v[i])  + '%e\t'%(py_v_MDL13_v_muscles_v[i])  + '%e\t'%(py_v_MDL14_v_muscles_v[i])  + '%e\t'%(py_v_MDL15_v_muscles_v[i])  + '%e\t'%(py_v_MDL16_v_muscles_v[i])  + '%e\t'%(py_v_MDL17_v_muscles_v[i])  + '%e\t'%(py_v_MDL18_v_muscles_v[i])  + '%e\t'%(py_v_MDL19_v_muscles_v[i])  + '%e\t'%(py_v_MDL20_v_muscles_v[i])  + '%e\t'%(py_v_MDL21_v_muscles_v[i])  + '%e\t'%(py_v_MDL22_v_muscles_v[i])  + '%e\t'%(py_v_MDL23_v_muscles_v[i])  + '%e\t'%(py_v_MDL24_v_muscles_v[i]) + '\n')
        f_muscles_v_f2.close()
        print("Saved data to: c302_C2_AVB_DB.muscles.dat")

        # ######################   File to save: c302_C2_AVB_DB.muscles.activity.dat (muscles_activity)
        py_v_MDR01_v_muscles_activity = [ float(x ) for x in h.v_MDR01_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MDR02_v_muscles_activity = [ float(x ) for x in h.v_MDR02_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MDR03_v_muscles_activity = [ float(x ) for x in h.v_MDR03_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MDR04_v_muscles_activity = [ float(x ) for x in h.v_MDR04_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MDR05_v_muscles_activity = [ float(x ) for x in h.v_MDR05_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MDR06_v_muscles_activity = [ float(x ) for x in h.v_MDR06_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MDR07_v_muscles_activity = [ float(x ) for x in h.v_MDR07_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MDR08_v_muscles_activity = [ float(x ) for x in h.v_MDR08_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MDR09_v_muscles_activity = [ float(x ) for x in h.v_MDR09_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MDR10_v_muscles_activity = [ float(x ) for x in h.v_MDR10_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MDR11_v_muscles_activity = [ float(x ) for x in h.v_MDR11_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MDR12_v_muscles_activity = [ float(x ) for x in h.v_MDR12_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MDR13_v_muscles_activity = [ float(x ) for x in h.v_MDR13_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MDR14_v_muscles_activity = [ float(x ) for x in h.v_MDR14_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MDR15_v_muscles_activity = [ float(x ) for x in h.v_MDR15_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MDR16_v_muscles_activity = [ float(x ) for x in h.v_MDR16_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MDR17_v_muscles_activity = [ float(x ) for x in h.v_MDR17_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MDR18_v_muscles_activity = [ float(x ) for x in h.v_MDR18_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MDR19_v_muscles_activity = [ float(x ) for x in h.v_MDR19_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MDR20_v_muscles_activity = [ float(x ) for x in h.v_MDR20_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MDR21_v_muscles_activity = [ float(x ) for x in h.v_MDR21_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MDR22_v_muscles_activity = [ float(x ) for x in h.v_MDR22_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MDR23_v_muscles_activity = [ float(x ) for x in h.v_MDR23_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MDR24_v_muscles_activity = [ float(x ) for x in h.v_MDR24_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MVR01_v_muscles_activity = [ float(x ) for x in h.v_MVR01_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MVR02_v_muscles_activity = [ float(x ) for x in h.v_MVR02_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MVR03_v_muscles_activity = [ float(x ) for x in h.v_MVR03_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MVR04_v_muscles_activity = [ float(x ) for x in h.v_MVR04_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MVR05_v_muscles_activity = [ float(x ) for x in h.v_MVR05_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MVR06_v_muscles_activity = [ float(x ) for x in h.v_MVR06_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MVR07_v_muscles_activity = [ float(x ) for x in h.v_MVR07_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MVR08_v_muscles_activity = [ float(x ) for x in h.v_MVR08_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MVR09_v_muscles_activity = [ float(x ) for x in h.v_MVR09_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MVR10_v_muscles_activity = [ float(x ) for x in h.v_MVR10_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MVR11_v_muscles_activity = [ float(x ) for x in h.v_MVR11_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MVR12_v_muscles_activity = [ float(x ) for x in h.v_MVR12_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MVR13_v_muscles_activity = [ float(x ) for x in h.v_MVR13_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MVR14_v_muscles_activity = [ float(x ) for x in h.v_MVR14_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MVR15_v_muscles_activity = [ float(x ) for x in h.v_MVR15_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MVR16_v_muscles_activity = [ float(x ) for x in h.v_MVR16_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MVR17_v_muscles_activity = [ float(x ) for x in h.v_MVR17_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MVR18_v_muscles_activity = [ float(x ) for x in h.v_MVR18_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MVR19_v_muscles_activity = [ float(x ) for x in h.v_MVR19_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MVR20_v_muscles_activity = [ float(x ) for x in h.v_MVR20_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MVR21_v_muscles_activity = [ float(x ) for x in h.v_MVR21_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MVR22_v_muscles_activity = [ float(x ) for x in h.v_MVR22_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MVR23_v_muscles_activity = [ float(x ) for x in h.v_MVR23_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MVL01_v_muscles_activity = [ float(x ) for x in h.v_MVL01_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MVL02_v_muscles_activity = [ float(x ) for x in h.v_MVL02_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MVL03_v_muscles_activity = [ float(x ) for x in h.v_MVL03_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MVL04_v_muscles_activity = [ float(x ) for x in h.v_MVL04_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MVL05_v_muscles_activity = [ float(x ) for x in h.v_MVL05_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MVL06_v_muscles_activity = [ float(x ) for x in h.v_MVL06_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MVL07_v_muscles_activity = [ float(x ) for x in h.v_MVL07_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MVL08_v_muscles_activity = [ float(x ) for x in h.v_MVL08_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MVL09_v_muscles_activity = [ float(x ) for x in h.v_MVL09_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MVL10_v_muscles_activity = [ float(x ) for x in h.v_MVL10_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MVL11_v_muscles_activity = [ float(x ) for x in h.v_MVL11_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MVL12_v_muscles_activity = [ float(x ) for x in h.v_MVL12_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MVL13_v_muscles_activity = [ float(x ) for x in h.v_MVL13_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MVL14_v_muscles_activity = [ float(x ) for x in h.v_MVL14_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MVL15_v_muscles_activity = [ float(x ) for x in h.v_MVL15_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MVL16_v_muscles_activity = [ float(x ) for x in h.v_MVL16_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MVL17_v_muscles_activity = [ float(x ) for x in h.v_MVL17_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MVL18_v_muscles_activity = [ float(x ) for x in h.v_MVL18_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MVL19_v_muscles_activity = [ float(x ) for x in h.v_MVL19_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MVL20_v_muscles_activity = [ float(x ) for x in h.v_MVL20_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MVL21_v_muscles_activity = [ float(x ) for x in h.v_MVL21_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MVL22_v_muscles_activity = [ float(x ) for x in h.v_MVL22_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MVL23_v_muscles_activity = [ float(x ) for x in h.v_MVL23_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MVL24_v_muscles_activity = [ float(x ) for x in h.v_MVL24_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MDL01_v_muscles_activity = [ float(x ) for x in h.v_MDL01_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MDL02_v_muscles_activity = [ float(x ) for x in h.v_MDL02_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MDL03_v_muscles_activity = [ float(x ) for x in h.v_MDL03_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MDL04_v_muscles_activity = [ float(x ) for x in h.v_MDL04_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MDL05_v_muscles_activity = [ float(x ) for x in h.v_MDL05_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MDL06_v_muscles_activity = [ float(x ) for x in h.v_MDL06_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MDL07_v_muscles_activity = [ float(x ) for x in h.v_MDL07_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MDL08_v_muscles_activity = [ float(x ) for x in h.v_MDL08_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MDL09_v_muscles_activity = [ float(x ) for x in h.v_MDL09_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MDL10_v_muscles_activity = [ float(x ) for x in h.v_MDL10_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MDL11_v_muscles_activity = [ float(x ) for x in h.v_MDL11_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MDL12_v_muscles_activity = [ float(x ) for x in h.v_MDL12_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MDL13_v_muscles_activity = [ float(x ) for x in h.v_MDL13_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MDL14_v_muscles_activity = [ float(x ) for x in h.v_MDL14_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MDL15_v_muscles_activity = [ float(x ) for x in h.v_MDL15_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MDL16_v_muscles_activity = [ float(x ) for x in h.v_MDL16_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MDL17_v_muscles_activity = [ float(x ) for x in h.v_MDL17_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MDL18_v_muscles_activity = [ float(x ) for x in h.v_MDL18_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MDL19_v_muscles_activity = [ float(x ) for x in h.v_MDL19_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MDL20_v_muscles_activity = [ float(x ) for x in h.v_MDL20_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MDL21_v_muscles_activity = [ float(x ) for x in h.v_MDL21_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MDL22_v_muscles_activity = [ float(x ) for x in h.v_MDL22_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MDL23_v_muscles_activity = [ float(x ) for x in h.v_MDL23_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_MDL24_v_muscles_activity = [ float(x ) for x in h.v_MDL24_v_muscles_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration

        f_muscles_activity_f2 = open('c302_C2_AVB_DB.muscles.activity.dat', 'w')
        num_points = len(py_v_time)  # Simulation may have been stopped before tstop...

        for i in range(num_points):
            f_muscles_activity_f2.write('%e\t'% py_v_time[i]  + '%e\t'%(py_v_MDR01_v_muscles_activity[i])  + '%e\t'%(py_v_MDR02_v_muscles_activity[i])  + '%e\t'%(py_v_MDR03_v_muscles_activity[i])  + '%e\t'%(py_v_MDR04_v_muscles_activity[i])  + '%e\t'%(py_v_MDR05_v_muscles_activity[i])  + '%e\t'%(py_v_MDR06_v_muscles_activity[i])  + '%e\t'%(py_v_MDR07_v_muscles_activity[i])  + '%e\t'%(py_v_MDR08_v_muscles_activity[i])  + '%e\t'%(py_v_MDR09_v_muscles_activity[i])  + '%e\t'%(py_v_MDR10_v_muscles_activity[i])  + '%e\t'%(py_v_MDR11_v_muscles_activity[i])  + '%e\t'%(py_v_MDR12_v_muscles_activity[i])  + '%e\t'%(py_v_MDR13_v_muscles_activity[i])  + '%e\t'%(py_v_MDR14_v_muscles_activity[i])  + '%e\t'%(py_v_MDR15_v_muscles_activity[i])  + '%e\t'%(py_v_MDR16_v_muscles_activity[i])  + '%e\t'%(py_v_MDR17_v_muscles_activity[i])  + '%e\t'%(py_v_MDR18_v_muscles_activity[i])  + '%e\t'%(py_v_MDR19_v_muscles_activity[i])  + '%e\t'%(py_v_MDR20_v_muscles_activity[i])  + '%e\t'%(py_v_MDR21_v_muscles_activity[i])  + '%e\t'%(py_v_MDR22_v_muscles_activity[i])  + '%e\t'%(py_v_MDR23_v_muscles_activity[i])  + '%e\t'%(py_v_MDR24_v_muscles_activity[i])  + '%e\t'%(py_v_MVR01_v_muscles_activity[i])  + '%e\t'%(py_v_MVR02_v_muscles_activity[i])  + '%e\t'%(py_v_MVR03_v_muscles_activity[i])  + '%e\t'%(py_v_MVR04_v_muscles_activity[i])  + '%e\t'%(py_v_MVR05_v_muscles_activity[i])  + '%e\t'%(py_v_MVR06_v_muscles_activity[i])  + '%e\t'%(py_v_MVR07_v_muscles_activity[i])  + '%e\t'%(py_v_MVR08_v_muscles_activity[i])  + '%e\t'%(py_v_MVR09_v_muscles_activity[i])  + '%e\t'%(py_v_MVR10_v_muscles_activity[i])  + '%e\t'%(py_v_MVR11_v_muscles_activity[i])  + '%e\t'%(py_v_MVR12_v_muscles_activity[i])  + '%e\t'%(py_v_MVR13_v_muscles_activity[i])  + '%e\t'%(py_v_MVR14_v_muscles_activity[i])  + '%e\t'%(py_v_MVR15_v_muscles_activity[i])  + '%e\t'%(py_v_MVR16_v_muscles_activity[i])  + '%e\t'%(py_v_MVR17_v_muscles_activity[i])  + '%e\t'%(py_v_MVR18_v_muscles_activity[i])  + '%e\t'%(py_v_MVR19_v_muscles_activity[i])  + '%e\t'%(py_v_MVR20_v_muscles_activity[i])  + '%e\t'%(py_v_MVR21_v_muscles_activity[i])  + '%e\t'%(py_v_MVR22_v_muscles_activity[i])  + '%e\t'%(py_v_MVR23_v_muscles_activity[i])  + '%e\t'%(py_v_MVL01_v_muscles_activity[i])  + '%e\t'%(py_v_MVL02_v_muscles_activity[i])  + '%e\t'%(py_v_MVL03_v_muscles_activity[i])  + '%e\t'%(py_v_MVL04_v_muscles_activity[i])  + '%e\t'%(py_v_MVL05_v_muscles_activity[i])  + '%e\t'%(py_v_MVL06_v_muscles_activity[i])  + '%e\t'%(py_v_MVL07_v_muscles_activity[i])  + '%e\t'%(py_v_MVL08_v_muscles_activity[i])  + '%e\t'%(py_v_MVL09_v_muscles_activity[i])  + '%e\t'%(py_v_MVL10_v_muscles_activity[i])  + '%e\t'%(py_v_MVL11_v_muscles_activity[i])  + '%e\t'%(py_v_MVL12_v_muscles_activity[i])  + '%e\t'%(py_v_MVL13_v_muscles_activity[i])  + '%e\t'%(py_v_MVL14_v_muscles_activity[i])  + '%e\t'%(py_v_MVL15_v_muscles_activity[i])  + '%e\t'%(py_v_MVL16_v_muscles_activity[i])  + '%e\t'%(py_v_MVL17_v_muscles_activity[i])  + '%e\t'%(py_v_MVL18_v_muscles_activity[i])  + '%e\t'%(py_v_MVL19_v_muscles_activity[i])  + '%e\t'%(py_v_MVL20_v_muscles_activity[i])  + '%e\t'%(py_v_MVL21_v_muscles_activity[i])  + '%e\t'%(py_v_MVL22_v_muscles_activity[i])  + '%e\t'%(py_v_MVL23_v_muscles_activity[i])  + '%e\t'%(py_v_MVL24_v_muscles_activity[i])  + '%e\t'%(py_v_MDL01_v_muscles_activity[i])  + '%e\t'%(py_v_MDL02_v_muscles_activity[i])  + '%e\t'%(py_v_MDL03_v_muscles_activity[i])  + '%e\t'%(py_v_MDL04_v_muscles_activity[i])  + '%e\t'%(py_v_MDL05_v_muscles_activity[i])  + '%e\t'%(py_v_MDL06_v_muscles_activity[i])  + '%e\t'%(py_v_MDL07_v_muscles_activity[i])  + '%e\t'%(py_v_MDL08_v_muscles_activity[i])  + '%e\t'%(py_v_MDL09_v_muscles_activity[i])  + '%e\t'%(py_v_MDL10_v_muscles_activity[i])  + '%e\t'%(py_v_MDL11_v_muscles_activity[i])  + '%e\t'%(py_v_MDL12_v_muscles_activity[i])  + '%e\t'%(py_v_MDL13_v_muscles_activity[i])  + '%e\t'%(py_v_MDL14_v_muscles_activity[i])  + '%e\t'%(py_v_MDL15_v_muscles_activity[i])  + '%e\t'%(py_v_MDL16_v_muscles_activity[i])  + '%e\t'%(py_v_MDL17_v_muscles_activity[i])  + '%e\t'%(py_v_MDL18_v_muscles_activity[i])  + '%e\t'%(py_v_MDL19_v_muscles_activity[i])  + '%e\t'%(py_v_MDL20_v_muscles_activity[i])  + '%e\t'%(py_v_MDL21_v_muscles_activity[i])  + '%e\t'%(py_v_MDL22_v_muscles_activity[i])  + '%e\t'%(py_v_MDL23_v_muscles_activity[i])  + '%e\t'%(py_v_MDL24_v_muscles_activity[i]) + '\n')
        f_muscles_activity_f2.close()
        print("Saved data to: c302_C2_AVB_DB.muscles.activity.dat")

        # ######################   File to save: c302_C2_AVB_DB.dat (neurons_v)
        py_v_AVBL_v_neurons_v = [ float(x  / 1000.0) for x in h.v_AVBL_v_neurons_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_AVBR_v_neurons_v = [ float(x  / 1000.0) for x in h.v_AVBR_v_neurons_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_DB1_v_neurons_v = [ float(x  / 1000.0) for x in h.v_DB1_v_neurons_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_DB2_v_neurons_v = [ float(x  / 1000.0) for x in h.v_DB2_v_neurons_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_DB3_v_neurons_v = [ float(x  / 1000.0) for x in h.v_DB3_v_neurons_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_DB4_v_neurons_v = [ float(x  / 1000.0) for x in h.v_DB4_v_neurons_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_DB5_v_neurons_v = [ float(x  / 1000.0) for x in h.v_DB5_v_neurons_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_DB6_v_neurons_v = [ float(x  / 1000.0) for x in h.v_DB6_v_neurons_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_DB7_v_neurons_v = [ float(x  / 1000.0) for x in h.v_DB7_v_neurons_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage

        f_neurons_v_f2 = open('c302_C2_AVB_DB.dat', 'w')
        num_points = len(py_v_time)  # Simulation may have been stopped before tstop...

        for i in range(num_points):
            f_neurons_v_f2.write('%e\t'% py_v_time[i]  + '%e\t'%(py_v_AVBL_v_neurons_v[i])  + '%e\t'%(py_v_AVBR_v_neurons_v[i])  + '%e\t'%(py_v_DB1_v_neurons_v[i])  + '%e\t'%(py_v_DB2_v_neurons_v[i])  + '%e\t'%(py_v_DB3_v_neurons_v[i])  + '%e\t'%(py_v_DB4_v_neurons_v[i])  + '%e\t'%(py_v_DB5_v_neurons_v[i])  + '%e\t'%(py_v_DB6_v_neurons_v[i])  + '%e\t'%(py_v_DB7_v_neurons_v[i]) + '\n')
        f_neurons_v_f2.close()
        print("Saved data to: c302_C2_AVB_DB.dat")

        save_end = time.time()
        save_time = save_end - self.sim_end
        print("Finished saving results in %f seconds"%(save_time))

        print("Done")

        quit()


if __name__ == '__main__':

    ns = NeuronSimulation(tstop=2000, dt=0.05, seed=123456789)

    ns.run()

