in this lab, we needed to implement a automaton to generate our day. 
I used 5 states: STATES = ["Tired", "Exused", "Moody", "Inactive", "Satisfied"]
And 7 events: EVENTS = ["Wake up","Air Allert","Exam","Lunch","Have a walk","Go to pub","Go sleep"]
I decided to generate the day of my first exam.
Also i have state.hungry and state.energy, so i can have a choice - go to sleep or go celebrate with friends. 

There are some examples of different days which automaton can generate:

I just Wake up, snd I'm already Exused
I want to lay down some more time, but i should go(
I should go to my uni to write an exam.
Air Allert. Again.
I'm going to have my exam now. I'm not even had a breakfast.
I'm still at my exam.
I'm still at my exam.
I'm going to have lunch
I'm going to go home and sleep


I just Wake up, snd I'm already Exused
I want to lay down some more time, but i should go(
I should go to my uni to write an exam.
Air Allert. Again.
I'm going to have my exam now. I'm not even had a breakfast.
I'm still at my exam.
I'm still at my exam.
I'm going to have lunch
I'm going to have a walk with my friends
We decided to go to pub.
We decided to continue our party at me friends home. Bye!


I just Wake up, snd I'm already Exused
I want to lay down some more time, but i should go(
I should go to my uni to write an exam.
Air Allert. Again.
I'm going to have my exam now. I'm not even had a breakfast.
I'm still at my exam.
I'm still at my exam.
I'm going to have lunch
I'm going to have a walk with my friends
We decided to go to pub.
We decided to go home and sleep