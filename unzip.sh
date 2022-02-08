#!/bin/bash

echo "Descompactacao de arquivos"
echo "Arquivos:        " 
ls datasets/*

echo "Inicio da descompactacao dos arquivos"
cp datasets/*.gz .
gzip -d -f ${origem}*gz 
cat NASA* > dataset_nasa
echo "Dataset preparado: " 
ls dataset*

rm -rf NASA*

echo "Fim da descompactacao dos arquivos"
