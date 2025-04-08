docker run \
    --name jupyterlite -it --rm \
    -v $(pwd):/workingdir \
    -v $(readlink -f ..):/data \
    --user $(id -u):$(id -g) \
    jupyterlite \
    bash