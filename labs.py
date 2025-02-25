from cadCAD.configuration.utils import config_sim

from templates.cadcad.model.experiment import exp
from templates.cadcad.model.params import SIM_CONFIG, GENESIS_STATES
from templates.cadcad.model.structure import PARTIAL_STATE_UPDATE_BLOCKS



model_dir ="templates.cadcad.model"
sim_params = config_sim(SIM_CONFIG)
exp.append_configs(
    sim_configs=sim_params,
    initial_state=GENESIS_STATES,
    partial_state_update_blocks= PARTIAL_STATE_UPDATE_BLOCKS
)

