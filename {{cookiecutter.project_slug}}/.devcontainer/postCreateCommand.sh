# make the terminal always activated with the correct env
echo "conda activate {{ cookiecutter.conda_env_name }}_dev" >> ~/.bashrc
echo "cd {{ cookiecutter.project_slug }}" >> ~/.bashrc

echo "alias ll='ls -lah'" >> ~/.alias

echo "source ~/.alias" >> ~/.bashrc
