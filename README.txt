first of all i would like to pay my high respect To Teacher ❤️❤️"Sol Vathanak"❤️❤️


================================================================================
                        CINEMA MANAGEMENT SYSTEM
================================================================================
A Python-based cinema management system that allows managers and cashiers to
manage movies, seat bookings, user accounts, and generate PDF tickets.

--------------------------------------------------------------------------------
1. LOGIN PASSWORD ADMIN
--------------------------------------------------------------------------------

manager account :
------------
username : admin
password : 123

cashier account :
------------
username : kimleng
password : aa11

--------------------------------------------------------------------------------
2. OVERVIEW
--------------------------------------------------------------------------------

This application provides two main roles:

  • CASHIER  – Can view movies, book seats, remove movies, and log out.
  • MANAGER  – Has all cashier functions plus the ability to add movies,
               manage users, view/clear history, and log out.

--------------------------------------------------------------------------------
3. HOW TO RUN
--------------------------------------------------------------------------------

  Open a terminal in the project directory and run:

        python main.py

  You will be prompt to log in. Depending on your credentials, you will
  enter either the Cashier menu or the Manager menu.

--------------------------------------------------------------------------------
4. MENU OPTIONS
--------------------------------------------------------------------------------

  cashier menu
  ------------
    [1] View movie            – Display all currently available movies.
    [2] Add Cart to pay       – Book seats and generate a PDF ticket.
    [3] Remove the movie      – Remove a movie by HALL number.
    [4] Logout                – Exit the cashier session.

  manager menu
  ------------
    [1] View movie            – Display all currently available movies.
    [2] Add New movie         – Add a movie with name, time, and price.
    [3] Add Cart to pay       – Book seats and generate a PDF ticket.
    [4] Remove the movie      – Remove a movie by HALL number.
    [5] Manage Users          – View or add manager/cashier accounts.
    [6] View history          – Show past bookings/transactions.
    [7] Clear history all data– Wipe all movie and client data.
    [8] Logout                – Exit the manager session.

--------------------------------------------------------------------------------
5. BOOKING FLOW
--------------------------------------------------------------------------------

  1. Choose "Add Cart to pay".
  2. Select the number of tickets and the HALL (movie).
  3. Enter a seat number between 1 and 100 for each ticket.
     - If the seat is already booked in that hall, you will be asked again.
  4. After all seats are confirmed, a PDF ticket is generated.
  5. The system returns to the main login screen.

  NOTE: Seat numbers are validate per hall, so the same seat number can be
        used in different halls.


================================================================================
                            END OF README
================================================================================

