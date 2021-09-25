import org.fairdatapipeline.simpleModel as simpleModel
import org.fairdatapipeline.api as pipeline
import os

token = os.environ.get('FDP_REGISTRY_DIR') + '/token'
script = os.environ.get('FDP_CONFIG_DIR') + '/SEIRSModelRun.py'
config = os.environ.get('FDP_CONFIG_DIR') + '/SEIRSconfig.yaml'

handle = pipeline.initialise(token, config, script)

initial_parameters = pipeline.link_read('SEIRS_model/parameters')
model_output = pipeline.link_write(handle, 'SEIRS_model/results/model_output')
model_plot = pipeline.link_write(handle, 'SEIRS_model/results/figure')

# Model Code
states = {
    's': 0.999,
    'e': 0.001,
    'i': 0,
    'r': 0
}

init_params = simpleModel.readInitialParameters(initial_parameters, False)

alpha = init_params['alpha']
beta = init_params['beta']
inv_gamma = init_params['inv_gamma']
inv_omega = init_params['inv_omega']
inv_mu = init_params['inv_mu']
inv_sigma = init_params['inv_sigma']
R0 = init_params['R0']

sm = simpleModel.SEIRS_Model(states,
    1000, 
    5, 
    alpha, 
    beta, 
    inv_gamma, 
    inv_omega, 
    inv_mu, 
    inv_sigma)

simpleModel.SEIRS_Plot(sm, model_plot)

simpleModel.write_model_to_csv(sm, model_output)

pipeline.finalise(token, handle)