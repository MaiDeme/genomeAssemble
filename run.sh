#snakemake --configfile test/config_test.yaml --use-conda --rulegraph | dot -Tpng > images/rulegraph.png
#snakemake --configfile test/config_test.yaml --use-conda --filegraph | dot -Tpng > images/filegraph.png
#snakemake --configfile test/config_test.yaml --use-conda --use-singularity

snakemake --use-conda --rulegraph | dot -Tpng > images/rulegraph.png
snakemake --use-conda --filegraph | dot -Tpng > images/filegraph.png
snakemake --use-conda --use-singularity --cores 10