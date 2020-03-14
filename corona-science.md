---
title: "Corona Science Journal"
date: 2020-03-14T10:13:25+01:00
draft: false
---
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@powerdns_bert">
<meta name="twitter:creator" content="@powerdns_bert">
<meta name="twitter:title" content="Corona Science Journal">
<meta name="twitter:description" content="An overview of the latest scientific and treatment developments of COVID-19, updated frequently, including links to original sources, preprints and papers">
<meta name="twitter:image" content="http://berthub.eu/articles/death-rate-feature.png">
Hello and welcome to this stream of consciousness I dare to call "the Corona
Science Journal". Updated frequently. Latest update: 14th of March 14:32 UTC. View history of
this page [on
GitHub](https://github.com/ahupowerdns/corona-science/commits/master)
([RSS](https://github.com/ahupowerdns/corona-science/commits/master/corona-science.md.atom)), where
you can also submit changes, fixes and updates.

There is [sufficient other
content](https://arstechnica.com/science/2020/03/dont-panic-the-comprehensive-ars-technica-guide-to-the-coronavirus/) out there that aims to tell you if things
will be bad or not. A lot of data can be found in
[Coronavirus Primer for Reasonably Rational
People](https://docs.google.com/document/d/1FfVZtg0ETPLaM8JbeFgQMz2zxmcPTpoBEoMgAzgQQvs/edit#). 
I have no specific epidemiological expertise, so I won't add to these
existing efforts.

What I can do very well however is read statistics and papers and determine
if some trend or conclusion is forming.  There are enough big questions out
there that don't get the attention they deserve. Sadly there is also a lot
of bad information and even some (very) bad science going round. In this
document I try to filter out the stuff which has a consensus forming around
it, or looks very plausible.

Here goes.

Feedback, content & interesting links are VERY welcome on bert@hubertnet.nl
or [@PowerDNS_Bert](https://twitter.com/PowerDNS_Bert).

Facts
-----
Most things COVID-19 are not yet facts because everything is so new. Here is
a brief collection of things we do know for sure:

 * It is far, far worse than seasonal flu.  Anyone who doubts this should
   look at the photos and videos from Wuhan and Northern Italy, or the graph
   below.
 * Younger and healthy people may do fine ('not die a lot'), but many people
   are not young or healthy, and we care about them too.
 * Slowing down the pandemic makes sense since it buys time for our
   healthcare systems and scientists to learn. It also spreads "peak
   illness" so our systems get less overloaded.
 * Washing hands [with normal soap](https://twitter.com/PalliThordarson/status/1236549305189597189), coughing hygiene, and "social distancing" are very
   effective in limiting the spread.  Social distancing means not going to
   that party and not organizing that event, and likely eventually not going
   to work or school.

The first feedback I got on this page was "it is just like the flu". This
graph from South Korea, where hundreds of thousands of tests have been
performed, shows the difference:

{{< figure src="/articles/death-rate-feature.png" caption="[Source](https://twitter.com/sachinrekhi/status/1236180106734735360/photo/1)">}}

Note that because of the hundreds of thousands of tests in South Korea, they
have also captured tons of asymptomatic people and not just hospital cases. 

On why it matters to slow down the outbreak, even if we perhaps can't stop
it, this graph is extremely useful:

{{< figure src="/articles/the-graph.jpg" >}}

This article
[Coronavirus: Why You Must Act
Now](https://medium.com/@tomaspueyo/coronavirus-act-today-or-people-will-die-f4d3d9cd99ca)
is also very helpful.

Will summer/warmer weather help?
--------------------------------
The official WHO word on this is "there is no evidence, don't count on it".
Hope is not a strategy, and warmer weather in the northern hemisphere will
do nothing for the south, but it remains a pertinent question.

One may wonder if [the pretty low
numbers](https://bnonews.com/index.php/2020/02/the-latest-coronavirus-cases/)
from warmer and more humid countries are fake (perhaps outright faked, or
just not doing testing), but they will eventually tell us a story.

Watching this one closely. There are papers that argue either side (it
[will help](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3550308)/[it won't
help](https://ccdd.hsph.harvard.edu/will-covid-19-go-away-on-its-own-in-warmer-weather/)). 
Note that "help" does not need to mean it kills
the virus - in our goal to stem the epidemic, even 10% reduction in
transmission can be helpful if it takes the reproduction number just under
1.0.

Some discussion is in this [AP article on Snopes.com
(!)](https://www.snopes.com/ap/2020/03/11/will-heat-stop-the-spread-of-new-virus-no-one-really-knows/).

The inestimable Marc Lipsitch has also weighed in: [Seasonality of SARS-CoV-2: Will COVID-19 go away on its own in warmer
weather?: tl;dr: probably not](https://ccdd.hsph.harvard.edu/will-covid-19-go-away-on-its-own-in-warmer-weather/).

Testing, infectiveness
----------------------
Earlier I wrote a bit on [how COVID-19 testing
works](https://berthub.eu/articles/posts/dna-grep-2019-ncov/), it is
important to realise that this is effectively "searching for viral genetic
material in swabs".

While it is amazing how this works, it does come with limitations: a swab in
the wrong place might miss the virus. And the other way around, just because
viral RNA is present, this does not have to come from competent virus
particles that can infect people.

This recent paper "[Clinical presentation and virological assessment of hospitalized cases of coronavirus disease 2019 in a travel-associated transmission
   cluster](https://www.medrxiv.org/content/10.1101/2020.03.05.20030502v1)"
discusses the nuances.  This [statnews.com
article](https://www.statnews.com/2020/03/09/people-shed-high-levels-of-coronavirus-study-finds-but-most-are-likely-not-infectious-after-recovery-begins/) 
provides a good explainer, and I recommend that you read it. But two key
sentences "Importantly, the scientists could not grow viruses from throat swabs or sputum specimens after day 8 of illness from people who had mild
infections.", but also "The researchers found very high levels of virus emitted from the throat of patients from the earliest point in their illness —when people are generally still going about their daily routines. Viral shedding dropped after day 5 in all but two of the patients, who had more serious illness. The two, who developed early signs of pneumonia, continued to shed high levels of virus from the throat until about day 10 or
11.".

Another way of testing is by measuring if a patient has generated antibodies
against COVID-19. This is a fascinating area which I am reading up on ([books
have arrived](https://twitter.com/PowerDNS_Bert/status/1237788602186293249)). There are early and later antibody responses
(IgM and IgG respectively). Excitingly, it appears to be possible to
determine presence of IgM and IgG for COVID-19 in 10 minutes based on a drop
of blood. Less excitingly, it also appears IgM is only present 1 or 2 weeks
after infection.

One such test is described
[on this page](https://www.biomedomics.com/products/infectious-disease/covid-19-rt/),
which includes manuals and protocols.

It appears that such a test will mainly allow you to 'look into the past' -
even if someone recovered, I think you can still see IgG antibodies.  

This kind of testing may have a role, but it is no substitute for doing
[PCR](https://berthub.eu/articles/posts/dna-grep-2019-ncov/), which takes
hours, requires special equipment and is quite laborious, but can detect the
disease at an early stage.

A brief intermezzo: reading about medical breakthroughs
-------------------------------------------------------
Because I keep track of a few unfortunate medical conditions for family and
friends, I am quite well versed in reading about "medical breakthroughs".
These happen a lot, at least on paper. It takes quite some skill to find out
if there is an actual breakthrough behind the hype.

I wrote about this before [way back in
2013](https://bert-hubert.blogspot.com/2013/07/a-null-result-bonus-to-improve-science.html),
but in short, we have a veritable chain of people who "want to believe",
including us.  This can distort the reality.

A cautious observation during patient treatment ('14 out of 20 patients
improved in clinical measurements') is spiced up slightly by the institute PR
department to 'most patients improved'.  A journalist, who also
wants to believe may spice this up a bit more: 'most of the patients tested
were cured'. Meanwhile, we as readers also want to believe, so we might not
pay that much attention to caveats. For example, perhaps the "cure" worked,
but only on a very specific subclass of patients. If we don't pay real close
attention, we may end up believing we read there was a cure for the whole
disease.

Keep this in mind when reading about COVID-19 cures or treatments that will
surely be reported in the coming weeks. 

Specific things to look out for:

 * You read about the news on a site you've never heard of before, or, it is
   on a known site full of nonsense like the Daily Mail. Note that even 'big
   name publications' fall for sensational news.
 * There is no way to find the actual research (this could be names you can
   Google, institutions or best, links to an actual preprint or paper)
 * The news is only about a few cases in a single hospital

From what I see, in the coming days/weeks we will be seeing some actually
encouraging news, but we'll be seeing way more nonsense. So be careful!

Antiviral medicines: will they help?
------------------------------------
This is actually a more complicated question: who will they help and when? 
Many anti-virals actually perform as promised, and inhibit viral replication
both in the lab ('vitro') and in primates or even people ('in vivo').  But
many papers note that best effects are achieved when the medicine is dosed
either slightly before (!!) infection, or shortly after.

This may be very helpful to stem an outbreak (if the medicine is widely
available, easy to administer and safe), but it is not necessarily much use
for someone already in the intensive care unit. 

Trials of various anti-virals are proceeding, some encouraging hints have
been picked up here and there, but there is no solid data yet. 

The big ones to watch are Remdesivir and
([Hydroxy](https://pubmed.ncbi.nlm.nih.gov/32150618-in-vitro-antiviral-activity-and-projection-of-optimized-dosing-design-of-hydroxychloroquine-for-the-treatment-of-severe-acute-respiratory-syndrome-coronavirus-2-sars-cov-2/?from_term=coronavirus+chloroquine&from_sort=date&from_pos=1))Chloroquine (an older Malaria
medicine, but with side effects and contra-indications), with an honerable mention for
[Camostat](https://www.pharmaceutical-technology.com/news/german-researchers-covid-19-drug/),
which is already approved in Japan for other treatments.

Some slight optimism on Remdesivir can be found [in this Guardian
article](https://www.theguardian.com/world/2020/mar/10/hopes-rise-over-experimental-drugs-effectiveness-against-coronavirus)
which notes that the producer has ramped up production in advance of the
outcome of trials (10th of March).  A further positive third-hand anecdote
can be found in [this
tweet](https://twitter.com/Chenbariatrics1/status/1238328364911345665),
which notes it even works on gravely ill patients, and even without
completing the 10 day course.  But it is a third-hand anecdote, and it notes
doses are scarce.

This is PURE speculation, but we might get lucky that specifically
[hydroxychloroquine](https://pubmed.ncbi.nlm.nih.gov/32150618-in-vitro-antiviral-activity-and-projection-of-optimized-dosing-design-of-hydroxychloroquine-for-the-treatment-of-severe-acute-respiratory-syndrome-coronavirus-2-sars-cov-2/?from_term=coronavirus+chloroquine&from_sort=date&from_pos=1) might be effective early in the disease and that we can
send it out to everyone who even appears to be infected.  We don't yet have
data on if this would work, but it is reasonably plausible.

Supportive medicine
-------------------
This is pretty new stuff, perhaps too new to report on yet, but it does look
interesting. Immune systems can beat the virus, but you do have to stay
alive while they do it, and this is actually what hospital and intensive
care units are trying to achieve.

There are early reports that
[Tocilizumab](https://en.wikipedia.org/wiki/Tocilizumab) /
[Actemra](https://www.reuters.com/article/us-health-coronavirus-china-roche-hldg-idUSKBN20R0LF)
has been effective on patients in
[Italy](https://www.leggo.it/italia/cronache/coronavirus_farmaco_anti_artrite_pazienti_curati_napoli_oggi_8_marzo_2020-5099254.html)
and [China](http://chinaxiv.org/abs/202003.00026). But these are very early
observational reports. Actemra is a 'blockbuster' arthritis drug, so we know
a lot about it. As of the 11th of March, there are a mounting number of
[anecdotes](https://www.repubblica.it/oncologia/news/2020/03/11/news/coronavirus_buoni_risultati_su_due_pazienti_gravi_con_tocilizumab_ora_serve_un_protocollo_per_estendere_l_uso_del_farmaco-250937051/) that Actemra is effective for certain patients, and Italy is
rolling out broader use. There is now also a [Lancet
paper](https://twitter.com/DrPujaMehta1/status/1238541499543011328).

In short, these medicines do not specifically kill or inhibit the virus, but
they aim to help fight off its effects & keep the patient alive.

Convalescent sera: using blood from recovered patients
------------------------------------------------------
Patients that have recovered will have generated COVID-19 specific
antibodies. These can be used to help cure current patients, or to
temporarily protect non-infected people, for example key medical staff.

Convalescent sera have a storied history of working and sometimes not, a
great discussion can be found in
[The convalescent sera option for containing
COVID-19](https://www.jci.org/articles/view/138003), which notes that it
likely works best for very recently infected patients, or early in the
course of the disease. 

Vaccinations
------------
To be honest I have no clue.  There is frantic ongoing activity by dozens of
groups and companies.  We don't currently know if any of these vaccines will
work (safely), nor how quickly they can be produced if they do.  Also, who
would get them?  Countries turn very nasty over such things.

This situation will hopefully clear up over time. It may be that small
quantities of vaccines become available early and could be used in targeted
fashion. 

It may also be that nothing works. But, a lot of attempts are being made and
there is solid science behind the efforts.

Can you stop the epidemic?
--------------------------
Oddly enough, it does appear you can pause it with great effort.  Notably
China, Hong Kong, Singapore, Taiwan appear to have been able to slow down things
hugely. Various academic papers have derived that after measures were in place,
every patient infected only 0.3 new patients in Wuhan.  But with a drastic
impact.

It is very early but the numbers coming out of [South
Korea](https://www.cdc.go.kr/board/board.es?mid=a30402000000&bid=0030) also
appear to be improving.  South Korea notably did not completely shut down
its country in the way Wuhan is still (9th of March) locked up.

So it appears that if a country (government AND its people) really wants to
and has the means, it can slow down the spread hugely.

An open question is if you can do this and remain a long-term viable
economy. Also you have to want it, and many countries appear to wait with
measures until they are unavoidable. The Netherlands (my own country) is
being shamefully naive in this (until the 9th of March at least).

Actual treatment guidelines
---------------------------
One of the reasons it makes sense to try to slow the epidemic is that it
buys time to learn about treatments. 

Some governments are publishing their guidelines, sometimes even in English:

 * [Chinese treatment guidelines](https://www.chinalawtranslate.com/en/tag/coronavirus/) as translated by [China Law Translate](https://www.chinalawtranslate.com) (thanks!)
 * [Dutch treatment guidelines](https://lci.rivm.nl/covid-19/bijlage/medicamenteuze-behandelopties) - in Dutch, but quite thorough. Updated every few days.

The Chinese guidelines briefly discuss Tocilizumab.

(more links welcome!)

Is this a normal virus? Can you get reinfected?
-----------------------------------------------
Everything points towards COVID-19 being a normal virus that generates a
normal immune response, which should provide protection against reinfection,
at least in the short term. 

(this section will need to get expanded, see serology below).

Recent interesting papers
-------------------------
Papers (actually non-peer reviewed preprints) that look interesting, but
have not been (fully) absorbed into a specific section of this page:

 * 8th of March: [Clinical presentation and virological assessment of hospitalized cases of coronavirus disease 2019 in a travel-associated transmission
   cluster](https://www.medrxiv.org/content/10.1101/2020.03.05.20030502v1) by Charite Universitaetsmedizin Berlin, Berlin,
   Germany. Touches on immune response and viral shedding and criteria for
   when a patient might no longer be infective. Discussion by the
   incomperable Kai Kupferschmidt in [this twitter
   thread](https://twitter.com/kakape/status/1237005500912480259). Explainer
   article on [statnews.com](https://www.statnews.com/2020/03/09/people-shed-high-levels-of-coronavirus-study-finds-but-most-are-likely-not-infectious-after-recovery-begins/).
 * 10th of March: [The demand for inpatient and ICU beds for COVID-19 in the US: lessons from Chinese cities](https://dash.harvard.edu/handle/1/42599304),
   containing the following absolutely KEY insight, backed up with data: "In **Wuhan**, strict disease control measures were implemented six weeks after sustained local transmission of SARS-CoV-2. Between January 10 and February 29, COVID-19 patients accounted for an average of 637 ICU patients and 3,454 serious inpatients on each day. During the epidemic peak, 19,425 patients (24.5 per 10,000 adults) were hospitalized, 9,689 (12.2 per 10,000 adults) were considered to be in serious condition, and 2,087 patients (2.6 per 10,000 adults) needed critical care per day. In **Guangzhou**, strict disease control measures were implemented within one week of case importation. Between January 24 and February 29, COVID-19 accounted for an average of
   **9 ICU patients and 20 inpatients on each day**"
 * 14th of March: [A human monoclonal 1 antibody blocking SARS-CoV-2 infection](https://www.biorxiv.org/content/10.1101/2020.03.11.987958v1).
   Details how work on SARSv1 helped find a '-mab' that blocks COVID-19.

Twitter must-follows
--------------------
There is a LOT of noise on twitter about COVID-19. However, here is a list
of highly responsible, very high signal-to-noise ratio tweeters:

 * [@kakape](https://twitter.com/kakape), Kai Kupferschmidt, science journalist. molecular biologist. Contributing Correspondent at 
   Science Magazine
 * [@mlipsitch](https://twitter.com/mlipsitch), Marc Lipsitch, Infectious disease epidemiologist and microbiologist, Harvard.
 * [@HelenBranswell](https://twitter.com/HelenBranswell), Senior writer, infectious diseases at
 the excellent [Statnews.com](https://statnews.com).

Todo: other open questions
--------------------------
This content needs to be written. If you have good links or data, bert@hubertnet.nl
or [@PowerDNS_Bert](https://twitter.com/PowerDNS_Bert) are the places to
send them.

 * Are 'superspreading events' important? Maybe. May drive &gt;80% of
   transmission. This is a good rationale for canceling large events.
   Technical term is 'overdispersion'. An [anecdote](https://twitter.com/BioTurboNick/status/1237467872588251136), [more detail](https://www.wbur.org/commonhealth/2020/03/12/coronavirus-outbreak-biogen-conference-superspreading)
 * Children get infected readily with COVID-19 but they have very mild
   disease. But do they spread it effectively? In other words, does closing
   schools help a lot (directly)? It is known that closing schools binds
   parents to their houses, which provides an indirect way to limit spread of
   disease.
 * Why is COVID-19 so lethal in Italy? (appears to be lots of infections among very old
   people, and by now (10th of March) an overwhelmed healthcare system)
 * Pure speculation: Hypertension is a major major risk factor for dying from COVID-19. COVID-19 uses the ACE2 receptor for entry into cells. Common
   high blood pressure medications increase expression of ACE2 mRNA. Here is some [speculation in a BMJ response
   letter](https://www.bmj.com/content/368/bmj.m810/rr-2) on if these medicines could possibly make things worse for users. Very speculative.
 * Why is COVID-19 almost non-lethal in Germany??
 * How can China be reporting only double digit new infections? Has China actually restarted its society?
   [Perhaps not so much](https://twitter.com/NAChristakis/status/1237020524934463488).
   As of March 12th this is becoming somewhat of a bigger mystery since
   China is now reporting *single* digit case numbers from Wuhan.
 * The Mask Question: all of Asia believes in wearing masks, the rest of the
   world tells us to leave the masks to professionals. What is it?

