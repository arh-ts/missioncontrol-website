# How to build an automation business case your CFO will sign

> Hours saved are not dollars saved. A structure for sizing automation that survives a sceptical finance team, with a worked example.

Published 22 November 2026 by the Mission Control team. Canonical: https://missioncntrl.io/news/automation-business-case-cfo

## Key points

- Most automation business cases fail scrutiny for the same reasons. They treat hours saved as cash saved, ignore adoption ramps and running costs, and use estimated volumes rather than measured ones.

- Build the case on measured volume and handling time, apply an automation rate and an adoption curve, then risk-adjust. Forrester's TEI method uses the same four elements: benefits, costs, flexibility and risk.

- Keep two numbers separate: capacity released and cash realised. Capacity only becomes cash when it avoids a hire, removes contractor or overtime spend, or lets you grow without adding headcount.

- Value elapsed time explicitly. Faster cycle times often matter more to cash flow and client experience than the hours saved.

Few documents lose credibility faster than an automation business case that promises to save "12 FTE". The CFO asks which 12 people, and when they are leaving. The answer is usually that nobody is leaving, and the case is quietly filed. That is a shame, because the underlying opportunity is often real. The problem is that it was sized in a way finance cannot bank.

This guide sets out a structure we think holds up in front of a sceptical finance team. It borrows from established investment appraisal practice. It is built on measured data rather than workshop estimates, and it is honest about the difference between time and money.

## Five mistakes that sink automation business cases

- **Hours saved presented as cash.** Releasing 2,000 hours across a team of 40 does not reduce cost unless something else changes. Without a plan for that capacity, the saving is theoretical.

- **Estimated volumes.** "We do about 100 a week" is often wrong by a wide margin in either direction. Volumes should come from system records.

- **No adoption ramp.** Automations rarely reach full use on day one. People keep doing things the old way, edge cases are routed back to humans, and trust is built slowly.

