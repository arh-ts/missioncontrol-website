# Why automation programs stall, and how to choose your first five

> From RPA to generative AI, most pilots never pay back. The problem is rarely the technology. It is what gets chosen for automation.

Published 22 November 2026 by the Mission Control team. Canonical: https://missioncntrl.io/news/why-automation-programs-stall

## Key points

- EY has reported that 30 to 50 per cent of initial RPA projects fail. MIT's 2025 research found most generative AI pilots produce no measurable P&L impact. The pattern repeats with each wave of technology.

- The common cause is not the technology. It is choosing what to automate by intuition and visibility rather than by measured flow.

- Automating a step that is not the bottleneck saves effort but rarely makes the business faster. It can simply grow the queue in front of the real constraint.

- Choose your first automations on five tests: volume, wait time removed, rule stability, data availability and position relative to the bottleneck.

Automation has a striking record of over-promising in the pilot and under-delivering at scale. In robotic process automation, EY reported in its [Get ready for robots](https://ey.com/en_qa/financial-services-emeia/get-ready-for-robotic-process-automation) paper that it had seen as many as 30 to 50 per cent of initial RPA projects fail. It was explicit that this was not a reflection of the technology. Among the common issues it listed were treating RPA as IT-led rather than business-led, and postponing the business case until after proofs of concept.

Generative AI is repeating the pattern faster. MIT NANDA's [2025 report The GenAI Divide](https://www.theregister.com/2025/08/18/generative_ai_zero_return_95_percent) found that 95 per cent of organisations in its research had seen no measurable return from generative AI. Only 5 per cent of custom enterprise AI tools reached production. The headline figure deserves caution. It comes from a preliminary study based on interviews, surveys and a sample of deployments, not a census. But the authors' explanation will be familiar to anyone who lived through RPA. [Coverage of the report](https://campustechnology.com/articles/2025/08/26/mit-report-most-organizations-see-no-business-return-on-gen-ai-investments.aspx) summarises it as brittle workflows, weak contextual learning and misalignment with day-to-day operations. The report also noted that the biggest returns appeared in back-office operations, not in the sales and marketing tools that attract most budget.

Meanwhile the theoretical ceiling keeps rising. McKinsey estimated in 2023 that current generative AI and other technologies [have the potential to automate work activities that absorb 60 to 70 per cent of employees' time](https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/the-economic-potential-of-generative-ai-the-next-productivity-frontier). The gap between that potential and what organisations actually bank is the real story. It is mostly a selection problem.

## The real reason programs stall: they automate what they can see

Most automation backlogs are built the same way. A workshop is run. Teams nominate tasks that are repetitive and annoying. A consultant scores them on effort and feasibility. The quick wins are built first.

The flaw is in the input. Teams nominate the steps they personally perform and can describe: re-keying a form, renaming files, sending a reminder. They cannot nominate the delays between steps, because those delays belong to no one. Deloitte's intelligent automation research is telling here. [Process fragmentation was cited by 36 per cent of respondents](https://www2.deloitte.com/us/en/insights/focus/technology-and-the-future-of-work/intelligent-automation-technologies-strategies.html) as the main barrier to adoption, more than twice the share citing IT readiness.

So programs fill up with automations of visible tasks inside single teams. Each one saves real effort. Then the business case is reviewed a year later. Clients are not served any faster, headcount has not changed, and the finance team cannot find the savings. The program loses sponsorship and stalls.

## Why saving effort is not the same as moving faster

Eliyahu Goldratt's [theory of constraints](https://en.wikipedia.org/wiki/Theory_of_constraints) makes a simple point. The throughput of a whole process is limited by its tightest constraint. Improving any step other than the constraint does not increase throughput.

In automation terms, imagine an onboarding flow where documents are collected, checked, approved by a partner and then set up in the billing system. The partner approval is the constraint: work queues there for days. Automate document checking and it becomes faster, but nothing reaches the partner sooner in any way that matters. Checked files simply join a longer queue. The flow is no quicker and the saving is hard to bank.

Now automate the transfer from approval into billing, and pre-assemble everything the partner needs so approval takes minutes rather than a search. Elapsed time drops, cash arrives sooner and the benefit is visible to the client. The second automation might save fewer hours on paper. It is worth far more.

This is why we argue that the right unit for selecting automation is the _flow_, not the task. You need to know where work waits before you decide what to build.

## How to choose your first five

Before anything is built, every candidate should be measured against the same five tests. Ideally this uses data from your own systems rather than estimates from a workshop.

- **Volume.** How many times a month does this happen? Automation rewards repetition. A painful task that happens twice a month rarely pays back.

- **Wait time removed.** Does automating this shorten elapsed time for the case, or only effort for the person? Prefer candidates at or immediately around the bottleneck, and at hand-offs between teams or systems.

- **Rule stability.** How many variants does the step have in practice? If cases take a dozen different paths, automate the dominant path first and route the rest to people. Do not try to encode every exception on day one.

- **Data availability.** Is the information the automation needs already captured in a system, in a consistent format? If not, the first project is data capture, not automation.

- **Ownership.** Is there a named person who owns the outcome and will maintain the automation? EY and UiPath both point to programs that [underestimate the work required after go-live](https://www.uipath.com/blog/rpa/why-rpa-deployments-fail). An automation without an owner decays as soon as the process around it changes.

Score each candidate. Size the value in hours and in elapsed time (we cover how to do this credibly in [a separate guide](https://missioncntrl.io/news/automation-business-case-cfo)). Then pick five that sit on the constrained path. A good first portfolio usually includes one or two hand-off automations, one data-capture fix and one or two classic task automations, chosen because they feed the bottleneck rather than because they were nominated loudest.

## Set kill criteria before you start

The other habit that separates programs that scale from those that stall is deciding in advance what failure looks like. Before building, write down three things: the measure the automation should move (elapsed time, hours, error rate), the expected size of the change, and the date by which you will check. If it does not move, switch it off and redeploy the effort.

That sounds obvious. In practice almost nobody does it, which is why automation estates fill up with bots and workflows that nobody can quite justify and nobody wants to turn off. Building fewer things and measuring them properly is less exciting than a long backlog. It is also how the 5 per cent get ahead.

## Questions

### Why do so many automation projects fail?

The most common reasons are choosing the wrong processes, treating automation as an IT project rather than a business one, and building before there is a business case. EY has reported that 30 to 50 per cent of initial RPA projects fail. It attributes this to how projects are run, not to the technology.

### How should you choose which processes to automate first?

Test each candidate on volume, the wait time it removes, how stable its rules are, whether the data it needs is available and who will own it. Prioritise candidates on or around the process bottleneck and at hand-offs, because those shorten elapsed time as well as effort.

### What is the difference between saving effort and improving flow?

Saving effort reduces the hours a person spends on a step. Improving flow reduces the elapsed time a case takes from start to finish. An automation can save effort without improving flow if the step it speeds up was never where work waited.

## Sources

- [EY, Get ready for robots: why planning makes the difference between success and disappointment](https://ey.com/en_qa/financial-services-emeia/get-ready-for-robotic-process-automation)

- [The Register, coverage of MIT NANDA, The GenAI Divide: State of AI in Business 2025](https://www.theregister.com/2025/08/18/generative_ai_zero_return_95_percent)

- [Campus Technology, MIT report: most organisations see no business return on gen AI investments](https://campustechnology.com/articles/2025/08/26/mit-report-most-organizations-see-no-business-return-on-gen-ai-investments.aspx)

- [McKinsey, The economic potential of generative AI (2023)](https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/the-economic-potential-of-generative-ai-the-next-productivity-frontier)

- [Deloitte, Automation with intelligence](https://www2.deloitte.com/us/en/insights/focus/technology-and-the-future-of-work/intelligent-automation-technologies-strategies.html)

- [Theory of constraints overview](https://en.wikipedia.org/wiki/Theory_of_constraints)

- [UiPath, Why some RPA deployments fail](https://www.uipath.com/blog/rpa/why-rpa-deployments-fail)
