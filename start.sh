docker run \
    --name jupyterlite -it --rm \
    -v $(pwd):/workingdir \
    --user $(id -u):$(id -g) \
    jupyterlite \
    bash