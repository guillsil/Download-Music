#!/bin/bash

directorio="/.venv"

preparar_entorno() {
    python3 -m venv .venv
    source .venv/bin/activate
}

if [ "$#" -eq 1 ]; then
    if [ -d "$directorio" ];then
        python3 -m pip install "$1"
    else
        preparar_entorno
        python3 -m pip install "$1"
    fi
    echo "Se instalo correctamente el paquete: "$1"."
else
    preparar_entorno
    echo "Se creo correctamente el entorno virtual .venv"
    exit 1
fi


