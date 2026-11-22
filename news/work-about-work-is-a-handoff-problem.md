# Work about work is a hand-off problem, not a people problem

> Surveys keep finding that more than half the week goes on coordination. The cause is not individual habits. It is the hand-offs nobody designed.

Published 22 November 2026 by the Mission Control team. Canonical: https://missioncntrl.io/news/work-about-work-is-a-handoff-problem

## Key points

- Large surveys put "work about work" at roughly 55 to 60 per cent of a knowledge worker's week. The figure has barely moved in years, despite more collaboration software than ever.

- Most of that time is spent at the hand-offs between people and teams: chasing status, searching for what the last person did, and re-explaining context.

- Asking people to focus harder does not fix a design problem. Making the state of each piece of work visible at the hand-off does.

- Do not ask people where their time goes. Measure where the work waits, using the timestamps your systems already record.

Every few years another study confirms what operators already feel: most of the working week is not spent doing the work. Asana's [Anatomy of Work Index 2022](https://www.businesswire.com/news/home/20220405005399/en/5182748/Asana-Anatomy-of-Work-Index-2022-Work-About-Work-Hampering-Organizational-Agility) surveyed 10,624 knowledge workers across Australia, France, Germany, Japan, Singapore, the UK and the US. It found that employees at medium and large companies spend 59 per cent of their day on what it calls work about work. The [2021 Australia and New Zealand cut](https://asana.com/resources/anz-anatomy-of-work-infographic) put the local figure at 58 per cent. The [UK figure](https://asana.com/resources/uk-anatomy-of-work-infographic) was 61 per cent.

