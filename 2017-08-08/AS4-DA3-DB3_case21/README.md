# Override default parameters with:
## Connections to include:
- ^AS\d+-DA.+$
- ^DA\d+-DB\d+$
- ^DB\d+-AS\d+$
- AVB.-DB.*
- DB\d+-AVB.*
- DA\d+-M(D|V)(L|R).*
- DB\d+-M(D|V)(L|R).*
- M(D|V)(L|R)\d+-M(D|V)(L|R).*
- DA\d+-DA.*
- DB\d+-DB.*
- AS\d+-AS.*
- AVB.-AS.*
- AVB.-AVB.*

## Change polarity of connections:
- DB7-AS10: inh
- DB4-AS6: inh
- DB5-AS7: inh
- DB1-AS2: inh
- DB1-AS1: inh
- DB1-AS4: inh
- DB5-AS8: inh
- DB2-AS4: inh
- DB7-AS11: inh
- DB3-AS5: inh
- DB3-AS4: inh
- DB6-AS8: inh
- DB6-AS9: inh
- DB2-AS3: inh

## Inject current:
- Cell: AVBL
    - delay: 50ms
    - end: 1900ms
    - amplitude: 1pA
- Cell: AVBR
    - delay: 50ms
    - end: 1900ms
    - amplitude: 1pA
- Cell: AS4
    - delay: 50ms
    - end: 1900ms
    - amplitude: 15.0pA

## Other parameters:
- neuron_to_neuron_inh_syn_conductance: 5.2 nS
- neuron_to_neuron_exc_syn_conductance: 4.2 nS

