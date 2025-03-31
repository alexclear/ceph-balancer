from setuptools import setup, find_packages

setup(
    name="ceph-balancer",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Add your dependencies here
    ],
    python_requires=">=3.6",
    author="Jonas Jelten",
    author_email="jj@sft.lol",
    description="A tool for balancing Ceph clusters",
    license="GPLv3+",
) 