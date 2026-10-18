FROM mambaorg/micromamba:1.5.10

USER root
WORKDIR /project
COPY --chown=$MAMBA_USER:$MAMBA_USER workflow/envs/workflow.yaml /tmp/workflow.yaml
USER $MAMBA_USER
RUN micromamba install --yes --name base --file /tmp/workflow.yaml \
    && micromamba clean --all --yes
ENV PATH=/opt/conda/bin:$PATH
COPY --chown=$MAMBA_USER:$MAMBA_USER . /project
WORKDIR /project
ENTRYPOINT ["snakemake", "--snakefile", "workflow/Snakefile"]
CMD ["--cores", "2"]
