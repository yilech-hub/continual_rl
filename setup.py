from setuptools import setup, find_packages

setup(
    name='continual_rl',
    version='1.0',
    description='Continual reinforcement learning baselines and standard experiments.',
    author='Sam Powers',
    author_email='snpowers@cs.cmu.edu',
    packages=find_packages(),
    py_modules=['continual_rl.available_policies', 'continual_rl.experiment_specs'],
    python_requires=">=3.8,<3.11",
    install_requires=[
        "numpy==1.23.5",
        "tensorboard",
        "torch-ac",
        "gym[atari,accept-rom-license]==0.25.2",
        "ale-py>=0.7,<0.9",
        "moviepy",
        "dotmap",
        "psutil",
        "opencv-python",
    ],
)
