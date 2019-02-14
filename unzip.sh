#!/bin/bash

echo "Descompactacao de arquivos"
echo "Arquivos:        " 
ls zip/*

echo "Inicio da descompactacao dos arquivos"
cp zip/*.gz .
gzip -d -f ${origem}*gz 
cat NASA* > dataset_nasa
echo "Dataset preparado: " 
ls dataset*

rm -rf NASA*

echo "Fim da descompactacao dos arquivos"
