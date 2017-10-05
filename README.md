# WebAssignHW
## Scrapes Webassign and outputs ics file of homework due

Webassign doesn't provide a proper way to get a iCal file or link to export your assingments.
This script scrapes Webassign for your courses and homework to exports it to an iCal file.
The idea is for this script to run daily and the iCal file to be hosted on a server.
With the link, you can sync it to Google Calendar for example to get an updated schedule of your assignments.

This uses Selenium and PhantomJS (although you can use any webdriver) as well as the dateutil and ics module.
Due to complications in parsing, time zone for this version requires you to specify the time zone to interpret

### You must create an account.key file for the script to read the information off of, which just contains four lines

>url=https://www.webassign.net/wa-auth/login <br />
>user=[YOUR EMAIL] <br />
>pass=[YOUR PASSWORD] <br />
>timezone=[YOUR TIMEZONE] <br />

URL argument is included in case it changes
