#!/bin/bash
#SBATCH --job-name=basic_sim
#SBATCH --account=rmacc-general
#SBATCH --partition=acpu
#SBATCH --qos=cpu-normal
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --time=00:05:00
#SBATCH --mem=1G
#SBATCH --output=basic_sim_%j.out
#SBATCH --error=basic_sim_%j.err

python3 basic_sim.py
