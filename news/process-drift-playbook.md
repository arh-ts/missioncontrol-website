# Process drift: closing the gap between the SOP and the real work

> Every documented process drifts from how work is really done. Here is a step-by-step playbook to find the gap, sort good drift from bad, and close it on a fixed cadence.

Published 23 November 2026 by the Mission Control team. Canonical: https://missioncntrl.io/news/process-drift-playbook

## Key points

- Every documented process drifts. The manual describes work as imagined. Your systems record work as done. The gap is information.

- Conformance checking, a process mining technique, compares recorded activity with the documented model. Real logs rarely fit perfectly.

- Not all drift is bad. Sort each variant into one of three buckets: good drift to adopt, bad drift to fix, or a workaround that signals a broken system.

- Regulators now expect documented processes that hold up under testing. APRA's CPS 230 commenced on 1 July 2025 and the FCA's operational resilience deadline passed on 31 March 2025.

- You can find drift by measuring how work moves between systems and teams. You do not need to read anyone's emails or log their keystrokes.

Open the procedure manual for any core workflow in your firm. Now ask the people who run it every day to walk you through what they actually do. The two versions will not match. They never do.

This is process drift: the slow, mostly invisible gap between the documented process and the real one. It builds through new systems, staff turnover and small fixes nobody wrote down. Most firms discover it during an incident, an audit or a failed automation project.

Our view is simple. Drift is not a compliance failure to stamp out. It is honest feedback on your operating model. The job is to find it, classify it and act on it on a fixed cadence.

## Work as imagined versus work as done

Safety science has studied this gap for decades. Erik Hollnagel, writing in EUROCONTROL's [HindSight magazine](https://www.skybrary.aero/sites/default/files/bookshelf/3934.pdf), puts it plainly: "the way that people think about work and the way that work is actually done are not necessarily the same." He adds that it is "impossible, in practice as well as in principle, precisely to prescribe how work should be done."

This is the core of the Safety-II view. Safety-I asks why things go wrong and treats any deviation from the procedure as the problem. Safety-II asks why things go right, and recognises that people adjust their work constantly to get it done. EUROCONTROL's [systems thinking principles](https://www.skybrary.aero/index.php/Toolkit:Systems_Thinking_for_Safety:_Ten_Principles) make the same point: "Performance of the same task or activity will and must vary."

For a services firm, the lesson is direct. A manual cannot anticipate every case, so people adapt. If nobody sees those adaptations, you lose control of risk, cost and quality. You need visibility, not stricter rules.

## Why documentation goes stale

Aviation maintenance has some of the best evidence on how procedures fail in practice. Robert Baron's review for the [Flight Safety Foundation](https://flightsafety.org/asw-article/procedural-drift-causes-and-consequences/) lists its causes: procedures that are missing, incomplete or unrealistic, technicians who find a "better way," and routine violations that spread until they become the norm. He cites NASA reporting data where missing information was the most common document deficiency, at 48 per cent of 458 reports. Aviation is far more tightly regulated than most services work. If its manuals drift, yours will too.

Office work shows the same pattern. APQC's [self-reported survey of 982 knowledge workers](https://www.apqc.org/about-apqc/news-press-release/apqc-survey-finds-one-quarter-knowledge-workers-time-lost-due) names "workarounds for broken systems and processes" among the main drains on their time.

## Process mining and conformance checking

