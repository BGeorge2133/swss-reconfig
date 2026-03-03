from dataclasses import dataclass
import copy

@dataclass
class HostInformation:
    host_id: int  # host id in integer
    host_name: str  # host name
    ip_addr: str  # host WAN IP address used for reconfiguration message
    nic_id: int  # NIC id in integer for the reconfigurable interface

@dataclass
class SwitchConfiguration:
    
    """
    This is a generic class that we want to use to describe a particular
    configuration of a switch.
    connections: a list of tuples, where each tuple is a truplet of integers
    representing the connection between two hosts and the wavelength ID.
    Wavelength ID is ignored for now, but it is used to identify the connection.
    duration: an integer representing the duration of the configuration im ms
    ring_configs: a dictionary mapping ring IDs to their voltage
    """

    connections: list[tuple[int, int, int]]  # list of connections (host1, host2, wavelength_id)
    duration: int
    ring_configs: tuple[int, float]
    

SWITCH_CONFIG_1 = SwitchConfiguration(
    connections=[
        (1, 2, 1), 
        (2, 1, 1),
        (3, 4, 1), 
        (4, 3, 1),
    ], 
    duration=2000,
    ring_configs={
        (79, 1.67),
        (78, 1.59),
        (77, 1.61),
        (73, 1.68),
        (64, 1.46),

        (80, 1.49),
        (81, 1.49),
        (92, 1.55),
        (91, 1.55),
        (53, 1.63),

        (8, 1.89),
        (7, 1.85),
        (23, 1.85),
        (24, 1.86),
        
        (20, 1.74),
        (16, 1.69),
        (15, 1.70),
        (14, 1.75),
        (41, 1.89),
    }
)

SWITCH_CONFIG_2 = SwitchConfiguration(
    connections=[
        (1, 4, 1), 
        (4, 1, 1),
        (2, 3, 1), 
        (3, 2, 1),
    ], 
    duration=2000,
    ring_configs={
        (69, 1.45),
        (70, 1.49),
        (23, 1.50),
        (24, 1.50),
        (37, 1.74),

        (20, 1.74),
        (16, 1.69),
        (77, 1.72),
        (73, 1.79),
        (64, 1.47),

        (79, 1.66),
        (78, 1.59),
        (15, 1.60),
        (14, 1.62),
        (41, 1.89),

        (4, 1.94),
        (3, 1.87),
        (90, 1.86),
        (89, 1.85),
        (53, 1.63),
    }
)

def config_direct_switch(cfg_old, cfg_new): 
    cfg_direct = copy.deepcopy(cfg_new)
    old_rings = set([config[0] for config in cfg_old.ring_configs])
    new_rings = set([config[0] for config in cfg_new.ring_configs])
    
    for ring in old_rings:
        if ring not in new_rings:
            cfg_direct.ring_configs.add((ring, 0))
    
    # print(f"Direct config {cfg_old} to {cfg_new}: \n{cfg_direct}")
    return cfg_direct


SW_CONFIGS = [
    config_direct_switch(SWITCH_CONFIG_2, SWITCH_CONFIG_1),
    config_direct_switch(SWITCH_CONFIG_1, SWITCH_CONFIG_2),
    
]

HOSTS = [
    
]