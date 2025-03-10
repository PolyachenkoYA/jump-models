# ?? do manually because "bash <this>" gets errors

#module purge
module load anaconda3/2024.10
conda activate jumpmodel

nohup bash -c "python time_cycle.py" &

# 1) // change time in time_cycle.py
# 2) module load anaconda3/2024.10; conda activate jumpmodel; nohup bash -c "python time_cycle.py" &
