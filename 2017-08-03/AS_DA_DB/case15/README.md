# Override default parameters with:
## Connections to include:
- AS*-DA*
- DA*-DB*
- DB*-AS*
- AVA*-DA*
- AVB*-DB*
- AVB*-DB*_GJ
- DA*-muscles
- DB*-muscles
- muscles-muscles

## Change polarity of connections:
- DB7-AS10: inh
- DB4-AS6: inh
- DB5-AS7: inh
- DB1-AS2: inh
- DB1-AS1: inh
- DB1-AS4: inh
- DB5-AS8: inh
- DB7-AS11: inh
- DB3-AS5: inh
- DB3-AS4: inh
- DB6-AS8: inh
- DB6-AS9: inh
- DB2-AS3: inh

## Inject current:
- Cell: AVAL
    - delay: 50ms
    - end: 1900ms
    - amplitude: 5pA
- Cell: AVAR
    - delay: 50ms
    - end: 1900ms
    - amplitude: 5pA
- Cell: AVBL
    - delay: 50ms
    - end: 1900ms
    - amplitude: 15pA
- Cell: AVBR
    - delay: 50ms
    - end: 1900ms
    - amplitude: 15pA

## Other parameters:
- neuron_to_neuron_exc_syn_conductance: 1.2 nS

