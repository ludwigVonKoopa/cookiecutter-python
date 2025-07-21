
FROM debian:bullseye-slim


# --- Install system dependencies ---
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        git \
        # git-lfs \
        # cmake \
        # wget \
        # unzip \
        # autoconf \
        # libtool \
        # pkg-config \
        ca-certificates \
        curl \
        # bzip2 \
        # openssh-client \
        make && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get autoremove -y && \
    apt-get autoclean -y

# --- Install Miniconda ---
ENV CONDA_DIR=/opt/conda
ENV PATH=$CONDA_DIR/bin:$PATH

# --- Set environment variables --
ENV WORKDIR=/opt/project
WORKDIR ${WORKDIR}


# --- Install conda ---
RUN curl -L https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -o miniconda.sh && \
    bash miniconda.sh -b -p $CONDA_DIR && \
    rm miniconda.sh && \
    conda config --set always_yes yes --set changeps1 no && \
    echo "channel_priority: strict\nchannels:\n  - conda-forge" > ${CONDA_DIR}/.condarc && \
    echo "channel_priority: strict\nchannels:\n  - conda-forge" > /root/.condarc && \
    conda update -q -c conda-forge conda && \
    conda install -c conda-forge mamba -n base && \
    conda clean --all -y

# RUN curl --help
# RUN curl -L https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -o miniconda.sh
# RUN bash miniconda.sh -b -p $CONDA_DIR
# RUN rm miniconda.sh
# RUN conda config --set always_yes yes --set changeps1 no
# RUN echo "channel_priority: strict\nchannels:\n  - conda-forge" > ${CONDA_DIR}/.condarc
# RUN echo "channel_priority: strict\nchannels:\n  - conda-forge" > /root/.condarc
# RUN conda update -q -c conda-forge conda
# RUN conda install -c conda-forge mamba -n base
# RUN conda clean --all -y

ENV SHELL="/bin/bash "
RUN conda init bash
ENV PATH=/opt/conda/bin:$PATH

RUN conda config --show-sources


COPY environment_dev.yml ${WORKDIR}

# --- Create Python env and install metimage_prototype using Makefile ---
# --- Create conda environment using mamba ---
RUN mamba env create -f environment_dev.yml -n {{ cookiecutter.conda_env_name }}_dev && mamba clean --all -y


ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME


# --- Default command ---
CMD ["/bin/bash"]
