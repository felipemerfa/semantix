#!/bin/bash

sh unzip.sh
spark-submit nasa.py dataset_nasa
rm dataset_nasa
