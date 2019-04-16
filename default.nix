let
    pkgs = import <nixpkgs> {};
in
    { multiStdenv ? pkgs.multiStdenv }:

    multiStdenv.mkDerivation {
        name = "GoPy";
        buildInputs = [
            pkgs.python3
            pkgs.python36Packages.ipython
            pkgs.python36Packages.ply
            pkgs.python36Packages.graphviz
            pkgs.gcc_multi
        ];
        #GOPY_PATH="${HOME}/Projects/gopy";
    }
