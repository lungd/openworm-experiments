# Override default parameters with:
## Connections to include:
- AVA.-AVB.*
- AVB.-AVA.*
- ^AS\d+-DA\d+$
- ^DA\d+-DB\d+$
- ^DB\d+-AS\d+$
- AVA.-DA.*
- AVB.-DB.*
- DA\d+-AVA.*
- DB\d+-AVB.*
- DA\d+-M(D|V)(L|R).*
- DB\d+-M(D|V)(L|R).*
- M(D|V)(L|R)\d+-M(D|V)(L|R).*
- DA\d+-DA.*
- DB\d+-DB.*
- AS\d+-AS.*

## Change polarity of connections:
- DB3-AS4: inh

## Inject current:
- Cell: AVBL
    - delay: 50ms
    - end: 1900ms
    - amplitude: 15pA
- Cell: AVBR
    - delay: 50ms
    - end: 1900ms
    - amplitude: 15pA
- Cell: AS4
    - delay: 50ms
    - end: 1900ms
    - amplitude: 1pA

## Other parameters:
- neuron_to_neuron_inh_syn_conductance: 2.5 nS
- neuron_to_neuron_exc_syn_conductance: 1.2 nS

