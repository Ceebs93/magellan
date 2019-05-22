#!/usr/bin/env bash

# - To the user:
# - Source this script while standing in the root dir of Magellan

###############################################
### --- Exporting environment variables --- ###
###############################################

# - Local path to magellan 
export Magellan_path=$(pwd)

# - Add path of python modules to PYTHONPATH
python_modules_path=${Magellan_path}/python/modules
export PYTHONPATH=${python_modules_path}:${PYTHONPATH}


# - Measurement directiories
measurement_python_modules_path=${Magellan_path}/data/measurements
export PYTHONPATH=${measurement_python_modules_path}:${PYTHONPATH}

# - Add cmd to PATH
cmd_path=${Magellan_path}/cmd
export PATH=${cmd_path}:${PATH}

# - Matplotlib styles directory
export ENV_MATPLOTLIB_STYLES_DIR=${Magellan_path}/python/matplotlib/styles/

# - Jupyter setup scripts
export ENV_JUPYTER_SETUPS_DIR=${Magellan_path}/python/jupyter/setups/



## -- Local configuration stored in `setup_local.sh`

if [ -f setup_local.sh ]; then
    echo "Found setup_local.sh, sourcing it..."
    source setup_local.sh
fi
