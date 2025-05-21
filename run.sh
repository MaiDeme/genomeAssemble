snakemake --use-conda --use-singularity -n --rulegraph  | dot -Tpng > images/rulegraph.png 
snakemake --use-conda --use-singularity -n --filegraph  | dot -Tpng > images/filegraph.png
snakemake --use-conda --use-singularity -n --dag   | dot -Tpng > images/dag.png
#snakemake --use-conda --use-singularity --cores 20