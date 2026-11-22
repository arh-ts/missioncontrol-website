# Flow efficiency: the number that explains why simple work takes weeks

> The work takes hours. The case takes weeks. Little's Law and a little queuing theory explain the gap, and how to close it.

Published 22 November 2026 by the Mission Control team. Canonical: https://missioncntrl.io/news/flow-efficiency-services-firms

## Key points

- Flow efficiency is the share of a case's elapsed time spent actively working on it. The rest is waiting.

- Practitioners commonly report figures in the 5 to 15 per cent range for knowledge work. No rigorous benchmark exists, but even generous estimates leave most elapsed time as waiting.

- Little's Law shows why: with demand held steady, the average time a case takes rises in direct proportion to how much work is open at once.

- High utilisation targets make waiting worse, not better. Queues grow sharply as people approach full capacity.

- The fastest way to deliver sooner is usually to cut waiting, not to make people work faster.

Ask a team how long it takes to onboard a client and you will usually get two answers. The work takes a few hours. The onboarding takes two weeks. The gap between those numbers is where most services businesses quietly lose speed, margin and client goodwill. It has a name: flow efficiency.

## What flow efficiency is

Flow efficiency is a simple ratio. Divide the time someone spent actively working on a case by the total elapsed time from start to finish:

**Flow efficiency = active time ÷ total elapsed time**

A matter that receives six hours of actual work across ten working days (80 working hours) has a flow efficiency of 7.5 per cent. For the other 92.5 per cent of the time it was waiting.

