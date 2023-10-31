# test if the project can be installed

PATH_FOLDER="/tmp/test/"
NAME_PROJECT="xxxx_testproject"

# rm -rf PATH_FOLDER
mkdir -p $PATH_FOLDER

python build_project.py \
    --project-path=$PATH_FOLDER \
    --project-name=$NAME_PROJECT \
    --user-name="obiwan" \
    --conda-env-name="xxxx_testmycondaenv"

cd $PATH_FOLDER/$NAME_PROJECT
git init
make install

make test
make check -k

# cd
# rm -rf $PATH_FOLDER/$NAME_PROJECT