- **Missing running costs.** Licences, hosting, monitoring and, above all, maintenance when the surrounding process or software changes. EY lists [not having a business case before proofs of concept](https://ey.com/en_qa/financial-services-emeia/get-ready-for-robotic-process-automation) among the common causes of failed RPA projects. UiPath notes that companies [underestimate the work required after automation is established](https://www.uipath.com/blog/rpa/why-rpa-deployments-fail).

- **Ignoring elapsed time.** A case built only on effort misses what is often the bigger prize: work that finishes days sooner, so invoices go out sooner and clients notice.

## A structure finance will recognise

Forrester's [Total Economic Impact methodology](https://www.forrester.com/policies/tei) has been used for over two decades to justify technology investments. It evaluates four components: cost, benefits, flexibility and risk. Its published studies present benefits and costs as risk-adjusted present values over three years. You do not need to commission a study to borrow the discipline. Every automation case should state each of those four elements explicitly.

### 1. Benefits: start from measured flow

**Annual capacity released = cases per year × minutes per case removed × automation rate × adoption**

Cases per year and current handling time should come from your systems. The automation rate is the share of cases the automation can handle without a person. Adoption is the share of eligible cases that actually go through it.

Convert hours to dollars with a fully loaded cost per productive hour, not a salary divided by 2,080. In Australia, average weekly ordinary time earnings for full-time adults were [$2,083.70 in May 2026](https://www.abs.gov.au/media-centre/media-releases/average-weekly-earnings-growth-lowest-2022), about $108,000 a year. Add the [12 per cent super guarantee that applies from 1 July 2025](https://www.ato.gov.au/businesses-and-organisations/small-business-newsroom/the-final-sg-rate-increase-is-coming-on-1-july), plus your own payroll tax, insurance, leave and overheads. Then divide by productive hours after leave and non-chargeable time. For an average full-time employee this often lands somewhere around $75 to $90 per productive hour. Use your own payroll data, by role, for the people whose work is affected.

### 2. Elapsed-time benefits: value the waiting

Where an automation removes a delay, size that separately. Two approaches work well:

- **Cash timing.** If billing starts when onboarding completes, cutting onboarding from eight days to three brings five days of revenue forward on every new engagement. That is a working capital gain your CFO can calculate.

- **Cost of delay.** Don Reinertsen argues that if you measure only one thing in flow, it should be [cost of delay](https://www.pmi.org/disciplined-agile/da-flex-toc/why-looking-at-the-value-stream-is-so-important): what each day of waiting costs in lost revenue, penalties or client churn. Even a rough figure beats leaving it out.

### 3. Costs: include the whole life

Include build or implementation, licences and hosting, monitoring, and a realistic maintenance allowance for each year after go-live. Include the internal time of the people who test, train and own it. If you would not run the automation without an owner, the owner's time is a cost.

### 4. Risk and flexibility: adjust, do not inflate

Apply an explicit risk adjustment to benefits, for example a 10 to 25 per cent reduction depending on how well understood the process is, and state why. List flexibility value separately, such as the option to extend the automation to a second team, but do not add it to the headline. Finance teams trust cases that visibly discount their own optimism.

## A worked example (illustrative)

The figures below are invented to show the method. They are not results from a client.

**Process:** client onboarding, 1,200 cases a month (14,400 a year), measured from system records.

**Step automated:** re-keying client details from intake forms into the practice and billing systems, measured at 35 minutes a case.

**Automation rate:** 70 per cent of cases handled end to end, the rest routed to a person.

**Adoption:** 50 per cent in the first quarter, 80 per cent after that.

**Loaded cost:** $80 per productive hour.

**Steady-state capacity released:** 14,400 × 35 min × 70% × 80% ≈ 4,704 hours a year, worth $376,320. Year one, with the ramp, is about 4,263 hours, worth $341,040.

**Risk adjustment:** 20 per cent, giving $272,832 in year one and $301,056 in each of years two and three.

**Costs:** $60,000 to build, $2,500 a month to run and $9,000 a year in maintenance from year two. That is $90,000 in year one and $39,000 a year after.

**Three-year view (undiscounted):** about $875,000 of risk-adjusted capacity value against $168,000 of cost.

Now the honest part. 4,704 hours is roughly 2.7 full-time people at around 1,750 productive hours each. That capacity becomes cash only if the business does something with it. Examples: absorbing growth without the next two hires, ending a contractor arrangement, or cutting overtime in peak periods. A credible case states which of those will happen, who has agreed to it and when. Anything not tied to a decision should be presented as capacity, not savings.

Then add the elapsed-time benefit separately. If removing re-keying also shortens onboarding by two days, and billing starts at the end of onboarding, two days of revenue on every new engagement is brought forward. The CFO can value that directly.

## What makes a case believable

- **Measured inputs.** Volumes, handling times and wait times from system data, with the date range stated.

- **Two headline numbers,** clearly labelled: capacity released and cash realised.

- **Named decisions** that turn capacity into cash, with owners.

- **A stated risk adjustment** and the reasoning behind it.

- **A review date** and the measure you will check, so the case can be proven right or wrong.

That last point matters most. A business case is a prediction. Cases that say in advance how they will be judged get approved more often. They also build the credibility that makes the next one easier.

## Questions

### How do you calculate the ROI of an automation?

Multiply measured annual volume by the minutes the automation removes per case, the share of cases it can handle and the expected adoption. Convert the hours to dollars at a fully loaded cost per productive hour, then apply a risk adjustment. Compare the result with the full-life cost of building, running and maintaining the automation over three years.

### Are hours saved the same as money saved?

No. Hours saved are capacity released. They become money saved only when the business acts on them, for example by avoiding a hire, ending contractor or overtime spend, or growing without adding headcount. A credible business case reports the two separately.

### What costs are usually missing from automation business cases?

Ongoing maintenance when processes or systems change, monitoring, licences and hosting, and the internal time of the people who test, train and own the automation. Adoption ramps are also often ignored, which overstates first-year benefits.

## Sources

- [Forrester, Total Economic Impact methodology](https://www.forrester.com/policies/tei)

- [Australian Bureau of Statistics, Average weekly earnings, May 2026](https://www.abs.gov.au/media-centre/media-releases/average-weekly-earnings-growth-lowest-2022)

- [Australian Taxation Office, The final SG rate increase is coming on 1 July](https://www.ato.gov.au/businesses-and-organisations/small-business-newsroom/the-final-sg-rate-increase-is-coming-on-1-july)

- [EY, Get ready for robots](https://ey.com/en_qa/financial-services-emeia/get-ready-for-robotic-process-automation)

- [UiPath, Why some RPA deployments fail](https://www.uipath.com/blog/rpa/why-rpa-deployments-fail)

- [PMI Disciplined Agile, Why looking at the value stream is so important](https://www.pmi.org/disciplined-agile/da-flex-toc/why-looking-at-the-value-stream-is-so-important)
