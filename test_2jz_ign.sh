#!/bin/sh

./ts_execute.py hw_qc_mode

while true; do 

./ts_execute.py bench_setpin PJ3
./ts_execute.py bench_setpin PJ4
./ts_execute.py bench_setpin PI15
./ts_execute.py bench_setpin PJ0
./ts_execute.py bench_setpin PH3
./ts_execute.py bench_setpin PH4

sleep 0.5

./ts_execute.py bench_clearpin PJ3
./ts_execute.py bench_clearpin PJ4
./ts_execute.py bench_clearpin PI15
./ts_execute.py bench_clearpin PJ0
./ts_execute.py bench_clearpin PH3
./ts_execute.py bench_clearpin PH4


sleep 0.5 
done
