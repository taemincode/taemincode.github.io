-- Keep a log of any SQL queries you execute as you solve the mystery.


-- See what files I have access to
.table
-- airports              crime_scene_reports   people
-- atm_transactions      flights               phone_calls
-- bakery_security_logs  interviews
-- bank_accounts         passengers


-- Look up whats inside crime_scene_reports
.schema crime_scene_reports


-- Find crime scene description
SELECT description
FROM crime_scene_reports
WHERE month = 7 AND day = 28 AND year = 2023 AND street = 'Humphrey Street';
-- | Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery. Interviews were conducted today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery. |
-- | Littering took place at 16:36. No known witnesses.


-- Find activity from bakery security logs
SELECT activity
FROM bakery_security_logs
WHERE month = 7 AND day = 28 AND year = 2023 AND hour = 10 AND minute = 15;


-- Couldn't find activity so looked up for the closest entrance time with 10:15 am
SELECT * FROM bakery_security_logs;
-- | id  | year | month | day | hour | minute | activity | license_plate |
-- | 259 | 2023 | 7     | 28  | 10   | 14     | entrance | 13FNH73       |


-- Look if there is any information related to license_plate
.schema
-- It has license_plate in people


-- Look up whats inside people
.schema people


-- Find who's license_plate matches with 13FNH73
SELECT *
FROM people
WHERE license_plate = '13FNH73';
-- |   id   |  name  |  phone_number  | passport_number | license_plate |
-- | 745650 | Sophia | (027) 555-1068 | 3642612721      | 13FNH73       |


-- Look up whats inside interviews
.schema interviews


-- Look for Sophia's interview
SELECT * FROM interviews WHERE name = 'Sophia';
--| 8  | Sophia | 2023 | 1     | 13  | “I never hope to see such a sight as that again, Mr. Holmes. From north, south, east, and west every man who had a shade of red in his hair had tramped into the city to answer the advertisement. Fleet Street was choked with red-headed folk, and Pope’s Court looked like a coster’s orange barrow. I should not have thought there were so many in the whole country as were brought together by that single advertisement. Every shade of colour they were—straw, lemon, orange, brick, Irish-setter, liver, clay; but, as Spaulding said, there were not many who had the real vivid flame-coloured tint. When I saw how many were waiting, I would have given it up in despair; but Spaulding would not hear of it. How he did it I could not imagine, but he pushed and pulled and butted until he got me through the crowd, and right up to the steps which led to the office. There was a double stream upon the stair, some going up in hope, and some coming back dejected; but we wedged in as well as we could and soon found ourselves in the office.” |


-- Look up whats inside bank_accounts
.schema bank_accounts


-- Look for Sophia's bank account
SELECT * FROM bank_accounts WHERE person_id = 745650;
-- | account_number | person_id | creation_year |
-- | 42445987       | 745650    | 2011          |


-- Look up whats inside atm_transactions
.schema atm_transactions


-- Look for Sophia's atm transactions
SELECT * FROM atm_transactions WHERE account_number = 42445987;


-- Look up whats inside passengers
.schema passengers


-- Look if Sophia was a passenger
SELECT * FROM passengers WHERE passport_number = 3642612721;
-- | flight_id | passport_number | seat |
-- | 6         | 3642612721      | 8A   |
-- | 31        | 3642612721      | 9B   |
-- | 43        | 3642612721      | 2C   |


-- Look up whats inside flights
.schema flights


-- Find fights Sophia took
SELECT * FROM flights WHERE id = 6 OR id = 31 OR id = 43;
-- This should be the flight
-- | id | origin_airport_id | destination_airport_id | year | month | day | hour | minute |
-- | 6  | 8                 | 5                      | 2023 | 7     | 28  | 13   | 49     |


-- Look up whats inside airports
.schema airports


-- Find where Sophia went
SELECT * FROM airports WHERE id = 8 OR id = 5;
-- | id | abbreviation |                full_name                |    city    |
-- | 5  | DFS          | Dallas/Fort Worth International Airport | Dallas     |
-- Sophia went to Dallas


-- Look up whats inside phone_calls
.schema phone_calls


-- Find out who Sophia called to
SELECT * FROM phone_calls WHERE caller = '(027) 555-1068' OR receiver = '(027) 555-1068';
-- She called (375) 555-8161 and (994) 555-3373


