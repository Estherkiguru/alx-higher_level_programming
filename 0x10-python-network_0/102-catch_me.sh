#!/bin/bash
#make request to 0.0.0.0:5000/catch_me,server responds with You got me!
curl -s -L -X PUT -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
