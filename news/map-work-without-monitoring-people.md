# How to map work without monitoring people

> Process discovery and employee surveillance are different things. Here is what the law says in Australia, the UK and the US, and the design principles that keep them apart.

Published 22 November 2026 by the Mission Control team. Canonical: https://missioncntrl.io/news/map-work-without-monitoring-people

## Key points

- Process discovery (studying how work items move) and employee monitoring (studying what individuals do) are different activities. They carry different legal and cultural risks.

- In Australia, NSW and the ACT require 14 days' written notice before computer surveillance. The ACT also requires consultation. Victoria's government has backed workplace surveillance reform in principle. Federal tranche 2 privacy reforms leave the employee records exemption in place.

- In the UK, the ICO's 2023 guidance expects transparency, a clear purpose, the least intrusive means and usually a data protection impact assessment.

- In the US, New York requires notice and acknowledgement for electronic monitoring. California's privacy law has covered employee data since 2023.

- The safest and most useful design measures the work, not the worker: case-level metadata, aggregated views, no content capture and no individual scoring.

Any serious attempt to understand how work moves through an organisation runs into the same question from HR, legal and staff: is this surveillance? It is the right question to ask. The answer depends less on the technology than on what is measured, why and who can see it.

This article sets out the legal landscape in Australia, the UK and the US as we understand it in November 2026. It then argues for a design approach that makes the question easy to answer. It is general information, not legal advice. Workplace privacy law varies by jurisdiction and changes often, so take advice for your own situation.

## Two very different things

**Employee monitoring** is about the individual: keystrokes, screenshots, active-window tracking, idle time, productivity scores. Its natural output is a judgement about a person.

