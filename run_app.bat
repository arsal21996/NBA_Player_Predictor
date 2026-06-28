@echo off
cd /d "%~dp0"

call conda activate jupyterenv

streamlit run app.py

pause