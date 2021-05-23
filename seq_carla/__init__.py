from gym.envs.registration import register

register(
    id='seq_carla-v0',
    entry_point='seq_carla.envs:CarlaEnv',
)