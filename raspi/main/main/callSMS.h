#! /bin/bash

printMsg () {
    echo 'Texting vehicle owner...'
}

printMsg

cd 
cd smsAttempt/
source sendsms/bin/activate
cd sendsms/
python3 sendsms.py
