# AI agents rarely fail at the task. They fail at the hand-off

> Agent projects in services operations stall where work moves between the agent, people and systems. Design the hand-off before you design the agent.

Published 23 November 2026 by the Mission Control team. Canonical: https://missioncntrl.io/news/ai-agents-fail-at-the-handoff

## Key points

- Most AI agent projects in services operations do not stall on the task itself. They stall where work moves between the agent, people and other systems.

- Benchmarks point the same way: in the CRMArena-Pro benchmark, leading agents fell from about 58 per cent success on single-turn tasks to about 35 per cent once a multi-turn conversation was involved.

- Gartner expects over 40 per cent of agentic AI projects to be cancelled by the end of 2027, citing cost, unclear value and weak risk controls.

- Regulators and government guidance ask for the same things a good hand-off needs: a named accountable person, real override points and a way to stop.

- Before you build an agent, write its hand-off spec: entry criteria, context packet, confidence and escalation rules, a named owner, an exception queue and a measure of hand-off wait time.

Most conversations about AI agents start with the task. Can it draft the engagement letter, triage the claim, reconcile the statement? In services operations, the task is rarely where an agent project dies.

It dies at the edges. The agent finishes its part and nobody picks up the exception. A reviewer gets a draft with no idea what the agent checked. The agent writes to the practice system, the update half fails, and nobody notices for a week. The case now waits in a new place.

