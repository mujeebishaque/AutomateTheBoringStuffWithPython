import logging

# the logging module lets you display log messages.
# first, you configure the pattern of logs, like
# should it show data-time? etc

'''
you do it by calling basicConfig() to set up and then
call logging.debug() to create a log message

you can disable them too using loggin.disable()

the five log levels are : 
1 - DEBUG
2 - INFO
3 - WARNING
4 - ERROR
5 - CRITICAL
use like logging.debug()
or logging.error() 
'''