The idea comes from lean operations. It was popularised for knowledge work by Niklas Modig and Pär Åhlström, who contrast _resource efficiency_ (keeping people busy) with _flow efficiency_ (keeping work moving). [One practitioner summary](https://www.scrum.org/resources/blog/business-efficiency-watch-ball-not-player) puts the shift well: watch the ball, not the player. In knowledge work what matters most is what is happening to the work, not what the workers are doing.

## How low is it, really?

Figures in the 5 to 15 per cent range are widely quoted. ASOS's engineering team [collected the common claims](https://medium.com/asos-techblog/our-survey-says-uncovering-the-real-numbers-behind-flow-efficiency-e54f136b1fab): most teams sit between 5 and 15 per cent, some as low as 2 per cent, and about 40 per cent after much effort. The same team made an important point in a [companion piece](https://medium.com/asos-techblog/the-many-flaws-in-flow-efficiency-bc7845ba4c9). They could not find a single rigorous study that validates these "typical" percentages.

We agree with that caution, and it does not change the conclusion. You do not need a precise industry benchmark to act. Even if your real figure were three times higher than the commonly quoted range, most of each case's life would still be spent waiting. The question worth answering is not "what is normal?" It is "where does our work wait, and why?"

## Little's Law: why open work equals slow work

In 1961 John Little published [a proof of the queuing formula L = λW](https://econpapers.repec.org/RePEc:inm:oropre:v:9:y:1961:i:3:p:383-387). It is now known as Little's Law. In plain terms: the average number of items in a system equals the average arrival rate multiplied by the average time each item spends in the system. Little later [reflected on its practical reach](https://people.cs.umass.edu/~emery/classes/cmpsci691st/readings/OS/Littles-Law-50-Years-Later.pdf) in a 50th-anniversary paper.

Rearranged, it says something every operations leader should keep in mind:

**Average time per case = work in progress ÷ throughput**

Illustrative example: a team completes 40 matters a week and has 200 open. The average matter takes about five weeks. If the same team, doing the same work at the same pace, holds 100 matters open instead of 200, the average falls to about two and a half weeks.

The law describes long-run averages in a reasonably stable system, so treat it as a guide rather than a stopwatch. But the direction is reliable. Starting more work than you finish does not make you faster. It makes every case slower, because each one spends longer queued behind the others.

## Why "everyone at full utilisation" backfires

Professional services firms are built around utilisation: billable hours, chargeable time, capacity plans that aim to keep everyone busy. That makes sense for cost. It is damaging for flow.

Queuing theory has shown for decades that waiting time does not rise in a straight line as utilisation rises. It climbs slowly at first, then very sharply as resources approach full capacity, and more so when work arrives unevenly. [Kingman's formula](https://en.wikipedia.org/wiki/Kingman%27s_formula) is the standard approximation. In a services team the arrivals are client requests, and the variability is everything that makes services work hard to predict. A team planned to run at 95 per cent will have long queues almost by design.

Don Reinertsen made this argument for product development in [The Principles of Product Development Flow](https://www.goodreads.com/en/book/show/6278270-the-principles-of-product-development-flow). His point applies directly to services. In knowledge work, inventory is information. It is invisible, so queues go unmanaged. You cannot walk the floor and see half-finished matters stacked against a wall. They sit in inboxes and systems, and the only symptom is that everything takes longer than it should.

## Where waiting hides in services work

When teams first measure flow, the waiting usually clusters in a few familiar places:

- **Approvals.** A review or sign-off step owned by one senior person who is, quite reasonably, busy with other things.

- **Specialist queues.** Work that only one team or person can do, such as compliance, tax or conflicts checks, and that everyone else is waiting on.

- **Waiting on the client.** Missing documents and unanswered questions. Some of this is outside your control. More of it than you expect is caused by asking for things late or one at a time.

- **Batching.** Work that is held until "we do those on Thursdays", so a case finished on Friday waits six days for the next batch.

- **Hand-offs between systems.** Information re-keyed from email into a practice system, or from a CRM into billing, whenever someone gets to it.

Separating internal waiting from client waiting matters. It stops a team blaming clients for delays it created, and it shows which delays are worth automating.

## How to measure your own flow efficiency

- **Pick one workflow** with a clear start and finish that clients or revenue depend on: onboarding, new matters, claims, monthly close.

- **Define its states** as they exist in your systems: created, assigned, in progress, waiting on client, in review, complete.

- **Pull timestamps** for a few hundred recent cases from the systems where those state changes are recorded.

- **Classify time as active or waiting.** Start with system states. They will be imperfect. That is fine for a first pass, as long as you are consistent.

- **Find the biggest queue,** not the slowest step. The step with the most work waiting in front of it is usually the constraint on the whole flow.

Then resist the instinct to speed up the work at that step. First ask why work waits there, and whether you can start less, batch less or remove the hand-off. Making people faster is hard. Making work wait less is usually much easier, and it moves the number clients actually experience.

## Questions

### What is flow efficiency?

Flow efficiency is the percentage of a work item's total elapsed time during which someone is actively working on it. If a case takes ten working days end to end but receives one working day of actual effort, its flow efficiency is 10 per cent.

### What is a good flow efficiency for knowledge work?

There is no rigorously validated benchmark. Practitioners often cite 5 to 15 per cent as typical and around 40 per cent as very good. It is more useful to track your own figure over time and find where your work waits than to chase an external number.

### How does Little's Law apply to services businesses?

Little's Law says average time in a system equals work in progress divided by throughput. For a services team, holding fewer cases open at once, without changing how fast cases are worked, lowers the average time each case takes.

## Sources

- [Little, J. D. C. (1961). A proof for the queuing formula: L = λW. Operations Research.](https://econpapers.repec.org/RePEc:inm:oropre:v:9:y:1961:i:3:p:383-387)

- [Little, J. D. C. (2011). Little's Law as viewed on its 50th anniversary. Operations Research.](https://people.cs.umass.edu/~emery/classes/cmpsci691st/readings/OS/Littles-Law-50-Years-Later.pdf)

- [ASOS Tech, Uncovering the real numbers behind flow efficiency](https://medium.com/asos-techblog/our-survey-says-uncovering-the-real-numbers-behind-flow-efficiency-e54f136b1fab)

- [ASOS Tech, The many flaws of flow efficiency](https://medium.com/asos-techblog/the-many-flaws-in-flow-efficiency-bc7845ba4c9)

- [Scrum.org, Business efficiency: watch the ball, not the player](https://www.scrum.org/resources/blog/business-efficiency-watch-ball-not-player)

- [Kingman's formula (queueing theory)](https://en.wikipedia.org/wiki/Kingman%27s_formula)

- [Reinertsen, D. G. (2009). The Principles of Product Development Flow.](https://www.goodreads.com/en/book/show/6278270-the-principles-of-product-development-flow)
