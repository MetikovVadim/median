# median
counts median, quantiles(25,75) and store to clickhouse table

# How to use:

1 clone repository and go to directory median
2  make files executable:
 $ chmod a+x generator.py receiver.py
2 run genereator.py and receiver.py connected via pipe:
 $ ./gererator.py | ./receiver.py
