#!/bin/bash

START=1841
END=1940

for ((a = START; a <= END; a=a+1)); do
  ./mcell-binary-out -quiet -seed ${a} AZmodel_mouse_main.mdl >> run.1.log
done
