# Override default parameters with:
## Connections to include:
- AVA.-AVB.*
- AVB.-AVA.*
- ^AS\d+-DA.+$
- ^DA\d+-DB\d+$
- ^DB\d+-AS\d+$
- AVB.-DB.*
- DA\d+-AVA.*
- DB\d+-AVB.*
- DA\d+-M(D|V)(L|R).*
- DB\d+-M(D|V)(L|R).*
- M(D|V)(L|R)\d+-M(D|V)(L|R).*
- DA\d+-DA.*
- DB\d+-DB.*
- AS\d+-AS.*
- AVB.-AS.*

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
- neuron_to_neuron_inh_syn_conductance: 7.2 nS
- DA3_to_DB3_exc_syn_conductance: 3.0 nS
- neuron_to_neuron_exc_syn_conductance: 4.2 nS

