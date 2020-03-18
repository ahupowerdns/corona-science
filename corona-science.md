---
title: "Corona Science Journal"
date: 2020-03-18T10:16:25+01:00
draft: false
---
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@powerdns_bert">
<meta name="twitter:creator" content="@powerdns_bert">
<meta name="twitter:title" content="Corona Science Journal">
<meta name="twitter:description" content="An overview of the latest scientific and treatment developments of COVID-19, updated frequently, including links to original sources, preprints and papers">
<meta name="twitter:image" content="http://berthub.eu/articles/death-rate-feature.png">
Hello and welcome to this stream of consciousness I dare to call "the Corona
Science Journal". Updated frequently. Latest update: 18th of March 16:01 UTC. View history of
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
or [@PowerDNS_Bert](https://twitter.com/PowerDNS_Bert). Many readers are
sending me a steady stream of updates, please keep it up! Special mention
for Oliver Germer who appears to be combing the internet for the best data.

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
after infection (or perhaps 3-5 days according to [another commercial
source](https://www.biopanda.co.uk/php/products/rapid/infectious_diseases/covid19.php).

One such test is described
[on this page](https://www.biomedomics.com/products/infectious-disease/covid-19-rt/),
which includes manuals and protocols.

> Note: I wrote a separate warning about buying these tests online.
> Please feel free to [forward this
> warning](https://berthub.eu/articles/posts/corona-selftest-warning/) to people considering buying a
> rapid at home "self-test"!

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

See below for the latest updates on (hydroxy)chloroquine. A lot of
information and some optimism can be found in this [Google
Doc](https://docs.google.com/document/d/e/2PACX-1vTi-g18ftNZUMRAj2SwRPodtscFio7bJ7GdNgbJAGbdfF67WuRJB3ZsidgpidB2eocFHAVjIL-7deJ7/pub)
on various national treatment strategies.

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
data on if this would work, but it is reasonably plausible. [Anecdotal
tweet](https://twitter.com/CasasolaGarcia/status/1238539079412834305).

17th of March Update: there is now [a clinical trial of this
idea](https://clinicaltrials.gov/ct2/show/NCT04308668?cond=%22wuhan+coronavirus%22&sfpd_s=03%2F03%2F2020&sfpd_d=14&sel_rss=new14)
so at least I am not alone in speculating.

17th of March second update, [a limited experiment on 24 patients in a French
hospital](https://www.20minutes.fr/sante/2742011-20200317-coronavirus-hydroxychloroquine-efficace-selon-professeur-raoult-ihu-marseille-apres-premier-test-restreint)
combined hydroxychloroquine (trade name Plaquenil) and an antibiotic known
to have anti-viral effects (Azithromycin), with positive results.  It is
early days, but the result is not implausible.

17th of March third update, a trial of favipiravir has finished in China,
with some encouraging results: [The results have shown patients treated with favipiravir took four days before being tested negative, whereas the control group took 11
days.](http://www.chinadaily.com.cn/a/202003/17/WS5e708666a31012821727fcbd.html).
This is a press report and not a preprint.

18th of March, here is [some more reporting on
hydroxycloroquine(/Azithromycin)
trials](https://www.connexionfrance.com/French-news/French-researcher-in-Marseille-posts-successful-Covid-19-coronavirus-drug-trial-results).

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

17th of March update, Italy is launching a [330-patient Tocilizumab
trial](https://www.labussolanews.it/2020/03/17/tocilizumab-si-dellaifa-a-studio-sperimentale/) after some
further positive experiences in several hospitals.

In short, these medicines do not specifically kill or inhibit the virus, but
they aim to help fight off its effects & keep the patient alive.

Monoclonal antibodies
---------------------
This is extremely fresh. A collaboration between universities in The
Netherlands (Erasmus and Utrecht) has developed a monoclonal antibody that binds
to the COVID-19 virus, and in doing so disrupts its proliferation. This is based on previous research on SARSv1, so they
had 'everything ready to go'. Details are in "[A human monoclonal 1 antibody blocking SARS-CoV-2
infection](https://www.biorxiv.org/content/10.1101/2020.03.11.987958v1)".
Note that this was an international paper by lead authors Chunyan Wang, Wentao Li
and Dubravka Drabek. 

Monoclonal antibodies ('mabs') are still relatively recent, but some of
them have been spectacularly effective. And expensive.

This specific antibody with the exciting name 47D11 appears to bind very
well to both SARSv1 and COVID-19. At the very least this might enable fast
and simple detection of an infection, since it binds directly to the virus,
without having to do all kinds of RNA and DNA processing.

With some further luck, 47D11 might also be of clinical use. I am very far
from an expert, but the concentrations at which this new 'mab' is active
appear to be feasible, requiring milligrams per patient if I read it right.

This last bit is relevant - by now we all know lowly soap also eviscerates
COVID-19, but the problem is that at concentration required, it would also
kill us. Turns out our bodies use lipid bilayers as well.

{{< figure src="/articles/cells_2x.png" caption="[Source](https://xkcd.com/1217/)">}}

Will 47D11 be useful on the timescales we need? I don't know. Some
background can be found in [this
interview](https://www.erasmusmagazine.nl/en/2020/03/14/unique-discovery-in-erasmus-mc-antibody-against-corona/?noredirect=en_US). 

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

Vaccines
--------
To be honest I have no clue.  There is frantic ongoing activity by dozens of
groups and companies.  We don't currently know if any of these vaccines will
work (safely), nor how quickly they can be produced if they do.  Also, who
would get them?  Countries turn very nasty over such things.

Some good discussion on vaccines and other treatments can be found [in this
Science
article](https://blogs.sciencemag.org/pipeline/archives/2020/03/09/covid-19-biologic-therapies-reviewed).

This situation will hopefully clear up over time. It may be that small
quantities of vaccines become available early and could be used in targeted
fashion. 

It may also be that nothing works. But, a lot of attempts are being made and
there is solid science behind the efforts.

Meanwhile, it appears one German company CureVac, which makes mRNA-based
vaccines, is [being enticed to work for the US
exclusively](https://twitter.com/alfonslopeztena/status/1239142131467464704).
Perhaps they [know something we
don't](https://www.dw.com/en/germany-and-us-wrestle-over-coronavirus-vaccine-report/a-52777990).

A brief word on mRNA-based vaccines. For an DNA/RNA primer, try my earlier
post '[What is life](https://berthub.eu/articles/posts/what-is-life/)' or
the followup
'[Is biology too complex to ever
understand?](https://berthub.eu/articles/posts/biologists-physics-envy/)'. 

So in short, our cells convert ('transcribe') DNA from our genome into
"messenger RNA".  Messenger RNA (mRNA) is subsequently converted
('translated') into proteins.  When a virus infects a cell, it hijacks this
mechanism by also creating mRNA, and turning the cell into a factory for new
viruses.

What an mRNA-based vaccine attempts to do is to get carefully crafted mRNA
inside our cells so those cells start producing proteins we have chosen.  We
pick proteins that also occur in (or on) the virus we want to generate
immunity for.

If done well, those cells will create those viral proteins, and our immune
system will get alerted to these alien proteins and develop antibodies and
hopefully long-lived immunity.

The nice thing about this trick is that the mRNA in an mRNA-vaccine does not
self replicate.  So if you inject x amount of vaccine, at most y
amount of protein will come out.  And you can calibrate y that it won't
actually kill or harm the patient. 

In a sense, an mRNA-vaccine is sort of a 'build it yourself' vaccine that
uses our own cells to create proteins that look like viral proteins (or
actually are), and then our immune system does the rest. IKEA-style vaccines
if you will.

There are also self-amplifying mRNA vaccines that do replicate and multiply
in our cells, which leads to a more potent immune system response, but is in
a sense playing with fire. 

mRNA-vaccine technology is pretty well advanced and has conquered many
hurdles already, but has as yet not delivered any vaccine against a Corona
or Influenza virus in humans.  It has done so in mice however.  A very good
writeup is in [this Nature
article](https://www.nature.com/articles/nrd.2017.243), which is the source
of most of this section.

Of note, some pretty clever things are already in the works to stimulate the
immune system to act on the newly generated viral proteins.  If I had to
guess, it looks like the field is maturing rapidly and it all does seem
plausible. But there's no proof in humans.

One final thing mRNA vaccines have going for them is that they can be
produced quickly. So let's see if this delivers.

Can you stop the epidemic?
--------------------------
Oddly enough, it does appear you can pause it with great effort.  Notably
China, Hong Kong, Singapore, Taiwan appear to have been able to slow down things
hugely. Various academic papers have derived that after measures were in place,
every patient infected only 0.3 new patients in Wuhan.  But with a drastic
impact.

It is still early but the numbers coming out of [South
Korea](https://www.cdc.go.kr/board/board.es?mid=a30402000000&bid=0030) are
definitely improving.  South Korea notably did not completely shut down
its country in the way Wuhan is still (9th of March) locked up.

So it appears that if a country (government AND its people) really wants to
and has the means, it can slow down the spread hugely.

An open question is if you can do this and remain a long-term viable
economy. Also you have to want it, and many countries appear to wait with
measures until they are unavoidable. This will not be of any use. The right
time for measures is when they appear to be overreactions - they will be
visionary soon enough.

Actual treatment guidelines
---------------------------
One of the reasons it makes sense to try to slow the epidemic is that it
buys time to learn about treatments. 

Some governments are publishing their guidelines, sometimes even in English:

 * [Chinese treatment guidelines](https://www.chinalawtranslate.com/en/tag/coronavirus/) as translated by [China Law Translate](https://www.chinalawtranslate.com) (thanks!)
 * [Dutch treatment guidelines](https://lci.rivm.nl/covid-19/bijlage/medicamenteuze-behandelopties) - in Dutch, but quite thorough. Updated every few days.
 * [Belgian guidelines, in English!](https://epidemio.wiv-isp.be/ID/Documents/Covid19/COVID-19_InterimGuidelines_Treatment_ENG.pdf)

The Chinese guidelines briefly discuss Tocilizumab.

This [Google
Document](https://docs.google.com/document/d/e/2PACX-1vTi-g18ftNZUMRAj2SwRPodtscFio7bJ7GdNgbJAGbdfF67WuRJB3ZsidgpidB2eocFHAVjIL-7deJ7/pub)
containst a list of treatment guidelines, also from Korea. I touches a lot
on (hydroxy)chloroquine as well. 

(more links welcome!)

Is this a normal virus? Can you get reinfected?
-----------------------------------------------
Everything points towards COVID-19 being a normal virus that generates a
normal immune response, which should provide protection against reinfection,
at least in the short term. 

There are some (two, that I know) reports of reinfection, but they are very
sparse so far, and one is thought to be a testing mishap. An [experiment in
rhesus
macaques](https://www.biorxiv.org/content/10.1101/2020.03.13.990226v1) showed they could not be reinfected (after a month).
This is great news if you are a rhesus macaque, but it likely extends to
humans as well.

It is however unknown how long built up immunity will last, and also how
strong the immune response remains.  A weaker response might turn an
infection into a far less dangerous but still inconvenient affair.  We know
surprisingly little about this.  There is a paper on [coronaviruses IN
MICE](https://www.ncbi.nlm.nih.gov/pubmed/2554852), which indicates a robust
response at least for one year. Update 17th of March: here is an [extremely
thorough paper](https://www.nature.com/articles/s41591-020-0819-2) on the
very normal immune system response to even mild COVID-19 disease. 

Although (rapid) reinfection currently does not appear to be a big thing it
is of course a subject of intense interest, so this paragraph will be
updates with everything we learn.

What about Ibuprofen/NSAIDs?
----------------------------
Here is what I understand is the full list of things we know about the
safety of Ibuprofen during pneumonia:

 * ...

The [warning to not use Ibuprofen from the French minister of
health](https://twitter.com/olivierveran/status/1238776545398923264) (who is
also a doctor) came without evidence or data but it also did not come out of
nowhere.

People frequently refer to [a paper in The
Lancet](https://www.thelancet.com/journals/lanres/article/PIIS2213-2600(20)30116-8/fulltext), but it only mentions Ibuprofen in
passing, without adding data.

In the absence of real data, it appears that if you have the choice between
Ibuprofen/NSAIDs or paracetamol (tylenol, acetominophen), use the latter, a
recommendation [echoed by the
WHO](https://www.sciencealert.com/who-recommends-to-avoid-taking-ibuprofen-for-covid-19-symptoms),
and also by this [BMJ article](https://www.bmj.com/content/368/bmj.m1086).

There are some unfortunate health authorities, including Dutch ones,
rubbishing the Ibuprofen warnings - I can't see how they do this since there
is an utter lack of data showing NSAIDs are safe or beneficial in these
situations. Best response right now is "we need more data, but it could well
be true". 

Will update this section as more data becomes available. 

Can we restart society after lockdown? (beware, speculation)
------------------------------------------------------------
The rest of this page is purely based on well reported science and serious
sources. In this section I speculate a bit. Please be aware of the
difference, this is me thinking out loud, and I am no expert.

From personal sources, I am convinced China is indeed starting up its
economy again. Even some Hubei (the Wuhan province) based companies where I
have second hand contacts are shipping things again to people I know.

It is estimated that around [1% of Wuhan got infected at
peak](https://www.imperial.ac.uk/media/imperial-college/medicine/sph/ide/gida-fellowships/Imperial-College-COVID19-repatriation-09-03-2020.pdf). 
This is very very far away from any kind of "herd immunity". Other sources
say 4%, but this is still not a lot.

So how is it possible things are starting up there again without the virus
roaring back?  And similarly, how come other large cities there did not get
huge outbreaks even with far more relaxed measures?

I think we are missing some factor.  If I do some non-expert speculation
(sorry), many cases of COVID-19 may have been PCR-negative (so never
detected), but perhaps did lead to some kind of immunity.  Serological
testing (the IgG, IgM story from above) will likely tell, and I anxiously
await the results.

It may also be that COVID-19 depends to a far larger extent on 'super
spreading events' and simply not doing very large gatherings is all you
need to keep things under control. Who knows.

Or perhaps extreme contact tracing for each remaining event is enough to
keep things under wraps once the explosive phase is over.

Could it be that masks do help if worn by all people that might be infected?

Perhaps it is a combination of multiple factors that, after the initial
outbreak is under control, drives down the reproduction number under 1
without halting your whole society. A combination then of some immunity,
less super spreading, masks, more favourable weather, perhaps. 

Some thoughts can also be found [in this
interview](https://www.calcalistech.com/ctech/articles/0,7340,L-3800632,00.html)
with Nobel-prize winning biophysicist Michael Levitt who called the peak of
infections in Wuhan correctly.

[Marcel Salathé](https://www.epfl.ch/labs/salathelab/), a professor of
digital epidemiology, describes a post-infection peak scenario in [this
post](https://blog.salathe.com/covid-19-some-thoughts-on-whats-next-mar-15)
where he estimates that once the worst is past, stringent and high-capacity
testing followed by isolation will keep things under control.  Perhaps that
is what we are seeing. 

Meanwhile, Marc Lipsitch who is an expert (linked below from the Twitter
section), opines [that Wuhan didn't solve
anything](https://twitter.com/mlipsitch/status/1239221053848727553) and that
if they relax their measures, the virus will just come back.

In "[Strongly heterogeneous transmission of COVID-19 in mainland China: local and regional
variation](https://www.medrxiv.org/content/10.1101/2020.03.10.20033852v1)"
we can read an analysis that indicates that outside of Wuhan, after people
were warned, the reproduction number of COVID-19 was below 2, even before
strong measures were implemented. This may also explain some of the relative
ease of keeping things under control in China, but unsure. 

Wild speculation ends here!

Graphs and numbers
------------------
There are so many graphs and numbers out there. Please be aware that we have
no 'Corona-meter'. All the numbers and especially the graphs we see are the
product of many policity decisions of whom and how many to test. Some tests
may also be more sensitive than others. Almost no country reports reliable
numbers on who is cured. We may ache for the certainty of hard figures, but
the numbers just don't work that way. 

One site that does appear to be making an effort is
"[Temporal variation in transmission during the COVID-19
outbreak](https://cmmid.github.io/topics/covid19/current-patterns-transmission/global-time-varying-transmission.html)"
by the UK's [Centre for Mathematical Modelling of Infections
Diseases](https://www.lshtm.ac.uk/research/centres/centre-mathematical-modelling-infectious-diseases). 

By comparing numbers not among countries but comparing them from day to day,
they can derive growth factors. They also attempt to account for the delay
in reporting new cases.

{{< figure src="/articles/cmmid.png" caption="COVID-19 in The Netherlands">}}

These graphs take some processing and are not up to the minute, but they do
show the numbers we need to know. Other sites may be more exciting, but I prefer
[this one](https://cmmid.github.io/topics/covid19/current-patterns-transmission/global-time-varying-transmission.html)!

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

Another outstanding follow is [@COVID_Evidence](https://twitter.com/COVID_Evidence)
which live-tweets the latest preprints and clinical trials.

[Russ Garrett](https://twitter.com/russss) also [maintains an exhaustive set of
bookmarks](https://pinboard.in/u:russ/t:covid19/).

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
   A great summary of the situation: [The Coronavirus Conundrum: ACE2 and Hypertension
   Edition](http://www.nephjc.com/news/covidace2).
 * Why is COVID-19 almost non-lethal in Germany??
 * How can China be reporting only double digit new infections? Has China actually restarted its society?
   [Perhaps not so much](https://twitter.com/NAChristakis/status/1237020524934463488).
   As of March 12th this is becoming somewhat of a bigger mystery since
   China is now reporting *single* digit case numbers from Wuhan.
 * The Mask Question: all of Asia believes in wearing masks, the rest of the
   world tells us to leave the masks to professionals. What is it?