Our view is simple. Design the hand-off before you design the agent. Hand-offs are where work stops moving, and, as we argued in [work about work is a hand-off problem](https://missioncntrl.io/news/work-about-work-is-a-handoff-problem), they are where most delay in services firms already lives.

## Stalling is the normal outcome, for now

The evidence on agent projects is early, but it points one way. In June 2025 Gartner predicted that [over 40 per cent of agentic AI projects will be cancelled by the end of 2027](https://sdtimes.com/agentic-ai/gartner-more-than-40-of-agentic-ai-projects-will-be-canceled-in-next-few-years/), due to escalating costs, unclear business value or inadequate risk controls. Gartner's advice was to redesign workflows rather than bolt agents onto legacy systems. Treat this as a forecast, not a measurement. The supporting poll was of 3,412 webinar attendees, only 19 per cent of whom reported significant investment.

McKinsey's survey data shows the same gap between trying and scaling. In its [State of AI 2025](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-2025) (1,993 participants, fielded June to July 2025), 23 per cent of respondents said their organisation was scaling an agentic system somewhere, and another 39 per cent were experimenting. The [2026 edition](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai) (1,719 participants, fielded May to June 2026) found about two in ten respondents scaling agents. Large enterprises rose to 40 per cent from 27 per cent, while smaller organisations stayed at 22 per cent.

The most quoted figure comes from MIT NANDA's "GenAI divide" report, which, as [The Register reported](https://www.theregister.com/software/2025/08/18/generative-ai-does-nothing-for-95-percent-of-companies/1118115), found that 95 per cent of organisations saw zero return from their generative AI efforts. Read it with care. It rests on 52 interviews, a survey of 153 people and a review of more than 300 public initiatives, and "return" is not tightly defined. Its diagnosis is more useful: the authors blamed systems' inability "to retain data, to adapt, and to learn over time", and said tools fail in critical workflows due to "lack of memory and customization". That is a context problem.

## Agents are weakest exactly where work changes hands

Research benchmarks show how agents actually behave. Four findings stand out.

- **Talking to people is hard for agents.** Carnegie Mellon's TheAgentCompany benchmark simulates a small company. The [best agent tested completed 24 per cent of tasks](https://www.cs.cmu.edu/news/2025/agent-company), or 34.4 per cent with partial credit. The failures were telling: one agent never contacted the HR manager when told to, and another, unable to find a colleague in the chat platform, renamed a different user to that person's name. These are hand-off failures, not skill failures.

- **Multi-turn work drops sharply.** The [CRMArena-Pro](https://arxiv.org/abs/2505.18878) benchmark found leading agents reached about 58 per cent success on single-turn business tasks and about 35 per cent in multi-turn settings.

- **Repeat runs are inconsistent.** The [tau-bench](https://arxiv.org/abs/2406.12045?context=cs) study tested agents in customer service conversations with tools and policy rules. The best succeeded on under half of tasks, and the chance of succeeding on the same task eight times in a row was below 25 per cent in the retail domain. Operations runs the same process thousands of times.

- **Agent to agent hand-offs fail too.** A study of more than 1,600 traces from seven multi-agent frameworks [identified 14 failure modes](https://arxiv.org/abs/2503.13657v3) in three groups: system design issues, inter-agent misalignment and task verification.

One more finding matters for design. METR measured agents on software tasks and found [near 100 per cent success on tasks that take humans under four minutes, and under 10 per cent on tasks over about four hours](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/). The trend is moving quickly. For now, the practical response is to break work into short, checkable steps. That raises the number of hand-offs, which is why designing them well is the whole game.

## Three hand-offs, three ways to fail

### Human to agent: the trigger and the context

The agent starts on an incomplete file, or starts too early, or nobody is sure what starts it at all. The fix is a clear trigger and a defined set of inputs that must be present before the agent begins.

### Agent to human: the escalation

Either everything escalates, so the reviewer becomes a rubber stamp, or nothing does, and errors reach clients. Escalations that arrive without context force the person to redo the agent's work. People who approve hundreds of clean outputs stop reading them, a risk the EU AI Act calls automation bias.

### Agent to system: the write-back

This one fails silently. The agent believes it updated the record, the system rejected half the fields, and the next step runs on stale data. Anthropic's engineering guidance says agents should [gain "ground truth" from the environment at each step](https://www.anthropic.com/research/building-effective-agents), pause for human feedback at checkpoints or when blocked, and use stopping conditions such as a maximum number of iterations.

## What the rule-makers already ask for

Article 14 of the EU AI Act, which applies to systems classed as high-risk, says people overseeing them must be able to [understand the system's capacities and limitations, stay aware of automation bias, correctly interpret its output, override or reverse it, and halt it through a "stop" button or similar procedure](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14). Most back-office agents will not be high-risk under the Act. The list still works well as a design spec.

Australia's National AI Centre takes a similar line. Its Guidance for AI Adoption replaces the Voluntary AI Safety Standard with six essential practices, including "decide who is accountable" and "maintain human control". As [Allens summarises it](https://www.allens.com.au/insights-news/insights/2025/11/governance-doesnt-stand-still-9-faqs-to-help-understand-the-governments-new-guidance-for-ai-adoption/), that means naming a specific person for each AI system, building in human override points, and keeping alternative pathways so critical functions continue if a system fails.

McKinsey's 2025 high performers were also more likely to have [defined processes to determine how and when model outputs need human validation](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-2025).

## The hand-off design checklist

Write one for every agent before anyone builds it. If you cannot fill a line in, you are not ready.

- **Entry criteria.** What event starts the agent, and which inputs must be present and valid first? If they are missing, who is asked, and by when?

- **Context packet.** What the agent receives, and what it passes on: the inputs it used, the checks it ran, what it could not verify and why it stopped.

- **Confidence and escalation rules.** Written conditions that send a case to a person: missing data, values outside set limits, a client flagged as sensitive, conflicting sources, repeated failed attempts.

- **Named human owner.** One person accountable for the agent's output and its exceptions, with authority to pause or stop it. A team name is not an owner.

- **Exception queue.** One visible place where escalations land, with a service level, a backup person and a fallback manual process if the agent is switched off.

- **Write-back and audit trail.** Every system update confirmed by reading it back. Every action logged with inputs, output, rule applied and who approved it.

- **Hand-off wait time.** Measured from the moment the agent escalates to the moment a person acts, and from the moment a person approves to the moment the next step starts.

**Illustrative example**

An agent prepares new client onboarding files. It completes its part in 10 minutes. One case in five escalates for a missing identity document, and those escalations sit in a shared inbox for an average of two working days. Those cases now wait longer at the hand-off than they ever spent in data entry. Fixing the queue, with a named owner and a same-day service level, does more for elapsed time than any improvement to the agent.

## Measure the wait, not just the accuracy

Most agent pilots report accuracy and hours saved. Neither tells you whether clients get served sooner. For that, track three numbers per agent: escalation rate, rework rate after human review, and hand-off wait time. If accuracy rises while elapsed time stays flat, the work is waiting somewhere you are not looking.

This is the same discipline behind [flow efficiency](https://missioncntrl.io/news/flow-efficiency-services-firms): most elapsed time is waiting, and agents can add new waiting points as easily as they remove old ones. It is also why so many [automation programs stall](https://missioncntrl.io/news/why-automation-programs-stall) after a promising pilot. At Mission Control we map how work moves between people, teams and systems before sizing an automation, because the hand-offs decide whether it pays.

## Questions

### Why do AI agent projects stall in services operations?

The agent often performs its core task well enough, but work stalls where it moves between the agent, people and systems. Missing inputs, escalations without context and unowned exception queues add new waiting points that cancel out the time saved.

### What should an AI agent hand-off include?

A good hand-off has clear entry criteria, a context packet showing what the agent used and checked, written escalation rules, one named human owner and a visible exception queue. Every system update should be confirmed and logged.

### How do you measure whether an AI agent is working?

Track escalation rate, rework rate after human review and hand-off wait time alongside accuracy. If accuracy improves but total elapsed time for each case does not fall, work is waiting at a hand-off that needs fixing.

## Sources

- [SD Times, Gartner: More than 40% of agentic AI projects will be canceled in the next few years (2025)](https://sdtimes.com/agentic-ai/gartner-more-than-40-of-agentic-ai-projects-will-be-canceled-in-next-few-years/)

- [McKinsey, The state of AI in 2025: Agents, innovation, and transformation (2025)](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-2025)

- [McKinsey, The state of AI in 2026: On the road to ROI (2026)](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai)

- [The Register, report on MIT NANDA's The GenAI Divide: State of AI in Business 2025 (2025)](https://www.theregister.com/software/2025/08/18/generative-ai-does-nothing-for-95-percent-of-companies/1118115)

- [Carnegie Mellon University School of Computer Science, TheAgentCompany benchmark results (2025)](https://www.cs.cmu.edu/news/2025/agent-company)

- [Huang et al., CRMArena-Pro: Holistic assessment of LLM agents across diverse business scenarios and interactions (2025)](https://arxiv.org/abs/2505.18878)

- [Yao et al., tau-bench: A benchmark for tool-agent-user interaction in real-world domains (2024)](https://arxiv.org/abs/2406.12045?context=cs)

- [Cemri et al., Why do multi-agent LLM systems fail? (2025)](https://arxiv.org/abs/2503.13657v3)

- [METR, Measuring AI ability to complete long tasks (2025)](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/)

- [Anthropic, Building effective agents (2024)](https://www.anthropic.com/research/building-effective-agents)

- [European Commission AI Act Service Desk, Article 14: Human oversight](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14)

- [Allens, Governance doesn't stand still: 9 FAQs on the Government's new Guidance for AI Adoption (2025)](https://www.allens.com.au/insights-news/insights/2025/11/governance-doesnt-stand-still-9-faqs-to-help-understand-the-governments-new-guidance-for-ai-adoption/)
