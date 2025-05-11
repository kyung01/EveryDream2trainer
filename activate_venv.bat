call venv/scripts/activate.bat
call set TF_ENABLE_ONEDNN_OPTS=0
call py train.py --config train.json