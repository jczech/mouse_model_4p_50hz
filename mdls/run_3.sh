#!/bin/bash

START=2041
END=2140

for ((a = START; a <= END; a=a+1)); do
  ./mcell-binary-out -quiet -seed ${a} AZmodel_mouse_main.mdl >> run.1.log
done