Microsoft reached a similar conclusion from a different direction. Its [2023 Work Trend Index](https://www.microsoft.com/en-us/worklab/work-trend-index/will-ai-fix-work) analysed signals from Microsoft 365. It found the average person spends 57 per cent of their time in that software communicating (meetings, chat and email) and 43 per cent creating. In the same report, 68 per cent of people said they lack enough uninterrupted focus time.

The usual response is a new tool, a no-meeting day or a focus campaign. We think that misreads the problem. Work about work is mostly not a personal productivity failure. It is what an organisation pays for hand-offs nobody designed.

## What the surveys are really measuring

Look at what falls under "work about work": status updates, searching for information, switching between apps, chasing approvals, duplicated effort. Almost none of it happens inside one person's task. It happens at the moments work changes hands.

The McKinsey Global Institute's [2012 analysis](https://www.mckinsey.com/industries/high-tech/our-insights/the-social-economy) estimated that the average interaction worker spends 28 per cent of the week managing email. It put nearly 20 per cent on looking for internal information or tracking down colleagues who can help. That second number describes a hand-off failure. Someone needed what a previous step produced, and could not find it or the person who held it.

Research on attention points the same way. Gloria Mark and colleagues at the University of California, Irvine [shadowed 36 knowledge workers](https://news.gallup.com/businessjournal/23146/too-many-interruptions-work.aspx), timing every event to the second. On average people juggled 12.2 separate "working spheres" a day. They switched between them roughly every ten and a half minutes. Much of that switching is driven by other people's dependencies arriving unannounced.

Treat these figures with care. They come from self-reported surveys, vendor telemetry and older estimates, and they do not agree on method. What matters is that every method lands in the same place: well over half the week goes on coordination. That consistency is the finding.

## Why the hand-off is where time disappears

Think about a typical services workflow: a new client is onboarded, an engagement is scoped, a matter is opened, a claim is assessed. On paper it is five or six steps. In practice each step ends with a hand-off. And each hand-off has three hidden costs.

- **Waiting.** The work sits in someone's queue, or in an inbox, until they notice it. Nobody is doing anything wrong. The work is simply idle.

- **Re-establishing context.** The next person has to work out what was done, what is missing and what the client asked for. Some of that is searching. Some of it is a message back to the person who just handed it over.

- **Status chasing.** Because nobody can see where the work is, managers and clients ask. Each question interrupts someone who is in the middle of something else.

None of these show up as "work" in a timesheet. All of them show up as elapsed time for the client and as fatigue for the team. And they multiply with every hand-off. A process that touches seven people has six seams, each leaking a little time.

## Why the usual fixes underdeliver

**More collaboration tools.** Most organisations already have too many places where status can live: email, chat, a practice management system, a CRM, a spreadsheet someone built in 2019. Another channel adds one more place to look. The problem was never a lack of ways to talk. It was that the state of the work was not recorded where the next person would find it.

**Focus campaigns.** Protecting deep work is good for individuals. But if a case cannot move until three people have each looked at it, protecting their focus time can make the case slower. Reducing interruptions only helps when you also reduce the reasons for them.

**Asking people where their time goes.** Time surveys and workshops tell you what people remember and what they think matters. They are poor at recovering wait time, which by definition nobody experiences as work. A step that "takes ten minutes" can routinely sit for three days before anyone starts it.

## A better approach: measure the hand-offs

The practical alternative is to study the work item instead of the worker. Pick one workflow that matters commercially. Then trace individual cases through it using the timestamps your systems already record. This is the core idea behind [process mining](https://en.wikipedia.org/wiki/Process_mining), a field built on event logs. Each event carries a case identifier, an activity and a timestamp.

For a first pass, four measures do most of the work:

- **Hand-offs per case.** How many times does a typical case change hands, and how much does that vary? Outliers usually point to unclear ownership.

- **Wait time per hand-off.** How long does work sit between one person finishing and the next starting? This is usually where most of the elapsed time is.

- **Rework loops.** How often does a case go backwards to a step it has already passed? Each loop is a hand-off that failed to carry enough context.

- **Path variety.** How many different routes do cases take in practice, compared with the one route in the procedure manual?

You need a few hundred cases at most to see the pattern. You do not need to watch anyone's screen. Timestamps on records, status changes and assignments are enough to show where work waits. (We cover how to do this without monitoring individuals in [a separate piece](https://missioncntrl.io/news/map-work-without-monitoring-people).)

## What to do with what you find

Once hand-offs are visible, the fixes tend to be unglamorous and effective:

- **Remove a hand-off entirely** where two steps can be done by one role. This is usually the cheapest improvement available.

- **Standardise what travels with the work** so the next person starts with context rather than a question. A short, required set of fields at each hand-off often beats a long procedure document.

- **Make the state of each case visible** to the people who chase it, so status questions stop being asked.

- **Automate the transfer, not just the task.** The most valuable automations often move information between systems at a hand-off, rather than speeding up a step that was never the delay.

The mistake is to treat work about work as an individual habit to be coached away. It is a property of how the organisation passes work around. That makes it measurable, and fixable, by the people accountable for how the business runs.

## Questions

### What is "work about work"?

It is time spent coordinating work rather than doing it: status updates, searching for information, switching between tools, chasing approvals and duplicating effort. Asana's Anatomy of Work research popularised the term. Its 2022 survey found that employees at medium and large companies spend 59 per cent of their day on it.

### Why is work about work so hard to reduce?

Because most of it happens at the hand-offs between people and teams, not inside any one person's task. Individual productivity tactics do not change how work is passed between roles. Changing hand-offs requires seeing them, and most organisations have no measure of them.

### How do you measure hand-offs without surveying staff?

Use the timestamps that business systems already record when a case is created, assigned, updated or closed. Tracing a few hundred cases shows how many hand-offs each case has, how long work waits between them and how often it loops back.

## Sources

- [Asana, Anatomy of Work Index 2022 (Business Wire release)](https://www.businesswire.com/news/home/20220405005399/en/5182748/Asana-Anatomy-of-Work-Index-2022-Work-About-Work-Hampering-Organizational-Agility)

- [Asana, Anatomy of Work Index 2021: Australia and New Zealand findings](https://asana.com/resources/anz-anatomy-of-work-infographic)

- [Asana, Anatomy of Work Index 2021: UK findings](https://asana.com/resources/uk-anatomy-of-work-infographic)

- [Microsoft, 2023 Work Trend Index: Will AI fix work?](https://www.microsoft.com/en-us/worklab/work-trend-index/will-ai-fix-work)

- [McKinsey Global Institute, The social economy (2012)](https://www.mckinsey.com/industries/high-tech/our-insights/the-social-economy)

- [Gallup Business Journal, interview with Gloria Mark on workplace interruptions](https://news.gallup.com/businessjournal/23146/too-many-interruptions-work.aspx)

- [Process mining overview](https://en.wikipedia.org/wiki/Process_mining)
