let
    pkgs = import <nixpkgs> {};
in
    { stdenv ? pkgs.stdenv }:

    stdenv.mkDerivation {
        name = "GoPy";
        buildInputs = [
            pkgs.python3
        ];
    }
