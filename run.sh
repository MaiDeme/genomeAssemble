snakemake --configfile test/config_test.yaml --use-conda --rulegraph | dot -Tpng > images/rulegraph.png
snakemake --configfile test/config_test.yaml --use-conda --dag | dot -Tpng > images/dag.png
snakemake --configfile test/config_test.yaml --use-conda --filegraph | dot -Tpng > images/filegraph.png
snakemake --configfile test/config_test.yaml --use-conda