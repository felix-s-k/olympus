#!/usr/bin/env python

from olympus import Planner, Surface
from olympus.planners import planner_names
from olympus.surfaces import surface_names
import pytest

# TODO: now tests only that they run, but later on for a few simple cases like Dejong we should probably test that
#  the minimum/maximum is found (approximately)

CONT_SURFACES = [
    'CatDejong', 'CatSlope', 'Dejong', 'Zakharov',
    'Matterhorn', 'Rastrigin', 'Kilimanjaro',
    'Rosenbrock', 'CatMichalewicz', 'NarrowFunnel',
    'DiscreteDoubleWell', 'MontBlanc', 'K2', 'Denali',
    'Schwefel', 'DiscreteMichalewicz', 'StyblinskiTang',
    'Levy', 'CatAckley', 'LinearFunnel', 'GaussianMixture',
    'Branin', 'AckleyPath', 'HyperEllipsoid', 'Everest',
    'Michalewicz', 'CatCamel', 'DiscreteAckley',
]

CAT_SURFACES = [
    'CatDejong', 'CatSlope' 'CatAckley', 'CatCamel', 'CatSlope'
]

CONT_PLANNERS = [
    'Snobfit', 'Phoenics', 'Slsqp', 'Genetic',
    'ConjugateGradient', 'RandomSearch', 'DifferentialEvolution',
    'ParticleSwarms', 'SteepestDescent', 'Cma', 'Grid',
    'Hyperopt', 'BasinHopping', 'Gpyopt', 'Lbfgs',
    'LatinHypercube', 'Sobol', 'Gryffin', 'Simplex',
]

CAT_PLANNERS = []


cont_tuples = []
for planner in CONT_PLANNERS:
    for surface in CONT_SURFACES:
        cont_tuples.append((planner, surface))

cat_tuples = []
for planner in CAT_PLANNERS:
    for surface in CAT_SURFACES:
        cat_tuples.append((planner, surface))


@pytest.mark.parametrize("planner, surface", cont_tuples)
def test_cont_surface_optimization(planner, surface):
    surface = Surface(kind=surface, param_dim=2)
    planner = Planner(kind=planner, goal='minimize')
    campaign = planner.optimize(emulator=surface, num_iter=3)

    #values = campaign.get_values()
    # now check that we are close to the minimum
    #assert np.min(values) < 0.5


# @pytest.mark.parametrize("planner, surface", cat_tuples)
# def test_cat_surface_optimization(planner, surface):
#     surface = Surface(kind=surface, param_dim=2, num_opts=21)
#     planner = Planner(kind=planner, goal='minimize')
#     campaign = planner.optimize(emulator=surface, num_iter=3)
