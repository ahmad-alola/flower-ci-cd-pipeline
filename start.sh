cd frontend
pip install -r requirements.txt
streamlit run app.py

pip install -r requirements.txt
python train.py
uvicorn app.main:app --reload

http://127.0.0.1:8000/health

http://127.0.0.1:8000/predict?sepal_length=5.1&sepal_width=3.5&petal_length=1.4&petal_width=0.2


pip install -r requirements.txt
streamlit run app.py

#!/bin/bash