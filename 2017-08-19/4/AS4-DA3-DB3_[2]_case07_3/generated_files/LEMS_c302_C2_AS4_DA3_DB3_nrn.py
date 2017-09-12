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
    AVAL_to_DA1_elec_syn (Type: gapJunction:  conductance=2.52E-12 (SI conductance))
    AVAL_to_DA2_elec_syn (Type: gapJunction:  conductance=2.52E-12 (SI conductance))
    AVAL_to_DA3_elec_syn (Type: gapJunction:  conductance=2.52E-12 (SI conductance))
    AVAL_to_DA4_elec_syn (Type: gapJunction:  conductance=2.52E-12 (SI conductance))
    AVAL_to_DA5_elec_syn (Type: gapJunction:  conductance=2.52E-12 (SI conductance))
    AVAL_to_DA6_elec_syn (Type: gapJunction:  conductance=2.52E-12 (SI conductance))
    AVAL_to_DA7_elec_syn (Type: gapJunction:  conductance=2.52E-12 (SI conductance))
    AVAL_to_DA8_elec_syn (Type: gapJunction:  conductance=2.52E-12 (SI conductance))
    AVAL_to_DA9_elec_syn (Type: gapJunction:  conductance=2.52E-12 (SI conductance))
    AVAR_to_DA1_elec_syn (Type: gapJunction:  conductance=2.52E-12 (SI conductance))
    AVAR_to_DA2_elec_syn (Type: gapJunction:  conductance=2.52E-12 (SI conductance))
    AVAR_to_DA3_elec_syn (Type: gapJunction:  conductance=2.52E-12 (SI conductance))
    AVAR_to_DA4_elec_syn (Type: gapJunction:  conductance=2.52E-12 (SI conductance))
    AVAR_to_DA5_elec_syn (Type: gapJunction:  conductance=2.52E-12 (SI conductance))
    AVAR_to_DA6_elec_syn (Type: gapJunction:  conductance=2.52E-12 (SI conductance))
    AVAR_to_DA8_elec_syn (Type: gapJunction:  conductance=2.52E-12 (SI conductance))
    AVAR_to_DA9_elec_syn (Type: gapJunction:  conductance=2.52E-12 (SI conductance))
    AVBL_to_DB2_elec_syn (Type: gapJunction:  conductance=3.0200000000000005E-12 (SI conductance))
    AVBL_to_DB3_elec_syn (Type: gapJunction:  conductance=3.0200000000000005E-12 (SI conductance))
    AVBL_to_DB4_elec_syn (Type: gapJunction:  conductance=3.0200000000000005E-12 (SI conductance))
    AVBL_to_DB5_elec_syn (Type: gapJunction:  conductance=3.0200000000000005E-12 (SI conductance))
    AVBL_to_DB6_elec_syn (Type: gapJunction:  conductance=3.0200000000000005E-12 (SI conductance))
    AVBL_to_DB7_elec_syn (Type: gapJunction:  conductance=3.0200000000000005E-12 (SI conductance))
    AVBR_to_DB1_elec_syn (Type: gapJunction:  conductance=3.0200000000000005E-12 (SI conductance))
    AVBR_to_DB2_elec_syn (Type: gapJunction:  conductance=3.0200000000000005E-12 (SI conductance))
    AVBR_to_DB3_elec_syn (Type: gapJunction:  conductance=3.0200000000000005E-12 (SI conductance))
    AVBR_to_DB4_elec_syn (Type: gapJunction:  conductance=3.0200000000000005E-12 (SI conductance))
    AVBR_to_DB5_elec_syn (Type: gapJunction:  conductance=3.0200000000000005E-12 (SI conductance))
    AVBR_to_DB6_elec_syn (Type: gapJunction:  conductance=3.0200000000000005E-12 (SI conductance))
    AVBR_to_DB7_elec_syn (Type: gapJunction:  conductance=3.0200000000000005E-12 (SI conductance))
    DA1_to_AVAL_elec_syn (Type: gapJunction:  conductance=2.52E-12 (SI conductance))
    DA1_to_AVAR_elec_syn (Type: gapJunction:  conductance=2.52E-12 (SI conductance))
    DA2_to_AVAL_elec_syn (Type: gapJunction:  conductance=2.52E-12 (SI conductance))
    DA2_to_AVAR_elec_syn (Type: gapJunction:  conductance=2.52E-12 (SI conductance))
    DA3_to_AVAL_elec_syn (Type: gapJunction:  conductance=2.52E-12 (SI conductance))
    DA3_to_AVAR_elec_syn (Type: gapJunction:  conductance=2.52E-12 (SI conductance))
    DA4_to_AVAL_elec_syn (Type: gapJunction:  conductance=2.52E-12 (SI conductance))
    DA4_to_AVAR_elec_syn (Type: gapJunction:  conductance=2.52E-12 (SI conductance))
    DA5_to_AVAL_elec_syn (Type: gapJunction:  conductance=2.52E-12 (SI conductance))
    DA5_to_AVAR_elec_syn (Type: gapJunction:  conductance=2.52E-12 (SI conductance))
    DA6_to_AVAL_elec_syn (Type: gapJunction:  conductance=2.52E-12 (SI conductance))
    DA6_to_AVAR_elec_syn (Type: gapJunction:  conductance=2.52E-12 (SI conductance))
    DA7_to_AVAL_elec_syn (Type: gapJunction:  conductance=2.52E-12 (SI conductance))
    DA8_to_AVAL_elec_syn (Type: gapJunction:  conductance=2.52E-12 (SI conductance))
    DA8_to_AVAR_elec_syn (Type: gapJunction:  conductance=2.52E-12 (SI conductance))
    DA9_to_AVAL_elec_syn (Type: gapJunction:  conductance=2.52E-12 (SI conductance))
    DA9_to_AVAR_elec_syn (Type: gapJunction:  conductance=2.52E-12 (SI conductance))
    DB1_to_AVBR_elec_syn (Type: gapJunction:  conductance=3.0200000000000005E-12 (SI conductance))
    DB2_to_AVBL_elec_syn (Type: gapJunction:  conductance=3.0200000000000005E-12 (SI conductance))
    DB2_to_AVBR_elec_syn (Type: gapJunction:  conductance=3.0200000000000005E-12 (SI conductance))
    DB3_to_AVBL_elec_syn (Type: gapJunction:  conductance=3.0200000000000005E-12 (SI conductance))
    DB3_to_AVBR_elec_syn (Type: gapJunction:  conductance=3.0200000000000005E-12 (SI conductance))
    DB4_to_AVBL_elec_syn (Type: gapJunction:  conductance=3.0200000000000005E-12 (SI conductance))
    DB4_to_AVBR_elec_syn (Type: gapJunction:  conductance=3.0200000000000005E-12 (SI conductance))
    DB5_to_AVBL_elec_syn (Type: gapJunction:  conductance=3.0200000000000005E-12 (SI conductance))
    DB5_to_AVBR_elec_syn (Type: gapJunction:  conductance=3.0200000000000005E-12 (SI conductance))
    DB6_to_AVBL_elec_syn (Type: gapJunction:  conductance=3.0200000000000005E-12 (SI conductance))
    DB6_to_AVBR_elec_syn (Type: gapJunction:  conductance=3.0200000000000005E-12 (SI conductance))
    DB7_to_AVBL_elec_syn (Type: gapJunction:  conductance=3.0200000000000005E-12 (SI conductance))
    DB7_to_AVBR_elec_syn (Type: gapJunction:  conductance=3.0200000000000005E-12 (SI conductance))
    silent (Type: silentSynapse)
    neuron_to_neuron_exc_syn (Type: gradedSynapse:  conductance=4.900000000000001E-10 (SI conductance) delta=0.005 (SI voltage) k=500.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.01 (SI voltage))
    AVAL_to_AVBL_inh_syn (Type: gradedSynapse:  conductance=5.9E-11 (SI conductance) delta=0.005 (SI voltage) k=15.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.07 (SI voltage))
    AVAL_to_DA1_exc_syn (Type: gradedSynapse:  conductance=1.0000000000000001E-11 (SI conductance) delta=0.005 (SI voltage) k=500.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.01 (SI voltage))
    AVAL_to_DA2_exc_syn (Type: gradedSynapse:  conductance=1.0000000000000001E-11 (SI conductance) delta=0.005 (SI voltage) k=500.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.01 (SI voltage))
    AVAL_to_DA3_exc_syn (Type: gradedSynapse:  conductance=1.0000000000000001E-11 (SI conductance) delta=0.005 (SI voltage) k=500.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.01 (SI voltage))
    AVAL_to_DA4_exc_syn (Type: gradedSynapse:  conductance=1.0000000000000001E-11 (SI conductance) delta=0.005 (SI voltage) k=500.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.01 (SI voltage))
    AVAL_to_DA5_exc_syn (Type: gradedSynapse:  conductance=1.0000000000000001E-11 (SI conductance) delta=0.005 (SI voltage) k=500.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.01 (SI voltage))
    AVAL_to_DA7_exc_syn (Type: gradedSynapse:  conductance=1.0000000000000001E-11 (SI conductance) delta=0.005 (SI voltage) k=500.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.01 (SI voltage))
    AVAL_to_DA8_exc_syn (Type: gradedSynapse:  conductance=1.0000000000000001E-11 (SI conductance) delta=0.005 (SI voltage) k=500.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.01 (SI voltage))
    AVAL_to_DA9_exc_syn (Type: gradedSynapse:  conductance=1.0000000000000001E-11 (SI conductance) delta=0.005 (SI voltage) k=500.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.01 (SI voltage))
    AVAR_to_AVBL_inh_syn (Type: gradedSynapse:  conductance=5.9E-11 (SI conductance) delta=0.005 (SI voltage) k=15.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.07 (SI voltage))
    AVAR_to_AVBR_inh_syn (Type: gradedSynapse:  conductance=5.9E-11 (SI conductance) delta=0.005 (SI voltage) k=15.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.07 (SI voltage))
    AVAR_to_DA1_exc_syn (Type: gradedSynapse:  conductance=1.0000000000000001E-11 (SI conductance) delta=0.005 (SI voltage) k=500.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.01 (SI voltage))
    AVAR_to_DA2_exc_syn (Type: gradedSynapse:  conductance=1.0000000000000001E-11 (SI conductance) delta=0.005 (SI voltage) k=500.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.01 (SI voltage))
    AVAR_to_DA3_exc_syn (Type: gradedSynapse:  conductance=1.0000000000000001E-11 (SI conductance) delta=0.005 (SI voltage) k=500.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.01 (SI voltage))
    AVAR_to_DA4_exc_syn (Type: gradedSynapse:  conductance=1.0000000000000001E-11 (SI conductance) delta=0.005 (SI voltage) k=500.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.01 (SI voltage))
    AVAR_to_DA5_exc_syn (Type: gradedSynapse:  conductance=1.0000000000000001E-11 (SI conductance) delta=0.005 (SI voltage) k=500.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.01 (SI voltage))
    AVAR_to_DA6_exc_syn (Type: gradedSynapse:  conductance=1.0000000000000001E-11 (SI conductance) delta=0.005 (SI voltage) k=500.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.01 (SI voltage))
    AVAR_to_DA7_exc_syn (Type: gradedSynapse:  conductance=1.0000000000000001E-11 (SI conductance) delta=0.005 (SI voltage) k=500.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.01 (SI voltage))
    AVAR_to_DA8_exc_syn (Type: gradedSynapse:  conductance=1.0000000000000001E-11 (SI conductance) delta=0.005 (SI voltage) k=500.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.01 (SI voltage))
    AVAR_to_DA9_exc_syn (Type: gradedSynapse:  conductance=1.0000000000000001E-11 (SI conductance) delta=0.005 (SI voltage) k=500.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.01 (SI voltage))
    AVBL_to_AVAL_inh_syn (Type: gradedSynapse:  conductance=1.9000000000000002E-11 (SI conductance) delta=0.005 (SI voltage) k=15.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.07 (SI voltage))
    AVBL_to_AVAR_inh_syn (Type: gradedSynapse:  conductance=1.9000000000000002E-11 (SI conductance) delta=0.005 (SI voltage) k=15.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.07 (SI voltage))
    AVBR_to_AVAL_inh_syn (Type: gradedSynapse:  conductance=1.9000000000000002E-11 (SI conductance) delta=0.005 (SI voltage) k=15.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.07 (SI voltage))
    AVBR_to_AVAR_inh_syn (Type: gradedSynapse:  conductance=1.9000000000000002E-11 (SI conductance) delta=0.005 (SI voltage) k=15.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.07 (SI voltage))
    DA1_to_DB1_exc_syn (Type: gradedSynapse:  conductance=1.4E-9 (SI conductance) delta=0.005 (SI voltage) k=500.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.01 (SI voltage))
    DA2_to_DB1_exc_syn (Type: gradedSynapse:  conductance=1.4E-9 (SI conductance) delta=0.005 (SI voltage) k=500.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.01 (SI voltage))
    DA3_to_DB3_exc_syn (Type: gradedSynapse:  conductance=1.4E-9 (SI conductance) delta=0.005 (SI voltage) k=500.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.01 (SI voltage))
    DA4_to_DB2_exc_syn (Type: gradedSynapse:  conductance=1.4E-9 (SI conductance) delta=0.005 (SI voltage) k=500.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.01 (SI voltage))
    DA5_to_DB4_exc_syn (Type: gradedSynapse:  conductance=1.4E-9 (SI conductance) delta=0.005 (SI voltage) k=500.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.01 (SI voltage))
    DA6_to_DB5_exc_syn (Type: gradedSynapse:  conductance=1.4E-9 (SI conductance) delta=0.005 (SI voltage) k=500.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.01 (SI voltage))
    DA7_to_DB6_exc_syn (Type: gradedSynapse:  conductance=1.4E-9 (SI conductance) delta=0.005 (SI voltage) k=500.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.01 (SI voltage))
    DA8_to_DB7_exc_syn (Type: gradedSynapse:  conductance=1.4E-9 (SI conductance) delta=0.005 (SI voltage) k=500.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.01 (SI voltage))
    DA9_to_DB7_exc_syn (Type: gradedSynapse:  conductance=1.4E-9 (SI conductance) delta=0.005 (SI voltage) k=500.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.01 (SI voltage))
    DB1_to_AS1_inh_syn (Type: gradedSynapse:  conductance=1.4E-9 (SI conductance) delta=0.005 (SI voltage) k=15.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.07 (SI voltage))
    DB1_to_AS2_inh_syn (Type: gradedSynapse:  conductance=1.4E-9 (SI conductance) delta=0.005 (SI voltage) k=15.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.07 (SI voltage))
    DB2_to_AS3_inh_syn (Type: gradedSynapse:  conductance=1.4E-9 (SI conductance) delta=0.005 (SI voltage) k=15.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.07 (SI voltage))
    DB2_to_AS4_inh_syn (Type: gradedSynapse:  conductance=1.4E-9 (SI conductance) delta=0.005 (SI voltage) k=15.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.07 (SI voltage))
    DB3_to_AS4_inh_syn (Type: gradedSynapse:  conductance=1.4E-9 (SI conductance) delta=0.005 (SI voltage) k=15.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.07 (SI voltage))
    DB3_to_AS5_inh_syn (Type: gradedSynapse:  conductance=1.4E-9 (SI conductance) delta=0.005 (SI voltage) k=15.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.07 (SI voltage))
    DB4_to_AS6_inh_syn (Type: gradedSynapse:  conductance=1.4E-9 (SI conductance) delta=0.005 (SI voltage) k=15.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.07 (SI voltage))
    DB5_to_AS7_inh_syn (Type: gradedSynapse:  conductance=1.4E-9 (SI conductance) delta=0.005 (SI voltage) k=15.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.07 (SI voltage))
    DB5_to_AS8_inh_syn (Type: gradedSynapse:  conductance=1.4E-9 (SI conductance) delta=0.005 (SI voltage) k=15.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.07 (SI voltage))
    DB6_to_AS8_inh_syn (Type: gradedSynapse:  conductance=1.4E-9 (SI conductance) delta=0.005 (SI voltage) k=15.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.07 (SI voltage))
    DB6_to_AS9_inh_syn (Type: gradedSynapse:  conductance=1.4E-9 (SI conductance) delta=0.005 (SI voltage) k=15.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.07 (SI voltage))
    DB7_to_AS10_inh_syn (Type: gradedSynapse:  conductance=1.4E-9 (SI conductance) delta=0.005 (SI voltage) k=15.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.07 (SI voltage))
    DB7_to_AS11_inh_syn (Type: gradedSynapse:  conductance=1.4E-9 (SI conductance) delta=0.005 (SI voltage) k=15.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.07 (SI voltage))
    AS1_to_DA1_exc_syn (Type: gradedSynapse:  conductance=1.0E-9 (SI conductance) delta=0.005 (SI voltage) k=500.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.01 (SI voltage))
    AS3_to_DA3_exc_syn (Type: gradedSynapse:  conductance=1.0E-9 (SI conductance) delta=0.005 (SI voltage) k=500.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.01 (SI voltage))
    AS4_to_DA3_exc_syn (Type: gradedSynapse:  conductance=1.0E-9 (SI conductance) delta=0.005 (SI voltage) k=500.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.01 (SI voltage))
    AS6_to_DA5_exc_syn (Type: gradedSynapse:  conductance=1.0E-9 (SI conductance) delta=0.005 (SI voltage) k=500.0 (SI per_time) Vth=0.0 (SI voltage) erev=-0.01 (SI voltage))
    GenericMuscleCell (Type: cell)
    GenericNeuronCell (Type: cell)
    offset_current (Type: pulseGenerator:  delay=0.0 (SI time) duration=2.0 (SI time) amplitude=0.0 (SI current))
    stim_AVBL_1 (Type: pulseGenerator:  delay=0.0 (SI time) duration=1.0 (SI time) amplitude=5.0E-12 (SI current))
    stim_AVBR_1 (Type: pulseGenerator:  delay=0.0 (SI time) duration=1.0 (SI time) amplitude=5.0E-12 (SI current))
    stim_AVAL_1 (Type: pulseGenerator:  delay=1.0 (SI time) duration=1.0 (SI time) amplitude=5.0E-12 (SI current))
    stim_AVAR_1 (Type: pulseGenerator:  delay=1.0 (SI time) duration=1.0 (SI time) amplitude=5.0E-12 (SI current))
    stim_AVBL_2 (Type: pulseGenerator:  delay=2.0 (SI time) duration=0.9 (SI time) amplitude=5.0E-12 (SI current))
    stim_AVBR_2 (Type: pulseGenerator:  delay=2.0 (SI time) duration=0.9 (SI time) amplitude=5.0E-12 (SI current))
    stim_AS1_1 (Type: pulseGenerator:  delay=0.0 (SI time) duration=2.9 (SI time) amplitude=5.0E-12 (SI current))
    stim_AS2_1 (Type: pulseGenerator:  delay=0.0 (SI time) duration=2.9 (SI time) amplitude=5.0E-12 (SI current))
    stim_AS3_1 (Type: pulseGenerator:  delay=0.0 (SI time) duration=2.9 (SI time) amplitude=5.0E-12 (SI current))
    stim_AS4_1 (Type: pulseGenerator:  delay=0.0 (SI time) duration=2.9 (SI time) amplitude=5.0E-12 (SI current))
    stim_AS5_1 (Type: pulseGenerator:  delay=0.0 (SI time) duration=2.9 (SI time) amplitude=5.0E-12 (SI current))
    stim_AS6_1 (Type: pulseGenerator:  delay=0.0 (SI time) duration=2.9 (SI time) amplitude=5.0E-12 (SI current))
    stim_AS7_1 (Type: pulseGenerator:  delay=0.0 (SI time) duration=2.9 (SI time) amplitude=5.0E-12 (SI current))
    stim_AS8_1 (Type: pulseGenerator:  delay=0.0 (SI time) duration=2.9 (SI time) amplitude=5.0E-12 (SI current))
    stim_AS9_1 (Type: pulseGenerator:  delay=0.0 (SI time) duration=2.9 (SI time) amplitude=5.0E-12 (SI current))
    stim_AS10_1 (Type: pulseGenerator:  delay=0.0 (SI time) duration=2.9 (SI time) amplitude=5.0E-12 (SI current))
    stim_AS11_1 (Type: pulseGenerator:  delay=0.0 (SI time) duration=2.9 (SI time) amplitude=5.0E-12 (SI current))
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
        # ######################   Population: AS1
        print("Population AS1 contains 1 instance(s) of component: GenericNeuronCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericNeuronCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericNeuronCell.hoc")
        a_AS1 = []
        h("{ n_AS1 = 1 }")
        h("objectvar a_AS1[n_AS1]")
        for i in range(int(h.n_AS1)):
            h("a_AS1[%i] = new GenericNeuronCell()"%i)
            h("access a_AS1[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_AS1[0].position(-0.275, -229.038000000000011, 4.738) }")

        h("proc initialiseV_AS1() { for i = 0, n_AS1-1 { a_AS1[i].set_initial_v() } }")
        h("objref fih_AS1")
        h('{fih_AS1 = new FInitializeHandler(0, "initialiseV_AS1()")}')

        h("proc initialiseIons_AS1() { for i = 0, n_AS1-1 { a_AS1[i].set_initial_ion_properties() } }")
        h("objref fih_ion_AS1")
        h('{fih_ion_AS1 = new FInitializeHandler(1, "initialiseIons_AS1()")}')

        # ######################   Population: AS10
        print("Population AS10 contains 1 instance(s) of component: GenericNeuronCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericNeuronCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericNeuronCell.hoc")
        a_AS10 = []
        h("{ n_AS10 = 1 }")
        h("objectvar a_AS10[n_AS10]")
        for i in range(int(h.n_AS10)):
            h("a_AS10[%i] = new GenericNeuronCell()"%i)
            h("access a_AS10[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_AS10[0].position(-1.9, 278.25, -24.) }")

        h("proc initialiseV_AS10() { for i = 0, n_AS10-1 { a_AS10[i].set_initial_v() } }")
        h("objref fih_AS10")
        h('{fih_AS10 = new FInitializeHandler(0, "initialiseV_AS10()")}')

        h("proc initialiseIons_AS10() { for i = 0, n_AS10-1 { a_AS10[i].set_initial_ion_properties() } }")
        h("objref fih_ion_AS10")
        h('{fih_ion_AS10 = new FInitializeHandler(1, "initialiseIons_AS10()")}')

        # ######################   Population: AS11
        print("Population AS11 contains 1 instance(s) of component: GenericNeuronCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericNeuronCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericNeuronCell.hoc")
        a_AS11 = []
        h("{ n_AS11 = 1 }")
        h("objectvar a_AS11[n_AS11]")
        for i in range(int(h.n_AS11)):
            h("a_AS11[%i] = new GenericNeuronCell()"%i)
            h("access a_AS11[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_AS11[0].position(-1.8750001, 315.699999999999989, -26.124998000000001) }")

        h("proc initialiseV_AS11() { for i = 0, n_AS11-1 { a_AS11[i].set_initial_v() } }")
        h("objref fih_AS11")
        h('{fih_AS11 = new FInitializeHandler(0, "initialiseV_AS11()")}')

        h("proc initialiseIons_AS11() { for i = 0, n_AS11-1 { a_AS11[i].set_initial_ion_properties() } }")
        h("objref fih_ion_AS11")
        h('{fih_ion_AS11 = new FInitializeHandler(1, "initialiseIons_AS11()")}')

        # ######################   Population: AS2
        print("Population AS2 contains 1 instance(s) of component: GenericNeuronCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericNeuronCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericNeuronCell.hoc")
        a_AS2 = []
        h("{ n_AS2 = 1 }")
        h("objectvar a_AS2[n_AS2]")
        for i in range(int(h.n_AS2)):
            h("a_AS2[%i] = new GenericNeuronCell()"%i)
            h("access a_AS2[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_AS2[0].position(-1.8750001, -203.875, -12.725) }")

        h("proc initialiseV_AS2() { for i = 0, n_AS2-1 { a_AS2[i].set_initial_v() } }")
        h("objref fih_AS2")
        h('{fih_AS2 = new FInitializeHandler(0, "initialiseV_AS2()")}')

        h("proc initialiseIons_AS2() { for i = 0, n_AS2-1 { a_AS2[i].set_initial_ion_properties() } }")
        h("objref fih_ion_AS2")
        h('{fih_ion_AS2 = new FInitializeHandler(1, "initialiseIons_AS2()")}')

        # ######################   Population: AS3
        print("Population AS3 contains 1 instance(s) of component: GenericNeuronCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericNeuronCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericNeuronCell.hoc")
        a_AS3 = []
        h("{ n_AS3 = 1 }")
        h("objectvar a_AS3[n_AS3]")
        for i in range(int(h.n_AS3)):
            h("a_AS3[%i] = new GenericNeuronCell()"%i)
            h("access a_AS3[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_AS3[0].position(-1.9, -151.400010000000009, -45.649997999999997) }")

        h("proc initialiseV_AS3() { for i = 0, n_AS3-1 { a_AS3[i].set_initial_v() } }")
        h("objref fih_AS3")
        h('{fih_AS3 = new FInitializeHandler(0, "initialiseV_AS3()")}')

        h("proc initialiseIons_AS3() { for i = 0, n_AS3-1 { a_AS3[i].set_initial_ion_properties() } }")
        h("objref fih_ion_AS3")
        h('{fih_ion_AS3 = new FInitializeHandler(1, "initialiseIons_AS3()")}')

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

        # ######################   Population: AS5
        print("Population AS5 contains 1 instance(s) of component: GenericNeuronCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericNeuronCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericNeuronCell.hoc")
        a_AS5 = []
        h("{ n_AS5 = 1 }")
        h("objectvar a_AS5[n_AS5]")
        for i in range(int(h.n_AS5)):
            h("a_AS5[%i] = new GenericNeuronCell()"%i)
            h("access a_AS5[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_AS5[0].position(-1.8750001, -3.7500002, -52.524999999999999) }")

        h("proc initialiseV_AS5() { for i = 0, n_AS5-1 { a_AS5[i].set_initial_v() } }")
        h("objref fih_AS5")
        h('{fih_AS5 = new FInitializeHandler(0, "initialiseV_AS5()")}')

        h("proc initialiseIons_AS5() { for i = 0, n_AS5-1 { a_AS5[i].set_initial_ion_properties() } }")
        h("objref fih_ion_AS5")
        h('{fih_ion_AS5 = new FInitializeHandler(1, "initialiseIons_AS5()")}')

        # ######################   Population: AS6
        print("Population AS6 contains 1 instance(s) of component: GenericNeuronCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericNeuronCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericNeuronCell.hoc")
        a_AS6 = []
        h("{ n_AS6 = 1 }")
        h("objectvar a_AS6[n_AS6]")
        for i in range(int(h.n_AS6)):
            h("a_AS6[%i] = new GenericNeuronCell()"%i)
            h("access a_AS6[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_AS6[0].position(-1.9, 28.25, -34.25) }")

        h("proc initialiseV_AS6() { for i = 0, n_AS6-1 { a_AS6[i].set_initial_v() } }")
        h("objref fih_AS6")
        h('{fih_AS6 = new FInitializeHandler(0, "initialiseV_AS6()")}')

        h("proc initialiseIons_AS6() { for i = 0, n_AS6-1 { a_AS6[i].set_initial_ion_properties() } }")
        h("objref fih_ion_AS6")
        h('{fih_ion_AS6 = new FInitializeHandler(1, "initialiseIons_AS6()")}')

        # ######################   Population: AS7
        print("Population AS7 contains 1 instance(s) of component: GenericNeuronCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericNeuronCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericNeuronCell.hoc")
        a_AS7 = []
        h("{ n_AS7 = 1 }")
        h("objectvar a_AS7[n_AS7]")
        for i in range(int(h.n_AS7)):
            h("a_AS7[%i] = new GenericNeuronCell()"%i)
            h("access a_AS7[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_AS7[0].position(-1.9, 119.900000000000006, 3.9500003) }")

        h("proc initialiseV_AS7() { for i = 0, n_AS7-1 { a_AS7[i].set_initial_v() } }")
        h("objref fih_AS7")
        h('{fih_AS7 = new FInitializeHandler(0, "initialiseV_AS7()")}')

        h("proc initialiseIons_AS7() { for i = 0, n_AS7-1 { a_AS7[i].set_initial_ion_properties() } }")
        h("objref fih_ion_AS7")
        h('{fih_ion_AS7 = new FInitializeHandler(1, "initialiseIons_AS7()")}')

        # ######################   Population: AS8
        print("Population AS8 contains 1 instance(s) of component: GenericNeuronCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericNeuronCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericNeuronCell.hoc")
        a_AS8 = []
        h("{ n_AS8 = 1 }")
        h("objectvar a_AS8[n_AS8]")
        for i in range(int(h.n_AS8)):
            h("a_AS8[%i] = new GenericNeuronCell()"%i)
            h("access a_AS8[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_AS8[0].position(-1.9, 181.849999999999994, -1.7750001) }")

        h("proc initialiseV_AS8() { for i = 0, n_AS8-1 { a_AS8[i].set_initial_v() } }")
        h("objref fih_AS8")
        h('{fih_AS8 = new FInitializeHandler(0, "initialiseV_AS8()")}')

        h("proc initialiseIons_AS8() { for i = 0, n_AS8-1 { a_AS8[i].set_initial_ion_properties() } }")
        h("objref fih_ion_AS8")
        h('{fih_ion_AS8 = new FInitializeHandler(1, "initialiseIons_AS8()")}')

        # ######################   Population: AS9
        print("Population AS9 contains 1 instance(s) of component: GenericNeuronCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericNeuronCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericNeuronCell.hoc")
        a_AS9 = []
        h("{ n_AS9 = 1 }")
        h("objectvar a_AS9[n_AS9]")
        for i in range(int(h.n_AS9)):
            h("a_AS9[%i] = new GenericNeuronCell()"%i)
            h("access a_AS9[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_AS9[0].position(-1.8750001, 228.924990000000008, -14.5) }")

        h("proc initialiseV_AS9() { for i = 0, n_AS9-1 { a_AS9[i].set_initial_v() } }")
        h("objref fih_AS9")
        h('{fih_AS9 = new FInitializeHandler(0, "initialiseV_AS9()")}')

        h("proc initialiseIons_AS9() { for i = 0, n_AS9-1 { a_AS9[i].set_initial_ion_properties() } }")
        h("objref fih_ion_AS9")
        h('{fih_ion_AS9 = new FInitializeHandler(1, "initialiseIons_AS9()")}')

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

        # ######################   Population: DA1
        print("Population DA1 contains 1 instance(s) of component: GenericNeuronCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericNeuronCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericNeuronCell.hoc")
        a_DA1 = []
        h("{ n_DA1 = 1 }")
        h("objectvar a_DA1[n_DA1]")
        for i in range(int(h.n_DA1)):
            h("a_DA1[%i] = new GenericNeuronCell()"%i)
            h("access a_DA1[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_DA1[0].position(-0.75, -227.075009999999992, 3.425) }")

        h("proc initialiseV_DA1() { for i = 0, n_DA1-1 { a_DA1[i].set_initial_v() } }")
        h("objref fih_DA1")
        h('{fih_DA1 = new FInitializeHandler(0, "initialiseV_DA1()")}')

        h("proc initialiseIons_DA1() { for i = 0, n_DA1-1 { a_DA1[i].set_initial_ion_properties() } }")
        h("objref fih_ion_DA1")
        h('{fih_ion_DA1 = new FInitializeHandler(1, "initialiseIons_DA1()")}')

        # ######################   Population: DA2
        print("Population DA2 contains 1 instance(s) of component: GenericNeuronCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericNeuronCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericNeuronCell.hoc")
        a_DA2 = []
        h("{ n_DA2 = 1 }")
        h("objectvar a_DA2[n_DA2]")
        for i in range(int(h.n_DA2)):
            h("a_DA2[%i] = new GenericNeuronCell()"%i)
            h("access a_DA2[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_DA2[0].position(-1.9, -190.75, -21.675000000000001) }")

        h("proc initialiseV_DA2() { for i = 0, n_DA2-1 { a_DA2[i].set_initial_v() } }")
        h("objref fih_DA2")
        h('{fih_DA2 = new FInitializeHandler(0, "initialiseV_DA2()")}')

        h("proc initialiseIons_DA2() { for i = 0, n_DA2-1 { a_DA2[i].set_initial_ion_properties() } }")
        h("objref fih_ion_DA2")
        h('{fih_ion_DA2 = new FInitializeHandler(1, "initialiseIons_DA2()")}')

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

        # ######################   Population: DA4
        print("Population DA4 contains 1 instance(s) of component: GenericNeuronCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericNeuronCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericNeuronCell.hoc")
        a_DA4 = []
        h("{ n_DA4 = 1 }")
        h("objectvar a_DA4[n_DA4]")
        for i in range(int(h.n_DA4)):
            h("a_DA4[%i] = new GenericNeuronCell()"%i)
            h("access a_DA4[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_DA4[0].position(-1.7, -32.399999999999999, -61.75) }")

        h("proc initialiseV_DA4() { for i = 0, n_DA4-1 { a_DA4[i].set_initial_v() } }")
        h("objref fih_DA4")
        h('{fih_DA4 = new FInitializeHandler(0, "initialiseV_DA4()")}')

        h("proc initialiseIons_DA4() { for i = 0, n_DA4-1 { a_DA4[i].set_initial_ion_properties() } }")
        h("objref fih_ion_DA4")
        h('{fih_ion_DA4 = new FInitializeHandler(1, "initialiseIons_DA4()")}')

        # ######################   Population: DA5
        print("Population DA5 contains 1 instance(s) of component: GenericNeuronCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericNeuronCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericNeuronCell.hoc")
        a_DA5 = []
        h("{ n_DA5 = 1 }")
        h("objectvar a_DA5[n_DA5]")
        for i in range(int(h.n_DA5)):
            h("a_DA5[%i] = new GenericNeuronCell()"%i)
            h("access a_DA5[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_DA5[0].position(-1.65, 84.200000000000003, -3.15) }")

        h("proc initialiseV_DA5() { for i = 0, n_DA5-1 { a_DA5[i].set_initial_v() } }")
        h("objref fih_DA5")
        h('{fih_DA5 = new FInitializeHandler(0, "initialiseV_DA5()")}')

        h("proc initialiseIons_DA5() { for i = 0, n_DA5-1 { a_DA5[i].set_initial_ion_properties() } }")
        h("objref fih_ion_DA5")
        h('{fih_ion_DA5 = new FInitializeHandler(1, "initialiseIons_DA5()")}')

        # ######################   Population: DA6
        print("Population DA6 contains 1 instance(s) of component: GenericNeuronCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericNeuronCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericNeuronCell.hoc")
        a_DA6 = []
        h("{ n_DA6 = 1 }")
        h("objectvar a_DA6[n_DA6]")
        for i in range(int(h.n_DA6)):
            h("a_DA6[%i] = new GenericNeuronCell()"%i)
            h("access a_DA6[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_DA6[0].position(-1.65, 198.675000000000011, -6.3500004) }")

        h("proc initialiseV_DA6() { for i = 0, n_DA6-1 { a_DA6[i].set_initial_v() } }")
        h("objref fih_DA6")
        h('{fih_DA6 = new FInitializeHandler(0, "initialiseV_DA6()")}')

        h("proc initialiseIons_DA6() { for i = 0, n_DA6-1 { a_DA6[i].set_initial_ion_properties() } }")
        h("objref fih_ion_DA6")
        h('{fih_ion_DA6 = new FInitializeHandler(1, "initialiseIons_DA6()")}')

        # ######################   Population: DA7
        print("Population DA7 contains 1 instance(s) of component: GenericNeuronCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericNeuronCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericNeuronCell.hoc")
        a_DA7 = []
        h("{ n_DA7 = 1 }")
        h("objectvar a_DA7[n_DA7]")
        for i in range(int(h.n_DA7)):
            h("a_DA7[%i] = new GenericNeuronCell()"%i)
            h("access a_DA7[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_DA7[0].position(-1.65, 281.600000000000023, -24.949999999999999) }")

        h("proc initialiseV_DA7() { for i = 0, n_DA7-1 { a_DA7[i].set_initial_v() } }")
        h("objref fih_DA7")
        h('{fih_DA7 = new FInitializeHandler(0, "initialiseV_DA7()")}')

        h("proc initialiseIons_DA7() { for i = 0, n_DA7-1 { a_DA7[i].set_initial_ion_properties() } }")
        h("objref fih_ion_DA7")
        h('{fih_ion_DA7 = new FInitializeHandler(1, "initialiseIons_DA7()")}')

        # ######################   Population: DA8
        print("Population DA8 contains 1 instance(s) of component: GenericNeuronCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericNeuronCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericNeuronCell.hoc")
        a_DA8 = []
        h("{ n_DA8 = 1 }")
        h("objectvar a_DA8[n_DA8]")
        for i in range(int(h.n_DA8)):
            h("a_DA8[%i] = new GenericNeuronCell()"%i)
            h("access a_DA8[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_DA8[0].position(1.275, 376.800000000000011, -10.925000000000001) }")

        h("proc initialiseV_DA8() { for i = 0, n_DA8-1 { a_DA8[i].set_initial_v() } }")
        h("objref fih_DA8")
        h('{fih_DA8 = new FInitializeHandler(0, "initialiseV_DA8()")}')

        h("proc initialiseIons_DA8() { for i = 0, n_DA8-1 { a_DA8[i].set_initial_ion_properties() } }")
        h("objref fih_ion_DA8")
        h('{fih_ion_DA8 = new FInitializeHandler(1, "initialiseIons_DA8()")}')

        # ######################   Population: DA9
        print("Population DA9 contains 1 instance(s) of component: GenericNeuronCell of type: cell")

        print("Setting the default initial concentrations for ca (used in GenericNeuronCell) to 0.0 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 0.0")
        h("cao0_ca_ion = 2.0")

        h.load_file("GenericNeuronCell.hoc")
        a_DA9 = []
        h("{ n_DA9 = 1 }")
        h("objectvar a_DA9[n_DA9]")
        for i in range(int(h.n_DA9)):
            h("a_DA9[%i] = new GenericNeuronCell()"%i)
            h("access a_DA9[%i].soma"%i)

            self.next_global_id+=1

        h("{ a_DA9[0].position(-4.6, 376.800000000000011, -10.925000000000001) }")

        h("proc initialiseV_DA9() { for i = 0, n_DA9-1 { a_DA9[i].set_initial_v() } }")
        h("objref fih_DA9")
        h('{fih_DA9 = new FInitializeHandler(0, "initialiseV_DA9()")}')

        h("proc initialiseIons_DA9() { for i = 0, n_DA9-1 { a_DA9[i].set_initial_ion_properties() } }")
        h("objref fih_ion_DA9")
        h('{fih_ion_DA9 = new FInitializeHandler(1, "initialiseIons_DA9()")}')

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

        # ######################   Electrical Projection: NC_AVAL_DA1_Generic_GJ
        print("Adding electrical projection: NC_AVAL_DA1_Generic_GJ from AVAL to DA1, with 1 connection(s)")

        h("objectvar syn_NC_AVAL_DA1_Generic_GJ_AVAL_to_DA1_elec_syn_A[1]")
        h("objectvar syn_NC_AVAL_DA1_Generic_GJ_AVAL_to_DA1_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVAL[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DA1[0].soma], weight: 2.0
        h("a_AVAL[0].soma { syn_NC_AVAL_DA1_Generic_GJ_AVAL_to_DA1_elec_syn_A[0] = new AVAL_to_DA1_elec_syn(0.5) }")
        h("a_DA1[0].soma { syn_NC_AVAL_DA1_Generic_GJ_AVAL_to_DA1_elec_syn_B[0] = new AVAL_to_DA1_elec_syn(0.5) }")
        h("a_AVAL[0].soma { syn_NC_AVAL_DA1_Generic_GJ_AVAL_to_DA1_elec_syn_A[0].weight = 2.0 }")
        h("a_DA1[0].soma { syn_NC_AVAL_DA1_Generic_GJ_AVAL_to_DA1_elec_syn_B[0].weight = 2.0 }")
        h("setpointer syn_NC_AVAL_DA1_Generic_GJ_AVAL_to_DA1_elec_syn_A[0].vpeer, a_DA1[0].soma.v(0.5)")
        h("setpointer syn_NC_AVAL_DA1_Generic_GJ_AVAL_to_DA1_elec_syn_B[0].vpeer, a_AVAL[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_AVAL_DA2_Generic_GJ
        print("Adding electrical projection: NC_AVAL_DA2_Generic_GJ from AVAL to DA2, with 1 connection(s)")

        h("objectvar syn_NC_AVAL_DA2_Generic_GJ_AVAL_to_DA2_elec_syn_A[1]")
        h("objectvar syn_NC_AVAL_DA2_Generic_GJ_AVAL_to_DA2_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVAL[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DA2[0].soma], weight: 7.0
        h("a_AVAL[0].soma { syn_NC_AVAL_DA2_Generic_GJ_AVAL_to_DA2_elec_syn_A[0] = new AVAL_to_DA2_elec_syn(0.5) }")
        h("a_DA2[0].soma { syn_NC_AVAL_DA2_Generic_GJ_AVAL_to_DA2_elec_syn_B[0] = new AVAL_to_DA2_elec_syn(0.5) }")
        h("a_AVAL[0].soma { syn_NC_AVAL_DA2_Generic_GJ_AVAL_to_DA2_elec_syn_A[0].weight = 7.0 }")
        h("a_DA2[0].soma { syn_NC_AVAL_DA2_Generic_GJ_AVAL_to_DA2_elec_syn_B[0].weight = 7.0 }")
        h("setpointer syn_NC_AVAL_DA2_Generic_GJ_AVAL_to_DA2_elec_syn_A[0].vpeer, a_DA2[0].soma.v(0.5)")
        h("setpointer syn_NC_AVAL_DA2_Generic_GJ_AVAL_to_DA2_elec_syn_B[0].vpeer, a_AVAL[0].soma.v(0.5)")

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

        # ######################   Electrical Projection: NC_AVAL_DA4_Generic_GJ
        print("Adding electrical projection: NC_AVAL_DA4_Generic_GJ from AVAL to DA4, with 1 connection(s)")

        h("objectvar syn_NC_AVAL_DA4_Generic_GJ_AVAL_to_DA4_elec_syn_A[1]")
        h("objectvar syn_NC_AVAL_DA4_Generic_GJ_AVAL_to_DA4_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVAL[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DA4[0].soma], weight: 2.0
        h("a_AVAL[0].soma { syn_NC_AVAL_DA4_Generic_GJ_AVAL_to_DA4_elec_syn_A[0] = new AVAL_to_DA4_elec_syn(0.5) }")
        h("a_DA4[0].soma { syn_NC_AVAL_DA4_Generic_GJ_AVAL_to_DA4_elec_syn_B[0] = new AVAL_to_DA4_elec_syn(0.5) }")
        h("a_AVAL[0].soma { syn_NC_AVAL_DA4_Generic_GJ_AVAL_to_DA4_elec_syn_A[0].weight = 2.0 }")
        h("a_DA4[0].soma { syn_NC_AVAL_DA4_Generic_GJ_AVAL_to_DA4_elec_syn_B[0].weight = 2.0 }")
        h("setpointer syn_NC_AVAL_DA4_Generic_GJ_AVAL_to_DA4_elec_syn_A[0].vpeer, a_DA4[0].soma.v(0.5)")
        h("setpointer syn_NC_AVAL_DA4_Generic_GJ_AVAL_to_DA4_elec_syn_B[0].vpeer, a_AVAL[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_AVAL_DA5_Generic_GJ
        print("Adding electrical projection: NC_AVAL_DA5_Generic_GJ from AVAL to DA5, with 1 connection(s)")

        h("objectvar syn_NC_AVAL_DA5_Generic_GJ_AVAL_to_DA5_elec_syn_A[1]")
        h("objectvar syn_NC_AVAL_DA5_Generic_GJ_AVAL_to_DA5_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVAL[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DA5[0].soma], weight: 2.0
        h("a_AVAL[0].soma { syn_NC_AVAL_DA5_Generic_GJ_AVAL_to_DA5_elec_syn_A[0] = new AVAL_to_DA5_elec_syn(0.5) }")
        h("a_DA5[0].soma { syn_NC_AVAL_DA5_Generic_GJ_AVAL_to_DA5_elec_syn_B[0] = new AVAL_to_DA5_elec_syn(0.5) }")
        h("a_AVAL[0].soma { syn_NC_AVAL_DA5_Generic_GJ_AVAL_to_DA5_elec_syn_A[0].weight = 2.0 }")
        h("a_DA5[0].soma { syn_NC_AVAL_DA5_Generic_GJ_AVAL_to_DA5_elec_syn_B[0].weight = 2.0 }")
        h("setpointer syn_NC_AVAL_DA5_Generic_GJ_AVAL_to_DA5_elec_syn_A[0].vpeer, a_DA5[0].soma.v(0.5)")
        h("setpointer syn_NC_AVAL_DA5_Generic_GJ_AVAL_to_DA5_elec_syn_B[0].vpeer, a_AVAL[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_AVAL_DA6_Generic_GJ
        print("Adding electrical projection: NC_AVAL_DA6_Generic_GJ from AVAL to DA6, with 1 connection(s)")

        h("objectvar syn_NC_AVAL_DA6_Generic_GJ_AVAL_to_DA6_elec_syn_A[1]")
        h("objectvar syn_NC_AVAL_DA6_Generic_GJ_AVAL_to_DA6_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVAL[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DA6[0].soma], weight: 4.0
        h("a_AVAL[0].soma { syn_NC_AVAL_DA6_Generic_GJ_AVAL_to_DA6_elec_syn_A[0] = new AVAL_to_DA6_elec_syn(0.5) }")
        h("a_DA6[0].soma { syn_NC_AVAL_DA6_Generic_GJ_AVAL_to_DA6_elec_syn_B[0] = new AVAL_to_DA6_elec_syn(0.5) }")
        h("a_AVAL[0].soma { syn_NC_AVAL_DA6_Generic_GJ_AVAL_to_DA6_elec_syn_A[0].weight = 4.0 }")
        h("a_DA6[0].soma { syn_NC_AVAL_DA6_Generic_GJ_AVAL_to_DA6_elec_syn_B[0].weight = 4.0 }")
        h("setpointer syn_NC_AVAL_DA6_Generic_GJ_AVAL_to_DA6_elec_syn_A[0].vpeer, a_DA6[0].soma.v(0.5)")
        h("setpointer syn_NC_AVAL_DA6_Generic_GJ_AVAL_to_DA6_elec_syn_B[0].vpeer, a_AVAL[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_AVAL_DA7_Generic_GJ
        print("Adding electrical projection: NC_AVAL_DA7_Generic_GJ from AVAL to DA7, with 1 connection(s)")

        h("objectvar syn_NC_AVAL_DA7_Generic_GJ_AVAL_to_DA7_elec_syn_A[1]")
        h("objectvar syn_NC_AVAL_DA7_Generic_GJ_AVAL_to_DA7_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVAL[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DA7[0].soma], weight: 10.0
        h("a_AVAL[0].soma { syn_NC_AVAL_DA7_Generic_GJ_AVAL_to_DA7_elec_syn_A[0] = new AVAL_to_DA7_elec_syn(0.5) }")
        h("a_DA7[0].soma { syn_NC_AVAL_DA7_Generic_GJ_AVAL_to_DA7_elec_syn_B[0] = new AVAL_to_DA7_elec_syn(0.5) }")
        h("a_AVAL[0].soma { syn_NC_AVAL_DA7_Generic_GJ_AVAL_to_DA7_elec_syn_A[0].weight = 10.0 }")
        h("a_DA7[0].soma { syn_NC_AVAL_DA7_Generic_GJ_AVAL_to_DA7_elec_syn_B[0].weight = 10.0 }")
        h("setpointer syn_NC_AVAL_DA7_Generic_GJ_AVAL_to_DA7_elec_syn_A[0].vpeer, a_DA7[0].soma.v(0.5)")
        h("setpointer syn_NC_AVAL_DA7_Generic_GJ_AVAL_to_DA7_elec_syn_B[0].vpeer, a_AVAL[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_AVAL_DA8_Generic_GJ
        print("Adding electrical projection: NC_AVAL_DA8_Generic_GJ from AVAL to DA8, with 1 connection(s)")

        h("objectvar syn_NC_AVAL_DA8_Generic_GJ_AVAL_to_DA8_elec_syn_A[1]")
        h("objectvar syn_NC_AVAL_DA8_Generic_GJ_AVAL_to_DA8_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVAL[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DA8[0].soma], weight: 8.0
        h("a_AVAL[0].soma { syn_NC_AVAL_DA8_Generic_GJ_AVAL_to_DA8_elec_syn_A[0] = new AVAL_to_DA8_elec_syn(0.5) }")
        h("a_DA8[0].soma { syn_NC_AVAL_DA8_Generic_GJ_AVAL_to_DA8_elec_syn_B[0] = new AVAL_to_DA8_elec_syn(0.5) }")
        h("a_AVAL[0].soma { syn_NC_AVAL_DA8_Generic_GJ_AVAL_to_DA8_elec_syn_A[0].weight = 8.0 }")
        h("a_DA8[0].soma { syn_NC_AVAL_DA8_Generic_GJ_AVAL_to_DA8_elec_syn_B[0].weight = 8.0 }")
        h("setpointer syn_NC_AVAL_DA8_Generic_GJ_AVAL_to_DA8_elec_syn_A[0].vpeer, a_DA8[0].soma.v(0.5)")
        h("setpointer syn_NC_AVAL_DA8_Generic_GJ_AVAL_to_DA8_elec_syn_B[0].vpeer, a_AVAL[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_AVAL_DA9_Generic_GJ
        print("Adding electrical projection: NC_AVAL_DA9_Generic_GJ from AVAL to DA9, with 1 connection(s)")

        h("objectvar syn_NC_AVAL_DA9_Generic_GJ_AVAL_to_DA9_elec_syn_A[1]")
        h("objectvar syn_NC_AVAL_DA9_Generic_GJ_AVAL_to_DA9_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVAL[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DA9[0].soma], weight: 1.0
        h("a_AVAL[0].soma { syn_NC_AVAL_DA9_Generic_GJ_AVAL_to_DA9_elec_syn_A[0] = new AVAL_to_DA9_elec_syn(0.5) }")
        h("a_DA9[0].soma { syn_NC_AVAL_DA9_Generic_GJ_AVAL_to_DA9_elec_syn_B[0] = new AVAL_to_DA9_elec_syn(0.5) }")
        h("setpointer syn_NC_AVAL_DA9_Generic_GJ_AVAL_to_DA9_elec_syn_A[0].vpeer, a_DA9[0].soma.v(0.5)")
        h("setpointer syn_NC_AVAL_DA9_Generic_GJ_AVAL_to_DA9_elec_syn_B[0].vpeer, a_AVAL[0].soma.v(0.5)")

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

        # ######################   Electrical Projection: NC_AVAR_DA1_Generic_GJ
        print("Adding electrical projection: NC_AVAR_DA1_Generic_GJ from AVAR to DA1, with 1 connection(s)")

        h("objectvar syn_NC_AVAR_DA1_Generic_GJ_AVAR_to_DA1_elec_syn_A[1]")
        h("objectvar syn_NC_AVAR_DA1_Generic_GJ_AVAR_to_DA1_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVAR[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DA1[0].soma], weight: 9.0
        h("a_AVAR[0].soma { syn_NC_AVAR_DA1_Generic_GJ_AVAR_to_DA1_elec_syn_A[0] = new AVAR_to_DA1_elec_syn(0.5) }")
        h("a_DA1[0].soma { syn_NC_AVAR_DA1_Generic_GJ_AVAR_to_DA1_elec_syn_B[0] = new AVAR_to_DA1_elec_syn(0.5) }")
        h("a_AVAR[0].soma { syn_NC_AVAR_DA1_Generic_GJ_AVAR_to_DA1_elec_syn_A[0].weight = 9.0 }")
        h("a_DA1[0].soma { syn_NC_AVAR_DA1_Generic_GJ_AVAR_to_DA1_elec_syn_B[0].weight = 9.0 }")
        h("setpointer syn_NC_AVAR_DA1_Generic_GJ_AVAR_to_DA1_elec_syn_A[0].vpeer, a_DA1[0].soma.v(0.5)")
        h("setpointer syn_NC_AVAR_DA1_Generic_GJ_AVAR_to_DA1_elec_syn_B[0].vpeer, a_AVAR[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_AVAR_DA2_Generic_GJ
        print("Adding electrical projection: NC_AVAR_DA2_Generic_GJ from AVAR to DA2, with 1 connection(s)")

        h("objectvar syn_NC_AVAR_DA2_Generic_GJ_AVAR_to_DA2_elec_syn_A[1]")
        h("objectvar syn_NC_AVAR_DA2_Generic_GJ_AVAR_to_DA2_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVAR[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DA2[0].soma], weight: 3.0
        h("a_AVAR[0].soma { syn_NC_AVAR_DA2_Generic_GJ_AVAR_to_DA2_elec_syn_A[0] = new AVAR_to_DA2_elec_syn(0.5) }")
        h("a_DA2[0].soma { syn_NC_AVAR_DA2_Generic_GJ_AVAR_to_DA2_elec_syn_B[0] = new AVAR_to_DA2_elec_syn(0.5) }")
        h("a_AVAR[0].soma { syn_NC_AVAR_DA2_Generic_GJ_AVAR_to_DA2_elec_syn_A[0].weight = 3.0 }")
        h("a_DA2[0].soma { syn_NC_AVAR_DA2_Generic_GJ_AVAR_to_DA2_elec_syn_B[0].weight = 3.0 }")
        h("setpointer syn_NC_AVAR_DA2_Generic_GJ_AVAR_to_DA2_elec_syn_A[0].vpeer, a_DA2[0].soma.v(0.5)")
        h("setpointer syn_NC_AVAR_DA2_Generic_GJ_AVAR_to_DA2_elec_syn_B[0].vpeer, a_AVAR[0].soma.v(0.5)")

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

        # ######################   Electrical Projection: NC_AVAR_DA4_Generic_GJ
        print("Adding electrical projection: NC_AVAR_DA4_Generic_GJ from AVAR to DA4, with 1 connection(s)")

        h("objectvar syn_NC_AVAR_DA4_Generic_GJ_AVAR_to_DA4_elec_syn_A[1]")
        h("objectvar syn_NC_AVAR_DA4_Generic_GJ_AVAR_to_DA4_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVAR[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DA4[0].soma], weight: 2.0
        h("a_AVAR[0].soma { syn_NC_AVAR_DA4_Generic_GJ_AVAR_to_DA4_elec_syn_A[0] = new AVAR_to_DA4_elec_syn(0.5) }")
        h("a_DA4[0].soma { syn_NC_AVAR_DA4_Generic_GJ_AVAR_to_DA4_elec_syn_B[0] = new AVAR_to_DA4_elec_syn(0.5) }")
        h("a_AVAR[0].soma { syn_NC_AVAR_DA4_Generic_GJ_AVAR_to_DA4_elec_syn_A[0].weight = 2.0 }")
        h("a_DA4[0].soma { syn_NC_AVAR_DA4_Generic_GJ_AVAR_to_DA4_elec_syn_B[0].weight = 2.0 }")
        h("setpointer syn_NC_AVAR_DA4_Generic_GJ_AVAR_to_DA4_elec_syn_A[0].vpeer, a_DA4[0].soma.v(0.5)")
        h("setpointer syn_NC_AVAR_DA4_Generic_GJ_AVAR_to_DA4_elec_syn_B[0].vpeer, a_AVAR[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_AVAR_DA5_Generic_GJ
        print("Adding electrical projection: NC_AVAR_DA5_Generic_GJ from AVAR to DA5, with 1 connection(s)")

        h("objectvar syn_NC_AVAR_DA5_Generic_GJ_AVAR_to_DA5_elec_syn_A[1]")
        h("objectvar syn_NC_AVAR_DA5_Generic_GJ_AVAR_to_DA5_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVAR[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DA5[0].soma], weight: 5.0
        h("a_AVAR[0].soma { syn_NC_AVAR_DA5_Generic_GJ_AVAR_to_DA5_elec_syn_A[0] = new AVAR_to_DA5_elec_syn(0.5) }")
        h("a_DA5[0].soma { syn_NC_AVAR_DA5_Generic_GJ_AVAR_to_DA5_elec_syn_B[0] = new AVAR_to_DA5_elec_syn(0.5) }")
        h("a_AVAR[0].soma { syn_NC_AVAR_DA5_Generic_GJ_AVAR_to_DA5_elec_syn_A[0].weight = 5.0 }")
        h("a_DA5[0].soma { syn_NC_AVAR_DA5_Generic_GJ_AVAR_to_DA5_elec_syn_B[0].weight = 5.0 }")
        h("setpointer syn_NC_AVAR_DA5_Generic_GJ_AVAR_to_DA5_elec_syn_A[0].vpeer, a_DA5[0].soma.v(0.5)")
        h("setpointer syn_NC_AVAR_DA5_Generic_GJ_AVAR_to_DA5_elec_syn_B[0].vpeer, a_AVAR[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_AVAR_DA6_Generic_GJ
        print("Adding electrical projection: NC_AVAR_DA6_Generic_GJ from AVAR to DA6, with 1 connection(s)")

        h("objectvar syn_NC_AVAR_DA6_Generic_GJ_AVAR_to_DA6_elec_syn_A[1]")
        h("objectvar syn_NC_AVAR_DA6_Generic_GJ_AVAR_to_DA6_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVAR[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DA6[0].soma], weight: 4.0
        h("a_AVAR[0].soma { syn_NC_AVAR_DA6_Generic_GJ_AVAR_to_DA6_elec_syn_A[0] = new AVAR_to_DA6_elec_syn(0.5) }")
        h("a_DA6[0].soma { syn_NC_AVAR_DA6_Generic_GJ_AVAR_to_DA6_elec_syn_B[0] = new AVAR_to_DA6_elec_syn(0.5) }")
        h("a_AVAR[0].soma { syn_NC_AVAR_DA6_Generic_GJ_AVAR_to_DA6_elec_syn_A[0].weight = 4.0 }")
        h("a_DA6[0].soma { syn_NC_AVAR_DA6_Generic_GJ_AVAR_to_DA6_elec_syn_B[0].weight = 4.0 }")
        h("setpointer syn_NC_AVAR_DA6_Generic_GJ_AVAR_to_DA6_elec_syn_A[0].vpeer, a_DA6[0].soma.v(0.5)")
        h("setpointer syn_NC_AVAR_DA6_Generic_GJ_AVAR_to_DA6_elec_syn_B[0].vpeer, a_AVAR[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_AVAR_DA8_Generic_GJ
        print("Adding electrical projection: NC_AVAR_DA8_Generic_GJ from AVAR to DA8, with 1 connection(s)")

        h("objectvar syn_NC_AVAR_DA8_Generic_GJ_AVAR_to_DA8_elec_syn_A[1]")
        h("objectvar syn_NC_AVAR_DA8_Generic_GJ_AVAR_to_DA8_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVAR[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DA8[0].soma], weight: 5.0
        h("a_AVAR[0].soma { syn_NC_AVAR_DA8_Generic_GJ_AVAR_to_DA8_elec_syn_A[0] = new AVAR_to_DA8_elec_syn(0.5) }")
        h("a_DA8[0].soma { syn_NC_AVAR_DA8_Generic_GJ_AVAR_to_DA8_elec_syn_B[0] = new AVAR_to_DA8_elec_syn(0.5) }")
        h("a_AVAR[0].soma { syn_NC_AVAR_DA8_Generic_GJ_AVAR_to_DA8_elec_syn_A[0].weight = 5.0 }")
        h("a_DA8[0].soma { syn_NC_AVAR_DA8_Generic_GJ_AVAR_to_DA8_elec_syn_B[0].weight = 5.0 }")
        h("setpointer syn_NC_AVAR_DA8_Generic_GJ_AVAR_to_DA8_elec_syn_A[0].vpeer, a_DA8[0].soma.v(0.5)")
        h("setpointer syn_NC_AVAR_DA8_Generic_GJ_AVAR_to_DA8_elec_syn_B[0].vpeer, a_AVAR[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_AVAR_DA9_Generic_GJ
        print("Adding electrical projection: NC_AVAR_DA9_Generic_GJ from AVAR to DA9, with 1 connection(s)")

        h("objectvar syn_NC_AVAR_DA9_Generic_GJ_AVAR_to_DA9_elec_syn_A[1]")
        h("objectvar syn_NC_AVAR_DA9_Generic_GJ_AVAR_to_DA9_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVAR[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DA9[0].soma], weight: 4.0
        h("a_AVAR[0].soma { syn_NC_AVAR_DA9_Generic_GJ_AVAR_to_DA9_elec_syn_A[0] = new AVAR_to_DA9_elec_syn(0.5) }")
        h("a_DA9[0].soma { syn_NC_AVAR_DA9_Generic_GJ_AVAR_to_DA9_elec_syn_B[0] = new AVAR_to_DA9_elec_syn(0.5) }")
        h("a_AVAR[0].soma { syn_NC_AVAR_DA9_Generic_GJ_AVAR_to_DA9_elec_syn_A[0].weight = 4.0 }")
        h("a_DA9[0].soma { syn_NC_AVAR_DA9_Generic_GJ_AVAR_to_DA9_elec_syn_B[0].weight = 4.0 }")
        h("setpointer syn_NC_AVAR_DA9_Generic_GJ_AVAR_to_DA9_elec_syn_A[0].vpeer, a_DA9[0].soma.v(0.5)")
        h("setpointer syn_NC_AVAR_DA9_Generic_GJ_AVAR_to_DA9_elec_syn_B[0].vpeer, a_AVAR[0].soma.v(0.5)")

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

        # ######################   Electrical Projection: NC_AVBL_DB2_Generic_GJ
        print("Adding electrical projection: NC_AVBL_DB2_Generic_GJ from AVBL to DB2, with 1 connection(s)")

        h("objectvar syn_NC_AVBL_DB2_Generic_GJ_AVBL_to_DB2_elec_syn_A[1]")
        h("objectvar syn_NC_AVBL_DB2_Generic_GJ_AVBL_to_DB2_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVBL[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DB2[0].soma], weight: 4.0
        h("a_AVBL[0].soma { syn_NC_AVBL_DB2_Generic_GJ_AVBL_to_DB2_elec_syn_A[0] = new AVBL_to_DB2_elec_syn(0.5) }")
        h("a_DB2[0].soma { syn_NC_AVBL_DB2_Generic_GJ_AVBL_to_DB2_elec_syn_B[0] = new AVBL_to_DB2_elec_syn(0.5) }")
        h("a_AVBL[0].soma { syn_NC_AVBL_DB2_Generic_GJ_AVBL_to_DB2_elec_syn_A[0].weight = 4.0 }")
        h("a_DB2[0].soma { syn_NC_AVBL_DB2_Generic_GJ_AVBL_to_DB2_elec_syn_B[0].weight = 4.0 }")
        h("setpointer syn_NC_AVBL_DB2_Generic_GJ_AVBL_to_DB2_elec_syn_A[0].vpeer, a_DB2[0].soma.v(0.5)")
        h("setpointer syn_NC_AVBL_DB2_Generic_GJ_AVBL_to_DB2_elec_syn_B[0].vpeer, a_AVBL[0].soma.v(0.5)")

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

        # ######################   Electrical Projection: NC_AVBL_DB4_Generic_GJ
        print("Adding electrical projection: NC_AVBL_DB4_Generic_GJ from AVBL to DB4, with 1 connection(s)")

        h("objectvar syn_NC_AVBL_DB4_Generic_GJ_AVBL_to_DB4_elec_syn_A[1]")
        h("objectvar syn_NC_AVBL_DB4_Generic_GJ_AVBL_to_DB4_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVBL[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DB4[0].soma], weight: 4.0
        h("a_AVBL[0].soma { syn_NC_AVBL_DB4_Generic_GJ_AVBL_to_DB4_elec_syn_A[0] = new AVBL_to_DB4_elec_syn(0.5) }")
        h("a_DB4[0].soma { syn_NC_AVBL_DB4_Generic_GJ_AVBL_to_DB4_elec_syn_B[0] = new AVBL_to_DB4_elec_syn(0.5) }")
        h("a_AVBL[0].soma { syn_NC_AVBL_DB4_Generic_GJ_AVBL_to_DB4_elec_syn_A[0].weight = 4.0 }")
        h("a_DB4[0].soma { syn_NC_AVBL_DB4_Generic_GJ_AVBL_to_DB4_elec_syn_B[0].weight = 4.0 }")
        h("setpointer syn_NC_AVBL_DB4_Generic_GJ_AVBL_to_DB4_elec_syn_A[0].vpeer, a_DB4[0].soma.v(0.5)")
        h("setpointer syn_NC_AVBL_DB4_Generic_GJ_AVBL_to_DB4_elec_syn_B[0].vpeer, a_AVBL[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_AVBL_DB5_Generic_GJ
        print("Adding electrical projection: NC_AVBL_DB5_Generic_GJ from AVBL to DB5, with 1 connection(s)")

        h("objectvar syn_NC_AVBL_DB5_Generic_GJ_AVBL_to_DB5_elec_syn_A[1]")
        h("objectvar syn_NC_AVBL_DB5_Generic_GJ_AVBL_to_DB5_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVBL[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DB5[0].soma], weight: 3.0
        h("a_AVBL[0].soma { syn_NC_AVBL_DB5_Generic_GJ_AVBL_to_DB5_elec_syn_A[0] = new AVBL_to_DB5_elec_syn(0.5) }")
        h("a_DB5[0].soma { syn_NC_AVBL_DB5_Generic_GJ_AVBL_to_DB5_elec_syn_B[0] = new AVBL_to_DB5_elec_syn(0.5) }")
        h("a_AVBL[0].soma { syn_NC_AVBL_DB5_Generic_GJ_AVBL_to_DB5_elec_syn_A[0].weight = 3.0 }")
        h("a_DB5[0].soma { syn_NC_AVBL_DB5_Generic_GJ_AVBL_to_DB5_elec_syn_B[0].weight = 3.0 }")
        h("setpointer syn_NC_AVBL_DB5_Generic_GJ_AVBL_to_DB5_elec_syn_A[0].vpeer, a_DB5[0].soma.v(0.5)")
        h("setpointer syn_NC_AVBL_DB5_Generic_GJ_AVBL_to_DB5_elec_syn_B[0].vpeer, a_AVBL[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_AVBL_DB6_Generic_GJ
        print("Adding electrical projection: NC_AVBL_DB6_Generic_GJ from AVBL to DB6, with 1 connection(s)")

        h("objectvar syn_NC_AVBL_DB6_Generic_GJ_AVBL_to_DB6_elec_syn_A[1]")
        h("objectvar syn_NC_AVBL_DB6_Generic_GJ_AVBL_to_DB6_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVBL[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DB6[0].soma], weight: 4.0
        h("a_AVBL[0].soma { syn_NC_AVBL_DB6_Generic_GJ_AVBL_to_DB6_elec_syn_A[0] = new AVBL_to_DB6_elec_syn(0.5) }")
        h("a_DB6[0].soma { syn_NC_AVBL_DB6_Generic_GJ_AVBL_to_DB6_elec_syn_B[0] = new AVBL_to_DB6_elec_syn(0.5) }")
        h("a_AVBL[0].soma { syn_NC_AVBL_DB6_Generic_GJ_AVBL_to_DB6_elec_syn_A[0].weight = 4.0 }")
        h("a_DB6[0].soma { syn_NC_AVBL_DB6_Generic_GJ_AVBL_to_DB6_elec_syn_B[0].weight = 4.0 }")
        h("setpointer syn_NC_AVBL_DB6_Generic_GJ_AVBL_to_DB6_elec_syn_A[0].vpeer, a_DB6[0].soma.v(0.5)")
        h("setpointer syn_NC_AVBL_DB6_Generic_GJ_AVBL_to_DB6_elec_syn_B[0].vpeer, a_AVBL[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_AVBL_DB7_Generic_GJ
        print("Adding electrical projection: NC_AVBL_DB7_Generic_GJ from AVBL to DB7, with 1 connection(s)")

        h("objectvar syn_NC_AVBL_DB7_Generic_GJ_AVBL_to_DB7_elec_syn_A[1]")
        h("objectvar syn_NC_AVBL_DB7_Generic_GJ_AVBL_to_DB7_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVBL[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DB7[0].soma], weight: 13.0
        h("a_AVBL[0].soma { syn_NC_AVBL_DB7_Generic_GJ_AVBL_to_DB7_elec_syn_A[0] = new AVBL_to_DB7_elec_syn(0.5) }")
        h("a_DB7[0].soma { syn_NC_AVBL_DB7_Generic_GJ_AVBL_to_DB7_elec_syn_B[0] = new AVBL_to_DB7_elec_syn(0.5) }")
        h("a_AVBL[0].soma { syn_NC_AVBL_DB7_Generic_GJ_AVBL_to_DB7_elec_syn_A[0].weight = 13.0 }")
        h("a_DB7[0].soma { syn_NC_AVBL_DB7_Generic_GJ_AVBL_to_DB7_elec_syn_B[0].weight = 13.0 }")
        h("setpointer syn_NC_AVBL_DB7_Generic_GJ_AVBL_to_DB7_elec_syn_A[0].vpeer, a_DB7[0].soma.v(0.5)")
        h("setpointer syn_NC_AVBL_DB7_Generic_GJ_AVBL_to_DB7_elec_syn_B[0].vpeer, a_AVBL[0].soma.v(0.5)")

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

        # ######################   Electrical Projection: NC_AVBR_DB1_Generic_GJ
        print("Adding electrical projection: NC_AVBR_DB1_Generic_GJ from AVBR to DB1, with 1 connection(s)")

        h("objectvar syn_NC_AVBR_DB1_Generic_GJ_AVBR_to_DB1_elec_syn_A[1]")
        h("objectvar syn_NC_AVBR_DB1_Generic_GJ_AVBR_to_DB1_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVBR[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DB1[0].soma], weight: 15.0
        h("a_AVBR[0].soma { syn_NC_AVBR_DB1_Generic_GJ_AVBR_to_DB1_elec_syn_A[0] = new AVBR_to_DB1_elec_syn(0.5) }")
        h("a_DB1[0].soma { syn_NC_AVBR_DB1_Generic_GJ_AVBR_to_DB1_elec_syn_B[0] = new AVBR_to_DB1_elec_syn(0.5) }")
        h("a_AVBR[0].soma { syn_NC_AVBR_DB1_Generic_GJ_AVBR_to_DB1_elec_syn_A[0].weight = 15.0 }")
        h("a_DB1[0].soma { syn_NC_AVBR_DB1_Generic_GJ_AVBR_to_DB1_elec_syn_B[0].weight = 15.0 }")
        h("setpointer syn_NC_AVBR_DB1_Generic_GJ_AVBR_to_DB1_elec_syn_A[0].vpeer, a_DB1[0].soma.v(0.5)")
        h("setpointer syn_NC_AVBR_DB1_Generic_GJ_AVBR_to_DB1_elec_syn_B[0].vpeer, a_AVBR[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_AVBR_DB2_Generic_GJ
        print("Adding electrical projection: NC_AVBR_DB2_Generic_GJ from AVBR to DB2, with 1 connection(s)")

        h("objectvar syn_NC_AVBR_DB2_Generic_GJ_AVBR_to_DB2_elec_syn_A[1]")
        h("objectvar syn_NC_AVBR_DB2_Generic_GJ_AVBR_to_DB2_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVBR[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DB2[0].soma], weight: 3.0
        h("a_AVBR[0].soma { syn_NC_AVBR_DB2_Generic_GJ_AVBR_to_DB2_elec_syn_A[0] = new AVBR_to_DB2_elec_syn(0.5) }")
        h("a_DB2[0].soma { syn_NC_AVBR_DB2_Generic_GJ_AVBR_to_DB2_elec_syn_B[0] = new AVBR_to_DB2_elec_syn(0.5) }")
        h("a_AVBR[0].soma { syn_NC_AVBR_DB2_Generic_GJ_AVBR_to_DB2_elec_syn_A[0].weight = 3.0 }")
        h("a_DB2[0].soma { syn_NC_AVBR_DB2_Generic_GJ_AVBR_to_DB2_elec_syn_B[0].weight = 3.0 }")
        h("setpointer syn_NC_AVBR_DB2_Generic_GJ_AVBR_to_DB2_elec_syn_A[0].vpeer, a_DB2[0].soma.v(0.5)")
        h("setpointer syn_NC_AVBR_DB2_Generic_GJ_AVBR_to_DB2_elec_syn_B[0].vpeer, a_AVBR[0].soma.v(0.5)")

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

        # ######################   Electrical Projection: NC_AVBR_DB4_Generic_GJ
        print("Adding electrical projection: NC_AVBR_DB4_Generic_GJ from AVBR to DB4, with 1 connection(s)")

        h("objectvar syn_NC_AVBR_DB4_Generic_GJ_AVBR_to_DB4_elec_syn_A[1]")
        h("objectvar syn_NC_AVBR_DB4_Generic_GJ_AVBR_to_DB4_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVBR[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DB4[0].soma], weight: 5.0
        h("a_AVBR[0].soma { syn_NC_AVBR_DB4_Generic_GJ_AVBR_to_DB4_elec_syn_A[0] = new AVBR_to_DB4_elec_syn(0.5) }")
        h("a_DB4[0].soma { syn_NC_AVBR_DB4_Generic_GJ_AVBR_to_DB4_elec_syn_B[0] = new AVBR_to_DB4_elec_syn(0.5) }")
        h("a_AVBR[0].soma { syn_NC_AVBR_DB4_Generic_GJ_AVBR_to_DB4_elec_syn_A[0].weight = 5.0 }")
        h("a_DB4[0].soma { syn_NC_AVBR_DB4_Generic_GJ_AVBR_to_DB4_elec_syn_B[0].weight = 5.0 }")
        h("setpointer syn_NC_AVBR_DB4_Generic_GJ_AVBR_to_DB4_elec_syn_A[0].vpeer, a_DB4[0].soma.v(0.5)")
        h("setpointer syn_NC_AVBR_DB4_Generic_GJ_AVBR_to_DB4_elec_syn_B[0].vpeer, a_AVBR[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_AVBR_DB5_Generic_GJ
        print("Adding electrical projection: NC_AVBR_DB5_Generic_GJ from AVBR to DB5, with 1 connection(s)")

        h("objectvar syn_NC_AVBR_DB5_Generic_GJ_AVBR_to_DB5_elec_syn_A[1]")
        h("objectvar syn_NC_AVBR_DB5_Generic_GJ_AVBR_to_DB5_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVBR[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DB5[0].soma], weight: 4.0
        h("a_AVBR[0].soma { syn_NC_AVBR_DB5_Generic_GJ_AVBR_to_DB5_elec_syn_A[0] = new AVBR_to_DB5_elec_syn(0.5) }")
        h("a_DB5[0].soma { syn_NC_AVBR_DB5_Generic_GJ_AVBR_to_DB5_elec_syn_B[0] = new AVBR_to_DB5_elec_syn(0.5) }")
        h("a_AVBR[0].soma { syn_NC_AVBR_DB5_Generic_GJ_AVBR_to_DB5_elec_syn_A[0].weight = 4.0 }")
        h("a_DB5[0].soma { syn_NC_AVBR_DB5_Generic_GJ_AVBR_to_DB5_elec_syn_B[0].weight = 4.0 }")
        h("setpointer syn_NC_AVBR_DB5_Generic_GJ_AVBR_to_DB5_elec_syn_A[0].vpeer, a_DB5[0].soma.v(0.5)")
        h("setpointer syn_NC_AVBR_DB5_Generic_GJ_AVBR_to_DB5_elec_syn_B[0].vpeer, a_AVBR[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_AVBR_DB6_Generic_GJ
        print("Adding electrical projection: NC_AVBR_DB6_Generic_GJ from AVBR to DB6, with 1 connection(s)")

        h("objectvar syn_NC_AVBR_DB6_Generic_GJ_AVBR_to_DB6_elec_syn_A[1]")
        h("objectvar syn_NC_AVBR_DB6_Generic_GJ_AVBR_to_DB6_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVBR[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DB6[0].soma], weight: 3.0
        h("a_AVBR[0].soma { syn_NC_AVBR_DB6_Generic_GJ_AVBR_to_DB6_elec_syn_A[0] = new AVBR_to_DB6_elec_syn(0.5) }")
        h("a_DB6[0].soma { syn_NC_AVBR_DB6_Generic_GJ_AVBR_to_DB6_elec_syn_B[0] = new AVBR_to_DB6_elec_syn(0.5) }")
        h("a_AVBR[0].soma { syn_NC_AVBR_DB6_Generic_GJ_AVBR_to_DB6_elec_syn_A[0].weight = 3.0 }")
        h("a_DB6[0].soma { syn_NC_AVBR_DB6_Generic_GJ_AVBR_to_DB6_elec_syn_B[0].weight = 3.0 }")
        h("setpointer syn_NC_AVBR_DB6_Generic_GJ_AVBR_to_DB6_elec_syn_A[0].vpeer, a_DB6[0].soma.v(0.5)")
        h("setpointer syn_NC_AVBR_DB6_Generic_GJ_AVBR_to_DB6_elec_syn_B[0].vpeer, a_AVBR[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_AVBR_DB7_Generic_GJ
        print("Adding electrical projection: NC_AVBR_DB7_Generic_GJ from AVBR to DB7, with 1 connection(s)")

        h("objectvar syn_NC_AVBR_DB7_Generic_GJ_AVBR_to_DB7_elec_syn_A[1]")
        h("objectvar syn_NC_AVBR_DB7_Generic_GJ_AVBR_to_DB7_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVBR[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DB7[0].soma], weight: 3.0
        h("a_AVBR[0].soma { syn_NC_AVBR_DB7_Generic_GJ_AVBR_to_DB7_elec_syn_A[0] = new AVBR_to_DB7_elec_syn(0.5) }")
        h("a_DB7[0].soma { syn_NC_AVBR_DB7_Generic_GJ_AVBR_to_DB7_elec_syn_B[0] = new AVBR_to_DB7_elec_syn(0.5) }")
        h("a_AVBR[0].soma { syn_NC_AVBR_DB7_Generic_GJ_AVBR_to_DB7_elec_syn_A[0].weight = 3.0 }")
        h("a_DB7[0].soma { syn_NC_AVBR_DB7_Generic_GJ_AVBR_to_DB7_elec_syn_B[0].weight = 3.0 }")
        h("setpointer syn_NC_AVBR_DB7_Generic_GJ_AVBR_to_DB7_elec_syn_A[0].vpeer, a_DB7[0].soma.v(0.5)")
        h("setpointer syn_NC_AVBR_DB7_Generic_GJ_AVBR_to_DB7_elec_syn_B[0].vpeer, a_AVBR[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_DA1_AVAL_Generic_GJ
        print("Adding electrical projection: NC_DA1_AVAL_Generic_GJ from DA1 to AVAL, with 1 connection(s)")

        h("objectvar syn_NC_DA1_AVAL_Generic_GJ_DA1_to_AVAL_elec_syn_A[1]")
        h("objectvar syn_NC_DA1_AVAL_Generic_GJ_DA1_to_AVAL_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DA1[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVAL[0].soma], weight: 2.0
        h("a_DA1[0].soma { syn_NC_DA1_AVAL_Generic_GJ_DA1_to_AVAL_elec_syn_A[0] = new DA1_to_AVAL_elec_syn(0.5) }")
        h("a_AVAL[0].soma { syn_NC_DA1_AVAL_Generic_GJ_DA1_to_AVAL_elec_syn_B[0] = new DA1_to_AVAL_elec_syn(0.5) }")
        h("a_DA1[0].soma { syn_NC_DA1_AVAL_Generic_GJ_DA1_to_AVAL_elec_syn_A[0].weight = 2.0 }")
        h("a_AVAL[0].soma { syn_NC_DA1_AVAL_Generic_GJ_DA1_to_AVAL_elec_syn_B[0].weight = 2.0 }")
        h("setpointer syn_NC_DA1_AVAL_Generic_GJ_DA1_to_AVAL_elec_syn_A[0].vpeer, a_AVAL[0].soma.v(0.5)")
        h("setpointer syn_NC_DA1_AVAL_Generic_GJ_DA1_to_AVAL_elec_syn_B[0].vpeer, a_DA1[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_DA1_AVAR_Generic_GJ
        print("Adding electrical projection: NC_DA1_AVAR_Generic_GJ from DA1 to AVAR, with 1 connection(s)")

        h("objectvar syn_NC_DA1_AVAR_Generic_GJ_DA1_to_AVAR_elec_syn_A[1]")
        h("objectvar syn_NC_DA1_AVAR_Generic_GJ_DA1_to_AVAR_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DA1[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVAR[0].soma], weight: 9.0
        h("a_DA1[0].soma { syn_NC_DA1_AVAR_Generic_GJ_DA1_to_AVAR_elec_syn_A[0] = new DA1_to_AVAR_elec_syn(0.5) }")
        h("a_AVAR[0].soma { syn_NC_DA1_AVAR_Generic_GJ_DA1_to_AVAR_elec_syn_B[0] = new DA1_to_AVAR_elec_syn(0.5) }")
        h("a_DA1[0].soma { syn_NC_DA1_AVAR_Generic_GJ_DA1_to_AVAR_elec_syn_A[0].weight = 9.0 }")
        h("a_AVAR[0].soma { syn_NC_DA1_AVAR_Generic_GJ_DA1_to_AVAR_elec_syn_B[0].weight = 9.0 }")
        h("setpointer syn_NC_DA1_AVAR_Generic_GJ_DA1_to_AVAR_elec_syn_A[0].vpeer, a_AVAR[0].soma.v(0.5)")
        h("setpointer syn_NC_DA1_AVAR_Generic_GJ_DA1_to_AVAR_elec_syn_B[0].vpeer, a_DA1[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_DA2_AVAL_Generic_GJ
        print("Adding electrical projection: NC_DA2_AVAL_Generic_GJ from DA2 to AVAL, with 1 connection(s)")

        h("objectvar syn_NC_DA2_AVAL_Generic_GJ_DA2_to_AVAL_elec_syn_A[1]")
        h("objectvar syn_NC_DA2_AVAL_Generic_GJ_DA2_to_AVAL_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DA2[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVAL[0].soma], weight: 7.0
        h("a_DA2[0].soma { syn_NC_DA2_AVAL_Generic_GJ_DA2_to_AVAL_elec_syn_A[0] = new DA2_to_AVAL_elec_syn(0.5) }")
        h("a_AVAL[0].soma { syn_NC_DA2_AVAL_Generic_GJ_DA2_to_AVAL_elec_syn_B[0] = new DA2_to_AVAL_elec_syn(0.5) }")
        h("a_DA2[0].soma { syn_NC_DA2_AVAL_Generic_GJ_DA2_to_AVAL_elec_syn_A[0].weight = 7.0 }")
        h("a_AVAL[0].soma { syn_NC_DA2_AVAL_Generic_GJ_DA2_to_AVAL_elec_syn_B[0].weight = 7.0 }")
        h("setpointer syn_NC_DA2_AVAL_Generic_GJ_DA2_to_AVAL_elec_syn_A[0].vpeer, a_AVAL[0].soma.v(0.5)")
        h("setpointer syn_NC_DA2_AVAL_Generic_GJ_DA2_to_AVAL_elec_syn_B[0].vpeer, a_DA2[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_DA2_AVAR_Generic_GJ
        print("Adding electrical projection: NC_DA2_AVAR_Generic_GJ from DA2 to AVAR, with 1 connection(s)")

        h("objectvar syn_NC_DA2_AVAR_Generic_GJ_DA2_to_AVAR_elec_syn_A[1]")
        h("objectvar syn_NC_DA2_AVAR_Generic_GJ_DA2_to_AVAR_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DA2[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVAR[0].soma], weight: 3.0
        h("a_DA2[0].soma { syn_NC_DA2_AVAR_Generic_GJ_DA2_to_AVAR_elec_syn_A[0] = new DA2_to_AVAR_elec_syn(0.5) }")
        h("a_AVAR[0].soma { syn_NC_DA2_AVAR_Generic_GJ_DA2_to_AVAR_elec_syn_B[0] = new DA2_to_AVAR_elec_syn(0.5) }")
        h("a_DA2[0].soma { syn_NC_DA2_AVAR_Generic_GJ_DA2_to_AVAR_elec_syn_A[0].weight = 3.0 }")
        h("a_AVAR[0].soma { syn_NC_DA2_AVAR_Generic_GJ_DA2_to_AVAR_elec_syn_B[0].weight = 3.0 }")
        h("setpointer syn_NC_DA2_AVAR_Generic_GJ_DA2_to_AVAR_elec_syn_A[0].vpeer, a_AVAR[0].soma.v(0.5)")
        h("setpointer syn_NC_DA2_AVAR_Generic_GJ_DA2_to_AVAR_elec_syn_B[0].vpeer, a_DA2[0].soma.v(0.5)")

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

        # ######################   Electrical Projection: NC_DA4_AVAL_Generic_GJ
        print("Adding electrical projection: NC_DA4_AVAL_Generic_GJ from DA4 to AVAL, with 1 connection(s)")

        h("objectvar syn_NC_DA4_AVAL_Generic_GJ_DA4_to_AVAL_elec_syn_A[1]")
        h("objectvar syn_NC_DA4_AVAL_Generic_GJ_DA4_to_AVAL_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DA4[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVAL[0].soma], weight: 2.0
        h("a_DA4[0].soma { syn_NC_DA4_AVAL_Generic_GJ_DA4_to_AVAL_elec_syn_A[0] = new DA4_to_AVAL_elec_syn(0.5) }")
        h("a_AVAL[0].soma { syn_NC_DA4_AVAL_Generic_GJ_DA4_to_AVAL_elec_syn_B[0] = new DA4_to_AVAL_elec_syn(0.5) }")
        h("a_DA4[0].soma { syn_NC_DA4_AVAL_Generic_GJ_DA4_to_AVAL_elec_syn_A[0].weight = 2.0 }")
        h("a_AVAL[0].soma { syn_NC_DA4_AVAL_Generic_GJ_DA4_to_AVAL_elec_syn_B[0].weight = 2.0 }")
        h("setpointer syn_NC_DA4_AVAL_Generic_GJ_DA4_to_AVAL_elec_syn_A[0].vpeer, a_AVAL[0].soma.v(0.5)")
        h("setpointer syn_NC_DA4_AVAL_Generic_GJ_DA4_to_AVAL_elec_syn_B[0].vpeer, a_DA4[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_DA4_AVAR_Generic_GJ
        print("Adding electrical projection: NC_DA4_AVAR_Generic_GJ from DA4 to AVAR, with 1 connection(s)")

        h("objectvar syn_NC_DA4_AVAR_Generic_GJ_DA4_to_AVAR_elec_syn_A[1]")
        h("objectvar syn_NC_DA4_AVAR_Generic_GJ_DA4_to_AVAR_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DA4[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVAR[0].soma], weight: 2.0
        h("a_DA4[0].soma { syn_NC_DA4_AVAR_Generic_GJ_DA4_to_AVAR_elec_syn_A[0] = new DA4_to_AVAR_elec_syn(0.5) }")
        h("a_AVAR[0].soma { syn_NC_DA4_AVAR_Generic_GJ_DA4_to_AVAR_elec_syn_B[0] = new DA4_to_AVAR_elec_syn(0.5) }")
        h("a_DA4[0].soma { syn_NC_DA4_AVAR_Generic_GJ_DA4_to_AVAR_elec_syn_A[0].weight = 2.0 }")
        h("a_AVAR[0].soma { syn_NC_DA4_AVAR_Generic_GJ_DA4_to_AVAR_elec_syn_B[0].weight = 2.0 }")
        h("setpointer syn_NC_DA4_AVAR_Generic_GJ_DA4_to_AVAR_elec_syn_A[0].vpeer, a_AVAR[0].soma.v(0.5)")
        h("setpointer syn_NC_DA4_AVAR_Generic_GJ_DA4_to_AVAR_elec_syn_B[0].vpeer, a_DA4[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_DA5_AVAL_Generic_GJ
        print("Adding electrical projection: NC_DA5_AVAL_Generic_GJ from DA5 to AVAL, with 1 connection(s)")

        h("objectvar syn_NC_DA5_AVAL_Generic_GJ_DA5_to_AVAL_elec_syn_A[1]")
        h("objectvar syn_NC_DA5_AVAL_Generic_GJ_DA5_to_AVAL_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DA5[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVAL[0].soma], weight: 2.0
        h("a_DA5[0].soma { syn_NC_DA5_AVAL_Generic_GJ_DA5_to_AVAL_elec_syn_A[0] = new DA5_to_AVAL_elec_syn(0.5) }")
        h("a_AVAL[0].soma { syn_NC_DA5_AVAL_Generic_GJ_DA5_to_AVAL_elec_syn_B[0] = new DA5_to_AVAL_elec_syn(0.5) }")
        h("a_DA5[0].soma { syn_NC_DA5_AVAL_Generic_GJ_DA5_to_AVAL_elec_syn_A[0].weight = 2.0 }")
        h("a_AVAL[0].soma { syn_NC_DA5_AVAL_Generic_GJ_DA5_to_AVAL_elec_syn_B[0].weight = 2.0 }")
        h("setpointer syn_NC_DA5_AVAL_Generic_GJ_DA5_to_AVAL_elec_syn_A[0].vpeer, a_AVAL[0].soma.v(0.5)")
        h("setpointer syn_NC_DA5_AVAL_Generic_GJ_DA5_to_AVAL_elec_syn_B[0].vpeer, a_DA5[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_DA5_AVAR_Generic_GJ
        print("Adding electrical projection: NC_DA5_AVAR_Generic_GJ from DA5 to AVAR, with 1 connection(s)")

        h("objectvar syn_NC_DA5_AVAR_Generic_GJ_DA5_to_AVAR_elec_syn_A[1]")
        h("objectvar syn_NC_DA5_AVAR_Generic_GJ_DA5_to_AVAR_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DA5[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVAR[0].soma], weight: 5.0
        h("a_DA5[0].soma { syn_NC_DA5_AVAR_Generic_GJ_DA5_to_AVAR_elec_syn_A[0] = new DA5_to_AVAR_elec_syn(0.5) }")
        h("a_AVAR[0].soma { syn_NC_DA5_AVAR_Generic_GJ_DA5_to_AVAR_elec_syn_B[0] = new DA5_to_AVAR_elec_syn(0.5) }")
        h("a_DA5[0].soma { syn_NC_DA5_AVAR_Generic_GJ_DA5_to_AVAR_elec_syn_A[0].weight = 5.0 }")
        h("a_AVAR[0].soma { syn_NC_DA5_AVAR_Generic_GJ_DA5_to_AVAR_elec_syn_B[0].weight = 5.0 }")
        h("setpointer syn_NC_DA5_AVAR_Generic_GJ_DA5_to_AVAR_elec_syn_A[0].vpeer, a_AVAR[0].soma.v(0.5)")
        h("setpointer syn_NC_DA5_AVAR_Generic_GJ_DA5_to_AVAR_elec_syn_B[0].vpeer, a_DA5[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_DA6_AVAL_Generic_GJ
        print("Adding electrical projection: NC_DA6_AVAL_Generic_GJ from DA6 to AVAL, with 1 connection(s)")

        h("objectvar syn_NC_DA6_AVAL_Generic_GJ_DA6_to_AVAL_elec_syn_A[1]")
        h("objectvar syn_NC_DA6_AVAL_Generic_GJ_DA6_to_AVAL_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DA6[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVAL[0].soma], weight: 4.0
        h("a_DA6[0].soma { syn_NC_DA6_AVAL_Generic_GJ_DA6_to_AVAL_elec_syn_A[0] = new DA6_to_AVAL_elec_syn(0.5) }")
        h("a_AVAL[0].soma { syn_NC_DA6_AVAL_Generic_GJ_DA6_to_AVAL_elec_syn_B[0] = new DA6_to_AVAL_elec_syn(0.5) }")
        h("a_DA6[0].soma { syn_NC_DA6_AVAL_Generic_GJ_DA6_to_AVAL_elec_syn_A[0].weight = 4.0 }")
        h("a_AVAL[0].soma { syn_NC_DA6_AVAL_Generic_GJ_DA6_to_AVAL_elec_syn_B[0].weight = 4.0 }")
        h("setpointer syn_NC_DA6_AVAL_Generic_GJ_DA6_to_AVAL_elec_syn_A[0].vpeer, a_AVAL[0].soma.v(0.5)")
        h("setpointer syn_NC_DA6_AVAL_Generic_GJ_DA6_to_AVAL_elec_syn_B[0].vpeer, a_DA6[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_DA6_AVAR_Generic_GJ
        print("Adding electrical projection: NC_DA6_AVAR_Generic_GJ from DA6 to AVAR, with 1 connection(s)")

        h("objectvar syn_NC_DA6_AVAR_Generic_GJ_DA6_to_AVAR_elec_syn_A[1]")
        h("objectvar syn_NC_DA6_AVAR_Generic_GJ_DA6_to_AVAR_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DA6[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVAR[0].soma], weight: 4.0
        h("a_DA6[0].soma { syn_NC_DA6_AVAR_Generic_GJ_DA6_to_AVAR_elec_syn_A[0] = new DA6_to_AVAR_elec_syn(0.5) }")
        h("a_AVAR[0].soma { syn_NC_DA6_AVAR_Generic_GJ_DA6_to_AVAR_elec_syn_B[0] = new DA6_to_AVAR_elec_syn(0.5) }")
        h("a_DA6[0].soma { syn_NC_DA6_AVAR_Generic_GJ_DA6_to_AVAR_elec_syn_A[0].weight = 4.0 }")
        h("a_AVAR[0].soma { syn_NC_DA6_AVAR_Generic_GJ_DA6_to_AVAR_elec_syn_B[0].weight = 4.0 }")
        h("setpointer syn_NC_DA6_AVAR_Generic_GJ_DA6_to_AVAR_elec_syn_A[0].vpeer, a_AVAR[0].soma.v(0.5)")
        h("setpointer syn_NC_DA6_AVAR_Generic_GJ_DA6_to_AVAR_elec_syn_B[0].vpeer, a_DA6[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_DA7_AVAL_Generic_GJ
        print("Adding electrical projection: NC_DA7_AVAL_Generic_GJ from DA7 to AVAL, with 1 connection(s)")

        h("objectvar syn_NC_DA7_AVAL_Generic_GJ_DA7_to_AVAL_elec_syn_A[1]")
        h("objectvar syn_NC_DA7_AVAL_Generic_GJ_DA7_to_AVAL_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DA7[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVAL[0].soma], weight: 10.0
        h("a_DA7[0].soma { syn_NC_DA7_AVAL_Generic_GJ_DA7_to_AVAL_elec_syn_A[0] = new DA7_to_AVAL_elec_syn(0.5) }")
        h("a_AVAL[0].soma { syn_NC_DA7_AVAL_Generic_GJ_DA7_to_AVAL_elec_syn_B[0] = new DA7_to_AVAL_elec_syn(0.5) }")
        h("a_DA7[0].soma { syn_NC_DA7_AVAL_Generic_GJ_DA7_to_AVAL_elec_syn_A[0].weight = 10.0 }")
        h("a_AVAL[0].soma { syn_NC_DA7_AVAL_Generic_GJ_DA7_to_AVAL_elec_syn_B[0].weight = 10.0 }")
        h("setpointer syn_NC_DA7_AVAL_Generic_GJ_DA7_to_AVAL_elec_syn_A[0].vpeer, a_AVAL[0].soma.v(0.5)")
        h("setpointer syn_NC_DA7_AVAL_Generic_GJ_DA7_to_AVAL_elec_syn_B[0].vpeer, a_DA7[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_DA8_AVAL_Generic_GJ
        print("Adding electrical projection: NC_DA8_AVAL_Generic_GJ from DA8 to AVAL, with 1 connection(s)")

        h("objectvar syn_NC_DA8_AVAL_Generic_GJ_DA8_to_AVAL_elec_syn_A[1]")
        h("objectvar syn_NC_DA8_AVAL_Generic_GJ_DA8_to_AVAL_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DA8[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVAL[0].soma], weight: 8.0
        h("a_DA8[0].soma { syn_NC_DA8_AVAL_Generic_GJ_DA8_to_AVAL_elec_syn_A[0] = new DA8_to_AVAL_elec_syn(0.5) }")
        h("a_AVAL[0].soma { syn_NC_DA8_AVAL_Generic_GJ_DA8_to_AVAL_elec_syn_B[0] = new DA8_to_AVAL_elec_syn(0.5) }")
        h("a_DA8[0].soma { syn_NC_DA8_AVAL_Generic_GJ_DA8_to_AVAL_elec_syn_A[0].weight = 8.0 }")
        h("a_AVAL[0].soma { syn_NC_DA8_AVAL_Generic_GJ_DA8_to_AVAL_elec_syn_B[0].weight = 8.0 }")
        h("setpointer syn_NC_DA8_AVAL_Generic_GJ_DA8_to_AVAL_elec_syn_A[0].vpeer, a_AVAL[0].soma.v(0.5)")
        h("setpointer syn_NC_DA8_AVAL_Generic_GJ_DA8_to_AVAL_elec_syn_B[0].vpeer, a_DA8[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_DA8_AVAR_Generic_GJ
        print("Adding electrical projection: NC_DA8_AVAR_Generic_GJ from DA8 to AVAR, with 1 connection(s)")

        h("objectvar syn_NC_DA8_AVAR_Generic_GJ_DA8_to_AVAR_elec_syn_A[1]")
        h("objectvar syn_NC_DA8_AVAR_Generic_GJ_DA8_to_AVAR_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DA8[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVAR[0].soma], weight: 5.0
        h("a_DA8[0].soma { syn_NC_DA8_AVAR_Generic_GJ_DA8_to_AVAR_elec_syn_A[0] = new DA8_to_AVAR_elec_syn(0.5) }")
        h("a_AVAR[0].soma { syn_NC_DA8_AVAR_Generic_GJ_DA8_to_AVAR_elec_syn_B[0] = new DA8_to_AVAR_elec_syn(0.5) }")
        h("a_DA8[0].soma { syn_NC_DA8_AVAR_Generic_GJ_DA8_to_AVAR_elec_syn_A[0].weight = 5.0 }")
        h("a_AVAR[0].soma { syn_NC_DA8_AVAR_Generic_GJ_DA8_to_AVAR_elec_syn_B[0].weight = 5.0 }")
        h("setpointer syn_NC_DA8_AVAR_Generic_GJ_DA8_to_AVAR_elec_syn_A[0].vpeer, a_AVAR[0].soma.v(0.5)")
        h("setpointer syn_NC_DA8_AVAR_Generic_GJ_DA8_to_AVAR_elec_syn_B[0].vpeer, a_DA8[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_DA9_AVAL_Generic_GJ
        print("Adding electrical projection: NC_DA9_AVAL_Generic_GJ from DA9 to AVAL, with 1 connection(s)")

        h("objectvar syn_NC_DA9_AVAL_Generic_GJ_DA9_to_AVAL_elec_syn_A[1]")
        h("objectvar syn_NC_DA9_AVAL_Generic_GJ_DA9_to_AVAL_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DA9[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVAL[0].soma], weight: 1.0
        h("a_DA9[0].soma { syn_NC_DA9_AVAL_Generic_GJ_DA9_to_AVAL_elec_syn_A[0] = new DA9_to_AVAL_elec_syn(0.5) }")
        h("a_AVAL[0].soma { syn_NC_DA9_AVAL_Generic_GJ_DA9_to_AVAL_elec_syn_B[0] = new DA9_to_AVAL_elec_syn(0.5) }")
        h("setpointer syn_NC_DA9_AVAL_Generic_GJ_DA9_to_AVAL_elec_syn_A[0].vpeer, a_AVAL[0].soma.v(0.5)")
        h("setpointer syn_NC_DA9_AVAL_Generic_GJ_DA9_to_AVAL_elec_syn_B[0].vpeer, a_DA9[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_DA9_AVAR_Generic_GJ
        print("Adding electrical projection: NC_DA9_AVAR_Generic_GJ from DA9 to AVAR, with 1 connection(s)")

        h("objectvar syn_NC_DA9_AVAR_Generic_GJ_DA9_to_AVAR_elec_syn_A[1]")
        h("objectvar syn_NC_DA9_AVAR_Generic_GJ_DA9_to_AVAR_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DA9[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVAR[0].soma], weight: 4.0
        h("a_DA9[0].soma { syn_NC_DA9_AVAR_Generic_GJ_DA9_to_AVAR_elec_syn_A[0] = new DA9_to_AVAR_elec_syn(0.5) }")
        h("a_AVAR[0].soma { syn_NC_DA9_AVAR_Generic_GJ_DA9_to_AVAR_elec_syn_B[0] = new DA9_to_AVAR_elec_syn(0.5) }")
        h("a_DA9[0].soma { syn_NC_DA9_AVAR_Generic_GJ_DA9_to_AVAR_elec_syn_A[0].weight = 4.0 }")
        h("a_AVAR[0].soma { syn_NC_DA9_AVAR_Generic_GJ_DA9_to_AVAR_elec_syn_B[0].weight = 4.0 }")
        h("setpointer syn_NC_DA9_AVAR_Generic_GJ_DA9_to_AVAR_elec_syn_A[0].vpeer, a_AVAR[0].soma.v(0.5)")
        h("setpointer syn_NC_DA9_AVAR_Generic_GJ_DA9_to_AVAR_elec_syn_B[0].vpeer, a_DA9[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_DB1_AVBR_Generic_GJ
        print("Adding electrical projection: NC_DB1_AVBR_Generic_GJ from DB1 to AVBR, with 1 connection(s)")

        h("objectvar syn_NC_DB1_AVBR_Generic_GJ_DB1_to_AVBR_elec_syn_A[1]")
        h("objectvar syn_NC_DB1_AVBR_Generic_GJ_DB1_to_AVBR_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB1[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVBR[0].soma], weight: 15.0
        h("a_DB1[0].soma { syn_NC_DB1_AVBR_Generic_GJ_DB1_to_AVBR_elec_syn_A[0] = new DB1_to_AVBR_elec_syn(0.5) }")
        h("a_AVBR[0].soma { syn_NC_DB1_AVBR_Generic_GJ_DB1_to_AVBR_elec_syn_B[0] = new DB1_to_AVBR_elec_syn(0.5) }")
        h("a_DB1[0].soma { syn_NC_DB1_AVBR_Generic_GJ_DB1_to_AVBR_elec_syn_A[0].weight = 15.0 }")
        h("a_AVBR[0].soma { syn_NC_DB1_AVBR_Generic_GJ_DB1_to_AVBR_elec_syn_B[0].weight = 15.0 }")
        h("setpointer syn_NC_DB1_AVBR_Generic_GJ_DB1_to_AVBR_elec_syn_A[0].vpeer, a_AVBR[0].soma.v(0.5)")
        h("setpointer syn_NC_DB1_AVBR_Generic_GJ_DB1_to_AVBR_elec_syn_B[0].vpeer, a_DB1[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_DB2_AVBL_Generic_GJ
        print("Adding electrical projection: NC_DB2_AVBL_Generic_GJ from DB2 to AVBL, with 1 connection(s)")

        h("objectvar syn_NC_DB2_AVBL_Generic_GJ_DB2_to_AVBL_elec_syn_A[1]")
        h("objectvar syn_NC_DB2_AVBL_Generic_GJ_DB2_to_AVBL_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB2[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVBL[0].soma], weight: 4.0
        h("a_DB2[0].soma { syn_NC_DB2_AVBL_Generic_GJ_DB2_to_AVBL_elec_syn_A[0] = new DB2_to_AVBL_elec_syn(0.5) }")
        h("a_AVBL[0].soma { syn_NC_DB2_AVBL_Generic_GJ_DB2_to_AVBL_elec_syn_B[0] = new DB2_to_AVBL_elec_syn(0.5) }")
        h("a_DB2[0].soma { syn_NC_DB2_AVBL_Generic_GJ_DB2_to_AVBL_elec_syn_A[0].weight = 4.0 }")
        h("a_AVBL[0].soma { syn_NC_DB2_AVBL_Generic_GJ_DB2_to_AVBL_elec_syn_B[0].weight = 4.0 }")
        h("setpointer syn_NC_DB2_AVBL_Generic_GJ_DB2_to_AVBL_elec_syn_A[0].vpeer, a_AVBL[0].soma.v(0.5)")
        h("setpointer syn_NC_DB2_AVBL_Generic_GJ_DB2_to_AVBL_elec_syn_B[0].vpeer, a_DB2[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_DB2_AVBR_Generic_GJ
        print("Adding electrical projection: NC_DB2_AVBR_Generic_GJ from DB2 to AVBR, with 1 connection(s)")

        h("objectvar syn_NC_DB2_AVBR_Generic_GJ_DB2_to_AVBR_elec_syn_A[1]")
        h("objectvar syn_NC_DB2_AVBR_Generic_GJ_DB2_to_AVBR_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB2[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVBR[0].soma], weight: 3.0
        h("a_DB2[0].soma { syn_NC_DB2_AVBR_Generic_GJ_DB2_to_AVBR_elec_syn_A[0] = new DB2_to_AVBR_elec_syn(0.5) }")
        h("a_AVBR[0].soma { syn_NC_DB2_AVBR_Generic_GJ_DB2_to_AVBR_elec_syn_B[0] = new DB2_to_AVBR_elec_syn(0.5) }")
        h("a_DB2[0].soma { syn_NC_DB2_AVBR_Generic_GJ_DB2_to_AVBR_elec_syn_A[0].weight = 3.0 }")
        h("a_AVBR[0].soma { syn_NC_DB2_AVBR_Generic_GJ_DB2_to_AVBR_elec_syn_B[0].weight = 3.0 }")
        h("setpointer syn_NC_DB2_AVBR_Generic_GJ_DB2_to_AVBR_elec_syn_A[0].vpeer, a_AVBR[0].soma.v(0.5)")
        h("setpointer syn_NC_DB2_AVBR_Generic_GJ_DB2_to_AVBR_elec_syn_B[0].vpeer, a_DB2[0].soma.v(0.5)")

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

        # ######################   Electrical Projection: NC_DB4_AVBL_Generic_GJ
        print("Adding electrical projection: NC_DB4_AVBL_Generic_GJ from DB4 to AVBL, with 1 connection(s)")

        h("objectvar syn_NC_DB4_AVBL_Generic_GJ_DB4_to_AVBL_elec_syn_A[1]")
        h("objectvar syn_NC_DB4_AVBL_Generic_GJ_DB4_to_AVBL_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB4[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVBL[0].soma], weight: 4.0
        h("a_DB4[0].soma { syn_NC_DB4_AVBL_Generic_GJ_DB4_to_AVBL_elec_syn_A[0] = new DB4_to_AVBL_elec_syn(0.5) }")
        h("a_AVBL[0].soma { syn_NC_DB4_AVBL_Generic_GJ_DB4_to_AVBL_elec_syn_B[0] = new DB4_to_AVBL_elec_syn(0.5) }")
        h("a_DB4[0].soma { syn_NC_DB4_AVBL_Generic_GJ_DB4_to_AVBL_elec_syn_A[0].weight = 4.0 }")
        h("a_AVBL[0].soma { syn_NC_DB4_AVBL_Generic_GJ_DB4_to_AVBL_elec_syn_B[0].weight = 4.0 }")
        h("setpointer syn_NC_DB4_AVBL_Generic_GJ_DB4_to_AVBL_elec_syn_A[0].vpeer, a_AVBL[0].soma.v(0.5)")
        h("setpointer syn_NC_DB4_AVBL_Generic_GJ_DB4_to_AVBL_elec_syn_B[0].vpeer, a_DB4[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_DB4_AVBR_Generic_GJ
        print("Adding electrical projection: NC_DB4_AVBR_Generic_GJ from DB4 to AVBR, with 1 connection(s)")

        h("objectvar syn_NC_DB4_AVBR_Generic_GJ_DB4_to_AVBR_elec_syn_A[1]")
        h("objectvar syn_NC_DB4_AVBR_Generic_GJ_DB4_to_AVBR_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB4[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVBR[0].soma], weight: 5.0
        h("a_DB4[0].soma { syn_NC_DB4_AVBR_Generic_GJ_DB4_to_AVBR_elec_syn_A[0] = new DB4_to_AVBR_elec_syn(0.5) }")
        h("a_AVBR[0].soma { syn_NC_DB4_AVBR_Generic_GJ_DB4_to_AVBR_elec_syn_B[0] = new DB4_to_AVBR_elec_syn(0.5) }")
        h("a_DB4[0].soma { syn_NC_DB4_AVBR_Generic_GJ_DB4_to_AVBR_elec_syn_A[0].weight = 5.0 }")
        h("a_AVBR[0].soma { syn_NC_DB4_AVBR_Generic_GJ_DB4_to_AVBR_elec_syn_B[0].weight = 5.0 }")
        h("setpointer syn_NC_DB4_AVBR_Generic_GJ_DB4_to_AVBR_elec_syn_A[0].vpeer, a_AVBR[0].soma.v(0.5)")
        h("setpointer syn_NC_DB4_AVBR_Generic_GJ_DB4_to_AVBR_elec_syn_B[0].vpeer, a_DB4[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_DB5_AVBL_Generic_GJ
        print("Adding electrical projection: NC_DB5_AVBL_Generic_GJ from DB5 to AVBL, with 1 connection(s)")

        h("objectvar syn_NC_DB5_AVBL_Generic_GJ_DB5_to_AVBL_elec_syn_A[1]")
        h("objectvar syn_NC_DB5_AVBL_Generic_GJ_DB5_to_AVBL_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB5[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVBL[0].soma], weight: 3.0
        h("a_DB5[0].soma { syn_NC_DB5_AVBL_Generic_GJ_DB5_to_AVBL_elec_syn_A[0] = new DB5_to_AVBL_elec_syn(0.5) }")
        h("a_AVBL[0].soma { syn_NC_DB5_AVBL_Generic_GJ_DB5_to_AVBL_elec_syn_B[0] = new DB5_to_AVBL_elec_syn(0.5) }")
        h("a_DB5[0].soma { syn_NC_DB5_AVBL_Generic_GJ_DB5_to_AVBL_elec_syn_A[0].weight = 3.0 }")
        h("a_AVBL[0].soma { syn_NC_DB5_AVBL_Generic_GJ_DB5_to_AVBL_elec_syn_B[0].weight = 3.0 }")
        h("setpointer syn_NC_DB5_AVBL_Generic_GJ_DB5_to_AVBL_elec_syn_A[0].vpeer, a_AVBL[0].soma.v(0.5)")
        h("setpointer syn_NC_DB5_AVBL_Generic_GJ_DB5_to_AVBL_elec_syn_B[0].vpeer, a_DB5[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_DB5_AVBR_Generic_GJ
        print("Adding electrical projection: NC_DB5_AVBR_Generic_GJ from DB5 to AVBR, with 1 connection(s)")

        h("objectvar syn_NC_DB5_AVBR_Generic_GJ_DB5_to_AVBR_elec_syn_A[1]")
        h("objectvar syn_NC_DB5_AVBR_Generic_GJ_DB5_to_AVBR_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB5[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVBR[0].soma], weight: 4.0
        h("a_DB5[0].soma { syn_NC_DB5_AVBR_Generic_GJ_DB5_to_AVBR_elec_syn_A[0] = new DB5_to_AVBR_elec_syn(0.5) }")
        h("a_AVBR[0].soma { syn_NC_DB5_AVBR_Generic_GJ_DB5_to_AVBR_elec_syn_B[0] = new DB5_to_AVBR_elec_syn(0.5) }")
        h("a_DB5[0].soma { syn_NC_DB5_AVBR_Generic_GJ_DB5_to_AVBR_elec_syn_A[0].weight = 4.0 }")
        h("a_AVBR[0].soma { syn_NC_DB5_AVBR_Generic_GJ_DB5_to_AVBR_elec_syn_B[0].weight = 4.0 }")
        h("setpointer syn_NC_DB5_AVBR_Generic_GJ_DB5_to_AVBR_elec_syn_A[0].vpeer, a_AVBR[0].soma.v(0.5)")
        h("setpointer syn_NC_DB5_AVBR_Generic_GJ_DB5_to_AVBR_elec_syn_B[0].vpeer, a_DB5[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_DB6_AVBL_Generic_GJ
        print("Adding electrical projection: NC_DB6_AVBL_Generic_GJ from DB6 to AVBL, with 1 connection(s)")

        h("objectvar syn_NC_DB6_AVBL_Generic_GJ_DB6_to_AVBL_elec_syn_A[1]")
        h("objectvar syn_NC_DB6_AVBL_Generic_GJ_DB6_to_AVBL_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB6[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVBL[0].soma], weight: 3.0
        h("a_DB6[0].soma { syn_NC_DB6_AVBL_Generic_GJ_DB6_to_AVBL_elec_syn_A[0] = new DB6_to_AVBL_elec_syn(0.5) }")
        h("a_AVBL[0].soma { syn_NC_DB6_AVBL_Generic_GJ_DB6_to_AVBL_elec_syn_B[0] = new DB6_to_AVBL_elec_syn(0.5) }")
        h("a_DB6[0].soma { syn_NC_DB6_AVBL_Generic_GJ_DB6_to_AVBL_elec_syn_A[0].weight = 3.0 }")
        h("a_AVBL[0].soma { syn_NC_DB6_AVBL_Generic_GJ_DB6_to_AVBL_elec_syn_B[0].weight = 3.0 }")
        h("setpointer syn_NC_DB6_AVBL_Generic_GJ_DB6_to_AVBL_elec_syn_A[0].vpeer, a_AVBL[0].soma.v(0.5)")
        h("setpointer syn_NC_DB6_AVBL_Generic_GJ_DB6_to_AVBL_elec_syn_B[0].vpeer, a_DB6[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_DB6_AVBR_Generic_GJ
        print("Adding electrical projection: NC_DB6_AVBR_Generic_GJ from DB6 to AVBR, with 1 connection(s)")

        h("objectvar syn_NC_DB6_AVBR_Generic_GJ_DB6_to_AVBR_elec_syn_A[1]")
        h("objectvar syn_NC_DB6_AVBR_Generic_GJ_DB6_to_AVBR_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB6[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVBR[0].soma], weight: 4.0
        h("a_DB6[0].soma { syn_NC_DB6_AVBR_Generic_GJ_DB6_to_AVBR_elec_syn_A[0] = new DB6_to_AVBR_elec_syn(0.5) }")
        h("a_AVBR[0].soma { syn_NC_DB6_AVBR_Generic_GJ_DB6_to_AVBR_elec_syn_B[0] = new DB6_to_AVBR_elec_syn(0.5) }")
        h("a_DB6[0].soma { syn_NC_DB6_AVBR_Generic_GJ_DB6_to_AVBR_elec_syn_A[0].weight = 4.0 }")
        h("a_AVBR[0].soma { syn_NC_DB6_AVBR_Generic_GJ_DB6_to_AVBR_elec_syn_B[0].weight = 4.0 }")
        h("setpointer syn_NC_DB6_AVBR_Generic_GJ_DB6_to_AVBR_elec_syn_A[0].vpeer, a_AVBR[0].soma.v(0.5)")
        h("setpointer syn_NC_DB6_AVBR_Generic_GJ_DB6_to_AVBR_elec_syn_B[0].vpeer, a_DB6[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_DB7_AVBL_Generic_GJ
        print("Adding electrical projection: NC_DB7_AVBL_Generic_GJ from DB7 to AVBL, with 1 connection(s)")

        h("objectvar syn_NC_DB7_AVBL_Generic_GJ_DB7_to_AVBL_elec_syn_A[1]")
        h("objectvar syn_NC_DB7_AVBL_Generic_GJ_DB7_to_AVBL_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB7[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVBL[0].soma], weight: 13.0
        h("a_DB7[0].soma { syn_NC_DB7_AVBL_Generic_GJ_DB7_to_AVBL_elec_syn_A[0] = new DB7_to_AVBL_elec_syn(0.5) }")
        h("a_AVBL[0].soma { syn_NC_DB7_AVBL_Generic_GJ_DB7_to_AVBL_elec_syn_B[0] = new DB7_to_AVBL_elec_syn(0.5) }")
        h("a_DB7[0].soma { syn_NC_DB7_AVBL_Generic_GJ_DB7_to_AVBL_elec_syn_A[0].weight = 13.0 }")
        h("a_AVBL[0].soma { syn_NC_DB7_AVBL_Generic_GJ_DB7_to_AVBL_elec_syn_B[0].weight = 13.0 }")
        h("setpointer syn_NC_DB7_AVBL_Generic_GJ_DB7_to_AVBL_elec_syn_A[0].vpeer, a_AVBL[0].soma.v(0.5)")
        h("setpointer syn_NC_DB7_AVBL_Generic_GJ_DB7_to_AVBL_elec_syn_B[0].vpeer, a_DB7[0].soma.v(0.5)")

        # ######################   Electrical Projection: NC_DB7_AVBR_Generic_GJ
        print("Adding electrical projection: NC_DB7_AVBR_Generic_GJ from DB7 to AVBR, with 1 connection(s)")

        h("objectvar syn_NC_DB7_AVBR_Generic_GJ_DB7_to_AVBR_elec_syn_A[1]")
        h("objectvar syn_NC_DB7_AVBR_Generic_GJ_DB7_to_AVBR_elec_syn_B[1]")

        # Elect Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB7[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AVBR[0].soma], weight: 3.0
        h("a_DB7[0].soma { syn_NC_DB7_AVBR_Generic_GJ_DB7_to_AVBR_elec_syn_A[0] = new DB7_to_AVBR_elec_syn(0.5) }")
        h("a_AVBR[0].soma { syn_NC_DB7_AVBR_Generic_GJ_DB7_to_AVBR_elec_syn_B[0] = new DB7_to_AVBR_elec_syn(0.5) }")
        h("a_DB7[0].soma { syn_NC_DB7_AVBR_Generic_GJ_DB7_to_AVBR_elec_syn_A[0].weight = 3.0 }")
        h("a_AVBR[0].soma { syn_NC_DB7_AVBR_Generic_GJ_DB7_to_AVBR_elec_syn_B[0].weight = 3.0 }")
        h("setpointer syn_NC_DB7_AVBR_Generic_GJ_DB7_to_AVBR_elec_syn_A[0].vpeer, a_AVBR[0].soma.v(0.5)")
        h("setpointer syn_NC_DB7_AVBR_Generic_GJ_DB7_to_AVBR_elec_syn_B[0].vpeer, a_DB7[0].soma.v(0.5)")

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

        # ######################   Continuous Projection: NC_AVAL_DA1_Acetylcholine
        print("Adding continuous projection: NC_AVAL_DA1_Acetylcholine from AVAL to DA1, with 1 connection(s)")

        h("objectvar syn_NC_AVAL_DA1_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_AVAL_DA1_Acetylcholine_AVAL_to_DA1_exc_syn_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVAL[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DA1[0].soma], weight: 6.0
        h("a_AVAL[0].soma { syn_NC_AVAL_DA1_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_DA1[0].soma { syn_NC_AVAL_DA1_Acetylcholine_AVAL_to_DA1_exc_syn_post[0] = new AVAL_to_DA1_exc_syn(0.500000) }")
        h("a_AVAL[0].soma { syn_NC_AVAL_DA1_Acetylcholine_silent_pre[0].weight = 6.0 }")
        h("a_DA1[0].soma { syn_NC_AVAL_DA1_Acetylcholine_AVAL_to_DA1_exc_syn_post[0].weight = 6.0 }")
        h("setpointer syn_NC_AVAL_DA1_Acetylcholine_silent_pre[0].vpeer, a_DA1[0].soma.v(0.500000)")
        h("setpointer syn_NC_AVAL_DA1_Acetylcholine_AVAL_to_DA1_exc_syn_post[0].vpeer, a_AVAL[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_AVAL_DA2_Acetylcholine
        print("Adding continuous projection: NC_AVAL_DA2_Acetylcholine from AVAL to DA2, with 1 connection(s)")

        h("objectvar syn_NC_AVAL_DA2_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_AVAL_DA2_Acetylcholine_AVAL_to_DA2_exc_syn_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVAL[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DA2[0].soma], weight: 10.0
        h("a_AVAL[0].soma { syn_NC_AVAL_DA2_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_DA2[0].soma { syn_NC_AVAL_DA2_Acetylcholine_AVAL_to_DA2_exc_syn_post[0] = new AVAL_to_DA2_exc_syn(0.500000) }")
        h("a_AVAL[0].soma { syn_NC_AVAL_DA2_Acetylcholine_silent_pre[0].weight = 10.0 }")
        h("a_DA2[0].soma { syn_NC_AVAL_DA2_Acetylcholine_AVAL_to_DA2_exc_syn_post[0].weight = 10.0 }")
        h("setpointer syn_NC_AVAL_DA2_Acetylcholine_silent_pre[0].vpeer, a_DA2[0].soma.v(0.500000)")
        h("setpointer syn_NC_AVAL_DA2_Acetylcholine_AVAL_to_DA2_exc_syn_post[0].vpeer, a_AVAL[0].soma.v(0.500000)")

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

        # ######################   Continuous Projection: NC_AVAL_DA4_Acetylcholine
        print("Adding continuous projection: NC_AVAL_DA4_Acetylcholine from AVAL to DA4, with 1 connection(s)")

        h("objectvar syn_NC_AVAL_DA4_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_AVAL_DA4_Acetylcholine_AVAL_to_DA4_exc_syn_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVAL[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DA4[0].soma], weight: 12.0
        h("a_AVAL[0].soma { syn_NC_AVAL_DA4_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_DA4[0].soma { syn_NC_AVAL_DA4_Acetylcholine_AVAL_to_DA4_exc_syn_post[0] = new AVAL_to_DA4_exc_syn(0.500000) }")
        h("a_AVAL[0].soma { syn_NC_AVAL_DA4_Acetylcholine_silent_pre[0].weight = 12.0 }")
        h("a_DA4[0].soma { syn_NC_AVAL_DA4_Acetylcholine_AVAL_to_DA4_exc_syn_post[0].weight = 12.0 }")
        h("setpointer syn_NC_AVAL_DA4_Acetylcholine_silent_pre[0].vpeer, a_DA4[0].soma.v(0.500000)")
        h("setpointer syn_NC_AVAL_DA4_Acetylcholine_AVAL_to_DA4_exc_syn_post[0].vpeer, a_AVAL[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_AVAL_DA5_Acetylcholine
        print("Adding continuous projection: NC_AVAL_DA5_Acetylcholine from AVAL to DA5, with 1 connection(s)")

        h("objectvar syn_NC_AVAL_DA5_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_AVAL_DA5_Acetylcholine_AVAL_to_DA5_exc_syn_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVAL[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DA5[0].soma], weight: 14.0
        h("a_AVAL[0].soma { syn_NC_AVAL_DA5_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_DA5[0].soma { syn_NC_AVAL_DA5_Acetylcholine_AVAL_to_DA5_exc_syn_post[0] = new AVAL_to_DA5_exc_syn(0.500000) }")
        h("a_AVAL[0].soma { syn_NC_AVAL_DA5_Acetylcholine_silent_pre[0].weight = 14.0 }")
        h("a_DA5[0].soma { syn_NC_AVAL_DA5_Acetylcholine_AVAL_to_DA5_exc_syn_post[0].weight = 14.0 }")
        h("setpointer syn_NC_AVAL_DA5_Acetylcholine_silent_pre[0].vpeer, a_DA5[0].soma.v(0.500000)")
        h("setpointer syn_NC_AVAL_DA5_Acetylcholine_AVAL_to_DA5_exc_syn_post[0].vpeer, a_AVAL[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_AVAL_DA7_Acetylcholine
        print("Adding continuous projection: NC_AVAL_DA7_Acetylcholine from AVAL to DA7, with 1 connection(s)")

        h("objectvar syn_NC_AVAL_DA7_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_AVAL_DA7_Acetylcholine_AVAL_to_DA7_exc_syn_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVAL[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DA7[0].soma], weight: 4.0
        h("a_AVAL[0].soma { syn_NC_AVAL_DA7_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_DA7[0].soma { syn_NC_AVAL_DA7_Acetylcholine_AVAL_to_DA7_exc_syn_post[0] = new AVAL_to_DA7_exc_syn(0.500000) }")
        h("a_AVAL[0].soma { syn_NC_AVAL_DA7_Acetylcholine_silent_pre[0].weight = 4.0 }")
        h("a_DA7[0].soma { syn_NC_AVAL_DA7_Acetylcholine_AVAL_to_DA7_exc_syn_post[0].weight = 4.0 }")
        h("setpointer syn_NC_AVAL_DA7_Acetylcholine_silent_pre[0].vpeer, a_DA7[0].soma.v(0.500000)")
        h("setpointer syn_NC_AVAL_DA7_Acetylcholine_AVAL_to_DA7_exc_syn_post[0].vpeer, a_AVAL[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_AVAL_DA8_Acetylcholine
        print("Adding continuous projection: NC_AVAL_DA8_Acetylcholine from AVAL to DA8, with 1 connection(s)")

        h("objectvar syn_NC_AVAL_DA8_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_AVAL_DA8_Acetylcholine_AVAL_to_DA8_exc_syn_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVAL[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DA8[0].soma], weight: 5.0
        h("a_AVAL[0].soma { syn_NC_AVAL_DA8_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_DA8[0].soma { syn_NC_AVAL_DA8_Acetylcholine_AVAL_to_DA8_exc_syn_post[0] = new AVAL_to_DA8_exc_syn(0.500000) }")
        h("a_AVAL[0].soma { syn_NC_AVAL_DA8_Acetylcholine_silent_pre[0].weight = 5.0 }")
        h("a_DA8[0].soma { syn_NC_AVAL_DA8_Acetylcholine_AVAL_to_DA8_exc_syn_post[0].weight = 5.0 }")
        h("setpointer syn_NC_AVAL_DA8_Acetylcholine_silent_pre[0].vpeer, a_DA8[0].soma.v(0.500000)")
        h("setpointer syn_NC_AVAL_DA8_Acetylcholine_AVAL_to_DA8_exc_syn_post[0].vpeer, a_AVAL[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_AVAL_DA9_Acetylcholine
        print("Adding continuous projection: NC_AVAL_DA9_Acetylcholine from AVAL to DA9, with 1 connection(s)")

        h("objectvar syn_NC_AVAL_DA9_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_AVAL_DA9_Acetylcholine_AVAL_to_DA9_exc_syn_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVAL[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DA9[0].soma], weight: 3.0
        h("a_AVAL[0].soma { syn_NC_AVAL_DA9_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_DA9[0].soma { syn_NC_AVAL_DA9_Acetylcholine_AVAL_to_DA9_exc_syn_post[0] = new AVAL_to_DA9_exc_syn(0.500000) }")
        h("a_AVAL[0].soma { syn_NC_AVAL_DA9_Acetylcholine_silent_pre[0].weight = 3.0 }")
        h("a_DA9[0].soma { syn_NC_AVAL_DA9_Acetylcholine_AVAL_to_DA9_exc_syn_post[0].weight = 3.0 }")
        h("setpointer syn_NC_AVAL_DA9_Acetylcholine_silent_pre[0].vpeer, a_DA9[0].soma.v(0.500000)")
        h("setpointer syn_NC_AVAL_DA9_Acetylcholine_AVAL_to_DA9_exc_syn_post[0].vpeer, a_AVAL[0].soma.v(0.500000)")

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

        # ######################   Continuous Projection: NC_AVAR_DA1_Acetylcholine
        print("Adding continuous projection: NC_AVAR_DA1_Acetylcholine from AVAR to DA1, with 1 connection(s)")

        h("objectvar syn_NC_AVAR_DA1_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_AVAR_DA1_Acetylcholine_AVAR_to_DA1_exc_syn_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVAR[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DA1[0].soma], weight: 2.0
        h("a_AVAR[0].soma { syn_NC_AVAR_DA1_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_DA1[0].soma { syn_NC_AVAR_DA1_Acetylcholine_AVAR_to_DA1_exc_syn_post[0] = new AVAR_to_DA1_exc_syn(0.500000) }")
        h("a_AVAR[0].soma { syn_NC_AVAR_DA1_Acetylcholine_silent_pre[0].weight = 2.0 }")
        h("a_DA1[0].soma { syn_NC_AVAR_DA1_Acetylcholine_AVAR_to_DA1_exc_syn_post[0].weight = 2.0 }")
        h("setpointer syn_NC_AVAR_DA1_Acetylcholine_silent_pre[0].vpeer, a_DA1[0].soma.v(0.500000)")
        h("setpointer syn_NC_AVAR_DA1_Acetylcholine_AVAR_to_DA1_exc_syn_post[0].vpeer, a_AVAR[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_AVAR_DA2_Acetylcholine
        print("Adding continuous projection: NC_AVAR_DA2_Acetylcholine from AVAR to DA2, with 1 connection(s)")

        h("objectvar syn_NC_AVAR_DA2_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_AVAR_DA2_Acetylcholine_AVAR_to_DA2_exc_syn_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVAR[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DA2[0].soma], weight: 9.0
        h("a_AVAR[0].soma { syn_NC_AVAR_DA2_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_DA2[0].soma { syn_NC_AVAR_DA2_Acetylcholine_AVAR_to_DA2_exc_syn_post[0] = new AVAR_to_DA2_exc_syn(0.500000) }")
        h("a_AVAR[0].soma { syn_NC_AVAR_DA2_Acetylcholine_silent_pre[0].weight = 9.0 }")
        h("a_DA2[0].soma { syn_NC_AVAR_DA2_Acetylcholine_AVAR_to_DA2_exc_syn_post[0].weight = 9.0 }")
        h("setpointer syn_NC_AVAR_DA2_Acetylcholine_silent_pre[0].vpeer, a_DA2[0].soma.v(0.500000)")
        h("setpointer syn_NC_AVAR_DA2_Acetylcholine_AVAR_to_DA2_exc_syn_post[0].vpeer, a_AVAR[0].soma.v(0.500000)")

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

        # ######################   Continuous Projection: NC_AVAR_DA4_Acetylcholine
        print("Adding continuous projection: NC_AVAR_DA4_Acetylcholine from AVAR to DA4, with 1 connection(s)")

        h("objectvar syn_NC_AVAR_DA4_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_AVAR_DA4_Acetylcholine_AVAR_to_DA4_exc_syn_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVAR[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DA4[0].soma], weight: 9.0
        h("a_AVAR[0].soma { syn_NC_AVAR_DA4_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_DA4[0].soma { syn_NC_AVAR_DA4_Acetylcholine_AVAR_to_DA4_exc_syn_post[0] = new AVAR_to_DA4_exc_syn(0.500000) }")
        h("a_AVAR[0].soma { syn_NC_AVAR_DA4_Acetylcholine_silent_pre[0].weight = 9.0 }")
        h("a_DA4[0].soma { syn_NC_AVAR_DA4_Acetylcholine_AVAR_to_DA4_exc_syn_post[0].weight = 9.0 }")
        h("setpointer syn_NC_AVAR_DA4_Acetylcholine_silent_pre[0].vpeer, a_DA4[0].soma.v(0.500000)")
        h("setpointer syn_NC_AVAR_DA4_Acetylcholine_AVAR_to_DA4_exc_syn_post[0].vpeer, a_AVAR[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_AVAR_DA5_Acetylcholine
        print("Adding continuous projection: NC_AVAR_DA5_Acetylcholine from AVAR to DA5, with 1 connection(s)")

        h("objectvar syn_NC_AVAR_DA5_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_AVAR_DA5_Acetylcholine_AVAR_to_DA5_exc_syn_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVAR[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DA5[0].soma], weight: 9.0
        h("a_AVAR[0].soma { syn_NC_AVAR_DA5_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_DA5[0].soma { syn_NC_AVAR_DA5_Acetylcholine_AVAR_to_DA5_exc_syn_post[0] = new AVAR_to_DA5_exc_syn(0.500000) }")
        h("a_AVAR[0].soma { syn_NC_AVAR_DA5_Acetylcholine_silent_pre[0].weight = 9.0 }")
        h("a_DA5[0].soma { syn_NC_AVAR_DA5_Acetylcholine_AVAR_to_DA5_exc_syn_post[0].weight = 9.0 }")
        h("setpointer syn_NC_AVAR_DA5_Acetylcholine_silent_pre[0].vpeer, a_DA5[0].soma.v(0.500000)")
        h("setpointer syn_NC_AVAR_DA5_Acetylcholine_AVAR_to_DA5_exc_syn_post[0].vpeer, a_AVAR[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_AVAR_DA6_Acetylcholine
        print("Adding continuous projection: NC_AVAR_DA6_Acetylcholine from AVAR to DA6, with 1 connection(s)")

        h("objectvar syn_NC_AVAR_DA6_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_AVAR_DA6_Acetylcholine_AVAR_to_DA6_exc_syn_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVAR[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DA6[0].soma], weight: 4.0
        h("a_AVAR[0].soma { syn_NC_AVAR_DA6_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_DA6[0].soma { syn_NC_AVAR_DA6_Acetylcholine_AVAR_to_DA6_exc_syn_post[0] = new AVAR_to_DA6_exc_syn(0.500000) }")
        h("a_AVAR[0].soma { syn_NC_AVAR_DA6_Acetylcholine_silent_pre[0].weight = 4.0 }")
        h("a_DA6[0].soma { syn_NC_AVAR_DA6_Acetylcholine_AVAR_to_DA6_exc_syn_post[0].weight = 4.0 }")
        h("setpointer syn_NC_AVAR_DA6_Acetylcholine_silent_pre[0].vpeer, a_DA6[0].soma.v(0.500000)")
        h("setpointer syn_NC_AVAR_DA6_Acetylcholine_AVAR_to_DA6_exc_syn_post[0].vpeer, a_AVAR[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_AVAR_DA7_Acetylcholine
        print("Adding continuous projection: NC_AVAR_DA7_Acetylcholine from AVAR to DA7, with 1 connection(s)")

        h("objectvar syn_NC_AVAR_DA7_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_AVAR_DA7_Acetylcholine_AVAR_to_DA7_exc_syn_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVAR[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DA7[0].soma], weight: 6.0
        h("a_AVAR[0].soma { syn_NC_AVAR_DA7_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_DA7[0].soma { syn_NC_AVAR_DA7_Acetylcholine_AVAR_to_DA7_exc_syn_post[0] = new AVAR_to_DA7_exc_syn(0.500000) }")
        h("a_AVAR[0].soma { syn_NC_AVAR_DA7_Acetylcholine_silent_pre[0].weight = 6.0 }")
        h("a_DA7[0].soma { syn_NC_AVAR_DA7_Acetylcholine_AVAR_to_DA7_exc_syn_post[0].weight = 6.0 }")
        h("setpointer syn_NC_AVAR_DA7_Acetylcholine_silent_pre[0].vpeer, a_DA7[0].soma.v(0.500000)")
        h("setpointer syn_NC_AVAR_DA7_Acetylcholine_AVAR_to_DA7_exc_syn_post[0].vpeer, a_AVAR[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_AVAR_DA8_Acetylcholine
        print("Adding continuous projection: NC_AVAR_DA8_Acetylcholine from AVAR to DA8, with 1 connection(s)")

        h("objectvar syn_NC_AVAR_DA8_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_AVAR_DA8_Acetylcholine_AVAR_to_DA8_exc_syn_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVAR[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DA8[0].soma], weight: 20.0
        h("a_AVAR[0].soma { syn_NC_AVAR_DA8_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_DA8[0].soma { syn_NC_AVAR_DA8_Acetylcholine_AVAR_to_DA8_exc_syn_post[0] = new AVAR_to_DA8_exc_syn(0.500000) }")
        h("a_AVAR[0].soma { syn_NC_AVAR_DA8_Acetylcholine_silent_pre[0].weight = 20.0 }")
        h("a_DA8[0].soma { syn_NC_AVAR_DA8_Acetylcholine_AVAR_to_DA8_exc_syn_post[0].weight = 20.0 }")
        h("setpointer syn_NC_AVAR_DA8_Acetylcholine_silent_pre[0].vpeer, a_DA8[0].soma.v(0.500000)")
        h("setpointer syn_NC_AVAR_DA8_Acetylcholine_AVAR_to_DA8_exc_syn_post[0].vpeer, a_AVAR[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_AVAR_DA9_Acetylcholine
        print("Adding continuous projection: NC_AVAR_DA9_Acetylcholine from AVAR to DA9, with 1 connection(s)")

        h("objectvar syn_NC_AVAR_DA9_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_AVAR_DA9_Acetylcholine_AVAR_to_DA9_exc_syn_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVAR[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DA9[0].soma], weight: 3.0
        h("a_AVAR[0].soma { syn_NC_AVAR_DA9_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_DA9[0].soma { syn_NC_AVAR_DA9_Acetylcholine_AVAR_to_DA9_exc_syn_post[0] = new AVAR_to_DA9_exc_syn(0.500000) }")
        h("a_AVAR[0].soma { syn_NC_AVAR_DA9_Acetylcholine_silent_pre[0].weight = 3.0 }")
        h("a_DA9[0].soma { syn_NC_AVAR_DA9_Acetylcholine_AVAR_to_DA9_exc_syn_post[0].weight = 3.0 }")
        h("setpointer syn_NC_AVAR_DA9_Acetylcholine_silent_pre[0].vpeer, a_DA9[0].soma.v(0.500000)")
        h("setpointer syn_NC_AVAR_DA9_Acetylcholine_AVAR_to_DA9_exc_syn_post[0].vpeer, a_AVAR[0].soma.v(0.500000)")

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

        # ######################   Continuous Projection: NC_AVBR_DB4_Acetylcholine
        print("Adding continuous projection: NC_AVBR_DB4_Acetylcholine from AVBR to DB4, with 1 connection(s)")

        h("objectvar syn_NC_AVBR_DB4_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_AVBR_DB4_Acetylcholine_neuron_to_neuron_exc_syn_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AVBR[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DB4[0].soma], weight: 1.0
        h("a_AVBR[0].soma { syn_NC_AVBR_DB4_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_DB4[0].soma { syn_NC_AVBR_DB4_Acetylcholine_neuron_to_neuron_exc_syn_post[0] = new neuron_to_neuron_exc_syn(0.500000) }")
        h("setpointer syn_NC_AVBR_DB4_Acetylcholine_silent_pre[0].vpeer, a_DB4[0].soma.v(0.500000)")
        h("setpointer syn_NC_AVBR_DB4_Acetylcholine_neuron_to_neuron_exc_syn_post[0].vpeer, a_AVBR[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DA1_DB1_Acetylcholine
        print("Adding continuous projection: NC_DA1_DB1_Acetylcholine from DA1 to DB1, with 1 connection(s)")

        h("objectvar syn_NC_DA1_DB1_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DA1_DB1_Acetylcholine_DA1_to_DB1_exc_syn_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DA1[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DB1[0].soma], weight: 1.0
        h("a_DA1[0].soma { syn_NC_DA1_DB1_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_DB1[0].soma { syn_NC_DA1_DB1_Acetylcholine_DA1_to_DB1_exc_syn_post[0] = new DA1_to_DB1_exc_syn(0.500000) }")
        h("setpointer syn_NC_DA1_DB1_Acetylcholine_silent_pre[0].vpeer, a_DB1[0].soma.v(0.500000)")
        h("setpointer syn_NC_DA1_DB1_Acetylcholine_DA1_to_DB1_exc_syn_post[0].vpeer, a_DA1[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DA2_DB1_Acetylcholine
        print("Adding continuous projection: NC_DA2_DB1_Acetylcholine from DA2 to DB1, with 1 connection(s)")

        h("objectvar syn_NC_DA2_DB1_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DA2_DB1_Acetylcholine_DA2_to_DB1_exc_syn_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DA2[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DB1[0].soma], weight: 1.0
        h("a_DA2[0].soma { syn_NC_DA2_DB1_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_DB1[0].soma { syn_NC_DA2_DB1_Acetylcholine_DA2_to_DB1_exc_syn_post[0] = new DA2_to_DB1_exc_syn(0.500000) }")
        h("setpointer syn_NC_DA2_DB1_Acetylcholine_silent_pre[0].vpeer, a_DB1[0].soma.v(0.500000)")
        h("setpointer syn_NC_DA2_DB1_Acetylcholine_DA2_to_DB1_exc_syn_post[0].vpeer, a_DA2[0].soma.v(0.500000)")

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

        # ######################   Continuous Projection: NC_DA4_DB2_Acetylcholine
        print("Adding continuous projection: NC_DA4_DB2_Acetylcholine from DA4 to DB2, with 1 connection(s)")

        h("objectvar syn_NC_DA4_DB2_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DA4_DB2_Acetylcholine_DA4_to_DB2_exc_syn_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DA4[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DB2[0].soma], weight: 2.0
        h("a_DA4[0].soma { syn_NC_DA4_DB2_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_DB2[0].soma { syn_NC_DA4_DB2_Acetylcholine_DA4_to_DB2_exc_syn_post[0] = new DA4_to_DB2_exc_syn(0.500000) }")
        h("a_DA4[0].soma { syn_NC_DA4_DB2_Acetylcholine_silent_pre[0].weight = 2.0 }")
        h("a_DB2[0].soma { syn_NC_DA4_DB2_Acetylcholine_DA4_to_DB2_exc_syn_post[0].weight = 2.0 }")
        h("setpointer syn_NC_DA4_DB2_Acetylcholine_silent_pre[0].vpeer, a_DB2[0].soma.v(0.500000)")
        h("setpointer syn_NC_DA4_DB2_Acetylcholine_DA4_to_DB2_exc_syn_post[0].vpeer, a_DA4[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DA5_DB4_Acetylcholine
        print("Adding continuous projection: NC_DA5_DB4_Acetylcholine from DA5 to DB4, with 1 connection(s)")

        h("objectvar syn_NC_DA5_DB4_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DA5_DB4_Acetylcholine_DA5_to_DB4_exc_syn_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DA5[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DB4[0].soma], weight: 1.0
        h("a_DA5[0].soma { syn_NC_DA5_DB4_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_DB4[0].soma { syn_NC_DA5_DB4_Acetylcholine_DA5_to_DB4_exc_syn_post[0] = new DA5_to_DB4_exc_syn(0.500000) }")
        h("setpointer syn_NC_DA5_DB4_Acetylcholine_silent_pre[0].vpeer, a_DB4[0].soma.v(0.500000)")
        h("setpointer syn_NC_DA5_DB4_Acetylcholine_DA5_to_DB4_exc_syn_post[0].vpeer, a_DA5[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DA6_DB5_Acetylcholine
        print("Adding continuous projection: NC_DA6_DB5_Acetylcholine from DA6 to DB5, with 1 connection(s)")

        h("objectvar syn_NC_DA6_DB5_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DA6_DB5_Acetylcholine_DA6_to_DB5_exc_syn_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DA6[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DB5[0].soma], weight: 1.0
        h("a_DA6[0].soma { syn_NC_DA6_DB5_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_DB5[0].soma { syn_NC_DA6_DB5_Acetylcholine_DA6_to_DB5_exc_syn_post[0] = new DA6_to_DB5_exc_syn(0.500000) }")
        h("setpointer syn_NC_DA6_DB5_Acetylcholine_silent_pre[0].vpeer, a_DB5[0].soma.v(0.500000)")
        h("setpointer syn_NC_DA6_DB5_Acetylcholine_DA6_to_DB5_exc_syn_post[0].vpeer, a_DA6[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DA7_DB6_Acetylcholine
        print("Adding continuous projection: NC_DA7_DB6_Acetylcholine from DA7 to DB6, with 1 connection(s)")

        h("objectvar syn_NC_DA7_DB6_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DA7_DB6_Acetylcholine_DA7_to_DB6_exc_syn_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DA7[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DB6[0].soma], weight: 1.0
        h("a_DA7[0].soma { syn_NC_DA7_DB6_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_DB6[0].soma { syn_NC_DA7_DB6_Acetylcholine_DA7_to_DB6_exc_syn_post[0] = new DA7_to_DB6_exc_syn(0.500000) }")
        h("setpointer syn_NC_DA7_DB6_Acetylcholine_silent_pre[0].vpeer, a_DB6[0].soma.v(0.500000)")
        h("setpointer syn_NC_DA7_DB6_Acetylcholine_DA7_to_DB6_exc_syn_post[0].vpeer, a_DA7[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DA8_DB7_Acetylcholine
        print("Adding continuous projection: NC_DA8_DB7_Acetylcholine from DA8 to DB7, with 1 connection(s)")

        h("objectvar syn_NC_DA8_DB7_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DA8_DB7_Acetylcholine_DA8_to_DB7_exc_syn_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DA8[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DB7[0].soma], weight: 1.0
        h("a_DA8[0].soma { syn_NC_DA8_DB7_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_DB7[0].soma { syn_NC_DA8_DB7_Acetylcholine_DA8_to_DB7_exc_syn_post[0] = new DA8_to_DB7_exc_syn(0.500000) }")
        h("setpointer syn_NC_DA8_DB7_Acetylcholine_silent_pre[0].vpeer, a_DB7[0].soma.v(0.500000)")
        h("setpointer syn_NC_DA8_DB7_Acetylcholine_DA8_to_DB7_exc_syn_post[0].vpeer, a_DA8[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DA9_DB7_Acetylcholine
        print("Adding continuous projection: NC_DA9_DB7_Acetylcholine from DA9 to DB7, with 1 connection(s)")

        h("objectvar syn_NC_DA9_DB7_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DA9_DB7_Acetylcholine_DA9_to_DB7_exc_syn_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DA9[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DB7[0].soma], weight: 1.0
        h("a_DA9[0].soma { syn_NC_DA9_DB7_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_DB7[0].soma { syn_NC_DA9_DB7_Acetylcholine_DA9_to_DB7_exc_syn_post[0] = new DA9_to_DB7_exc_syn(0.500000) }")
        h("setpointer syn_NC_DA9_DB7_Acetylcholine_silent_pre[0].vpeer, a_DB7[0].soma.v(0.500000)")
        h("setpointer syn_NC_DA9_DB7_Acetylcholine_DA9_to_DB7_exc_syn_post[0].vpeer, a_DA9[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB1_AS1_Acetylcholine
        print("Adding continuous projection: NC_DB1_AS1_Acetylcholine from DB1 to AS1, with 1 connection(s)")

        h("objectvar syn_NC_DB1_AS1_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB1_AS1_Acetylcholine_DB1_to_AS1_inh_syn_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB1[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AS1[0].soma], weight: 28.0
        h("a_DB1[0].soma { syn_NC_DB1_AS1_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_AS1[0].soma { syn_NC_DB1_AS1_Acetylcholine_DB1_to_AS1_inh_syn_post[0] = new DB1_to_AS1_inh_syn(0.500000) }")
        h("a_DB1[0].soma { syn_NC_DB1_AS1_Acetylcholine_silent_pre[0].weight = 28.0 }")
        h("a_AS1[0].soma { syn_NC_DB1_AS1_Acetylcholine_DB1_to_AS1_inh_syn_post[0].weight = 28.0 }")
        h("setpointer syn_NC_DB1_AS1_Acetylcholine_silent_pre[0].vpeer, a_AS1[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB1_AS1_Acetylcholine_DB1_to_AS1_inh_syn_post[0].vpeer, a_DB1[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB1_AS2_Acetylcholine
        print("Adding continuous projection: NC_DB1_AS2_Acetylcholine from DB1 to AS2, with 1 connection(s)")

        h("objectvar syn_NC_DB1_AS2_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB1_AS2_Acetylcholine_DB1_to_AS2_inh_syn_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB1[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AS2[0].soma], weight: 4.0
        h("a_DB1[0].soma { syn_NC_DB1_AS2_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_AS2[0].soma { syn_NC_DB1_AS2_Acetylcholine_DB1_to_AS2_inh_syn_post[0] = new DB1_to_AS2_inh_syn(0.500000) }")
        h("a_DB1[0].soma { syn_NC_DB1_AS2_Acetylcholine_silent_pre[0].weight = 4.0 }")
        h("a_AS2[0].soma { syn_NC_DB1_AS2_Acetylcholine_DB1_to_AS2_inh_syn_post[0].weight = 4.0 }")
        h("setpointer syn_NC_DB1_AS2_Acetylcholine_silent_pre[0].vpeer, a_AS2[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB1_AS2_Acetylcholine_DB1_to_AS2_inh_syn_post[0].vpeer, a_DB1[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB2_AS3_Acetylcholine
        print("Adding continuous projection: NC_DB2_AS3_Acetylcholine from DB2 to AS3, with 1 connection(s)")

        h("objectvar syn_NC_DB2_AS3_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB2_AS3_Acetylcholine_DB2_to_AS3_inh_syn_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB2[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AS3[0].soma], weight: 3.0
        h("a_DB2[0].soma { syn_NC_DB2_AS3_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_AS3[0].soma { syn_NC_DB2_AS3_Acetylcholine_DB2_to_AS3_inh_syn_post[0] = new DB2_to_AS3_inh_syn(0.500000) }")
        h("a_DB2[0].soma { syn_NC_DB2_AS3_Acetylcholine_silent_pre[0].weight = 3.0 }")
        h("a_AS3[0].soma { syn_NC_DB2_AS3_Acetylcholine_DB2_to_AS3_inh_syn_post[0].weight = 3.0 }")
        h("setpointer syn_NC_DB2_AS3_Acetylcholine_silent_pre[0].vpeer, a_AS3[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB2_AS3_Acetylcholine_DB2_to_AS3_inh_syn_post[0].vpeer, a_DB2[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB2_AS4_Acetylcholine
        print("Adding continuous projection: NC_DB2_AS4_Acetylcholine from DB2 to AS4, with 1 connection(s)")

        h("objectvar syn_NC_DB2_AS4_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB2_AS4_Acetylcholine_DB2_to_AS4_inh_syn_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB2[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AS4[0].soma], weight: 2.0
        h("a_DB2[0].soma { syn_NC_DB2_AS4_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_AS4[0].soma { syn_NC_DB2_AS4_Acetylcholine_DB2_to_AS4_inh_syn_post[0] = new DB2_to_AS4_inh_syn(0.500000) }")
        h("a_DB2[0].soma { syn_NC_DB2_AS4_Acetylcholine_silent_pre[0].weight = 2.0 }")
        h("a_AS4[0].soma { syn_NC_DB2_AS4_Acetylcholine_DB2_to_AS4_inh_syn_post[0].weight = 2.0 }")
        h("setpointer syn_NC_DB2_AS4_Acetylcholine_silent_pre[0].vpeer, a_AS4[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB2_AS4_Acetylcholine_DB2_to_AS4_inh_syn_post[0].vpeer, a_DB2[0].soma.v(0.500000)")

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

        # ######################   Continuous Projection: NC_DB3_AS5_Acetylcholine
        print("Adding continuous projection: NC_DB3_AS5_Acetylcholine from DB3 to AS5, with 1 connection(s)")

        h("objectvar syn_NC_DB3_AS5_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB3_AS5_Acetylcholine_DB3_to_AS5_inh_syn_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB3[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AS5[0].soma], weight: 1.0
        h("a_DB3[0].soma { syn_NC_DB3_AS5_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_AS5[0].soma { syn_NC_DB3_AS5_Acetylcholine_DB3_to_AS5_inh_syn_post[0] = new DB3_to_AS5_inh_syn(0.500000) }")
        h("setpointer syn_NC_DB3_AS5_Acetylcholine_silent_pre[0].vpeer, a_AS5[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB3_AS5_Acetylcholine_DB3_to_AS5_inh_syn_post[0].vpeer, a_DB3[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB4_AS6_Acetylcholine
        print("Adding continuous projection: NC_DB4_AS6_Acetylcholine from DB4 to AS6, with 1 connection(s)")

        h("objectvar syn_NC_DB4_AS6_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB4_AS6_Acetylcholine_DB4_to_AS6_inh_syn_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB4[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AS6[0].soma], weight: 2.0
        h("a_DB4[0].soma { syn_NC_DB4_AS6_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_AS6[0].soma { syn_NC_DB4_AS6_Acetylcholine_DB4_to_AS6_inh_syn_post[0] = new DB4_to_AS6_inh_syn(0.500000) }")
        h("a_DB4[0].soma { syn_NC_DB4_AS6_Acetylcholine_silent_pre[0].weight = 2.0 }")
        h("a_AS6[0].soma { syn_NC_DB4_AS6_Acetylcholine_DB4_to_AS6_inh_syn_post[0].weight = 2.0 }")
        h("setpointer syn_NC_DB4_AS6_Acetylcholine_silent_pre[0].vpeer, a_AS6[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB4_AS6_Acetylcholine_DB4_to_AS6_inh_syn_post[0].vpeer, a_DB4[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB5_AS7_Acetylcholine
        print("Adding continuous projection: NC_DB5_AS7_Acetylcholine from DB5 to AS7, with 1 connection(s)")

        h("objectvar syn_NC_DB5_AS7_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB5_AS7_Acetylcholine_DB5_to_AS7_inh_syn_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB5[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AS7[0].soma], weight: 3.0
        h("a_DB5[0].soma { syn_NC_DB5_AS7_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_AS7[0].soma { syn_NC_DB5_AS7_Acetylcholine_DB5_to_AS7_inh_syn_post[0] = new DB5_to_AS7_inh_syn(0.500000) }")
        h("a_DB5[0].soma { syn_NC_DB5_AS7_Acetylcholine_silent_pre[0].weight = 3.0 }")
        h("a_AS7[0].soma { syn_NC_DB5_AS7_Acetylcholine_DB5_to_AS7_inh_syn_post[0].weight = 3.0 }")
        h("setpointer syn_NC_DB5_AS7_Acetylcholine_silent_pre[0].vpeer, a_AS7[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB5_AS7_Acetylcholine_DB5_to_AS7_inh_syn_post[0].vpeer, a_DB5[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB5_AS8_Acetylcholine
        print("Adding continuous projection: NC_DB5_AS8_Acetylcholine from DB5 to AS8, with 1 connection(s)")

        h("objectvar syn_NC_DB5_AS8_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB5_AS8_Acetylcholine_DB5_to_AS8_inh_syn_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB5[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AS8[0].soma], weight: 2.0
        h("a_DB5[0].soma { syn_NC_DB5_AS8_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_AS8[0].soma { syn_NC_DB5_AS8_Acetylcholine_DB5_to_AS8_inh_syn_post[0] = new DB5_to_AS8_inh_syn(0.500000) }")
        h("a_DB5[0].soma { syn_NC_DB5_AS8_Acetylcholine_silent_pre[0].weight = 2.0 }")
        h("a_AS8[0].soma { syn_NC_DB5_AS8_Acetylcholine_DB5_to_AS8_inh_syn_post[0].weight = 2.0 }")
        h("setpointer syn_NC_DB5_AS8_Acetylcholine_silent_pre[0].vpeer, a_AS8[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB5_AS8_Acetylcholine_DB5_to_AS8_inh_syn_post[0].vpeer, a_DB5[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB6_AS8_Acetylcholine
        print("Adding continuous projection: NC_DB6_AS8_Acetylcholine from DB6 to AS8, with 1 connection(s)")

        h("objectvar syn_NC_DB6_AS8_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB6_AS8_Acetylcholine_DB6_to_AS8_inh_syn_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB6[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AS8[0].soma], weight: 2.0
        h("a_DB6[0].soma { syn_NC_DB6_AS8_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_AS8[0].soma { syn_NC_DB6_AS8_Acetylcholine_DB6_to_AS8_inh_syn_post[0] = new DB6_to_AS8_inh_syn(0.500000) }")
        h("a_DB6[0].soma { syn_NC_DB6_AS8_Acetylcholine_silent_pre[0].weight = 2.0 }")
        h("a_AS8[0].soma { syn_NC_DB6_AS8_Acetylcholine_DB6_to_AS8_inh_syn_post[0].weight = 2.0 }")
        h("setpointer syn_NC_DB6_AS8_Acetylcholine_silent_pre[0].vpeer, a_AS8[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB6_AS8_Acetylcholine_DB6_to_AS8_inh_syn_post[0].vpeer, a_DB6[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB6_AS9_Acetylcholine
        print("Adding continuous projection: NC_DB6_AS9_Acetylcholine from DB6 to AS9, with 1 connection(s)")

        h("objectvar syn_NC_DB6_AS9_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB6_AS9_Acetylcholine_DB6_to_AS9_inh_syn_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB6[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AS9[0].soma], weight: 1.0
        h("a_DB6[0].soma { syn_NC_DB6_AS9_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_AS9[0].soma { syn_NC_DB6_AS9_Acetylcholine_DB6_to_AS9_inh_syn_post[0] = new DB6_to_AS9_inh_syn(0.500000) }")
        h("setpointer syn_NC_DB6_AS9_Acetylcholine_silent_pre[0].vpeer, a_AS9[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB6_AS9_Acetylcholine_DB6_to_AS9_inh_syn_post[0].vpeer, a_DB6[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB7_AS10_Acetylcholine
        print("Adding continuous projection: NC_DB7_AS10_Acetylcholine from DB7 to AS10, with 1 connection(s)")

        h("objectvar syn_NC_DB7_AS10_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB7_AS10_Acetylcholine_DB7_to_AS10_inh_syn_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB7[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AS10[0].soma], weight: 2.0
        h("a_DB7[0].soma { syn_NC_DB7_AS10_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_AS10[0].soma { syn_NC_DB7_AS10_Acetylcholine_DB7_to_AS10_inh_syn_post[0] = new DB7_to_AS10_inh_syn(0.500000) }")
        h("a_DB7[0].soma { syn_NC_DB7_AS10_Acetylcholine_silent_pre[0].weight = 2.0 }")
        h("a_AS10[0].soma { syn_NC_DB7_AS10_Acetylcholine_DB7_to_AS10_inh_syn_post[0].weight = 2.0 }")
        h("setpointer syn_NC_DB7_AS10_Acetylcholine_silent_pre[0].vpeer, a_AS10[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB7_AS10_Acetylcholine_DB7_to_AS10_inh_syn_post[0].vpeer, a_DB7[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_DB7_AS11_Acetylcholine
        print("Adding continuous projection: NC_DB7_AS11_Acetylcholine from DB7 to AS11, with 1 connection(s)")

        h("objectvar syn_NC_DB7_AS11_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_DB7_AS11_Acetylcholine_DB7_to_AS11_inh_syn_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_DB7[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_AS11[0].soma], weight: 2.0
        h("a_DB7[0].soma { syn_NC_DB7_AS11_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_AS11[0].soma { syn_NC_DB7_AS11_Acetylcholine_DB7_to_AS11_inh_syn_post[0] = new DB7_to_AS11_inh_syn(0.500000) }")
        h("a_DB7[0].soma { syn_NC_DB7_AS11_Acetylcholine_silent_pre[0].weight = 2.0 }")
        h("a_AS11[0].soma { syn_NC_DB7_AS11_Acetylcholine_DB7_to_AS11_inh_syn_post[0].weight = 2.0 }")
        h("setpointer syn_NC_DB7_AS11_Acetylcholine_silent_pre[0].vpeer, a_AS11[0].soma.v(0.500000)")
        h("setpointer syn_NC_DB7_AS11_Acetylcholine_DB7_to_AS11_inh_syn_post[0].vpeer, a_DB7[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_AS1_DA1_Acetylcholine
        print("Adding continuous projection: NC_AS1_DA1_Acetylcholine from AS1 to DA1, with 1 connection(s)")

        h("objectvar syn_NC_AS1_DA1_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_AS1_DA1_Acetylcholine_AS1_to_DA1_exc_syn_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AS1[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DA1[0].soma], weight: 8.0
        h("a_AS1[0].soma { syn_NC_AS1_DA1_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_DA1[0].soma { syn_NC_AS1_DA1_Acetylcholine_AS1_to_DA1_exc_syn_post[0] = new AS1_to_DA1_exc_syn(0.500000) }")
        h("a_AS1[0].soma { syn_NC_AS1_DA1_Acetylcholine_silent_pre[0].weight = 8.0 }")
        h("a_DA1[0].soma { syn_NC_AS1_DA1_Acetylcholine_AS1_to_DA1_exc_syn_post[0].weight = 8.0 }")
        h("setpointer syn_NC_AS1_DA1_Acetylcholine_silent_pre[0].vpeer, a_DA1[0].soma.v(0.500000)")
        h("setpointer syn_NC_AS1_DA1_Acetylcholine_AS1_to_DA1_exc_syn_post[0].vpeer, a_AS1[0].soma.v(0.500000)")

        # ######################   Continuous Projection: NC_AS3_DA3_Acetylcholine
        print("Adding continuous projection: NC_AS3_DA3_Acetylcholine from AS3 to DA3, with 1 connection(s)")

        h("objectvar syn_NC_AS3_DA3_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_AS3_DA3_Acetylcholine_AS3_to_DA3_exc_syn_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AS3[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DA3[0].soma], weight: 1.0
        h("a_AS3[0].soma { syn_NC_AS3_DA3_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_DA3[0].soma { syn_NC_AS3_DA3_Acetylcholine_AS3_to_DA3_exc_syn_post[0] = new AS3_to_DA3_exc_syn(0.500000) }")
        h("setpointer syn_NC_AS3_DA3_Acetylcholine_silent_pre[0].vpeer, a_DA3[0].soma.v(0.500000)")
        h("setpointer syn_NC_AS3_DA3_Acetylcholine_AS3_to_DA3_exc_syn_post[0].vpeer, a_AS3[0].soma.v(0.500000)")

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

        # ######################   Continuous Projection: NC_AS6_DA5_Acetylcholine
        print("Adding continuous projection: NC_AS6_DA5_Acetylcholine from AS6 to DA5, with 1 connection(s)")

        h("objectvar syn_NC_AS6_DA5_Acetylcholine_silent_pre[1]")
        h("objectvar syn_NC_AS6_DA5_Acetylcholine_AS6_to_DA5_exc_syn_post[1]")

        # Continuous Connection 0: cell 0, seg 0 (0.5) [0.5 on a_AS6[0].soma] -> cell 0, seg 0 (0.5) [0.5 on a_DA5[0].soma], weight: 1.0
        h("a_AS6[0].soma { syn_NC_AS6_DA5_Acetylcholine_silent_pre[0] = new silent(0.500000) }")
        h("a_DA5[0].soma { syn_NC_AS6_DA5_Acetylcholine_AS6_to_DA5_exc_syn_post[0] = new AS6_to_DA5_exc_syn(0.500000) }")
        h("setpointer syn_NC_AS6_DA5_Acetylcholine_silent_pre[0].vpeer, a_DA5[0].soma.v(0.500000)")
        h("setpointer syn_NC_AS6_DA5_Acetylcholine_AS6_to_DA5_exc_syn_post[0].vpeer, a_AS6[0].soma.v(0.500000)")

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

        # ######################   Input List: Input_AS1_stim_AS1_1
        print("Adding input list: Input_AS1_stim_AS1_1 to AS1, with 1 inputs of type stim_AS1_1")

        # Adding single input: Component(id=0 type=input)
        h("objref Input_AS1_stim_AS1_1_0")
        h("a_AS1[0].soma { Input_AS1_stim_AS1_1_0 = new stim_AS1_1(0.5) } ")

        # ######################   Input List: Input_AS2_stim_AS2_1
        print("Adding input list: Input_AS2_stim_AS2_1 to AS2, with 1 inputs of type stim_AS2_1")

        # Adding single input: Component(id=0 type=input)
        h("objref Input_AS2_stim_AS2_1_0")
        h("a_AS2[0].soma { Input_AS2_stim_AS2_1_0 = new stim_AS2_1(0.5) } ")

        # ######################   Input List: Input_AS3_stim_AS3_1
        print("Adding input list: Input_AS3_stim_AS3_1 to AS3, with 1 inputs of type stim_AS3_1")

        # Adding single input: Component(id=0 type=input)
        h("objref Input_AS3_stim_AS3_1_0")
        h("a_AS3[0].soma { Input_AS3_stim_AS3_1_0 = new stim_AS3_1(0.5) } ")

        # ######################   Input List: Input_AS4_stim_AS4_1
        print("Adding input list: Input_AS4_stim_AS4_1 to AS4, with 1 inputs of type stim_AS4_1")

        # Adding single input: Component(id=0 type=input)
        h("objref Input_AS4_stim_AS4_1_0")
        h("a_AS4[0].soma { Input_AS4_stim_AS4_1_0 = new stim_AS4_1(0.5) } ")

        # ######################   Input List: Input_AS5_stim_AS5_1
        print("Adding input list: Input_AS5_stim_AS5_1 to AS5, with 1 inputs of type stim_AS5_1")

        # Adding single input: Component(id=0 type=input)
        h("objref Input_AS5_stim_AS5_1_0")
        h("a_AS5[0].soma { Input_AS5_stim_AS5_1_0 = new stim_AS5_1(0.5) } ")

        # ######################   Input List: Input_AS6_stim_AS6_1
        print("Adding input list: Input_AS6_stim_AS6_1 to AS6, with 1 inputs of type stim_AS6_1")

        # Adding single input: Component(id=0 type=input)
        h("objref Input_AS6_stim_AS6_1_0")
        h("a_AS6[0].soma { Input_AS6_stim_AS6_1_0 = new stim_AS6_1(0.5) } ")

        # ######################   Input List: Input_AS7_stim_AS7_1
        print("Adding input list: Input_AS7_stim_AS7_1 to AS7, with 1 inputs of type stim_AS7_1")

        # Adding single input: Component(id=0 type=input)
        h("objref Input_AS7_stim_AS7_1_0")
        h("a_AS7[0].soma { Input_AS7_stim_AS7_1_0 = new stim_AS7_1(0.5) } ")

        # ######################   Input List: Input_AS8_stim_AS8_1
        print("Adding input list: Input_AS8_stim_AS8_1 to AS8, with 1 inputs of type stim_AS8_1")

        # Adding single input: Component(id=0 type=input)
        h("objref Input_AS8_stim_AS8_1_0")
        h("a_AS8[0].soma { Input_AS8_stim_AS8_1_0 = new stim_AS8_1(0.5) } ")

        # ######################   Input List: Input_AS9_stim_AS9_1
        print("Adding input list: Input_AS9_stim_AS9_1 to AS9, with 1 inputs of type stim_AS9_1")

        # Adding single input: Component(id=0 type=input)
        h("objref Input_AS9_stim_AS9_1_0")
        h("a_AS9[0].soma { Input_AS9_stim_AS9_1_0 = new stim_AS9_1(0.5) } ")

        # ######################   Input List: Input_AS10_stim_AS10_1
        print("Adding input list: Input_AS10_stim_AS10_1 to AS10, with 1 inputs of type stim_AS10_1")

        # Adding single input: Component(id=0 type=input)
        h("objref Input_AS10_stim_AS10_1_0")
        h("a_AS10[0].soma { Input_AS10_stim_AS10_1_0 = new stim_AS10_1(0.5) } ")

        # ######################   Input List: Input_AS11_stim_AS11_1
        print("Adding input list: Input_AS11_stim_AS11_1 to AS11, with 1 inputs of type stim_AS11_1")

        # Adding single input: Component(id=0 type=input)
        h("objref Input_AS11_stim_AS11_1_0")
        h("a_AS11[0].soma { Input_AS11_stim_AS11_1_0 = new stim_AS11_1(0.5) } ")

        trec = h.Vector()
        trec.record(h._ref_t)

        h.tstop = tstop

        h.dt = dt

        h.steps_per_ms = 1/h.dt



        # ######################   File to save: c302_C2_AS4_DA3_DB3.activity.dat (neurons_activity)
        # Column: AS1/0/GenericNeuronCell/caConc
        h(' objectvar v_AS1_v_neurons_activity ')
        h(' { v_AS1_v_neurons_activity = new Vector() } ')
        h(' { v_AS1_v_neurons_activity.record(&a_AS1[0].soma.cai(0.5)) } ')
        h.v_AS1_v_neurons_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: AS10/0/GenericNeuronCell/caConc
        h(' objectvar v_AS10_v_neurons_activity ')
        h(' { v_AS10_v_neurons_activity = new Vector() } ')
        h(' { v_AS10_v_neurons_activity.record(&a_AS10[0].soma.cai(0.5)) } ')
        h.v_AS10_v_neurons_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: AS11/0/GenericNeuronCell/caConc
        h(' objectvar v_AS11_v_neurons_activity ')
        h(' { v_AS11_v_neurons_activity = new Vector() } ')
        h(' { v_AS11_v_neurons_activity.record(&a_AS11[0].soma.cai(0.5)) } ')
        h.v_AS11_v_neurons_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: AS2/0/GenericNeuronCell/caConc
        h(' objectvar v_AS2_v_neurons_activity ')
        h(' { v_AS2_v_neurons_activity = new Vector() } ')
        h(' { v_AS2_v_neurons_activity.record(&a_AS2[0].soma.cai(0.5)) } ')
        h.v_AS2_v_neurons_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: AS3/0/GenericNeuronCell/caConc
        h(' objectvar v_AS3_v_neurons_activity ')
        h(' { v_AS3_v_neurons_activity = new Vector() } ')
        h(' { v_AS3_v_neurons_activity.record(&a_AS3[0].soma.cai(0.5)) } ')
        h.v_AS3_v_neurons_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: AS4/0/GenericNeuronCell/caConc
        h(' objectvar v_AS4_v_neurons_activity ')
        h(' { v_AS4_v_neurons_activity = new Vector() } ')
        h(' { v_AS4_v_neurons_activity.record(&a_AS4[0].soma.cai(0.5)) } ')
        h.v_AS4_v_neurons_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: AS5/0/GenericNeuronCell/caConc
        h(' objectvar v_AS5_v_neurons_activity ')
        h(' { v_AS5_v_neurons_activity = new Vector() } ')
        h(' { v_AS5_v_neurons_activity.record(&a_AS5[0].soma.cai(0.5)) } ')
        h.v_AS5_v_neurons_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: AS6/0/GenericNeuronCell/caConc
        h(' objectvar v_AS6_v_neurons_activity ')
        h(' { v_AS6_v_neurons_activity = new Vector() } ')
        h(' { v_AS6_v_neurons_activity.record(&a_AS6[0].soma.cai(0.5)) } ')
        h.v_AS6_v_neurons_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: AS7/0/GenericNeuronCell/caConc
        h(' objectvar v_AS7_v_neurons_activity ')
        h(' { v_AS7_v_neurons_activity = new Vector() } ')
        h(' { v_AS7_v_neurons_activity.record(&a_AS7[0].soma.cai(0.5)) } ')
        h.v_AS7_v_neurons_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: AS8/0/GenericNeuronCell/caConc
        h(' objectvar v_AS8_v_neurons_activity ')
        h(' { v_AS8_v_neurons_activity = new Vector() } ')
        h(' { v_AS8_v_neurons_activity.record(&a_AS8[0].soma.cai(0.5)) } ')
        h.v_AS8_v_neurons_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: AS9/0/GenericNeuronCell/caConc
        h(' objectvar v_AS9_v_neurons_activity ')
        h(' { v_AS9_v_neurons_activity = new Vector() } ')
        h(' { v_AS9_v_neurons_activity.record(&a_AS9[0].soma.cai(0.5)) } ')
        h.v_AS9_v_neurons_activity.resize((h.tstop * h.steps_per_ms) + 1)
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
        # Column: DA1/0/GenericNeuronCell/caConc
        h(' objectvar v_DA1_v_neurons_activity ')
        h(' { v_DA1_v_neurons_activity = new Vector() } ')
        h(' { v_DA1_v_neurons_activity.record(&a_DA1[0].soma.cai(0.5)) } ')
        h.v_DA1_v_neurons_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: DA2/0/GenericNeuronCell/caConc
        h(' objectvar v_DA2_v_neurons_activity ')
        h(' { v_DA2_v_neurons_activity = new Vector() } ')
        h(' { v_DA2_v_neurons_activity.record(&a_DA2[0].soma.cai(0.5)) } ')
        h.v_DA2_v_neurons_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: DA3/0/GenericNeuronCell/caConc
        h(' objectvar v_DA3_v_neurons_activity ')
        h(' { v_DA3_v_neurons_activity = new Vector() } ')
        h(' { v_DA3_v_neurons_activity.record(&a_DA3[0].soma.cai(0.5)) } ')
        h.v_DA3_v_neurons_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: DA4/0/GenericNeuronCell/caConc
        h(' objectvar v_DA4_v_neurons_activity ')
        h(' { v_DA4_v_neurons_activity = new Vector() } ')
        h(' { v_DA4_v_neurons_activity.record(&a_DA4[0].soma.cai(0.5)) } ')
        h.v_DA4_v_neurons_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: DA5/0/GenericNeuronCell/caConc
        h(' objectvar v_DA5_v_neurons_activity ')
        h(' { v_DA5_v_neurons_activity = new Vector() } ')
        h(' { v_DA5_v_neurons_activity.record(&a_DA5[0].soma.cai(0.5)) } ')
        h.v_DA5_v_neurons_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: DA6/0/GenericNeuronCell/caConc
        h(' objectvar v_DA6_v_neurons_activity ')
        h(' { v_DA6_v_neurons_activity = new Vector() } ')
        h(' { v_DA6_v_neurons_activity.record(&a_DA6[0].soma.cai(0.5)) } ')
        h.v_DA6_v_neurons_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: DA7/0/GenericNeuronCell/caConc
        h(' objectvar v_DA7_v_neurons_activity ')
        h(' { v_DA7_v_neurons_activity = new Vector() } ')
        h(' { v_DA7_v_neurons_activity.record(&a_DA7[0].soma.cai(0.5)) } ')
        h.v_DA7_v_neurons_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: DA8/0/GenericNeuronCell/caConc
        h(' objectvar v_DA8_v_neurons_activity ')
        h(' { v_DA8_v_neurons_activity = new Vector() } ')
        h(' { v_DA8_v_neurons_activity.record(&a_DA8[0].soma.cai(0.5)) } ')
        h.v_DA8_v_neurons_activity.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: DA9/0/GenericNeuronCell/caConc
        h(' objectvar v_DA9_v_neurons_activity ')
        h(' { v_DA9_v_neurons_activity = new Vector() } ')
        h(' { v_DA9_v_neurons_activity.record(&a_DA9[0].soma.cai(0.5)) } ')
        h.v_DA9_v_neurons_activity.resize((h.tstop * h.steps_per_ms) + 1)
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

        # ######################   File to save: c302_C2_AS4_DA3_DB3.dat (neurons_v)
        # Column: AS1/0/GenericNeuronCell/v
        h(' objectvar v_AS1_v_neurons_v ')
        h(' { v_AS1_v_neurons_v = new Vector() } ')
        h(' { v_AS1_v_neurons_v.record(&a_AS1[0].soma.v(0.5)) } ')
        h.v_AS1_v_neurons_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: AS10/0/GenericNeuronCell/v
        h(' objectvar v_AS10_v_neurons_v ')
        h(' { v_AS10_v_neurons_v = new Vector() } ')
        h(' { v_AS10_v_neurons_v.record(&a_AS10[0].soma.v(0.5)) } ')
        h.v_AS10_v_neurons_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: AS11/0/GenericNeuronCell/v
        h(' objectvar v_AS11_v_neurons_v ')
        h(' { v_AS11_v_neurons_v = new Vector() } ')
        h(' { v_AS11_v_neurons_v.record(&a_AS11[0].soma.v(0.5)) } ')
        h.v_AS11_v_neurons_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: AS2/0/GenericNeuronCell/v
        h(' objectvar v_AS2_v_neurons_v ')
        h(' { v_AS2_v_neurons_v = new Vector() } ')
        h(' { v_AS2_v_neurons_v.record(&a_AS2[0].soma.v(0.5)) } ')
        h.v_AS2_v_neurons_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: AS3/0/GenericNeuronCell/v
        h(' objectvar v_AS3_v_neurons_v ')
        h(' { v_AS3_v_neurons_v = new Vector() } ')
        h(' { v_AS3_v_neurons_v.record(&a_AS3[0].soma.v(0.5)) } ')
        h.v_AS3_v_neurons_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: AS4/0/GenericNeuronCell/v
        h(' objectvar v_AS4_v_neurons_v ')
        h(' { v_AS4_v_neurons_v = new Vector() } ')
        h(' { v_AS4_v_neurons_v.record(&a_AS4[0].soma.v(0.5)) } ')
        h.v_AS4_v_neurons_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: AS5/0/GenericNeuronCell/v
        h(' objectvar v_AS5_v_neurons_v ')
        h(' { v_AS5_v_neurons_v = new Vector() } ')
        h(' { v_AS5_v_neurons_v.record(&a_AS5[0].soma.v(0.5)) } ')
        h.v_AS5_v_neurons_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: AS6/0/GenericNeuronCell/v
        h(' objectvar v_AS6_v_neurons_v ')
        h(' { v_AS6_v_neurons_v = new Vector() } ')
        h(' { v_AS6_v_neurons_v.record(&a_AS6[0].soma.v(0.5)) } ')
        h.v_AS6_v_neurons_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: AS7/0/GenericNeuronCell/v
        h(' objectvar v_AS7_v_neurons_v ')
        h(' { v_AS7_v_neurons_v = new Vector() } ')
        h(' { v_AS7_v_neurons_v.record(&a_AS7[0].soma.v(0.5)) } ')
        h.v_AS7_v_neurons_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: AS8/0/GenericNeuronCell/v
        h(' objectvar v_AS8_v_neurons_v ')
        h(' { v_AS8_v_neurons_v = new Vector() } ')
        h(' { v_AS8_v_neurons_v.record(&a_AS8[0].soma.v(0.5)) } ')
        h.v_AS8_v_neurons_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: AS9/0/GenericNeuronCell/v
        h(' objectvar v_AS9_v_neurons_v ')
        h(' { v_AS9_v_neurons_v = new Vector() } ')
        h(' { v_AS9_v_neurons_v.record(&a_AS9[0].soma.v(0.5)) } ')
        h.v_AS9_v_neurons_v.resize((h.tstop * h.steps_per_ms) + 1)
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
        # Column: DA1/0/GenericNeuronCell/v
        h(' objectvar v_DA1_v_neurons_v ')
        h(' { v_DA1_v_neurons_v = new Vector() } ')
        h(' { v_DA1_v_neurons_v.record(&a_DA1[0].soma.v(0.5)) } ')
        h.v_DA1_v_neurons_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: DA2/0/GenericNeuronCell/v
        h(' objectvar v_DA2_v_neurons_v ')
        h(' { v_DA2_v_neurons_v = new Vector() } ')
        h(' { v_DA2_v_neurons_v.record(&a_DA2[0].soma.v(0.5)) } ')
        h.v_DA2_v_neurons_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: DA3/0/GenericNeuronCell/v
        h(' objectvar v_DA3_v_neurons_v ')
        h(' { v_DA3_v_neurons_v = new Vector() } ')
        h(' { v_DA3_v_neurons_v.record(&a_DA3[0].soma.v(0.5)) } ')
        h.v_DA3_v_neurons_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: DA4/0/GenericNeuronCell/v
        h(' objectvar v_DA4_v_neurons_v ')
        h(' { v_DA4_v_neurons_v = new Vector() } ')
        h(' { v_DA4_v_neurons_v.record(&a_DA4[0].soma.v(0.5)) } ')
        h.v_DA4_v_neurons_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: DA5/0/GenericNeuronCell/v
        h(' objectvar v_DA5_v_neurons_v ')
        h(' { v_DA5_v_neurons_v = new Vector() } ')
        h(' { v_DA5_v_neurons_v.record(&a_DA5[0].soma.v(0.5)) } ')
        h.v_DA5_v_neurons_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: DA6/0/GenericNeuronCell/v
        h(' objectvar v_DA6_v_neurons_v ')
        h(' { v_DA6_v_neurons_v = new Vector() } ')
        h(' { v_DA6_v_neurons_v.record(&a_DA6[0].soma.v(0.5)) } ')
        h.v_DA6_v_neurons_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: DA7/0/GenericNeuronCell/v
        h(' objectvar v_DA7_v_neurons_v ')
        h(' { v_DA7_v_neurons_v = new Vector() } ')
        h(' { v_DA7_v_neurons_v.record(&a_DA7[0].soma.v(0.5)) } ')
        h.v_DA7_v_neurons_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: DA8/0/GenericNeuronCell/v
        h(' objectvar v_DA8_v_neurons_v ')
        h(' { v_DA8_v_neurons_v = new Vector() } ')
        h(' { v_DA8_v_neurons_v.record(&a_DA8[0].soma.v(0.5)) } ')
        h.v_DA8_v_neurons_v.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: DA9/0/GenericNeuronCell/v
        h(' objectvar v_DA9_v_neurons_v ')
        h(' { v_DA9_v_neurons_v = new Vector() } ')
        h(' { v_DA9_v_neurons_v.record(&a_DA9[0].soma.v(0.5)) } ')
        h.v_DA9_v_neurons_v.resize((h.tstop * h.steps_per_ms) + 1)
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

        # ######################   File to save: c302_C2_AS4_DA3_DB3.activity.dat (neurons_activity)
        py_v_AS1_v_neurons_activity = [ float(x ) for x in h.v_AS1_v_neurons_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_AS10_v_neurons_activity = [ float(x ) for x in h.v_AS10_v_neurons_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_AS11_v_neurons_activity = [ float(x ) for x in h.v_AS11_v_neurons_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_AS2_v_neurons_activity = [ float(x ) for x in h.v_AS2_v_neurons_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_AS3_v_neurons_activity = [ float(x ) for x in h.v_AS3_v_neurons_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_AS4_v_neurons_activity = [ float(x ) for x in h.v_AS4_v_neurons_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_AS5_v_neurons_activity = [ float(x ) for x in h.v_AS5_v_neurons_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_AS6_v_neurons_activity = [ float(x ) for x in h.v_AS6_v_neurons_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_AS7_v_neurons_activity = [ float(x ) for x in h.v_AS7_v_neurons_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_AS8_v_neurons_activity = [ float(x ) for x in h.v_AS8_v_neurons_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_AS9_v_neurons_activity = [ float(x ) for x in h.v_AS9_v_neurons_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_AVAL_v_neurons_activity = [ float(x ) for x in h.v_AVAL_v_neurons_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_AVAR_v_neurons_activity = [ float(x ) for x in h.v_AVAR_v_neurons_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_AVBL_v_neurons_activity = [ float(x ) for x in h.v_AVBL_v_neurons_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_AVBR_v_neurons_activity = [ float(x ) for x in h.v_AVBR_v_neurons_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_DA1_v_neurons_activity = [ float(x ) for x in h.v_DA1_v_neurons_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_DA2_v_neurons_activity = [ float(x ) for x in h.v_DA2_v_neurons_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_DA3_v_neurons_activity = [ float(x ) for x in h.v_DA3_v_neurons_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_DA4_v_neurons_activity = [ float(x ) for x in h.v_DA4_v_neurons_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_DA5_v_neurons_activity = [ float(x ) for x in h.v_DA5_v_neurons_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_DA6_v_neurons_activity = [ float(x ) for x in h.v_DA6_v_neurons_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_DA7_v_neurons_activity = [ float(x ) for x in h.v_DA7_v_neurons_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_DA8_v_neurons_activity = [ float(x ) for x in h.v_DA8_v_neurons_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_DA9_v_neurons_activity = [ float(x ) for x in h.v_DA9_v_neurons_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_DB1_v_neurons_activity = [ float(x ) for x in h.v_DB1_v_neurons_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_DB2_v_neurons_activity = [ float(x ) for x in h.v_DB2_v_neurons_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_DB3_v_neurons_activity = [ float(x ) for x in h.v_DB3_v_neurons_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_DB4_v_neurons_activity = [ float(x ) for x in h.v_DB4_v_neurons_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_DB5_v_neurons_activity = [ float(x ) for x in h.v_DB5_v_neurons_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_DB6_v_neurons_activity = [ float(x ) for x in h.v_DB6_v_neurons_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration
        py_v_DB7_v_neurons_activity = [ float(x ) for x in h.v_DB7_v_neurons_activity.to_python() ]  # Convert to Python list for speed, variable has dim: concentration

        f_neurons_activity_f2 = open('c302_C2_AS4_DA3_DB3.activity.dat', 'w')
        num_points = len(py_v_time)  # Simulation may have been stopped before tstop...

        for i in range(num_points):
            f_neurons_activity_f2.write('%e\t'% py_v_time[i]  + '%e\t'%(py_v_AS1_v_neurons_activity[i])  + '%e\t'%(py_v_AS10_v_neurons_activity[i])  + '%e\t'%(py_v_AS11_v_neurons_activity[i])  + '%e\t'%(py_v_AS2_v_neurons_activity[i])  + '%e\t'%(py_v_AS3_v_neurons_activity[i])  + '%e\t'%(py_v_AS4_v_neurons_activity[i])  + '%e\t'%(py_v_AS5_v_neurons_activity[i])  + '%e\t'%(py_v_AS6_v_neurons_activity[i])  + '%e\t'%(py_v_AS7_v_neurons_activity[i])  + '%e\t'%(py_v_AS8_v_neurons_activity[i])  + '%e\t'%(py_v_AS9_v_neurons_activity[i])  + '%e\t'%(py_v_AVAL_v_neurons_activity[i])  + '%e\t'%(py_v_AVAR_v_neurons_activity[i])  + '%e\t'%(py_v_AVBL_v_neurons_activity[i])  + '%e\t'%(py_v_AVBR_v_neurons_activity[i])  + '%e\t'%(py_v_DA1_v_neurons_activity[i])  + '%e\t'%(py_v_DA2_v_neurons_activity[i])  + '%e\t'%(py_v_DA3_v_neurons_activity[i])  + '%e\t'%(py_v_DA4_v_neurons_activity[i])  + '%e\t'%(py_v_DA5_v_neurons_activity[i])  + '%e\t'%(py_v_DA6_v_neurons_activity[i])  + '%e\t'%(py_v_DA7_v_neurons_activity[i])  + '%e\t'%(py_v_DA8_v_neurons_activity[i])  + '%e\t'%(py_v_DA9_v_neurons_activity[i])  + '%e\t'%(py_v_DB1_v_neurons_activity[i])  + '%e\t'%(py_v_DB2_v_neurons_activity[i])  + '%e\t'%(py_v_DB3_v_neurons_activity[i])  + '%e\t'%(py_v_DB4_v_neurons_activity[i])  + '%e\t'%(py_v_DB5_v_neurons_activity[i])  + '%e\t'%(py_v_DB6_v_neurons_activity[i])  + '%e\t'%(py_v_DB7_v_neurons_activity[i]) + '\n')
        f_neurons_activity_f2.close()
        print("Saved data to: c302_C2_AS4_DA3_DB3.activity.dat")

        # ######################   File to save: c302_C2_AS4_DA3_DB3.dat (neurons_v)
        py_v_AS1_v_neurons_v = [ float(x  / 1000.0) for x in h.v_AS1_v_neurons_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_AS10_v_neurons_v = [ float(x  / 1000.0) for x in h.v_AS10_v_neurons_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_AS11_v_neurons_v = [ float(x  / 1000.0) for x in h.v_AS11_v_neurons_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_AS2_v_neurons_v = [ float(x  / 1000.0) for x in h.v_AS2_v_neurons_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_AS3_v_neurons_v = [ float(x  / 1000.0) for x in h.v_AS3_v_neurons_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_AS4_v_neurons_v = [ float(x  / 1000.0) for x in h.v_AS4_v_neurons_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_AS5_v_neurons_v = [ float(x  / 1000.0) for x in h.v_AS5_v_neurons_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_AS6_v_neurons_v = [ float(x  / 1000.0) for x in h.v_AS6_v_neurons_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_AS7_v_neurons_v = [ float(x  / 1000.0) for x in h.v_AS7_v_neurons_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_AS8_v_neurons_v = [ float(x  / 1000.0) for x in h.v_AS8_v_neurons_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_AS9_v_neurons_v = [ float(x  / 1000.0) for x in h.v_AS9_v_neurons_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_AVAL_v_neurons_v = [ float(x  / 1000.0) for x in h.v_AVAL_v_neurons_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_AVAR_v_neurons_v = [ float(x  / 1000.0) for x in h.v_AVAR_v_neurons_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_AVBL_v_neurons_v = [ float(x  / 1000.0) for x in h.v_AVBL_v_neurons_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_AVBR_v_neurons_v = [ float(x  / 1000.0) for x in h.v_AVBR_v_neurons_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_DA1_v_neurons_v = [ float(x  / 1000.0) for x in h.v_DA1_v_neurons_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_DA2_v_neurons_v = [ float(x  / 1000.0) for x in h.v_DA2_v_neurons_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_DA3_v_neurons_v = [ float(x  / 1000.0) for x in h.v_DA3_v_neurons_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_DA4_v_neurons_v = [ float(x  / 1000.0) for x in h.v_DA4_v_neurons_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_DA5_v_neurons_v = [ float(x  / 1000.0) for x in h.v_DA5_v_neurons_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_DA6_v_neurons_v = [ float(x  / 1000.0) for x in h.v_DA6_v_neurons_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_DA7_v_neurons_v = [ float(x  / 1000.0) for x in h.v_DA7_v_neurons_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_DA8_v_neurons_v = [ float(x  / 1000.0) for x in h.v_DA8_v_neurons_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_DA9_v_neurons_v = [ float(x  / 1000.0) for x in h.v_DA9_v_neurons_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_DB1_v_neurons_v = [ float(x  / 1000.0) for x in h.v_DB1_v_neurons_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_DB2_v_neurons_v = [ float(x  / 1000.0) for x in h.v_DB2_v_neurons_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_DB3_v_neurons_v = [ float(x  / 1000.0) for x in h.v_DB3_v_neurons_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_DB4_v_neurons_v = [ float(x  / 1000.0) for x in h.v_DB4_v_neurons_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_DB5_v_neurons_v = [ float(x  / 1000.0) for x in h.v_DB5_v_neurons_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_DB6_v_neurons_v = [ float(x  / 1000.0) for x in h.v_DB6_v_neurons_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_DB7_v_neurons_v = [ float(x  / 1000.0) for x in h.v_DB7_v_neurons_v.to_python() ]  # Convert to Python list for speed, variable has dim: voltage

        f_neurons_v_f2 = open('c302_C2_AS4_DA3_DB3.dat', 'w')
        num_points = len(py_v_time)  # Simulation may have been stopped before tstop...

        for i in range(num_points):
            f_neurons_v_f2.write('%e\t'% py_v_time[i]  + '%e\t'%(py_v_AS1_v_neurons_v[i])  + '%e\t'%(py_v_AS10_v_neurons_v[i])  + '%e\t'%(py_v_AS11_v_neurons_v[i])  + '%e\t'%(py_v_AS2_v_neurons_v[i])  + '%e\t'%(py_v_AS3_v_neurons_v[i])  + '%e\t'%(py_v_AS4_v_neurons_v[i])  + '%e\t'%(py_v_AS5_v_neurons_v[i])  + '%e\t'%(py_v_AS6_v_neurons_v[i])  + '%e\t'%(py_v_AS7_v_neurons_v[i])  + '%e\t'%(py_v_AS8_v_neurons_v[i])  + '%e\t'%(py_v_AS9_v_neurons_v[i])  + '%e\t'%(py_v_AVAL_v_neurons_v[i])  + '%e\t'%(py_v_AVAR_v_neurons_v[i])  + '%e\t'%(py_v_AVBL_v_neurons_v[i])  + '%e\t'%(py_v_AVBR_v_neurons_v[i])  + '%e\t'%(py_v_DA1_v_neurons_v[i])  + '%e\t'%(py_v_DA2_v_neurons_v[i])  + '%e\t'%(py_v_DA3_v_neurons_v[i])  + '%e\t'%(py_v_DA4_v_neurons_v[i])  + '%e\t'%(py_v_DA5_v_neurons_v[i])  + '%e\t'%(py_v_DA6_v_neurons_v[i])  + '%e\t'%(py_v_DA7_v_neurons_v[i])  + '%e\t'%(py_v_DA8_v_neurons_v[i])  + '%e\t'%(py_v_DA9_v_neurons_v[i])  + '%e\t'%(py_v_DB1_v_neurons_v[i])  + '%e\t'%(py_v_DB2_v_neurons_v[i])  + '%e\t'%(py_v_DB3_v_neurons_v[i])  + '%e\t'%(py_v_DB4_v_neurons_v[i])  + '%e\t'%(py_v_DB5_v_neurons_v[i])  + '%e\t'%(py_v_DB6_v_neurons_v[i])  + '%e\t'%(py_v_DB7_v_neurons_v[i]) + '\n')
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

