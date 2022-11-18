echo [$(date)]:"start"
echo [$(date)]:"create conda env"
conda create --prefix ./envv python=3.8 -y
echo [$(date)]:"activate env"
source activate ./envv
echo [$(date)]:"pip install start"
pip install -r requirements_dev.txt
echo [$(date)]:"end"