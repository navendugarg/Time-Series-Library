from pathlib import Path

from setuptools import find_packages, setup

BASE_DIR = Path(__file__).parent
README = (BASE_DIR / "README.md").read_text(encoding="utf-8")

INSTALL_REQUIRES = [
    "torch>=2.3.1,<3.0.0",
    "numpy>=1.26.4,<2.0.0",
    "pandas>=2.1.4,<2.3.0",
    "scikit-learn>=1.3.0,<1.6.0",
    "scipy>=1.11.4,<2.0.0",
    "sktime>=0.27.0,<0.36.0",
    "matplotlib>=3.8.0,<3.9.0",
    "tqdm>=4.66.1,<5.0.0",
    "einops>=0.8.0,<1.0.0",
    "local-attention>=1.9.14",
    "reformer-pytorch>=1.4.4",
    "patool>=1.12",
    "sympy>=1.12,<2.0",
    "PyWavelets>=1.5.0,<1.7.0",
    "datasets>=2.19.0,<3.0.0",
    "huggingface-hub>=0.20.0,<1.0.0",
    "statsmodels>=0.14.2,<1.0.0",
    "arch>=6.3.0,<7.0.0",
]

EXTRAS_REQUIRE = {
    "mamba": ["mamba-ssm>=1.2.0"],
    "dev": ["black", "ruff", "pytest"],
}

CLASSIFIERS = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Topic :: Scientific/Engineering :: Artificial Intelligence",
    "Topic :: Scientific/Engineering :: Information Analysis",
]


setup(
    name="time-series-library",
    version="0.2.0",
    description="Comprehensive deep time series benchmark for forecasting, imputation, anomaly detection, and classification.",
    long_description=README,
    long_description_content_type="text/markdown",
    author="THUML (Tsinghua University)",
    license="MIT",
    python_requires=">=3.9",
    packages=find_packages(include=["data_provider*", "exp*", "layers*", "models*", "utils*", "tslib_wrapper*"]),
    py_modules=["run"],
    include_package_data=True,
    package_data={"": ["README.md", "LICENSE"]},
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    classifiers=CLASSIFIERS,
    project_urls={
        "Homepage": "https://github.com/thuml/Time-Series-Library",
        "Issues": "https://github.com/thuml/Time-Series-Library/issues",
    },
)
