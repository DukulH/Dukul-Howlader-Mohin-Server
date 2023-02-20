echo " BUILD START"
python3.10 -m pip install -r requirements.txt

echo "Make Migration..."
python3.10 manage.py makemigrations --noinput
python3.10 manage.py migrate --noinput

echo "Build end .."