**Process discovery** is about the work item: when a case was created, assigned, updated, waiting and closed, and which team handled each step. Academic process mining is built on exactly this. An event log records a [case identifier, an activity and a timestamp](https://en.wikipedia.org/wiki/Process_mining). Its natural output is a picture of a workflow.

The two can blur. Case data still contains who did what, and a poorly designed tool can turn a process view into a league table of individuals. That is why design choices matter as much as legal compliance.

## Australia

**Federal privacy law.** The Privacy Act 1988 contains an [employee records exemption](https://www.pinsentmasons.com/out-law/analysis/privacy-exemption-for-australian-private-sector-employee-records-has-uncertain-future) for private-sector employers. It covers acts directly related to a current or former employment relationship and the employee records the employer holds. Do not read that as a free pass. A [new statutory tort for serious invasions of privacy commenced on 10 June 2025](https://corrs.com.au/insights/australias-ongoing-privacy-reforms-bolstering-australias-privacy-regulatory-framework), and commentators note it may limit how far employers can rely on the exemption. The exemption also does not cover contractors, clients or other third parties whose information appears in workflow data. Reform of the exemption was recommended by the Privacy Act Review. But the [tranche 2 exposure draft released on 31 August 2026](https://www.gtlaw.com.au/insights/one-giant-leap-tranche-2-of-privacy-act-reform) does not address it.

**New South Wales.** The [Workplace Surveillance Act 2005](https://legislation.nsw.gov.au/view/whole/html/inforce/2024-07-01/act-2005-047) regulates camera, computer and tracking surveillance of employees at work. Notice must be given at least 14 days before surveillance begins, unless the employee agrees to less. Computer surveillance must also be carried out [in line with a policy](https://webiis08.mondaq.com/australia/employee-rights-labour-relations/629474/workplace-surveillance-in-nsw-having-a-computer-surveillance-policy-is-a-mandatory-requirement) the employee has been told about.

**Australian Capital Territory.** The [Workplace Privacy Act 2011](https://www.legislation.act.gov.au/DownloadFile/a/2011-4/current/PDF/2011-4.PDF) also requires 14 days' written notice for optical, tracking and data surveillance. It adds a duty to [consult in good faith](https://www.mondaq.com/australia/employee-rights-labour-relations/137436/workplace-privacy-act-2011-act) with workers who raise concerns during that period.

**Victoria.** A Legislative Assembly committee tabled its [Inquiry into workplace surveillance](https://www.parliament.vic.gov.au/inquiryintoworkplacesurveillance) report on 13 May 2025 with 18 recommendations. They include new technology-neutral laws requiring surveillance to be reasonable, necessary and proportionate. The government's November 2025 response gave [in-principle support to 15 of the 18 recommendations](https://corrs.com.au/insights/victorian-government-backs-landmark-workplace-surveillance-reforms). Organisations with Victorian staff should expect stricter rules.

## United Kingdom

On 3 October 2023 the Information Commissioner's Office published [guidance on monitoring workers](https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2023/10/ico-publishes-guidance-to-ensure-lawful-monitoring-in-the-workplace) under the UK GDPR. Summaries from [Simmons & Simmons](https://www.simmons-simmons.com/en/publications/clntro05s00v4udeo8l5vndzs/employee-monitoring-updated-ico-guidance) and [Hunton](https://www.huntonprivacyblog.com/2023/10/05/uk-ico-publishes-guidance-on-workplace-monitoring/) draw out the essentials:

- Tell workers about the nature, extent and reasons for monitoring.

- Do not monitor "just in case". Document why you are monitoring and what you will do with the information.

- Use the least intrusive means that achieves the purpose.

- Carry out a data protection impact assessment where processing is likely to be high risk. The ICO encourages one even where it is not strictly required.

- Recognise that people working from home have a greater expectation of privacy.

## United States

There is no single federal standard for workplace monitoring, so state law matters.

- **New York.** Since 7 May 2022, [Civil Rights Law § 52-c](https://www.outtengolden.com/newsroom/new-yorks-new-privacy-law-entitles-employees-to-notice-of-electronic-monitoring/) has required private employers that monitor employees' telephone, email or internet use to give written notice on hiring, obtain an acknowledgement and post a notice. [Civil penalties](https://www.kelleydrye.com/viewpoints/blogs/labor-days/ny-requires-notice-of-electronic-monitoring-to-employees-are-you-in-compliance) start at $500 for a first violation. Connecticut and Delaware have similar notice laws.

- **California.** The employee data exemption in the California Consumer Privacy Act [expired on 1 January 2023](https://www.morganlewis.com/pubs/2022/10/california-consumer-privacy-act-employee-and-b2b-exemptions-expire-january-1-2023). Covered employers now owe California staff privacy notices, access and deletion rights, and appropriate contracts with service providers.

## Our view: measure the work, not the worker

Across these regimes the direction is consistent. Regulators want transparency, a clear purpose, proportionality and minimal data. A process discovery program designed around those principles is easier to defend, easier to roll out and more useful. People cooperate with a project they understand, and resist one they suspect.

We think seven design principles matter most:

- **Case-level, not person-level.** The unit of analysis is the work item and its journey. Views are by workflow, step and team.

- **Metadata, not content.** Timestamps, status changes and assignments are enough to show where work waits. The contents of emails, documents and messages are not needed and should not be collected.

- **Aggregate by default.** Report at team or step level with minimum group sizes, so individuals cannot be singled out.

- **No individual performance scoring.** Process data should never become a ranking of people. If it does, trust and data quality both collapse.

- **A written purpose.** State what the program is for, such as reducing cycle time or sizing automation, and what it will not be used for.

- **Notice and consultation everywhere,** including where the law does not strictly require them. Tell people before anything starts, explain what is and is not collected, and give them a channel for concerns.

- **Short retention and tight access.** Keep data only as long as the analysis needs it, and limit who can see raw records.

These principles also produce better analysis. Systems record wait time between steps faithfully. Watching people in the moment mostly shows who looks busy. The question that matters to a services business is where the work waits. You can answer it fully without looking at anyone's screen.

## Questions

### Is process mining the same as employee monitoring?

No. Process mining analyses how work items move through a workflow using system event data such as case identifiers, activities and timestamps. Employee monitoring tracks what individuals do, such as keystrokes, screenshots or active time. Process discovery can still involve personal information, so it should be designed and disclosed carefully.

### Do Australian employers need to give notice before computer surveillance?

In New South Wales and the Australian Capital Territory, yes. Both require written notice at least 14 days before surveillance begins, unless the employee agrees to less. The ACT also requires good-faith consultation. Other states regulate surveillance differently, and Victoria is moving towards new laws. Take legal advice for your situation.

### What does the UK ICO expect from employers that monitor workers?

The ICO's October 2023 guidance expects employers to tell workers what monitoring takes place and why, to avoid monitoring "just in case", to use the least intrusive means available and to carry out a data protection impact assessment where the processing is likely to be high risk.

## Sources

- [Workplace Surveillance Act 2005 (NSW)](https://legislation.nsw.gov.au/view/whole/html/inforce/2024-07-01/act-2005-047)

- [Workplace Privacy Act 2011 (ACT)](https://www.legislation.act.gov.au/DownloadFile/a/2011-4/current/PDF/2011-4.PDF)

- [Parliament of Victoria, Inquiry into workplace surveillance](https://www.parliament.vic.gov.au/inquiryintoworkplacesurveillance)

- [Corrs Chambers Westgarth, Victorian Government backs landmark workplace surveillance reforms](https://corrs.com.au/insights/victorian-government-backs-landmark-workplace-surveillance-reforms)

- [Corrs Chambers Westgarth, Australia's ongoing privacy reforms](https://corrs.com.au/insights/australias-ongoing-privacy-reforms-bolstering-australias-privacy-regulatory-framework)

- [Gilbert + Tobin, One giant leap: tranche 2 of Privacy Act reform](https://www.gtlaw.com.au/insights/one-giant-leap-tranche-2-of-privacy-act-reform)

- [ICO, Guidance to ensure lawful monitoring in the workplace](https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2023/10/ico-publishes-guidance-to-ensure-lawful-monitoring-in-the-workplace)

- [Outten & Golden, New York's electronic monitoring notice law](https://www.outtengolden.com/newsroom/new-yorks-new-privacy-law-entitles-employees-to-notice-of-electronic-monitoring/)

- [Morgan Lewis, CCPA employee and B2B exemptions expire](https://www.morganlewis.com/pubs/2022/10/california-consumer-privacy-act-employee-and-b2b-exemptions-expire-january-1-2023)
