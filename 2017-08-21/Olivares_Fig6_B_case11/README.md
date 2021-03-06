# Override default parameters with:
## Connections to include:
- AVA.-AVA.*
- AVA.-AVB.*
- AVB.-AVB.*
- AVB.-AVA.*
- AVA.-DA.*
- ^DA3-AVA.\_GJ$
- AVA.-VA.*
- ^VA4-AVA.\_GJ$
- AVB.-DB.*
- ^DB3-AVB.\_GJ$
- AVB.-VB.*
- ^VB3-AVB.\_GJ$
- AS4-DA3
- DA3-DB3
- DB3-AS4
- AS4-VD4
- VD4-VA4
- VD4-VB3

## Change polarity of connections:
- AVA.-AVB.: inh
- AS4-VD4: inh
- AVB.-AVA.: inh
- DB3-AS4: inh
- VD4-VA4: exc
- VD4-VB3: exc

## Inject current:
- Cell: AVBL
    - delay: 0ms
    - end: 1000ms
    - amplitude: 5pA
- Cell: AVBR
    - delay: 0ms
    - end: 1000ms
    - amplitude: 5pA
- Cell: AVAL
    - delay: 1000ms
    - end: 1000ms
    - amplitude: 5pA
- Cell: AVAR
    - delay: 1000ms
    - end: 1000ms
    - amplitude: 5pA
- Cell: AVBL
    - delay: 2000ms
    - end: 900ms
    - amplitude: 5pA
- Cell: AVBR
    - delay: 2000ms
    - end: 900ms
    - amplitude: 5pA
- Cell: AS4
    - delay: 0ms
    - end: 2900ms
    - amplitude: 5.0pA
- Cell: VD4
    - delay: 0ms
    - end: 2900ms
    - amplitude: 5.0pA

## Other parameters:
- ^AVA._to_DA3$_exc_syn_conductance: 0.01 nS
- ^VB3_to_AVB.\_GJ$_elec_syn_gbase: 0.00302 nS
- ^AVA._to_VA4$_exc_syn_conductance: 0.01 nS
- ^DA3_to_AVA.\_GJ$_elec_syn_gbase: 0.00252 nS
- AS4_to_VD4_inh_syn_conductance: 0.09 nS
- VD4_to_VA4_exc_syn_conductance: 0.5 nS
- ^AVA._to_DA3\_GJ$_elec_syn_gbase: 0.00252 nS
- DA3_to_DB3_exc_syn_conductance: 2.0 nS
- ^AVB._to_DB3\_GJ$_elec_syn_gbase: 0.00302 nS
- ^AVB._to_VB3\_GJ$_elec_syn_gbase: 0.00302 nS
- ^VA4_to_AVA.\_GJ$_elec_syn_gbase: 0.00152 nS
- ^AVA._to_AVB.$_inh_syn_conductance: 0.059 nS
- VD4_to_VB3_exc_syn_conductance: 0.6 nS
- ^AVB._to_AVA.$_inh_syn_conductance: 0.019 nS
- AS4_to_DA3_exc_syn_conductance: 1.0 nS
- ^AVA._to_VA4\_GJ$_elec_syn_gbase: 0.00152 nS
- DB3_to_AS4_inh_syn_conductance: 1.6 nS
- ^DB3_to_AVB.\_GJ$_elec_syn_gbase: 0.00302 nS

