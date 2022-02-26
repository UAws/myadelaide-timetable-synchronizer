# Myadelaide Timetable Synchronizer

A fascinating tool that synchronizes your timetable to University Managed Office365 Instance Or any preferable calendar management system. e.g. Google calendar, iCloud calendar ...

## Demo Video


[![Youtube](https://img.youtube.com/vi/9wOfDHSXDs8/0.jpg)](https://youtu.be/9wOfDHSXDs8)

## Prerequisites 
1. Chrome Browser
2. Python >= 3.6

## Quick Start

```code
git clone  https://github.com/UAws/myadelaide-timetable-synchronizer.git
cd myadelaide-timetable-synchronizer
pip install -r requirements.txt
python main.py
```

## Privacy Notice

### This tool will **NOT** record any data and send to third party data collection services 

The author of project (me) takes serious consideration to protect your privacy and data integrity. 

This tool will request the your timetable on your behalf via api.adelaide.edu.au, all of sensitive data including authorization header, username, password **WILL NOT** store to any persistent storage even on your computer. All of data transformation including details of timetable events are processing within the memory, and will destroy once program finish execution. 

This tool will and **ONLY** requests following domains under your authorization: 

1. {id,api,myadelaide.uni}.adelaide.edu.au -> managed by UOFA
2. *.office365.com -> managed by microsoft online services

As this project is **NOT** an artifact of UOFA, and there is no clear documents that classified the scope and expiration policy of bearer authorization token, the author would highly recommend do not share this token with anyone else.

## Known limitations

1. The Api is not official documented by UOFA, any further API change will damage the logic inside of program
2.  The automatic upload ics to Office365 relay on the `selenium` AKA end to end testing system, therefore this component based on the UI of Office365, any further Office365 UI change will damage the logic inside of program

## FAQ

1. how to upload the timetable to my favorite calendar management system

   Google how to upload ics to {your preferred calendar}

2. how to prepare the local environment

   Google how to install python3 to {your OS} {macos | Linux | windows}

3. how does auther test the code

   This project is based on several external api and services and UOFA authentication platform based on Otka 2FA, therefore there is tool change for create CI (continues integration) for Auto Testing. In this senario the test has been done locally on MacOS 12.2, Linux ubuntu 20.04, Window 10 LTSC (thanks for friends verify the functionality for different system)

4. How to get support for this tool

   Open a github issue and provide your OS version, Python version, Chrome version.

## Licensed under MIT

```
Copyright 2022 UAWS/AkideLiu

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

