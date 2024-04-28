# Dockerfile to build, run and train the Heilman and Sagae (2015)
# RST discourse parser on the RST Discourse Treebank (RST-DT)

FROM nlpbox/nlpbox-base:22.04

RUN apt-get update -y && \
    apt-get install -y build-essential

# install conda
WORKDIR /opt
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-py310_24.3.0-0-Linux-x86_64.sh -O /opt/miniconda.sh \
    && chmod +x /opt/miniconda.sh \
    && bash /opt/miniconda.sh -b -p /opt/miniconda \
    && rm /opt/miniconda.sh

# Add Miniconda to PATH
ENV PATH="/opt/miniconda/bin:${PATH}"

# add path for nltk tagger model
ENV NLTK_DATA="$HOME/nltk_data"

# Initialize Conda and create the environment in one RUN command
# download NLTK tagger model
RUN conda init bash && \
    . /opt/miniconda/etc/profile.d/conda.sh && \
    conda create -y -n rstenv -c conda-forge -c ets python=3.10 rstfinder && \
    pip install python-zpar && \
    conda activate rstenv && \
    python -m nltk.downloader maxent_treebank_pos_tagger punkt
