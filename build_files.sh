echo "Building the project"
python-3.10.6 -m pip install -r requirment.txt

echo "Make Migration..."
python-3.10.6 manage.py makemigrations --noinput
python-3.10.6 manage.py migrate --noinput

echo "Build end .."