rm -rf /tmp/to_delete
mkdir /tmp/to_delete
cookiecutter .  -o /tmp/to_delete -f --no-input
cd /tmp/to_delete/awesome_project

git init
git add *
git commit -m "test"

rm -rf /tcenas/home/cbusche/miniconda3/envs/test_ipp/lib/python3.10/site-packages/awesome_project*
conda activate test_ipp
make install
make doc
