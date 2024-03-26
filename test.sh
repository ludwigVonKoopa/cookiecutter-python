rm -rf /tmp/to_delete
mkdir /tmp/to_delete
cookiecutter .  -o /tmp/to_delete -f --no-input
cd /tmp/to_delete/awesome_project

git init
git add *
git commit -m "test"

LIBRARY_PATH=$(python -c "import sys; import os; print(os.path.join(os.path.dirname(os.path.dirname(sys.executable)), 'lib', 'python3.10', 'site-packages', 'awesome_project'))")
rm -rf $LIBRARY_PATH*
conda activate test_ipp
make install
make doc