-- Find out who has those numbers
SELECT name
FROM people
WHERE phone_number = '(994) 555-3373' OR '(505) 555-5698' OR '(594) 555-6254' OR '(717) 555-134';
-- Robin,



----------------------------------------------------------------------------------- Incorrect; try again

SELECT DISTINCT people.name--, city, flights.year, flights.month, flights.day, hour, minute--,
,transcript
FROM people
JOIN passengers ON people.passport_number = passengers.passport_number
JOIN flights ON passengers.flight_id = flights.id
JOIN airports ON flights.destination_airport_id = airports.id
JOIN interviews ON people.name = interviews.name
WHERE people.license_plate IN
(SELECT license_plate
FROM bakery_security_logs
WHERE month = 7 AND day = 28 AND year = 2023 AND activity = 'entrance' AND hour < 11)
AND flights.origin_airport_id IN
(SELECT id
FROM airports
WHERE city = 'Fiftyville')
AND flights.year = 2023 AND flights.month = 7 AND flights.day >= 28
ORDER BY flights.year, flights.day, flights.month, hour, minute;


SELECT * from crime_scene_reports WHERE year = 2023 AND month = 7 AND day = 28 AND street = 'Humphrey Street';

--- | 161 | Ruth    | 2023 | 7     | 28  | Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away. If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.                                                          |
SELECT name, bakery_security_logs.*
FROM bakery_security_logs
JOIN people ON people.license_plate = bakery_security_logs.license_plate
WHERE year = 2023 AND month = 7 AND day = 28 AND activity = 'exit' AND hour = 10 AND minute >= 15;


--- | 162 | Eugene  | 2023 | 7     | 28  | I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.
SELECT *
FROM atm_transactions
WHERE account_number IN
(SELECT account_number
FROM bank_accounts
WHERE person_id IN
(SELECT id
FROM people
WHERE name = 'James' OR name = 'Robin'));


--- | 163 | Raymond | 2023 | 7     | 28  | As the thief was leaving the bakery, they called someone who talked to them for less than a minute. In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow. The thief then asked the person on the other end of the phone to purchase the flight ticket.
SELECT name, phone_calls.*
FROM phone_calls
JOIN people ON people.phone_number = phone_calls.caller
WHERE caller IN
(SELECT phone_number
FROM people
WHERE name = 'Bruce' OR name = 'Luca' OR name = 'Taylor')
AND duration <= 60;


SELECT *
FROM people
WHERE phone_number = '(375) 555-8161' OR phone_number = '(676) 555-6554';


SELECT *
FROM flights
WHERE origin_airport_id =
(SELECT id
FROM airports
WHERE city = 'Fiftyville')
AND year = 2023 AND month = 7 AND day = 29
ORDER BY hour, minute;
-- Went to 4


SELECT *
FROM airports
WHERE id = 4;
-- New York City

SELECT *
FROM flights
WHERE id =
(SELECT flight_id
FROM passengers
WHERE passport_number =
(SELECT passport_number
FROM people
WHERE name = 'Diana'));


SELECT people.name, bakery_security_logs.minute
FROM people
JOIN bank_accounts ON bank_accounts.person_id = people.id
JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
JOIN bakery_security_logs ON people.license_plate = bakery_security_logs.license_plate
WHERE passport_number IN
(SELECT passport_number
FROM passengers
WHERE flight_id = 36)
AND atm_location = 'Leggett Street' AND atm_transactions.year = 2023 AND atm_transactions.month = 7 AND atm_transactions.day = 28 AND transaction_type = 'withdraw'
AND bakery_security_logs.year = 2023 AND bakery_security_logs.month = 7 AND bakery_security_logs.day = 28 AND bakery_security_logs.activity = 'exit' AND bakery_security_logs.hour = 10 AND bakery_security_logs.minute >= 15;

SELECT *
FROM atm_transactions
JOIN bank_accounts ON bank_accounts.account_number = atm_transactions.account_number
JOIN people ON bank_accounts.person_id = people.id
WHERE atm_location = 'Leggett Street' AND year = 2023 AND month = 7 AND day = 28 AND transaction_type = 'withdraw';
