from setuptools import setup, find_packages

setup(
    name="ai_colorectal_survival_ml",
    version="0.0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
