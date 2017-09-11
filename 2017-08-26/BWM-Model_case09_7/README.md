# Override default parameters with:
## Connections to include:
- DB2-MDL12
- DD2-MDL12

## Inject current:
- Cell: MDL12
    - delay: 3000ms
    - end: 3000ms
    - amplitude: 0.5pA
- Cell: MDL12
    - delay: 6500ms
    - end: 3000ms
    - amplitude: -1pA

## Other parameters:
- custom_component_type_gate_overrides: {'ca_muscle__m__scale': '3.5 mV', 'ca_muscle__h__tau': '7 ms', 'k_muscle__n__scale': '8.5 mV', 'ca_muscle__m__midpoint': '-3.7 mV', 'k_muscle__n__tau': '55 ms', 'ca_muscle__m__tau': '1 ms', 'k_muscle__n__midpoint': '3 mV'}
- muscle_k_slow_erev: -83 mV
- muscle_ca_boyle_cond_density: 0.284 mS_per_cm2
- muscle_leak_cond_density: 0.0062 mS_per_cm2
- muscle_leak_erev: -17 mV
- muscle_k_slow_cond_density: 0.964 mS_per_cm2
- muscle_ca_boyle_erev: 36 mV

