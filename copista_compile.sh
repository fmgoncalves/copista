#! /bin/sh

ROOT_PATH=`pwd`
DOCUMENT_PATH=$ROOT_PATH"/docs"
BIN_PATH=$ROOT_PATH"/bin"
BASE_PATH=$ROOT_PATH"/base"



TEXINPUTS=$BASE_PATH: pdflatex -interaction=batchmode -output-directory=$BIN_PATH $DOCUMENT_PATH/$1/$1.tex
TEXINPUTS=$BASE_PATH: pdflatex -interaction=batchmode -output-directory=$BIN_PATH $DOCUMENT_PATH/$1/$1.tex
