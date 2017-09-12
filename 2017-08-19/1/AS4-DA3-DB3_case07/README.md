# Override default parameters with:
## Change polarity of connections:
- ^AVB.-AVA.+$: inh
- ^AVA.-AVB.+$: inh
- DB3-AS4: inh

## Inject current:
- Cell: AVAL
    - delay: 50ms
    - end: 1900ms
    - amplitude: 2pA
- Cell: AVAR
    - delay: 50ms
    - end: 1900ms
    - amplitude: 2pA
- Cell: AS4
    - delay: 50ms
    - end: 1900ms
    - amplitude: 15.0pA

## Other parameters:
- neuron_to_neuron_inh_syn_conductance: 7.2 nS
- DA3_to_DB3_exc_syn_conductance: 3.0 nS
- neuron_to_neuron_exc_syn_conductance: 4.2 nS

