#! /usr/bin/env bash

if [ ! -f $1 ]; then
    echo "File not found" >&2
	exit 1
fi

exec 1>res

echo 'Count'
cat $1 | wc -l
echo ''

echo 'MethodCount'
cat $1 | awk -F '[" ]' '{print $7}' | sort | uniq -c | awk '{print $2,$1}'
echo ''

echo 'BiggestQuerys'
cat $1 | awk -F '[" ]' '{print $12,$11,$8}' | sort -r | head -10 | awk '{print $3,$2,$1}'
echo ''

echo 'ClientErrors'
cat $1 | awk -F '[" ]' '$11>=400 && $11<500 {print $11,$1,$8}' | uniq -c -f 2 | sort -k 1,1rn | head -10 | awk '{print $4,$3,$2,$1}'
echo ''

echo 'ServerError'
cat $1 | awk -F '[" ]' '$11>=500 {print $12, $11,$1,$8}' | sort -k 1,1rn | head -10