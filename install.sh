#!/bin/bash

SITEDIR=$(python3.5 -m site --user-site)
mkdir -p "$SITEDIR"
cd brainfuck_kernel
PTH=$(pwd)
echo "$PTH"> "$SITEDIR/bfkernel.pth"
