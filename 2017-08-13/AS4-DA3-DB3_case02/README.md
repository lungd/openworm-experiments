# Override default parameters with:
## Connections to include:
- AVA.-AVA.*
- AVA.-AVB.*
- AVB.-AVB.*
- AVB.-AVA.*
- AVB.-AS.*
- AVB.-DB.*
- ^AS\d+-DA.+$
- ^DA\d+-AS\d+_GJ$
- ^DA\d+-DB\d+$
- ^DB\d+-AS\d+$
- AVA.-DA.*
- DA\d+-AVA.*
- DB\d+-AVB.*
- AS\d+-M(D|V)(L|R).*
- DA\d+-M(D|V)(L|R).*
- DB\d+-M(D|V)(L|R).*
- M(D|V)(L|R)\d+-M(D|V)(L|R).*

## Change polarity of connections:
- AVAR-AVBL: inh
- AVBR-AVAR: inh
- AVBL-AVAR: inh
- AVAL-AVBR: inh
- AVAL-AVBL: inh
- AVBL-AVAL: inh
- AVAR-AVBR: inh
- DB3-AS4: inh
- AVBR-AVAL: inh

## Inject current:
- Cell: AVBL
    - delay: 500ms
    - end: 1900ms
    - amplitude: 2pA
- Cell: AVBR
    - delay: 500ms
    - end: 1900ms
    - amplitude: 2pA
- Cell: AS4
    - delay: 50ms
    - end: 1900ms
    - amplitude: 10.0pA

## Other parameters:
- DB3_to_AVBL_elec_syn_gbase: 0.001 nS
- DA3_to_AVAR_elec_syn_gbase: 0 nS
- DA3_to_DB3_exc_syn_conductance: 2.2 nS
- DA3_to_AVAL_elec_syn_gbase: 0 nS
- neuron_to_neuron_exc_syn_conductance: 4.2 nS
- AVBR_to_DB3_elec_syn_gbase: 0.001 nS
- DB3_to_AVBR_elec_syn_gbase: 0.001 nS
- AVBL_to_DB3_elec_syn_gbase: 0.001 nS
- AVAL_to_DA3_elec_syn_gbase: 0 nS
- AVAR_to_DA3_elec_syn_gbase: 0 nS
- neuron_to_neuron_inh_syn_conductance: 7.2 nS

