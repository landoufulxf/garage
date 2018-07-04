from garage.algos import TRPO
from garage.baselines import LinearFeatureBaseline
from garage.envs import normalize
from garage.envs.util import spec
from garage.policies import CategoricalMLPPolicy
from garage.misc.instrument import run_experiment
from garage.envs.bullet_env import CartPoleBulletEnv
# import time
# import pybullet as p
# import pybullet_data 


def run_task(*_):
	env = CartPoleBulletEnv(renders=False)
	env.reset()
	env.horizon = 40

	policy = CategoricalMLPPolicy(env_spec=spec(env), hidden_sizes=(32, 32))

	baseline = LinearFeatureBaseline(env_spec=spec(env))

	algo = TRPO(
	        env=env,
	        policy=policy,
	        baseline=baseline,
	        batch_size=4000,
	        max_path_length=env.horizon,
	        n_itr=50,
	        discount=0.99,
	        step_size=0.01,
	        # Uncomment both lines (this and the plot parameter below) to enable
	        # plotting
	        # plot=True,
	    )
	algo.train()

run_experiment(
    run_task,
    # Number of parallel workers for sampling
    n_parallel=1,
    # Only keep the snapshot parameters for the last iteration
    snapshot_mode="last",
    # Specifies the seed for the experiment. If this is not provided, a random
    # seed will be used
    seed=1,
    # plot=True,
)

