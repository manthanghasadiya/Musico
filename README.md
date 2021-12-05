# Musico

## Website
[Musico](https://muzico.herokuapp.com/)

## Team Name 
Debug Thugs

## Team Members 
* [Rushi Javiya ](https://github.com/Rushijaviya) 
* [Tapan Savani](https://github.com/Stapan17)
* [Devang Delvadiya](https://github.com/DevangDelvadiya)
* [Manthan Ghasadiya](https://github.com/manthanghasadiya)

## Database

<p align="center">
  <img src='https://raw.githubusercontent.com/cockroachdb/cockroach/master/docs/media/cockroach_db.png' width='10%'>
</p>

---

## Problem Statement

* No system exists where you can listen to songs as well as upload your own creation publicly and privately.
* There is no platform for storing your favorite music.
* Sharing your uploaded songs with friends is also not available.

## Our Solution

* We built a platform where anyone can register and log in using their basic identity information. 
* We use Twilio to verify using by sending OTP to their entered mobile number and giving choice to get OTP by SMS or call.
* We use the CockroachDB database to save user info. 
* We use Spotify API for music fetching. 
* User can see the recent tracks and download them.  
* User can search for any song. We use Spotify API to get a search result.
* User can also upload their own song on our platform and make it public or private.  
* Users can share their uploaded song with friends by making it public or just upload it privately to make it visible only to you.

## Impact

* Making the platform where sharing of music between friends is allowed.
* User can also store their music on our website.
* User is verified by Twilio verify system.
* The perfect place for music lovers.
* Search for music, see their artist and search for the artist.
* Start playing songs directly on our website.

## How we built it

* Started with Django and bootstrap to build pipeline and connecting webpage.
* CockroachDB database is added for storing all data related to users like user info and their uploaded music.
* Used Twilio to authorize users and verify their identity by phone number and send a text message when user login.
* Integrated Spotify API for the searching song, seeing artists of song, release date, and thumbnail as well.

## Challenges we ran into

* Spotify API consumes a lot of time for searching and sorting relevant results.
* Integrating Twilio API is also challenging.
* Creating a CockroachDB database for storing uploaded songs.
* Making a real-time music player in a web app.

## What we learned
* How Spotify API works.
* How Twilio API works and its implementation.
* CockroachDB database integration with Django.
* How music player is created for web-app using Django.

## What's next for Musico

* Upgrading security by using other features provided by Twilio.
* Making more from the CockroachDB database.
* Upgrade Musico to a higher scale and make it available to all.