Workshops tell you what people believe happens. System data tells you what was recorded. The [Process Mining Manifesto](https://www.win.tue.nl/ieeetfpm/shared/process_mining_manifesto-small.pdf), published by the IEEE Task Force on Process Mining in 2011, defines the discipline as a way to "discover, monitor and improve real processes (i.e., not assumed processes) by extracting knowledge from event logs."

Its conformance checking technique measures drift. It compares an existing process model with an event log of the same process to check "if reality, as recorded in the log, conforms to the model and vice versa." Two measures matter. **Fitness** asks whether the documented model can reproduce what actually happened. **Precision** asks whether the model allows far more behaviour than ever occurs. Work by [Adriansyah, van der Aalst and colleagues](https://www.vdaalst.com/publications/p818.pdf) notes that deviations between recorded behaviour and models "often occur in practice," and none of the real logs they tested fitted their models perfectly.

### Process mining is not task mining

The two are often confused. As [IBM explains](https://www.ibm.com/think/topics/task-mining), process mining uses event logs from systems such as ERP and CRM to analyse end-to-end processes. Task mining uses desktop data: "keystrokes, mouse clicks and data entries," and sometimes screenshots.

That distinction matters for trust. The UK ICO's [guidance on monitoring workers](https://ico.org.uk/media/for-organisations/uk-gdpr-guidance-and-resources/employment-information/employment-practices-and-data-protection-monitoring-workers-1-0.pdf) lists keystroke monitoring as high-risk processing that needs a data protection impact assessment, and says "If you can achieve your aim in a less intrusive way, you must do so." For process drift, it usually exists. Status changes, assignments and handoffs between systems tell you how work moves without recording what anyone typed. More in [how to map work without monitoring people](https://missioncntrl.io/news/map-work-without-monitoring-people).

## Why it matters now: regulators want processes that work

APRA's [Prudential Standard CPS 230](https://www.apra.gov.au/sites/default/files/2023-07/Prudential%20Standard%20CPS%20230%20Operational%20Risk%20Management%20-%20clean.pdf) commenced on 1 July 2025. It requires regulated entities to "identify and document the processes and resources needed to deliver critical operations," including people, technology, information, facilities and service providers. It also requires tolerance levels for each critical operation and a systematic testing program for business continuity. APRA's [announcement](https://www.apra.gov.au/news-and-publications/apras-new-prudential-standard-operational-risk-management-comes-force) covers banks, insurers and superannuation funds.

In the UK, the [FCA](https://www.fca.org.uk/firms/operational-resilience) required in-scope firms to be able to operate important business services within impact tolerances by 31 March 2025, with mapping and testing complete. In its [March 2026 observations](https://www.fca.org.uk/publications/good-and-poor-practice/operational-resilience-insights-observations-one-year), the FCA found that mapping "has been largely focused on technology," and said firms should also include "facilities, people, processes, information." It also noted that "Clear ownership and accountability of mapping data reduce the risk of outdated or inaccurate information."

A process map that describes work as imagined will not survive a real test. If you are not regulated yourself, your regulated clients may be, and their expectations flow down to service providers.

## The playbook: seven steps to find and close drift

- **Pick one workflow that matters.** Choose one with a clear start and end, real volume and real consequences, such as onboarding or claims.

- **Collect the documented version.** Gather the SOP, process map and training material. Note who owns each and when it was last reviewed.

- **Extract the recorded version.** Pull case IDs, activity names, timestamps and team or role from the systems where the work lives. Use metadata only. You need to know that a file moved from intake to review on Tuesday, not what the email said.

- **Compare the two.** Check the most common paths against the documented steps. Look for skipped steps, extra steps, steps in a different order, rework loops and work leaving the system of record.

- **Talk to the people doing the work.** Bring the variants to the team, not only their managers. Ask why each path exists. The people closest to the work understand its constraints best.

- **Classify every material variant.** Use the three buckets below. Each one gets an owner and a decision.

- **Close the loop.** Update the document, fix the system or retrain, then re-measure on the next cycle to confirm the change held.

### The drift checklist

- Is the SOP more than 12 months past its last review?

- Do the documented steps match the activity names in your systems?

- What share of cases follow the documented path end to end?

- Where do cases loop back to an earlier step?

- Where does work leave the system of record, into email, spreadsheets or chat?

- Do controls in the document, such as approvals or checks, actually show up in the data?

## Classifying variants: adopt, fix or redesign

Steven Alter's [theory of workarounds](https://core.ac.uk/download/301377276.pdf) defines a workaround as "a goal-driven adaptation, improvisation, or other change to one or more aspects of an existing work system." His review shows workarounds cut both ways: they can "illuminate a path toward greater efficiency," and they can "obscure latent errors and inefficiencies." That is why classification matters more than detection.

- **Good drift: adopt it.** The team found a faster or safer path that still meets every control. Write it into the standard and spread it.

- **Bad drift: fix it.** A step that protects the client or the firm is being skipped, usually under time pressure. Example: a conflicts check recorded after work starts. Fix the pressure that made skipping feel reasonable, not only the behaviour.

- **Workaround: redesign the system.** People leave the official path because the official path does not work. Example: a shared spreadsheet tracking status because the practice system cannot. Do not ban the spreadsheet. Fix what made it necessary.

**Illustrative example**

A 300-person firm checks its onboarding SOP against six months of system data. Many cases loop back from review to intake for missing documents. Some skip sign-off entirely. The loop is a workaround caused by a weak intake form. The skipped sign-off is bad drift. One team's single upfront document checklist is good drift worth adopting firm-wide.

## Set a cadence

Drift is continuous, so the review must be too:

- **Monthly:** track conformance and rework rates for your most critical workflows. Flag any sudden change.

- **Quarterly:** run the full seven-step review on one or two workflows. Rotate through your process inventory.

- **After any change:** re-measure after a system rollout, restructure or new client segment. These are when drift accelerates.

- **Annually:** confirm every SOP has a named owner and a review date, and that regulated processes have been tested against real data.

Drift often shows up first at handoffs, a theme we explored in [why work about work is a handoff problem](https://missioncntrl.io/news/work-about-work-is-a-handoff-problem). Mission Control was built on the same principle: measure how work moves between people and teams, not what they write.

## Questions

### What is process drift?

Process drift is the gap between how a process is documented and how it is actually performed. It builds through system changes, turnover and informal fixes. Some drift improves the process and some creates risk, so classify it rather than simply eliminating it.

### What is the difference between process mining and task mining?

Process mining analyses event logs from business systems to reconstruct end-to-end processes. Task mining captures desktop activity such as clicks, keystrokes and sometimes screenshots. Process mining is far less intrusive, which matters for trust and privacy.

### How often should we review SOPs against real practice?

Track conformance on critical workflows monthly and run a full review on one or two workflows each quarter. Re-measure after any major system or organisational change. Make sure every SOP has a named owner and a review date.

## Sources

- [Hollnagel, E., Can we ever imagine how work is done? HindSight 25, EUROCONTROL (2017)](https://www.skybrary.aero/sites/default/files/bookshelf/3934.pdf)

- [EUROCONTROL, Systems Thinking for Safety: Ten Principles (2014)](https://www.skybrary.aero/index.php/Toolkit:Systems_Thinking_for_Safety:_Ten_Principles)

- [Baron, R., Procedural drift: causes and consequences, Flight Safety Foundation (2018)](https://flightsafety.org/asw-article/procedural-drift-causes-and-consequences/)

- [APQC, Survey finds one quarter of knowledge workers' time is lost due to productivity drains (2021)](https://www.apqc.org/about-apqc/news-press-release/apqc-survey-finds-one-quarter-knowledge-workers-time-lost-due)

- [IEEE Task Force on Process Mining, Process Mining Manifesto (2011)](https://www.win.tue.nl/ieeetfpm/shared/process_mining_manifesto-small.pdf)

- [Adriansyah, A., Munoz-Gama, J., Carmona, J., van Dongen, B. F. and van der Aalst, W. M. P., Measuring precision of modeled behavior](https://www.vdaalst.com/publications/p818.pdf)

- [IBM, What is task mining?](https://www.ibm.com/think/topics/task-mining)

- [ICO, Employment practices and data protection: monitoring workers (2023)](https://ico.org.uk/media/for-organisations/uk-gdpr-guidance-and-resources/employment-information/employment-practices-and-data-protection-monitoring-workers-1-0.pdf)

- [APRA, Prudential Standard CPS 230 Operational Risk Management (2023)](https://www.apra.gov.au/sites/default/files/2023-07/Prudential%20Standard%20CPS%20230%20Operational%20Risk%20Management%20-%20clean.pdf)

- [APRA, APRA's new prudential standard on operational risk management comes into force (2025)](https://www.apra.gov.au/news-and-publications/apras-new-prudential-standard-operational-risk-management-comes-force)

- [FCA, Operational resilience](https://www.fca.org.uk/firms/operational-resilience)

- [FCA, Operational resilience: insights and observations one year on (2026)](https://www.fca.org.uk/publications/good-and-poor-practice/operational-resilience-insights-observations-one-year)

- [Alter, S., Theory of workarounds, Communications of the Association for Information Systems (2014)](https://core.ac.uk/download/301377276.pdf)
