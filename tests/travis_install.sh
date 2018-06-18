#!/bin/bash
# This script is meant to be called by the "install" step defined in
# .travis.yml. See http://docs.travis-ci.com/ for more details.
# The behavior of the script is controlled by environment variabled defined
# in the .travis.yml in the top level folder of the project.
#
# This script is taken from Scikit-Learn (http://scikit-learn.org/)
#
# THIS SCRIPT IS SUPPOSED TO BE AN EXAMPLE. MODIFY IT ACCORDING TO YOUR NEEDS!

set -e

if [[ "$DISTRIB" == "conda" ]]; then
    # Deactivate the travis-provided virtual environment and setup a
    # conda-based environment instead
    deactivate

    if [[ -f "$HOME/miniconda/bin/conda" ]]; then
        echo "Skip install conda"
    else
      rm -rf "$HOME/miniconda"
      # ^  Caching creates empty dir that conflicts with conda installer

      # Use the miniconda installer for faster download / install of conda
      # itself
      wget http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh \
          -O miniconda.sh
      chmod +x miniconda.sh && ./miniconda.sh -b -p $HOME/miniconda
    fi
    export PATH=$HOME/miniconda/bin:$PATH
    conda update --yes conda

    # Configure the conda environment and put it in the path using the
    # provided versions
    conda create -p ./.venv --yes python=${PYTHON_VERSION} pip virtualenv
    source activate ./.venv
fi


if [[ "$COVERAGE" == "true" ]]; then
    pip install coverage coveralls
fi

# for all
pip install -U pip setuptools
pip install sphinx
pip install tox

travis-cleanup() {
  printf "Cleaning up environments ... "  # printf avoids new lines
  if [[ "$DISTRIB" == "conda" ]]; then
    # Force the env to be recreated next time, for build consistency
    source deactivate
    conda remove -p ./.venv --all --yes
    rm -rf ./.venv
  fi
  echo "DONE"
}
