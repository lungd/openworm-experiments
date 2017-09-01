This is a repository for some OpenWorm experiments

Here we blog about our daily activity on understading the brain of the worm through simulated experiments with OpenWorm simulation platforms. 

Daily reports contains the properties of the performed simulations.

In the early experiments, from 7-14 to 7-31, the goal is to create a propagating wave in a sequence of muscles in the c. elegans.  In some experiments, automatic optimization is used to optimize parameters.  However, too many parameters to optimize along creates the problem of being stuck in a local minimum.  Therefore, further experiments use a targeted approach to select a subset of parameters to allow optimization to occur over.  Some results from automated optimization are being fed into future experiments that hand-tuning is being done on.

The rationale for the subsets of circuits that are being chosen are partially based on the goal, but also based on a decomposition process for simplicity of optimization.

The first goal was to go from simultaneous activation of muscles to getting the first spike time to be staggered.  The [first experiment on 7-14](https://github.com/lungd/openworm-experiments/blob/master/2017-07-14/AVB-DB-DorsalMuscles_Case1/README.md) did not produce good results for first spike time because it hit a local minimum.  The next [experiment on 7-24](https://github.com/lungd/openworm-experiments/blob/master/2017-07-24/AVB-DB-DorsalMuscles_Case2/README.md) used a subset of parameters but produced reasonable first spike times.  The [experiment on 7-25](https://github.com/lungd/openworm-experiments/blob/master/2017-07-25/AVB-DB-DorsalMuscles_Case3/README.md) attempted to optimize the spike frequency of the muscles, and was successful in spike frequency but then spike timing of subsequent spikes had jitter.  [Experiments on 7-31](https://github.com/lungd/openworm-experiments/blob/master/2017-07-31/README.md) began hand tuning the spike timing of subsequent spikes.

