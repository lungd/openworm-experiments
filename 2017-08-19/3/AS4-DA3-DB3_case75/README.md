# Override default parameters with:
## Connections to include:
- AVA.-DA.*
- ^DA3-AVA.\_GJ$
- AVB.-DB.*
- ^DB3-AVB.\_GJ$
- AS4-DA3
- DA3-DB3
- DB3-AS4

## Change polarity of connections:
- DB3-AS4: inh

## Inject current:
- Cell: AVBL
    - delay: 0ms
    - end: 1000ms
    - amplitude: 3pA
- Cell: AVBR
    - delay: 0ms
    - end: 1000ms
    - amplitude: 3pA
- Cell: AVAL
    - delay: 1000ms
    - end: 1000ms
    - amplitude: 2pA
- Cell: AVAR
    - delay: 1000ms
    - end: 1000ms
    - amplitude: 2pA
- Cell: AVBL
    - delay: 2000ms
    - end: 900ms
    - amplitude: 3pA
- Cell: AVBR
    - delay: 2000ms
    - end: 900ms
    - amplitude: 3pA
- Cell: AS4
    - delay: 0ms
    - end: 2900ms
    - amplitude: 10.0pA

## Other parameters:
- ^AVA._to_DA3$_exc_syn_conductance: 1 nS
- ^DA3_to_AVA.\_GJ$_elec_syn_gbase: 0.00152 nS
- ^AVB._to_DB3$_exc_syn_conductance: 5 nS
- DB3_to_AS4_inh_syn_conductance: 1.7 nS
- AS4_to_DA3_exc_syn_conductance: 3.1 nS
- ^DB3_to_AVB.\_GJ$_elec_syn_gbase: 0.00202 nS
- ^AVA._to_DA3\_GJ$_elec_syn_gbase: 0.00152 nS
- DA3_to_DB3_exc_syn_conductance: 1.6 nS
- ^AVB._to_DB3\_GJ$_elec_syn_gbase: 0.00202 nS

