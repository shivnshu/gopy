let
    pkgs = import <nixpkgs> {};
in
    { stdenv ? pkgs.stdenv }:

    stdenv.mkDerivation {
        name = "GoPy";
        buildInputs = [
            pkgs.python3
            pkgs.python36Packages.ipython
            pkgs.python36Packages.ply
            pkgs.python36Packages.graphviz
        ];
    }
