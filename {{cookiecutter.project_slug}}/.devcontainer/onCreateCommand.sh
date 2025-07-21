conda init bash
conda run -n {{ cookiecutter.conda_env_name }}_dev bash -c "pip install -e /workspaces/{{ cookiecutter.project_slug }} "
echo "loading done :)"
