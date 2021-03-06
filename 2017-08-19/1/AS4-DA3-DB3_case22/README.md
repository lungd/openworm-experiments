# Override default parameters with:
## Connections to include:
- AVA.-AVB.*
- AVB.-AVA.*
- ^AS\d+-DA.+$
- ^DA\d+-DB\d+$
- ^DB\d+-AS\d+$
- AVA.-DA.*
- AVB.-DB.*
- DA\d+-AVA.*
- DB\d+-AVB.*
- DA\d+-M(D|V)(L|R).*
- DB\d+-M(D|V)(L|R).*
- M(D|V)(L|R)\d+-M(D|V)(L|R).*
- AVB.-AS.*
- AVA.-AS.*

## Change polarity of connections:
- ^AVB.-AVA.+$: inh
- ^AVA.-AVB.+$: inh
- DB3-AS4: inh

## Inject current:
- Cell: AVBL
    - delay: 50ms
    - end: 700ms
    - amplitude: 1pA
- Cell: AVBR
    - delay: 50ms
    - end: 700ms
    - amplitude: 1pA
- Cell: AVAL
    - delay: 700ms
    - end: 1500ms
    - amplitude: 1.5pA
- Cell: AVAR
    - delay: 700ms
    - end: 1500ms
    - amplitude: 1.5pA
- Cell: AVBL
    - delay: 1500ms
    - end: 1900ms
    - amplitude: 1pA
- Cell: AVBR
    - delay: 1500ms
    - end: 1900ms
    - amplitude: 1pA
- Cell: AS4
    - delay: 50ms
    - end: 1900ms
    - amplitude: 15.0pA

## Other parameters:
- ^AVA._to_AVB.\_GJ$_elec_syn_gbase: 0.00052 nS
- ^AS\d+_to_DA\d+\_GJ$_elec_syn_conductance: 0.00052 nS
- ^AVA._to_AVB.$_inh_syn_conductance: 5.7 nS
- neuron_to_neuron_inh_syn_conductance: 7.2 nS
- neuron_to_neuron_exc_syn_conductance: 5.2 nS
- ^AVB._to_AVA.$_inh_syn_conductance: 3.2 nS
- ^AVB._to_AVA.\_GJ$_elec_syn_gbase: 0.00052 nS
- DA3_to_DB3_exc_syn_conductance: 2.6 nS
- ^AVA._to_DA\d+\_GJ$_elec_syn_gbase: 0.00052 nS

